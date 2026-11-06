#!/usr/bin/env python3
"""Đồng bộ files/ của mọi dự án <-> OneDrive (chạy mỗi giờ bằng launchd, hoặc tay).

- Đẩy:  Mac files/  -> OneDrive "0. Dự án Agent/<dự án>/"   (file mới hơn mới chép)
- Kéo:  OneDrive    -> Mac files/                             (file mới hơn mới chép)
- STATUS.md + CLAUDE.md: sao lưu 1 chiều lên OneDrive "<dự án>/_so-mac/" (chỉ để phòng hỏng máy, không sửa ở đó).
- KHÔNG BAO GIỜ xoá ở bất kỳ bên nào. Muốn xoá: xoá cả 2 nơi (hoặc nhắn Sidekick).
- Bỏ qua node_modules, .git, build... (xem LOAI_TRU).
- Không đẩy file có đường dẫn quá dài (OneDrive báo "path is too long" rồi tự tắt — sự cố 03–06/11/2026):
  đường dẫn tính từ gốc OneDrive > GIOI_HAN ký tự, hoặc 1 tên > 255 ký tự -> bỏ qua + cảnh báo.
- OneDrive mở lên rồi tắt ngay -> quét cả OneDrive tìm đường dẫn dài / node_modules và báo #can-hero.
Sau đó chạy bang_viec.py để gộp bảng việc.

Cách dùng: python3 dong_bo.py [dự-án ...] [--chi-day | --chi-keo]
"""
import os, subprocess, sys, datetime, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cau_hinh import DU_AN, LOAI_TRU, mac_dir, od_moi, OD

args = [a for a in sys.argv[1:] if not a.startswith("--")]
keys = args or list(DU_AN)
LOG = os.path.expanduser("~/Library/Logs/hero-dong-bo.log")

def log(s):
    line = f"{datetime.datetime.now():%Y-%m-%d %H:%M} {s}"
    print(line)
    with open(LOG, "a") as f: f.write(line + "\n")

GIOI_HAN = 380   # OneDrive cho tối đa 400 ký tự; chừa lề

def bao(msg):
    subprocess.run([os.path.expanduser("~/Projects/dream-hero-agent/tools/discord-say.sh"),
                    "sidekick", "can-hero", msg])

def qua_dai(rel_od):
    return len(rel_od) > GIOI_HAN or any(len(p) > 255 for p in rel_od.split("/"))

def tim_qua_dai(goc, tien_to=""):
    """Trả về các đường dẫn (tương đối với goc) mà khi nằm trên OneDrive sẽ quá dài. Không đi vào thư mục LOAI_TRU."""
    bo = {e for e in LOAI_TRU if "*" not in e}
    ra = []
    for d, dirs, files in os.walk(goc):
        dirs[:] = [x for x in dirs if x not in bo]
        for n in dirs + files:
            rel = os.path.relpath(os.path.join(d, n), goc)
            if qua_dai(os.path.join(tien_to, rel)):
                ra.append(rel)
                if n in dirs: dirs.remove(n)
    return ra

def kiem_tra_onedrive():
    """Quét cả OneDrive: đường dẫn quá dài + node_modules lọt vào (nguyên nhân hay gặp khiến OneDrive tự tắt)."""
    dai, nm = [], []
    for d, dirs, files in os.walk(OD):
        if "node_modules" in dirs:
            nm.append(os.path.relpath(os.path.join(d, "node_modules"), OD)); dirs.remove("node_modules")
        for n in dirs + files:
            rel = os.path.relpath(os.path.join(d, n), OD)
            if qua_dai(rel): dai.append(rel)
        if len(dai) > 20: break
    return dai, nm

def onedrive_chay():
    return subprocess.run(["pgrep", "-f", "OneDrive.app/Contents/MacOS/OneDrive"], capture_output=True).returncode == 0

if not onedrive_chay():
    log("OneDrive chưa chạy -> mở lại")
    subprocess.run(["open", "-a", "OneDrive"]); time.sleep(150)   # OneDrive gặp đường dẫn dài thường tắt sau ~2 phút
    if not onedrive_chay():
        dai, nm = kiem_tra_onedrive()
        ly_do = ""
        if nm: ly_do += "\nnode_modules trong OneDrive: " + "; ".join(nm[:5])
        if dai: ly_do += "\nĐường dẫn quá dài: " + "; ".join(x[-120:] for x in dai[:5])
        log("⚠️ OneDrive mở lên rồi tắt / không mở được, bỏ qua lượt này" + ly_do.replace("\n", " | "))
        bao("⚠️ OneDrive trên Mac mini không chạy — sao lưu files/ đang dừng." + (ly_do or "\nKhông thấy đường dẫn dài; xem màn hình Mac mini."))
        sys.exit(1)

ex = sum([["--exclude", e] for e in LOAI_TRU], [])
for k in keys:
    src = os.path.join(mac_dir(k), "files") + "/"
    dst = od_moi(k) + "/"
    if not os.path.isdir(src):
        continue
    os.makedirs(dst, exist_ok=True)
    if "--chi-keo" not in sys.argv:
        dai = tim_qua_dai(src, os.path.relpath(dst, OD))
        ex_dai = sum([["--exclude", "/" + x] for x in dai], [])
        if dai:
            log(f"{k}: ⚠️ bỏ qua {len(dai)} đường dẫn quá dài: " + "; ".join(dai[:3]))
            bao(f"⚠️ {k}: {len(dai)} file/thư mục đường dẫn quá dài, KHÔNG đẩy lên OneDrive (đổi tên ngắn lại):\n" + "\n".join(dai[:5]))
        r = subprocess.run(["rsync", "-a", "--update", *ex, *ex_dai, src, dst], capture_output=True, text=True)
        log(f"{k}: đẩy {'ok' if r.returncode == 0 else 'LỖI ' + r.stderr[:200]}")
    # sao lưu sổ (1 chiều Mac -> OneDrive, thư mục _so-mac/, không kéo về)
    so = [os.path.join(mac_dir(k), f) for f in ("STATUS.md", "CLAUDE.md") if os.path.exists(os.path.join(mac_dir(k), f))]
    if so and "--chi-keo" not in sys.argv:
        os.makedirs(dst + "_so-mac", exist_ok=True)
        subprocess.run(["rsync", "-a", *so, dst + "_so-mac/"], capture_output=True)
    if "--chi-day" not in sys.argv:
        r = subprocess.run(["rsync", "-a", "--update", *ex, "--exclude", "_so-mac", dst, src], capture_output=True, text=True)
        log(f"{k}: kéo {'ok' if r.returncode == 0 else 'LỖI ' + r.stderr[:200]}")

subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "bang_viec.py")])
