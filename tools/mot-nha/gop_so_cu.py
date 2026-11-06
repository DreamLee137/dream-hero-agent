#!/usr/bin/env python3
"""Chép nguyên văn sổ cũ (files/output/_luu-tru/TRANG-THAI-truoc-*.md) vào cuối STATUS.md,
tại chỗ đánh dấu <!-- CHO-GOP-SO-CU -->. Sửa đường dẫn cũ sang chỗ mới. Chạy 1 lần sau khi chuyen_nha.py
đã lấy đủ TRANG-THAI.md. --chot: dự án không có sổ cũ thì ghi "(không có)" và bỏ dấu."""
import os, sys, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cau_hinh import DU_AN, mac_dir

DAU = "<!-- CHO-GOP-SO-CU -->"
DOI = [("~/Projects/company/nhalo/Claude outputs", "files/output/claude-outputs"),
       ("~/Projects/company/nhalo/_video-tham-khao", "files/inbox/video-tham-khao"),
       ("~/Projects/company/chinchu/Claude outputs", "files/output/claude-outputs")]

for k in DU_AN:
    p = os.path.join(mac_dir(k), "STATUS.md")
    if not os.path.exists(p): continue
    s = open(p, encoding="utf-8").read()
    if DAU not in s: continue
    cu = sorted(glob.glob(os.path.join(mac_dir(k), "files/output/_luu-tru/TRANG-THAI-truoc-*.md")))
    if not cu:
        if "--chot" in sys.argv:
            s = s.replace(DAU, "- (không có sổ cũ)"); open(p, "w", encoding="utf-8").write(s)
            print(f"{k}: không có sổ cũ")
        else:
            print(f"{k}: chưa có sổ cũ, để chờ")
        continue
    t = open(cu[-1], encoding="utf-8").read().splitlines()
    t = [l for l in t if not l.startswith("# TRANG-THAI") and not l.startswith("_Sổ chung")]
    t = ["#" + l if l.startswith("## ") else l for l in t]
    body = "\n".join(t).strip()
    for a, b in DOI: body = body.replace(a, b)
    s = s.replace(DAU, f"_Chép nguyên văn từ OneDrive TRANG-THAI.md ({os.path.basename(cu[-1])}); mục mới ghi ở các phần phía trên._\n\n" + body)
    open(p, "w", encoding="utf-8").write(s)
    print(f"{k}: đã gộp {os.path.basename(cu[-1])}")
