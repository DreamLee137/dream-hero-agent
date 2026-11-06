#!/usr/bin/env python3
"""Gộp "## Bảng việc" trong STATUS.md của mọi dự án -> ~/Projects/BANG-VIEC.md (+ trang web Netlify nếu đã cấu hình).

1. Nếu có ~/.secrets/netlify/bang-viec.json ({"url": "https://<site>.netlify.app", "token": "<BV_TOKEN>"}):
   lấy các dòng Hero tick "Xong" trên trang -> ghi vào STATUS.md (trạng thái ✅ Xong) -> báo trang đã nhận.
2. Gộp bảng -> BANG-VIEC.md; đẩy dữ liệu lên trang web.
3. Chỉ khi Bảng việc THAY ĐỔI so với lần chạy trước (việc mới, hoặc đổi trạng thái 🔵/🔴/🦹/👀/⏸/✅)
   -> nhắn Discord kênh can-hero, chỉ liệt kê phần thay đổi. Không đổi -> không gửi.
   Giờ yên lặng 20:00–7:00: không gửi; gom vào ~/.hero/bang-viec-gio-yen-lang.json để báo cáo sáng 7:52 đưa vào.

Cách dùng: python3 bang_viec.py [--im-lang]   (--im-lang: chỉ ghi file + web, không nhắn, không chốt trạng thái)
"""
import os, re, json, sys, datetime, subprocess, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cau_hinh import DU_AN, mac_dir, PROJECTS

NHOM = [("🔴", "Cần Hero"), ("👀", "Chờ Hero xem kết quả"), ("🔵", "Đang làm"), ("⏸", "Đang chờ"), ("🦹", "Cần Anti-hero (sếp)"), ("✅", "Xong")]
STATE = os.path.expanduser("~/.hero/bang-viec-state.json")
YEN_LANG = os.path.expanduser("~/.hero/bang-viec-gio-yen-lang.json")
WEB_CFG = os.path.expanduser("~/.secrets/netlify/bang-viec.json")
OUT = os.path.join(PROJECTS, "BANG-VIEC.md")
DISCORD = os.path.expanduser("~/Projects/dream-hero-agent/tools/discord-say.sh")
now = datetime.datetime.now()

def http(cfg, method, path, body=None):
    req = urllib.request.Request(cfg["url"].rstrip("/") + "/api/" + path, method=method,
                                 data=json.dumps(body, ensure_ascii=False).encode() if body is not None else None,
                                 headers={"authorization": "Bearer " + cfg["token"], "content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode() or "null")

def doc_bang(lines):
    """Trả về [(chỉ số dòng, [ô...])] của bảng trong mục ## Bảng việc."""
    rows, trong = [], False
    for n, line in enumerate(lines):
        if line.startswith("## "):
            trong = line.strip().lower().startswith("## bảng việc"); continue
        if trong and line.startswith("|") and not re.match(r"^\|\s*-", line):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(c) >= 3 and c[0].lower() != "id":
                rows.append((n, c + [""] * (5 - len(c))))
    return rows

# 1) phản hồi từ trang web
cfg = None
if os.path.exists(WEB_CFG):
    try: cfg = json.load(open(WEB_CFG))
    except Exception as e: print("⚠️ đọc cấu hình web lỗi:", e)
if cfg:
    try:
        ticks = http(cfg, "GET", "phan-hoi") or []
        done = []
        for t in ticks:
            if t.get("du_an") not in DU_AN: continue
            p = os.path.join(mac_dir(t["du_an"]), "STATUS.md")
            if not os.path.exists(p): continue
            lines = open(p, encoding="utf-8").read().split("\n")
            for n, c in doc_bang(lines):
                if c[0] == t["id"]:
                    ghi = c[3] + f" · Hero tick xong trên web {now:%d/%m %H:%M}" + (f": {t['ghi_chu']}" if t.get("ghi_chu") else "")
                    lines[n] = f"| {c[0]} | {c[1]} | ✅ Xong | {ghi} | {now:%d/%m} |"
                    lines = [re.sub(r"^Cập nhật lần cuối:.*", f"Cập nhật lần cuối: {now:%d/%m/%Y} — Hero (tick trên Bảng việc web)", l) for l in lines]
                    open(p, "w", encoding="utf-8").write("\n".join(lines))
                    done.append(t); break
            else:
                done.append(t)  # không tìm thấy dòng -> bỏ khỏi hàng chờ
        if done:
            http(cfg, "POST", "phan-hoi", {"done": done}); print(f"Ghi {len(done)} tick từ web vào STATUS.md")
    except Exception as e:
        print("⚠️ lấy phản hồi web lỗi:", e)

# 2) gộp
def ra_ngay(dd, mm, yyyy=None):
    d, m = int(dd), int(mm)
    y = int(yyyy) if yyyy else (now.year - 1 if m > now.month + 1 else now.year)
    try: return datetime.date(y, m, d).isoformat()
    except ValueError: return None

def doc_da_lam(path, k, ten):
    """Các dòng '- DD/MM · …' trong mọi mục 'Đã xong gần đây' (kể cả sổ cũ đã gộp)."""
    out, trong = [], False
    for line in open(path, encoding="utf-8"):
        if line.startswith("#"):
            trong = "đã xong" in line.lower(); continue
        m = re.match(r"^- (\d{1,2})/(\d{1,2})(?:/(\d{4}))?\s*(?:·|—|-)?\s*(.+)$", line.strip()) if trong else None
        if m and ra_ngay(m[1], m[2], m[3]):
            out.append(dict(du_an=k, ten_du_an=ten, ngay=ra_ngay(m[1], m[2], m[3]), viec=m[4].strip(), nguon="sổ"))
    return out

da_lam = []
tat_ca, moi, hien = [], [], {}
try: cu = json.load(open(STATE))
except Exception: cu = {}
for k, (khu, _, ten, _) in DU_AN.items():
    p = os.path.join(mac_dir(k), "STATUS.md")
    if not os.path.exists(p): continue
    tuoi = (now - datetime.datetime.fromtimestamp(os.path.getmtime(p))).days
    xong = 0
    da_lam.extend(doc_da_lam(p, k, ten))
    for _, (id_, viec, tt, ghichu, cn) in [(n, c[:5]) for n, c in doc_bang(open(p, encoding="utf-8").read().split("\n"))]:
        icon = next((i for i, _ in NHOM if tt.startswith(i)), None)
        if not icon: continue
        if icon == "✅":
            xong += 1
        tat_ca.append(dict(icon=icon, du_an=k, ten_du_an=ten, khu=khu, id=id_, viec=viec, trang_thai=tt, ghi_chu=ghichu, cap_nhat=cn, tuoi_so=tuoi))
        key = f"{k}/{id_}"
        if key in hien: key += f"#{sum(1 for x in hien if x.split('#')[0] == key)+1}"  # ID trùng trong sổ
        hien[key] = {"icon": icon, "viec": viec, "du_an": ten}
        truoc = cu.get(key)
        truoc_icon = truoc.get("icon") if isinstance(truoc, dict) else truoc
        if truoc is None:
            moi.append(dict(du_an=ten, id=id_, viec=viec, cu=None, moi=icon))
        elif truoc_icon != icon:
            moi.append(dict(du_an=ten, id=id_, viec=viec, cu=truoc_icon, moi=icon))

out = [f"# Bảng việc tổng — tự sinh {now:%d/%m/%Y %H:%M}", "",
       "_Không sửa file này. Sửa `STATUS.md` trong thư mục dự án; file này tự gộp mỗi giờ._", ""]
for icon, ten in NHOM[:5]:
    ds = [r for r in tat_ca if r["icon"] == icon]
    out.append(f"## {icon} {ten} ({len(ds)})")
    if not ds: out.append("- (không có)")
    for r in ds:
        cu_ = f" ⚠️ sổ {r['tuoi_so']} ngày chưa cập nhật" if icon == "🔵" and r["tuoi_so"] >= 3 else ""
        out.append(f"- **{r['ten_du_an']}** · {r['id']} · {r['viec']} — {r['ghi_chu']} _(cập nhật {r['cap_nhat']})_{cu_}")
    out.append("")
open(OUT, "w", encoding="utf-8").write("\n".join(out))
os.makedirs(os.path.dirname(STATE), exist_ok=True)
if "--im-lang" not in sys.argv:  # chạy im lặng thì không chốt trạng thái, để lần chạy thường sau vẫn báo đủ
    json.dump(hien, open(STATE, "w"), ensure_ascii=False)

# 3) đẩy lên web + báo Discord
if cfg:
    try:
        xong_bang = [dict(du_an=r["du_an"], ten_du_an=r["ten_du_an"], ngay=ra_ngay(*r["cap_nhat"].split("/")[:2]) if re.match(r"^\d{1,2}/\d{1,2}", r["cap_nhat"]) else None,
                          viec=f'{r["id"]} · {r["viec"]}', ghi_chu=r["ghi_chu"], nguon="bảng") for r in tat_ca if r["icon"] == "✅"]
        dl = sorted([d for d in da_lam + xong_bang if d.get("ngay")], key=lambda d: d["ngay"], reverse=True)[:1500]
        http(cfg, "PUT", "data", {"generated": f"{now:%d/%m/%Y %H:%M}", "items": [r for r in tat_ca if r["icon"] != "✅"], "da_lam": dl}); print("Đã đẩy lên trang web")
    except Exception as e:
        print("⚠️ đẩy web lỗi:", e)
def dong(t):
    v = t["viec"] if len(t["viec"]) <= 70 else t["viec"][:67] + "…"
    doi = f"mới {t['moi']}" if t["cu"] is None else f"{t['cu']} → {t['moi']}"
    return f"• {t['du_an']} · {t['id']} · {v}: {doi}"

if cu and moi:  # lần chạy đầu (chưa có trạng thái cũ) thì không báo
    yen_lang = now.hour >= 20 or now.hour < 7
    if yen_lang or "--im-lang" in sys.argv:
        if yen_lang:
            try: gom = json.load(open(YEN_LANG))
            except Exception: gom = []
            gom += [dict(t, luc=f"{now:%d/%m %H:%M}") for t in moi]
            json.dump(gom, open(YEN_LANG, "w"), ensure_ascii=False, indent=1)
            print(f"Giờ yên lặng: gom {len(moi)} thay đổi cho báo cáo sáng")
    elif os.path.exists(DISCORD):
        ds = [dong(t) for t in moi]
        msg = f"📋 Bảng việc thay đổi ({now:%H:%M}):\n" + "\n".join(ds[:15]) + (f"\n…và {len(ds)-15} thay đổi khác" if len(ds) > 15 else "")
        subprocess.run([DISCORD, "sidekick", "can-hero", msg])
print(f"Đã gộp {len(tat_ca)} việc -> {OUT}; thay đổi: {len(moi)}")
