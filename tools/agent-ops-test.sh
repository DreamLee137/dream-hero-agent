#!/bin/bash
# Kiểm tra quyền của dream-agent-deploy trên server Balheh (Hero chạy trên Mac mini).
# Cách dùng: bash ~/Projects/dream-hero-agent/tools/agent-ops-test.sh
S="ssh -i $HOME/.secrets/lightsail/dream-agent-deploy -o IdentitiesOnly=yes -o StrictHostKeyChecking=accept-new dream-agent-deploy@15.165.84.55"
echo "== 0. Đăng nhập + quyền sudo";             $S 'whoami; sudo -n -l 2>&1 | tail -2'
echo "== 1. NhàLo dev: xem (PHẢI ĐƯỢC)";         $S 'sudo -n /usr/local/sbin/agent-ops nhalo-dev ps 2>&1 | head -5'
echo "== 2. NhàLo prod: xem (PHẢI ĐƯỢC)";        $S 'sudo -n /usr/local/sbin/agent-ops nhalo-prod ps 2>&1 | head -4'
echo "== 3. NhàLo prod: restart (PHẢI BỊ CHẶN)"; $S 'sudo -n /usr/local/sbin/agent-ops nhalo-prod restart 2>&1'
echo "== 4. MOA Calendar (PHẢI BỊ CHẶN)";        $S 'sudo -n /usr/local/sbin/agent-ops moa-calendar ps 2>&1 | head -2'
echo "== 5. Docker trực tiếp (PHẢI BỊ CHẶN)";    $S 'docker ps 2>&1 | head -1; sudo -n docker ps 2>&1 | head -1'
