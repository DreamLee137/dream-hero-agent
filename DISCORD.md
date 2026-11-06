# Discord "Tiệm Heroes" — kênh tin nhắn của đội

_06/11/2026: bỏ văn phòng pixel/quán cafe; Discord chỉ còn là kênh tin nhắn + thông báo đẩy về điện thoại. Việc 🔴/👀 do `tools/mot-nha/bang_viec.py` tự báo vào `can-hero`._

### Kênh (dọn 06/11/2026 — chỉ còn 3)
| Kênh | Dùng cho | Ai nhắn |
|---|---|---|
| `#📑-bao-cao` | Báo cáo sáng + cuối ngày, tổng kết tuần | Sidekick |
| `#📢-can-hero` | Việc mới chuyển 🔴 cần Hero / 👀 chờ Hero xem (tự động từ `bang_viec.py`) | Sidekick, Claude |
| `#🚨-khan-cap` | Sự cố: production lỗi, build hỏng, nghi lộ chìa khoá | Claude (kèm @Hero) |

### Khi nào nhắn (luật)
**Nhắn** khi: cần Hero duyệt · bị chặn > 30 phút · xong một cột mốc (spec chốt, bản build mới, phát hành) · test/CI hỏng trên `main` · sự cố production · phát hiện rủi ro (pháp lý, bảo mật, chi phí).
**Không nhắn** việc thường ngày: những việc đó vào báo cáo email 8:00/17:30.
Mỗi tin ≤ 5 dòng: **[sản phẩm] chuyện gì · ảnh hưởng · cần Hero làm gì (nếu có) · link**.

### Cách hoạt động
- **Giai đoạn 1 (tuần 2):** agent gửi tin qua **webhook** bằng `tools/discord-say.sh`. Một webhook mỗi kênh. Hero trả lời/giao việc trong Cowork hoặc Claude Code.
- **Giai đoạn 2 (sau này):** thêm **bot Discord** chạy trên Mac mini để agent đọc được tin Hero nhắn trong nhóm (giao việc từ điện thoại ngay trong Discord).
- Webhook URL là bí mật → cất ở `~/.secrets/discord/<kenh>.url`, đăng ký trong `SECRETS.md`.

### Hero cần làm: tạo webhook (≈ 10 phút, nên làm trên máy tính)
Webhook = một "khe thư" riêng của từng kênh. Ai có link thì bỏ thư vào kênh đó được (chỉ gửi, không đọc được) → coi như chìa khoá, không chia sẻ.
1. Mở Discord trên máy tính, vào server **Tiệm Heroes**.
2. Rê chuột vào kênh (vd. `#☕-quay-chung`) → bấm **⚙️ (Edit Channel / Chỉnh sửa kênh)**.
3. Chọn **Integrations (Tích hợp)** → **Webhooks** → **New Webhook (Webhook mới)**.
4. Đặt tên `Tiệm Heroes` (tên thật sẽ đổi theo từng agent khi gửi) → **Copy Webhook URL**.
5. Mở Terminal trên Mac mini, lưu link (thay `<LINK>` bằng link vừa copy):
   ```bash
   mkdir -p ~/.secrets/discord && chmod 700 ~/.secrets ~/.secrets/discord
   pbpaste > ~/.secrets/discord/quay-chung.url && chmod 600 ~/.secrets/discord/quay-chung.url
   ```
   (`pbpaste` dán thẳng nội dung vừa copy; nếu copy trên máy khác thì dùng `nano ~/.secrets/discord/quay-chung.url` rồi dán.)
6. Lặp lại cho các kênh còn lại, tên file: `bao-cao.url`, `can-hero.url`, `khan-cap.url`, `nhalo.url`.
7. Thử: `~/dream-hero-agent/tools/discord-say.sh sidekick quay-chung "Tiệm mở cửa rồi! ☕"`
8. Trên điện thoại: bật thông báo cho `#📢-can-hero`, `#🚨-khan-cap`, `#📑-bao-cao`; tắt bớt các kênh còn lại.

---
