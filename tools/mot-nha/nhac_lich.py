#!/usr/bin/env python3
"""Nhắc lịch qua Discord (kênh can-hero) trước giờ bắt đầu N phút (mặc định 15).
Danh sách lịch: ~/.hero/nhac-lich.json  [{"bat_dau": "2026-11-09T09:00", "tieu_de": "...", "dia_diem": "...", "truoc": 15, "da_nhac": false}]
- launchd chạy file này mỗi phút (com.hero.nhac-lich).
- Thêm lịch: python3 nhac_lich.py them "2026-11-09T09:00" "Tiêu đề" ["địa điểm"] [phút-trước]
  (trùng giờ + tiêu đề thì bỏ qua, không thêm 2 lần).
"""
import json, os, sys, datetime, subprocess
F = os.path.expanduser("~/.hero/nhac-lich.json")
DISCORD = os.path.expanduser("~/Projects/dream-hero-agent/tools/discord-say.sh")
now = datetime.datetime.now()

def doc():
    try: return json.load(open(F))
    except Exception: return []
def ghi(ds):
    os.makedirs(os.path.dirname(F), exist_ok=True)
    json.dump(ds, open(F, "w"), ensure_ascii=False, indent=1)

ds = doc()
if len(sys.argv) > 1 and sys.argv[1] == "them":
    bd, td = sys.argv[2], sys.argv[3]
    dd = sys.argv[4] if len(sys.argv) > 4 else ""
    tr = int(sys.argv[5]) if len(sys.argv) > 5 else 15
    if any(x["bat_dau"] == bd and x["tieu_de"] == td for x in ds):
        print("đã có:", bd, td); sys.exit(0)
    ds.append(dict(bat_dau=bd, tieu_de=td, dia_diem=dd, truoc=tr, da_nhac=False)); ghi(ds); print("thêm:", bd, td); sys.exit(0)

doi = False
for x in ds:
    if x.get("da_nhac"): continue
    bd = datetime.datetime.fromisoformat(x["bat_dau"])
    if bd - datetime.timedelta(minutes=x.get("truoc", 15)) <= now < bd + datetime.timedelta(minutes=5):
        msg = f"⏰ {bd:%H:%M} (còn {max(0, int((bd - now).total_seconds() // 60))} phút): {x['tieu_de']}" + (f"\n📍 {x['dia_diem']}" if x.get("dia_diem") else "")
        if subprocess.run([DISCORD, "sidekick", "can-hero", msg], capture_output=True).returncode == 0:
            x["da_nhac"] = True; doi = True
    elif now >= bd + datetime.timedelta(minutes=5):
        x["da_nhac"] = "qua-gio"; doi = True  # máy tắt/lỡ giờ: không nhắn muộn
# giữ 30 ngày gần nhất
ds2 = [x for x in ds if datetime.datetime.fromisoformat(x["bat_dau"]) > now - datetime.timedelta(days=30)]
if doi or len(ds2) != len(ds): ghi(ds2)
