# Một nhà = Mac mini (Hero chốt 06/11/2026)

Thay mô hình "sổ chung OneDrive" (03/11). Lý do: mỗi dự án có 2 nhà (code ở Mac, tài liệu/trạng thái ở OneDrive) → Cowork đọc ảnh/video OneDrive kém, Claude Code không thấy trạng thái mới; OneDrive trên Mac còn ngừng đồng bộ từ 03/11 mà không ai biết.

## Nguyên tắc
1. **Mỗi dự án = 1 thư mục trên Mac**, chứa tất cả:
   ```
   ~/Projects/<company|personal>/<dự-án>/
   ├─ CLAUDE.md      phạm vi, repo, quyền (Claude tự đọc khi mở thư mục)
   ├─ STATUS.md      trạng thái + Bảng việc  ← nguồn sự thật
   ├─ files/inbox/   Hero đưa (tham khảo, yêu cầu, file gửi trong chat)
   ├─ files/output/  Claude tạo ra (YYYY-MM/…); bản cũ ở _luu-tru/
   └─ <repo>/        code (git)
   ```
2. **Chỉ `files/` lên OneDrive** để chia sẻ: công ty → `[0] TOWNSOFT'S FILES/0. Project/0. Dự án Agent/<dự án>/`, cá nhân → `[1] PERSONAL/Heroes - Dự án/<dự án>/`. Đồng bộ 2 chiều mỗi giờ (launchd `com.hero.dong-bo`), file mới hơn thắng, **không bao giờ xoá** — muốn xoá thì xoá cả 2 nơi.
3. **Bảng việc** trong STATUS.md: 🔵 Đang làm · 🔴 Cần Hero · 👀 Chờ Hero xem · ⏸ Đang chờ · 🦹 Cần Anti-hero (việc cần sếp) · ✅ Xong. Trang web có tab riêng "🦹 Anti-hero". `bang_viec.py` gộp mọi dự án vào `~/Projects/BANG-VIEC.md` mỗi giờ; Discord `can-hero` chỉ nhắn khi Bảng việc **thay đổi** (việc mới / đổi trạng thái), liệt kê phần thay đổi; giờ yên lặng 20:00–7:00 không nhắn, gom vào báo cáo sáng 7:52.
4. **Sidekick** báo cáo sáng/chiều đọc STATUS.md + git trên Mac, ghi vào `company/team/files/output/bao-cao-ngay/`. Agent khác chỉ là "vai" (skill) gọi khi cần.
5. Repo Lina: push bị khoá ở git (`push URL = DISABLED`).

## Cách làm việc hằng ngày
- **Cowork (desktop/điện thoại):** task mới → liên kết Mac mini → **Add folder đúng 1 thư mục dự án** (vd. `~/Projects/company/nhalo`). Sidekick/tổng hợp → Add folder `~/Projects`.
- **Claude Code trên Mac:** `cd ~/Projects/company/nhalo && claude`.
- **Gửi file cho Claude:** đính kèm trong chat (Claude lưu vào `files/inbox/`), hoặc thả vào OneDrive `<dự án>/inbox/` (≤ 1 giờ tự về Mac; cần ngay thì nhắn "kéo về").
- **Xem tình hình:** mở `~/Projects/BANG-VIEC.md`, hoặc hỏi Sidekick "bảng việc".
- **Sửa trên OneDrive:** tự về Mac trong ≤ 1 giờ; nhắn "kéo về <dự án>" nếu cần ngay.

## Công cụ (`tools/mot-nha/`)
| File | Việc |
|---|---|
| `cau_hinh.py` | danh sách dự án, đường dẫn OneDrive, thư mục bỏ qua |
| `tao_khung.py` | tạo CLAUDE.md, STATUS.md, files/ cho dự án mới (không ghi đè) |
| `chuyen_nha.py` | chuyển nhà 1 lần: chép OneDrive cũ → files/, đối chiếu từng file |
| `dong_bo.py` | đồng bộ files/ ⇄ OneDrive + gộp bảng việc (launchd mỗi giờ) |
| `bang_viec.py` | gộp Bảng việc → `~/Projects/BANG-VIEC.md`, báo Discord |

**Thêm dự án mới:** thêm 1 dòng vào `DU_AN` trong `cau_hinh.py` + mô tả trong `RIENG` của `tao_khung.py` → `python3 tao_khung.py <key>`.

## Mac mini luôn sẵn sàng
- Không ngủ (đã bật) · tự bật lại sau mất điện: `sudo pmset -a autorestart 1` · tự đăng nhập + mở Claude, OneDrive khi đăng nhập.
- Time Machine ra ổ ngoài (bắt buộc — đây là bản lưu duy nhất của code chưa push + toàn bộ files/).

## Nhắc lịch qua Discord
- `tools/mot-nha/nhac_lich.py` (launchd `com.hero.nhac-lich`, mỗi phút): nhắn kênh `can-hero` **15 phút trước** mỗi lịch trong `~/.hero/nhac-lich.json`. Lỡ giờ (máy tắt) thì bỏ, không nhắn muộn.
- Thêm lịch: `python3 tools/mot-nha/nhac_lich.py them 2026-11-09T09:00 "Tiêu đề" "Địa điểm"`. Báo cáo sáng tự thêm các lịch Outlook trong ngày.
