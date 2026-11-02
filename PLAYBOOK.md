# Quy trình dự án: từ con số 0 đến hoàn thành

Áp dụng cho mọi sản phẩm. Mỗi giai đoạn ghi rõ: **Hero cung cấp gì · Agent làm gì · Kết quả lưu ở đâu · Cổng duyệt**.
Quy tắc về chìa khoá/mật khẩu: xem `SECRETS.md`.

---

## Giai đoạn 0 · Khởi tạo (≈ 1 giờ)
**Hero cung cấp**
- Tên sản phẩm, mô tả 2–3 câu, ai là người quyết định (Hero, sếp...)
- Hạn chót, ngân sách (nếu có)
- Quyền truy cập: tạo/cho Hero quyền vào repo trên GitHub công ty, file Figma, nơi lưu tài liệu
- Tài liệu sẵn có (biên bản họp, yêu cầu khách...)

**Sidekick làm**
- **Repo mới / chưa có docs:** thêm `docs/product/` từ `templates/product/` + đoạn `CLAUDE-snippet.md` vào `CLAUDE.md`
- **Repo đã có docs** (vd. NhàLo): KHÔNG tạo thư mục mới. Thêm `docs/README.md` làm mục lục (mỗi chủ đề 1 file nguồn), cập nhật file cũ tại chỗ, gộp file trùng, chỉ thêm `LINKS.md` + `OPEN-QUESTIONS.md` nếu chưa có, file lỗi thời → `docs/_archive/` (không xoá)
- Thêm 1 dòng vào `products.md`
- Clone về Mac mini: `~/Projects/<san-pham>/` (FE, BE cùng thư mục)
- Điền `links.md`, mục "Bí mật" ghi các chìa khoá sẽ cần (chưa có giá trị)

**Cổng duyệt:** Hero xác nhận `brief.md` bản nháp.

## Giai đoạn 1 · Nghiên cứu — Hoa tiêu
**Hero cung cấp:** câu hỏi cần trả lời, người dùng thật có thể hỏi/phỏng vấn (nếu có), đối thủ đã biết.
**Kết quả:** `docs/product/outputs/research-*.md` (persona, đối thủ, pháp lý, khả thi bên thứ 3 + chi phí).
**Cổng duyệt:** Hero chốt có làm tiếp không, nhắm vào ai.

## Giai đoạn 2 · Phạm vi & Spec — Kiến trúc sư
**Hero cung cấp:** ưu tiên tính năng, trả lời `open-questions.md`.
**Kết quả:** trang "Phạm vi bản 1: làm / không làm / để sau" → requirements, business rules, user flows, screen spec (`docs/`), quyết định vào `docs/DECISIONS.md`.
**Cổng duyệt:** ⛔ **CHỐT PHẠM VI.** Sau cổng này, mọi thay đổi phạm vi phải qua Sidekick đánh giá tác động.

## Giai đoạn 3 · Thiết kế — Thợ may
**Hero cung cấp:** link file Figma (hoặc để Thợ may tạo), brand/logo, ví dụ app thích.
**Kết quả:** Figma (ID node ghi vào `links.md`), đủ trạng thái màn, prototype.
**Cổng duyệt:** Hero duyệt thiết kế từng cụm màn.

## Giai đoạn 4 · Phát triển — Thợ xây
**Hero cung cấp (chìa khoá — xem `SECRETS.md`)**
- Quyền push repo công ty (qua tài khoản GitHub đã đăng nhập trên Mac mini)
- File `.env` cho dev (DB, dịch vụ bên thứ 3) — đặt trực tiếp lên Mac mini, không gửi qua chat
- Tài khoản/khoá dịch vụ: Firebase, Zalo, email, cloud... (bản dev/test trước)

**Kết quả:** code trên nhánh `feature/*`, hợp đồng API (`openapi.yaml`), `tech.md` cập nhật, changelog.
**Cổng duyệt:** Hero duyệt Pull Request trước khi merge `main`.

## Giai đoạn 5 · Kiểm thử — Thợ săn
**Hero cung cấp:** thiết bị thật (hoặc cho phép dùng máy ảo), tài khoản test, dữ liệu mẫu thật (đã ẩn thông tin cá nhân).
**Kết quả:** `outputs/test-*.md` (tỉ lệ đạt), issue GitHub cho mỗi lỗi.
**Cổng duyệt:** không còn lỗi mức "chặn phát hành".

## Giai đoạn 6 · Phát hành — Gác cổng
**Hero cung cấp (chìa khoá):** App Store Connect API Key (`.p8`), Google Play service account (`.json`), quyền deploy server (hoặc người phụ trách server), tài khoản demo cho người duyệt store.
**Kết quả:** `outputs/release-<phiên-bản>.md` (checklist), listing + release notes trong repo.
**Cổng duyệt:** ⛔ **Hero bấm nộp store / cho phép deploy production.**

## Giai đoạn 7 · Marketing — Hát rong
**Hero cung cấp:** ngân sách, kênh được phép dùng, quyền vào trang/kênh (Fanpage, TikTok, YouTube, Zalo OA...), brand guideline.
**Kết quả:** kế hoạch + lịch nội dung + bài nháp (`outputs/marketing/`), báo cáo tuần bằng số liệu thật.
**Cổng duyệt:** Hero duyệt trước khi đăng/chi tiền.

## Giai đoạn 8 · Vận hành & nâng cấp (lặp lại)
- Lịch tự động: Sidekick báo cáo sáng; Thợ săn chạy test hằng đêm; Hát rong báo cáo tuần; Hoa tiêu theo dõi đánh giá store + đối thủ hằng tháng.
- Mỗi bản nâng cấp đi lại vòng 2 → 6 (bản thu nhỏ).
- Mỗi tháng: rà `SECRETS.md`, đổi chìa khoá sắp hết hạn.

## Giai đoạn 9 · Kết thúc / bàn giao
- `status.md` ghi trạng thái cuối, `retro.md` (đã tốt / cần sửa) → cập nhật SKILL.md của agent liên quan.
- **Thu hồi toàn bộ chìa khoá** đã cấp cho agent của dự án.
- Bàn giao: người tiếp nhận chỉ cần đọc `docs/product/`.
