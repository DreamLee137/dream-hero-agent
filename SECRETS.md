# Quy tắc chìa khoá (mật khẩu, token, key)

## 5 luật cứng
1. **Không gửi mật khẩu/key qua chat**, kể cả cho Sidekick. Hero tự đặt lên Mac mini.
2. **Không bao giờ commit bí mật** vào git (kể cả repo private). Grep trước mỗi commit.
3. **Mỗi việc một chìa khoá, quyền tối thiểu, có hạn dùng** (tối đa 90 ngày nếu được chọn).
4. **Không dùng mật khẩu tài khoản chính cho tự động hoá.** Dùng token/key thu hồi được.
5. **Nghi lộ → thu hồi ngay → tạo cái mới → ghi lại.**

## Cất ở đâu (trên Mac mini)
| Loại | Nơi cất |
|---|---|
| Đăng nhập GitHub (cá nhân + công ty) | `gh auth login` → macOS Keychain |
| SSH key | `~/.ssh/` (quyền 600) |
| File `.env` của dự án | `~/Projects/<san-pham>/<repo>/.env` (đã có trong `.gitignore`) |
| File khoá (`.p8`, `.json` service account...) | `~/.secrets/<san-pham>/` (quyền 700, ngoài mọi repo) |
| Mật khẩu người dùng cần nhớ | Trình quản lý mật khẩu của Hero (không phải file) |

## Hiện trạng trên Mac mini (02/11/2026)
- `~/.secrets/{discord,nhalo,personal,lightsail}` — đã tạo, quyền 700.
- `~/SSH-Keys/` — khoá SSH server (Lightsail Balheh, Lina), giữ nguyên chỗ cũ vì cấu hình đang trỏ tới; đã chỉnh quyền về 600. `LightsailDefaultKey` là khoá cũ đã gỡ khỏi Lightsail → xoá file.
- Ai có quyền gì trên server/DB/tài khoản: **Sổ cấp quyền** (OneDrive `0. Báo cáo Agent/Quản trị truy cập/`), Nội trợ giữ sổ.
- `~/keystores/nhalo/` — keystore ký app Android (key.properties trỏ tới).
- `~/.appstoreconnect/private_keys/` — khoá App Store Connect.
- ⚠️ Việc Hero cần xử lý: chuyển nội dung 2 file `passphrase*.rtf` vào trình quản lý mật khẩu rồi xoá file; khoá riêng (private key) của người khác (dev/khách) nên để chính họ giữ — xác nhận rồi gỡ khỏi máy.

## Sổ đăng ký chìa khoá (chỉ ghi TÊN, không ghi giá trị)
Mỗi sản phẩm có mục **"Bí mật"** trong `docs/product/links.md`:

| Tên | Dùng cho | Cất ở | Chủ sở hữu | Hết hạn | Agent dùng |
|---|---|---|---|---|---|
| `GH token townsoft-dev` | push repo app/BE | Keychain | Hero | 2027-02-01 | Thợ xây, Gác cổng |
| `ASC_API_KEY` | upload TestFlight | `~/.secrets/<sp>/AuthKey.p8` | Hero | không | Gác cổng |
| `.env dev` | chạy local | repo/.env | Hero | — | Thợ xây |
| `discord/<kenh>.url` | Webhook nhóm "Tiệm Heroes" | `~/.secrets/discord/` | Hero | không (tạo lại nếu lộ) | Mọi agent |

## GitHub: cá nhân vs. công ty
- Nếu tài khoản `DreamLee137` là thành viên org `townsoft-dev` → **một lần `gh auth login`** dùng được cho cả hai.
- Cần giới hạn chặt hơn cho agent chạy tự động → tạo **fine-grained token riêng cho từng org** (chỉ chọn repo cần, quyền Contents + Pull requests, hạn 90 ngày).
- Không thêm quyền admin org cho token của agent.
- ⚠️ `DreamLee137` có quyền **admin** org `townsoft-dev` → khi agent dùng phiên `gh` đã đăng nhập, agent cũng có quyền admin. Vì vậy **cấm agent** chạy các lệnh quản trị: xoá/đổi tên/chuyển repo, đổi visibility, sửa branch protection, quản lý thành viên/quyền, xoá release/tag, `gh api` với phương thức DELETE/PATCH/PUT vào cài đặt org/repo. Đặt các lệnh này vào danh sách `deny` của `.claude/settings.json`. Khi cần, Hero tự làm.

## 2FA
- App xác thực 6 số (TOTP) dùng bình thường, không cần đổi.
- Cất **recovery codes** của GitHub vào trình quản lý mật khẩu.
- GitHub Mobile là tuỳ chọn, tiện để duyệt PR / đăng nhập từ điện thoại.
