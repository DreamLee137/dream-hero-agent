#!/usr/bin/env bash
# Gửi tin vào nhóm Discord "Tiệm Heroes" dưới tên của một agent.
# Cách dùng: tools/discord-say.sh <agent> <kenh> "<noi dung>"
#   agent: sidekick | claude
#   kenh : tên file webhook trong ~/.secrets/discord/ (bao-cao | can-hero | khan-cap)
set -euo pipefail
agent="${1:?thiếu agent}"; kenh="${2:?thiếu kênh}"; msg="${3:?thiếu nội dung}"
hook_file="$HOME/.secrets/discord/${kenh}.url"
[ -f "$hook_file" ] || { echo "Chưa có webhook cho kênh '$kenh' ($hook_file)"; exit 1; }
case "$agent" in
  sidekick) name="☕ Sidekick" ;;
  claude)   name="🤖 Claude" ;;
  *) echo "Agent không hợp lệ: $agent (sidekick | claude)"; exit 1 ;;
esac
avatar_base="${HERO_AVATAR_BASE:-}"   # để trống cho tới khi có avatar pixel
payload=$(python3 -c 'import json,sys; a=sys.argv; d={"username":a[1],"content":a[2][:1900]}; 
d.update({"avatar_url":a[3]+"/"+a[4]+".png"} if a[3] else {}); print(json.dumps(d))' "$name" "$msg" "$avatar_base" "$agent")
curl -fsS -H "Content-Type: application/json" -d "$payload" "$(cat "$hook_file")" >/dev/null && echo "Đã gửi."
