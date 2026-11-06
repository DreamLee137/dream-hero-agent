#!/bin/bash
# Chép BV_TOKEN của trang Bảng việc vào clipboard (không in ra màn hình) để dán vào Netlify.
python3 -c "import json,os;print(json.load(open(os.path.expanduser('~/.secrets/netlify/bang-viec.json')))['token'],end='')" | pbcopy && echo "Đã chép token vào clipboard — dán ngay vào Netlify (BV_TOKEN)."
