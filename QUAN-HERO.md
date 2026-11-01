# ☕ Quán Hero: nhóm chat & văn phòng của đội

## 1. Nhóm chat Discord "Quán Hero"

### Kênh
| Kênh | Dùng cho | Ai nhắn |
|---|---|---|
| `#☕-quay-chung` | Tin đặc biệt của cả đội: cột mốc, phát hành xong, chào tuần mới, khen nhau | Mọi agent |
| `#🔔-can-hero` | Cần Hero duyệt/quyết, có việc bị chặn | Mọi agent |
| `#🚨-khan-cap` | Sự cố: production lỗi, build hỏng, nghi lộ chìa khoá | Mọi agent (kèm @Hero) |
| `#🌿-<san-pham>` | Tin của riêng từng sản phẩm (vd. `#🌿-nhalo`) | Agent làm sản phẩm đó |
| `#📮-hero-giao-viec` | Hero ghi chú việc nhanh từ điện thoại; Sidekick đọc khi bắt đầu phiên (giai đoạn 2) | Hero |

### Khi nào nhắn (luật)
**Nhắn** khi: cần Hero duyệt · bị chặn > 30 phút · xong một cột mốc (spec chốt, bản build mới, phát hành) · test/CI hỏng trên `main` · sự cố production · phát hiện rủi ro (pháp lý, bảo mật, chi phí).
**Không nhắn** việc thường ngày: những việc đó vào báo cáo email 8:00/17:30.
Mỗi tin ≤ 5 dòng: **[sản phẩm] chuyện gì · ảnh hưởng · cần Hero làm gì (nếu có) · link**.

### Cách hoạt động
- **Giai đoạn 1 (tuần 2):** agent gửi tin qua **webhook** bằng `tools/discord-say.sh`. Một webhook mỗi kênh, tên và biểu tượng thay đổi theo từng agent, nên trong nhóm trông như 8 thành viên riêng. Hero trả lời/giao việc trong Cowork hoặc Claude Code.
- **Giai đoạn 2 (sau này):** thêm **bot Discord** chạy trên Mac mini để agent đọc được tin Hero nhắn trong nhóm (giao việc từ điện thoại ngay trong Discord).
- Webhook URL là bí mật → cất ở `~/.secrets/discord/<kenh>.url`, đăng ký trong `SECRETS.md`.

### Hero cần làm (≈ 10 phút, làm được trên điện thoại)
1. Tạo server Discord "Quán Hero" (riêng tư).
2. Tạo các kênh ở bảng trên.
3. Mỗi kênh: Cài đặt kênh → Tích hợp → Webhook → Tạo → Sao chép URL.
4. Trên Mac mini: dán từng URL vào `~/.secrets/discord/quay-chung.url`, `can-hero.url`, `khan-cap.url`, `nhalo.url`.
5. Bật thông báo điện thoại cho `#🔔-can-hero` và `#🚨-khan-cap`; tắt bớt các kênh còn lại.

---

## 2. Văn phòng pixel: concept "Quán cà phê sân vườn"

**Không khí:** chill, yên bình, lo-fi. Ánh nắng xuyên qua giàn cây, tiếng nước chảy từ hồ cá, mưa nhẹ buổi chiều. Ngày/đêm theo giờ thật Việt Nam. Động vật tự do đi lại.

### Bố cục & chỗ ngồi
| Agent | Chỗ ngồi | Hành động khi đang làm việc |
|---|---|---|
| ☕ **Sidekick** | Quầy pha chế ở giữa quán | Pha cà phê, đưa giấy giao việc cho mọi người |
| 🧭 **Hoa tiêu** | Bàn cạnh cửa sổ, bản đồ + ống nhòm nhìn ra vườn | Lật bản đồ, ghi chép |
| 📐 **Kiến trúc sư** | Bàn gỗ dài, trải bản vẽ | Đo vẽ, dán giấy note |
| 🧵 **Thợ may** | Góc sáng nhiều cây, giá vẽ + máy may | Vẽ, phối màu |
| 🔨 **Thợ xây** | Nhà kính trong vườn, bàn làm việc | Gõ máy, xếp gạch |
| 🏹 **Thợ săn** | Bên hồ cá koi, cầm vợt | Vớt "bọ" (bug) lên khỏi hồ |
| 🛡️ **Gác cổng** | Cổng vườn có chuông gió, cạnh chú chó | Kiểm tra từng "kiện hàng" trước khi mở cổng |
| 🎤 **Hát rong** | Sân khấu nhỏ dưới gốc cây | Đàn hát, chụp ảnh, quay video |
| 🦸 **Hero** | Ghế xích đu giữa vườn | Xuất hiện khi Hero online |

### Động vật (welcome!)
- 🐈 Mèo cam ngủ trên quầy Sidekick, thỉnh thoảng đi dạo qua các bàn.
- 🐕 Chó nhỏ nằm cạnh Gác cổng, vẫy đuôi khi có bản phát hành mới.
- 🐟 Đàn cá koi trong hồ của Thợ săn.
- 🐦 Chim sẻ đậu trên giàn cây, bay đi khi có tin khẩn.

### Trạng thái hiển thị
| Trạng thái thật | Trong quán |
|---|---|
| Đang làm việc | Ngồi đúng chỗ, có hoạt ảnh làm việc |
| Rảnh | Ra vườn uống cà phê, ngắm cá, vuốt mèo |
| Chờ Hero duyệt | Giơ tay + chuông nhỏ trên quầy rung |
| Bị chặn / lỗi | Đèn bàn chuyển cam, mây nhỏ trên đầu |
| Phát hành thành công | Đèn dây trong vườn sáng lên, chó vẫy đuôi |
| Sự cố khẩn | Chim bay đi, đèn quầy nhấp nháy |

### Kỹ thuật (để rà soát repo mã nguồn mở sau)
- Nguồn dữ liệu: log/hooks của Claude Code + trạng thái từ GitHub + tin Discord → một file trạng thái chung → web pixel đọc và hiển thị.
- Ưu tiên repo mã nguồn mở đã có sẵn, thay "da" (tileset) theo concept quán cà phê.
- Chạy trên Mac mini, xem được từ MacBook và điện thoại qua Tailscale.
