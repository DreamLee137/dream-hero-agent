#!/usr/bin/env python3
"""Gộp "## Bảng việc" trong STATUS.md của mọi dự án -> ~/Projects/BANG-VIEC.md.
Việc MỚI chuyển sang 🔴 (cần Hero) hoặc 👀 (chờ Hero xem) -> nhắn Discord kênh can-hero
(điện thoại có app Discord sẽ nhận push).

Cách dùng: python3 bang_viec.py [--im-lang]   (--im-lang: không nhắn, chỉ ghi)
"""
import os, re, json, sys, glob, datetime, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cau_hinh import DU_AN, mac_dir, PROJECTS

NHOM = [("🔴", "Cần Hero"), ("👀", "Chờ Hero xem kết quả"), ("🔵", "Đang làm"), ("⏸", "Đang chờ")]
STATE = os.path.expanduser("~/.hero/bang-viec-state.json")
OUT = os.path.join(PROJECTS, "BANG-VIEC.md")
DISCORD = os.path.expanduser("~/Projects/dream-hero-agent/tools/discord-say.sh")

def doc_bang(path):
    rows, trong = [], False
    for line in open(path, encoding="utf-8"):
        if line.startswith("## "):
            trong = line.strip().lower().startswith("## bảng việc")
            continue
        if trong and line.startswith("|") and not re.match(r"^\|\s*-", line):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(c) >= 3 and c[0].lower() != "id":
                rows.append(c + [""] * (5 - len(c)))
    return rows

tat_ca, moi = [], []
cu = {}
try: cu = json.load(open(STATE))
except Exception: pass
hien = {}

for k in DU_AN:
    p = os.path.join(mac_dir(k), "STATUS.md")
    if not os.path.exists(p): continue
    tuoi = (datetime.datetime.now() - datetime.datetime.fromtimestamp(os.path.getmtime(p))).days
    for id_, viec, tt, ghichu, cn in [r[:5] for r in doc_bang(p)]:
        icon = next((i for i, _ in NHOM if tt.startswith(i)), None)
        if not icon: continue
        tat_ca.append((icon, k, id_, viec, ghichu, cn, tuoi))
        key = f"{k}/{id_}"; hien[key] = icon
        if icon in ("🔴", "👀") and cu.get(key) != icon:
            moi.append(f"{icon} {k} · {id_} · {viec} — {ghichu}")

now = datetime.datetime.now()
out = [f"# Bảng việc tổng — tự sinh {now:%d/%m/%Y %H:%M}", "",
       "_Không sửa file này. Sửa `STATUS.md` trong thư mục dự án; file này tự gộp mỗi giờ._", ""]
for icon, ten in NHOM:
    ds = [r for r in tat_ca if r[0] == icon]
    out.append(f"## {icon} {ten} ({len(ds)})")
    if not ds: out.append("- (không có)")
    for _, k, id_, viec, ghichu, cn, tuoi in ds:
        cu_ = f" ⚠️ sổ {tuoi} ngày chưa cập nhật" if icon == "🔵" and tuoi >= 3 else ""
        out.append(f"- **{k}** · {id_} · {viec} — {ghichu} _(cập nhật {cn})_{cu_}")
    out.append("")
open(OUT, "w", encoding="utf-8").write("\n".join(out))
os.makedirs(os.path.dirname(STATE), exist_ok=True)
json.dump(hien, open(STATE, "w"), ensure_ascii=False)

if moi and "--im-lang" not in sys.argv and os.path.exists(DISCORD):
    msg = "📋 Việc mới cần cậu:\n" + "\n".join(moi[:15])
    subprocess.run([DISCORD, "sidekick", "can-hero", msg])
print(f"Đã gộp {len(tat_ca)} việc -> {OUT}; báo mới: {len(moi)}")
