#!/bin/bash
# Cập nhật trạng thái 1 agent trong Tiệm Heroes.
# Cách dùng: tools/tiem-status.sh <agent> <state> "<việc đang làm>" [dự án]
#   agent: sidekick hoa-tieu kien-truc-su tho-may tho-xay tho-san gac-cong hat-rong noi-tro hero
#   state: working | idle | waiting | blocked | done | offline   (hero: online | offline)
set -euo pipefail
F="${TIEM_STATUS:-$HOME/.tiem-heroes/status.json}"
mkdir -p "$(dirname "$F")"
python3 - "$F" "$@" <<'PY'
import json, sys, os, datetime
f, agent, state = sys.argv[1], sys.argv[2], sys.argv[3]
task = sys.argv[4] if len(sys.argv) > 4 else ""
project = sys.argv[5] if len(sys.argv) > 5 else ""
try: d = json.load(open(f))
except Exception: d = {"agents": {}}
now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
if agent == "hero":
    d["hero_online"] = state == "online"
else:
    d.setdefault("agents", {})[agent] = {"state": state, "task": task, "project": project, "updated": now}
d["updated"] = now
tmp = f + ".tmp"; json.dump(d, open(tmp, "w"), ensure_ascii=False, indent=1); os.replace(tmp, f)
print(f"{agent}: {state} {task}")
PY
