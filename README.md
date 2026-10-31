# dream-hero-agent

Đội agent cá nhân của Dream (Hero). Xem `CLAUDE.md` để biết nội quy và đội hình.

## Cấu trúc
```
CLAUDE.md            nội quy + đội hình
products.md          danh bạ sản phẩm (tên + repo)
team/<agent>/SKILL.md   định nghĩa từng agent
templates/product/   mẫu hồ sơ sản phẩm (copy vào docs/product/ của repo sản phẩm)
inbox/               hộp thư tham khảo: skill, prompt, repo chờ Sidekick rà soát
prompts/             prompt đã duyệt
CHANGELOG.md         lịch sử cải tiến quy trình
```

## Cài lên máy (Mac mini / MacBook)
```bash
git clone https://github.com/DreamLee137/dream-hero-agent.git ~/dream-hero-agent
mkdir -p ~/.claude/skills
for d in ~/dream-hero-agent/team/*/; do ln -sfn "$d" ~/.claude/skills/$(basename "$d"); done
```
Symlink giúp mỗi lần `git pull` là mọi phiên Claude Code có skill mới nhất.
