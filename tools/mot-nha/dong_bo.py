#!/usr/bin/env python3
"""Đồng bộ files/ của mọi dự án <-> OneDrive (chạy mỗi giờ bằng launchd, hoặc tay).

- Đẩy:  Mac files/  -> OneDrive "0. Dự án Agent/<dự án>/"   (file mới hơn mới chép)
- Kéo:  OneDrive    -> Mac files/                             (file mới hơn mới chép)
- KHÔNG BAO GIỜ xoá ở bất kỳ bên nào. Muốn xoá: xoá cả 2 nơi (hoặc nhắn Sidekick).
- Bỏ qua node_modules, .git, build... (xem LOAI_TRU).
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

def onedrive_chay():
    return subprocess.run(["pgrep", "-x", "OneDrive"], capture_output=True).returncode == 0

if not onedrive_chay():
    log("OneDrive chưa chạy -> mở lại")
    subprocess.run(["open", "-a", "OneDrive"]); time.sleep(30)
    if not onedrive_chay():
        log("⚠️ Không mở được OneDrive, bỏ qua lượt này")
        subprocess.run([os.path.expanduser("~/Projects/dream-hero-agent/tools/discord-say.sh"),
                        "sidekick", "can-hero", "⚠️ OneDrive trên Mac mini không chạy — sao lưu files/ đang dừng."])
        sys.exit(1)

ex = sum([["--exclude", e] for e in LOAI_TRU], [])
for k in keys:
    src = os.path.join(mac_dir(k), "files") + "/"
    dst = od_moi(k) + "/"
    if not os.path.isdir(src):
        continue
    os.makedirs(dst, exist_ok=True)
    if "--chi-keo" not in sys.argv:
        r = subprocess.run(["rsync", "-a", "--update", *ex, src, dst], capture_output=True, text=True)
        log(f"{k}: đẩy {'ok' if r.returncode == 0 else 'LỖI ' + r.stderr[:200]}")
    if "--chi-day" not in sys.argv:
        r = subprocess.run(["rsync", "-a", "--update", *ex, dst, src], capture_output=True, text=True)
        log(f"{k}: kéo {'ok' if r.returncode == 0 else 'LỖI ' + r.stderr[:200]}")

subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "bang_viec.py")])
