#!/usr/bin/env python3
"""Chuyển nhà 1 lần: CHÉP (không xoá, không ghi đè) tài liệu từ OneDrive cũ về
~/Projects/<khu>/<dự án>/files/{inbox,output}, gom các thư mục lẻ trên Mac vào files/,
rồi đối chiếu từng file (tên + dung lượng). Chạy lại nhiều lần được (chỉ bổ sung file thiếu).

Cách dùng:  python3 chuyen_nha.py            # chạy thật
            python3 chuyen_nha.py --thu       # chỉ in ra sẽ làm gì
"""
import os, subprocess, sys, unicodedata, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cau_hinh import DU_AN, INBOX_TEN, mac_dir, od_cu, PROJECTS

THU = "--thu" in sys.argv
HOM_NAY = datetime.date.today().isoformat()
BO_QUA = {".DS_Store", "Icon\r"}

# Thư mục lẻ đang nằm ngoài files/ trên Mac -> đưa vào files/ (mv, không xoá)
GOM_MAC = {
    "nhalo":   [("Claude outputs", "output/claude-outputs"),
                ("_fb-ads-tmp", "output/_fb-ads-tmp"),
                ("_video-tham-khao", "inbox/video-tham-khao")],
    "chinchu": [("Claude outputs", "output/claude-outputs")],
}

nhat_ky = []
def log(s):
    print(s); nhat_ky.append(s)

def nfc(s): return unicodedata.normalize("NFC", s)

def rsync(src, dst):
    """Chép src vào dst. Không ghi đè file đã có, không xoá gì."""
    if THU:
        log(f"  [thử] rsync {src} -> {dst}"); return
    os.makedirs(os.path.dirname(dst.rstrip("/")) or dst, exist_ok=True)
    r = subprocess.run(["rsync", "-a", "--ignore-existing", src, dst], capture_output=True, text=True)
    if r.returncode != 0:
        log(f"  ⚠️ rsync lỗi {src}: {r.stderr.strip()[:300]}")

def doi_chieu(src, dst):
    """Mọi file trong src phải có trong dst cùng dung lượng. Trả về (số file, số byte, danh sách thiếu)."""
    thieu, n, b = [], 0, 0
    if os.path.isfile(src):
        cap = [(src, dst if not dst.endswith("/") else os.path.join(dst, os.path.basename(src)))]
    else:
        cap = []
        for goc, dirs, files in os.walk(src):
            for f in files:
                if f in BO_QUA: continue
                p = os.path.join(goc, f)
                cap.append((p, os.path.join(dst, os.path.relpath(p, src))))
    for p, q in cap:
        n += 1
        try: sz = os.stat(p).st_size
        except OSError: continue
        b += sz
        if not os.path.exists(q) or os.stat(q).st_size != sz:
            thieu.append(os.path.relpath(p, os.path.dirname(src)))
    return n, b, thieu

tong_thieu = []
for key, (khu, _, ten, nguon) in DU_AN.items():
    md = mac_dir(key); files = os.path.join(md, "files")
    log(f"\n== {key}  ({md})")
    for sub in ("inbox", "output", "output/_luu-tru"):
        if not THU: os.makedirs(os.path.join(files, sub), exist_ok=True)

    # 1) OneDrive cũ -> files/
    viec = []  # (src, dst_dir_with_trailing_slash or dst_dir)
    for src_rel, dich in nguon:
        src = od_cu(key, src_rel)
        if not os.path.exists(src):
            log(f"  (không có trên OneDrive cũ: {src_rel})"); continue
        if dich == "auto":
            for con in sorted(os.listdir(src)):
                if con in BO_QUA: continue
                p = os.path.join(src, con)
                if nfc(con) == "TRANG-THAI.md":
                    viec.append((p, os.path.join(files, f"output/_luu-tru/TRANG-THAI-truoc-{HOM_NAY}.md"), "file"))
                    continue
                vung = "inbox" if nfc(con) in {nfc(x) for x in INBOX_TEN} else "output"
                viec.append((p, os.path.join(files, vung) + "/", "item"))
        elif dich.endswith("/"):
            viec.append((src, os.path.join(files, dich), "item"))
        else:
            viec.append((src + "/", os.path.join(files, dich) + "/", "noi-dung"))

    # 2) thư mục lẻ trên Mac -> files/ (mv)
    for ten_cu, dich in GOM_MAC.get(key, []):
        p = os.path.join(md, ten_cu); q = os.path.join(files, dich)
        if os.path.exists(p) and not os.path.exists(q):
            log(f"  gom Mac: {ten_cu} -> files/{dich}")
            if not THU:
                os.makedirs(os.path.dirname(q), exist_ok=True); os.rename(p, q)
        elif os.path.exists(p):
            log(f"  ⚠️ files/{dich} đã có, để nguyên {ten_cu}")

    for src, dst, kieu in viec:
        if kieu == "file":
            if not os.path.exists(dst) and not THU:
                subprocess.run(["cp", "-p", src, dst])
            continue
        rsync(src, dst)
    if THU: continue

    # 3) đối chiếu
    for src, dst, kieu in viec:
        if kieu == "file":
            n, b, thieu = doi_chieu(src, dst)
        elif kieu == "item":
            n, b, thieu = doi_chieu(src, os.path.join(dst, os.path.basename(src)) if os.path.isdir(src) else dst)
        else:
            n, b, thieu = doi_chieu(src.rstrip("/"), dst.rstrip("/"))
        ok = "✅" if not thieu else f"❌ thiếu {len(thieu)}"
        log(f"  {ok}  {os.path.basename(src.rstrip('/'))}: {n} file, {b/1e6:.1f} MB")
        tong_thieu += [f"{key}: {t}" for t in thieu]

log(f"\nTỔNG: {'KHÔNG thiếu file nào ✅' if not tong_thieu else str(len(tong_thieu)) + ' file thiếu ❌'}")
for t in tong_thieu[:200]: log("  thiếu: " + t)
if not THU:
    p = os.path.join(PROJECTS, "company/team/files/output/_luu-tru", f"chuyen-nha-{HOM_NAY}.log")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "a") as f: f.write("\n".join(nhat_ky) + "\n")
    print("Nhật ký:", p)
