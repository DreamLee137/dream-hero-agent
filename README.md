# dream-hero-agent

Đội agent cá nhân của Dream (Hero). Xem `CLAUDE.md` để biết nội quy và đội hình.

## Cấu trúc
```
CLAUDE.md            nội quy + đội hình
PLAYBOOK.md          quy trình dự án từ 0 đến hoàn thành
SECRETS.md           quy tắc chìa khoá: cất ở đâu, đăng ký thế nào
TOOLS.md             công cụ của từng agent + nguyên tắc tiết kiệm
PERSONAL.md          quy tắc dự án cá nhân (demo miễn phí, dễ chuyển server)
DISCORD.md           kênh tin nhắn Discord (webhook, luật nhắn)
runbooks/MOT-NHA.md  "Một nhà = Mac mini": thư mục dự án, đồng bộ OneDrive, bảng việc
web/bang-viec/       trang Bảng việc trên Netlify
tools/               script dùng chung (discord-say.sh, mot-nha/)
products.md          danh bạ sản phẩm (tên + repo)
team/sidekick/SKILL.md  Sidekick (báo cáo, bảng việc tổng)
templates/product/   mẫu hồ sơ sản phẩm (copy vào docs/product/ của repo sản phẩm)
CHANGELOG.md         lịch sử cải tiến quy trình
```

## Cài lên máy (Mac mini / MacBook)
```bash
git clone https://github.com/DreamLee137/dream-hero-agent.git ~/dream-hero-agent
mkdir -p ~/.claude/skills && ln -sfn ~/dream-hero-agent/team/sidekick/ ~/.claude/skills/sidekick
```
Symlink giúp mỗi lần `git pull` là mọi phiên Claude Code có skill mới nhất.
