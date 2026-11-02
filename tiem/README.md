# ☕🎶 Tiệm Heroes — văn phòng pixel

Chạy trên Mac mini: `node tiem/server.js` → mở http://localhost:4747

- Tự vẽ hoàn toàn bằng code (không dùng hình/nhạc có bản quyền). Nhạc lo-fi tự sinh bằng WebAudio, đổi theo giờ Việt Nam.
- Trạng thái đọc từ `~/.tiem-heroes/status.json`. Chưa có file → **chế độ xem thử**.
- Agent cập nhật trạng thái: `tools/tiem-status.sh <agent> <working|idle|waiting|blocked|done|offline> "<việc>" [dự án]`
- Hero: `tools/tiem-status.sh hero online` / `offline`
- Bấm vào nhân vật → xem việc đang làm, mở kênh Discord, copy câu giao việc.

## Giai đoạn sau
- Tự cập nhật trạng thái từ log/hook của Claude Code (không cần agent gọi script).
- Bấm nhân vật → chat trực tiếp với agent đó.
- Xem từ MacBook/điện thoại qua Tailscale.
