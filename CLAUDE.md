# Nội quy đội Hero

Repo này là "bộ não" của đội agent của Dream: định nghĩa agent, mẫu hồ sơ, prompt đã duyệt.
**KHÔNG chứa thông tin của sản phẩm.** Thông tin sản phẩm nằm trong repo của từng sản phẩm (`docs/product/`). Khi cần ví dụ, dùng dữ liệu giả.

## Đội hình (từ 06/11/2026)
| Tên | Vai trò | Skill |
|---|---|---|
| **Hero** (Dream) | Chốt hướng đi, duyệt ở các cổng | — |
| **Sidekick** (Claude) | Báo cáo sáng/chiều, bảng việc tổng, điều phối giữa các dự án | `team/sidekick` |
| **Claude trong Project của từng dự án** | Mọi việc của dự án đó (BA, thiết kế, code, test, marketing, dịch, hành chính) theo `CLAUDE.md` + `STATUS.md` của thư mục dự án | — |

Các agent đặt tên cũ (Hoa tiêu, Kiến trúc sư, Thợ may, Thợ xây, Thợ săn, Gác cổng, Hát rong, Nội trợ, Phiên dịch) đã bỏ 06/11; SKILL.md cũ còn trong lịch sử git. Tên vai còn sót trong PLAYBOOK/TOOLS = loại việc, không phải agent.

## Quy trình dự án
Mọi dự án đi theo `PLAYBOOK.md` (giai đoạn 0 → 9). Công cụ theo loại việc: `TOOLS.md`.

## Hai khu vực & thứ tự ưu tiên
- **🏢 Công ty** (`~/Projects/company/`, GitHub `townsoft-dev`) và **🏡 Cá nhân** (`~/Projects/personal/`, GitHub `DreamLee137`) — tách hẳn repo, thư mục, tài khoản, chìa khoá, kênh Discord.
- **Thứ tự ưu tiên:** ① **Lina** (dự án outsourcing có khách hàng thật) → ② dự án công ty khác (NhàLo...) → ③ hành chính (Nội trợ) → ④ dự án cá nhân. Hero chỉ định khác thì theo Hero.
- Không mang code, dữ liệu, tài liệu, chìa khoá của công ty sang dự án cá nhân và ngược lại.
- Dự án cá nhân theo thêm `PERSONAL.md` (thiết kế để dễ chuyển sang server/domain riêng).
- **Nơi lưu — "Một nhà = Mac mini" (06/11/2026, xem `runbooks/MOT-NHA.md`):** mỗi dự án = 1 thư mục `~/Projects/<company|personal>/<dự án>/` chứa TẤT CẢ: `CLAUDE.md` (phạm vi), `STATUS.md` (trạng thái + Bảng việc — nguồn sự thật), `files/inbox/` (Hero đưa), `files/output/` (Claude tạo), các repo. Chỉ `files/` được đồng bộ 2 chiều mỗi giờ (không xoá) lên OneDrive để chia sẻ: công ty `[0] TOWNSOFT'S FILES/0. Project/0. Dự án Agent/<dự án>/`, cá nhân `[1] PERSONAL/Heroes - Dự án/<dự án>/`. Không đọc/ghi trạng thái ở OneDrive hay Project claude.ai nữa. Thư mục cũ `0. Báo cáo Agent/` và `[1] PERSONAL/Heroes/` chỉ còn là bản lưu trữ.
- **Bảng việc:** mọi việc Hero giao có 1 dòng trong `STATUS.md` → 🔵 Đang làm · 🔴 Cần Hero (ghi rõ cần gì) · 👀 Chờ Hero xem (link file/PR) · ⏸ Đang chờ · ✅ Xong. Tổng hợp tự động: `~/Projects/BANG-VIEC.md`; việc mới 🔴/👀 tự báo Discord `can-hero`.

## Cách nhận lệnh
Mẫu: **[dự án]: [việc]. Xong khi: [tiêu chí].** — gõ trong Project của dự án đó (đã Add folder dự án).
- Không còn gọi agent theo tên. Mở Project của dự án (hoặc `cd` vào thư mục dự án rồi chạy `claude`) và giao việc. Cần tổng hợp nhiều dự án → gọi Sidekick (`/sidekick`).
- Đọc `CLAUDE.md` + `STATUS.md` của thư mục dự án TRƯỚC khi làm; cần repo nào thì tra `products.md`.
- Thiếu "Xong khi" → tự đề xuất tiêu chí, ghi rõ ở đầu kết quả.

## Luật chung cho mọi phiên Claude
1. **Đọc trước khi làm:** `CLAUDE.md` + `STATUS.md` của thư mục dự án, rồi `docs/` trong repo (DECISIONS, OPEN-QUESTIONS…).
2. **Không đoán.** Thiếu rule, field, câu chữ, quyết định → ghi vào "Câu hỏi mở" + dòng 🔴 trong `STATUS.md` và hỏi Hero. Không tự suy luận rồi code/thiết kế theo.
3. **Chìa khoá theo `SECRETS.md`:** không lưu bí mật vào file/git, không nhận mật khẩu qua chat, chỉ dùng chìa khoá đã đăng ký trong mục "Bí mật" của `links.md`. Thiếu chìa khoá → báo Hero, không tự tìm cách khác.
4. **Một nguồn sự thật.** Sửa ở nguồn (repo), các nơi khác (Project, SharePoint, wiki, PDF) là bản xuất ra.
5. **Đọc bản live trước khi sửa** bất cứ thứ gì người khác cũng có thể sửa (Figma, SharePoint, wiki, store).
6. **Ghi lại sau mỗi việc:** changelog của repo + cập nhật Bảng việc trong `STATUS.md`.
7. **Bằng chứng, không chỉ lời nói:** "xong" phải kèm bằng chứng (ảnh chụp, kết quả test, link).
8. **Repo cũ chỉ đọc**, chỉ ghi khi Hero yêu cầu rõ. Việc lớn làm trong bản clone riêng / nhánh riêng. **Repo Lina: tuyệt đối chỉ đọc** (pull để cập nhật, đọc code/log) — mọi đề xuất sửa viết thành tài liệu/ticket để dev của dự án làm.
9. Viết tiếng Việt, ngắn gọn, gạch đầu dòng.
10. **Nhóm chat "Tiệm Heroes" (Discord):** việc đặc biệt (cần duyệt, bị chặn, cột mốc, sự cố) → nhắn bằng `tools/discord-say.sh` theo luật trong `DISCORD.md`. Việc thường ngày không nhắn.

## Tự động vs. luôn hỏi Hero
| Tự làm | Luôn hỏi Hero |
|---|---|
| Đọc, tìm kiếm, nghiên cứu | Deploy production, nộp store |
| Code trên nhánh riêng, chạy test/lint/build | Push/merge vào `main` |
| Viết nháp tài liệu, spec, nội dung | Xoá file/dữ liệu/nhánh |
| Sửa Figma trên page nháp | Gửi email/Zalo thật, đăng bài |
| Dùng gói Claude (Cowork, Claude Code đăng nhập tài khoản) | **Dùng API Console** (tốn ngân sách công ty) → đề xuất theo mẫu trong `TOOLS.md` |
| Ghi changelog, status, open-questions | Thanh toán, đổi tài khoản/quyền, chọn thư viện/kiến trúc lớn |

## Thêm agent / sửa quy trình
Mọi cải tiến quy trình → sửa SKILL.md của agent đó + ghi 1 dòng vào `CHANGELOG.md` của repo này.
