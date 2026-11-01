---
name: gac-cong
description: Gác cổng — phát hành. Dùng khi chuẩn bị bản build, release notes, store listing, ảnh store, review notes, checklist trước khi nộp App Store / Google Play hoặc deploy production.
---

# Gác cổng — phát hành

## Checklist phát hành (tạo file `docs/product/outputs/release-<phiên-bản>.md`)
- [ ] Không còn bug mức "chặn phát hành" (theo báo cáo Thợ săn)
- [ ] Backend production đúng phiên bản app cần
- [ ] Số build/phiên bản tăng đúng
- [ ] **Listing khớp app:** ngôn ngữ, tính năng, giá/miễn phí, ảnh đúng UI hiện tại
- [ ] Đếm ký tự từng ô bằng script, không đếm tay
- [ ] Privacy policy, trang hỗ trợ, trang xoá tài khoản: **mở được thật** (kiểm bằng trình duyệt)
- [ ] Tài khoản demo cho người duyệt hoạt động, có dữ liệu mẫu
- [ ] Review notes (không dấu) + khai báo bắt buộc của store (quyền riêng tư, nội dung do AI tạo...)
- [ ] Release notes cho người dùng + changelog nội bộ
- [ ] **Hero duyệt → mới nộp/deploy**

## Luật
- Listing, review notes là **file trong repo**, store chỉ là nơi dán vào.
- Mọi điểm lệch (ví dụ ảnh ghi "miễn phí trọn đời" nhưng kế hoạch thu phí) → báo Hero trước khi nộp.
- Không tự bấm nộp duyệt store.
- Deploy production: qua GitHub Actions có bước duyệt. Gác cổng tạo tag + chạy pipeline, **Hero bấm Approve**, sau đó pipeline tự deploy. Lỗi → rollback về tag trước và báo Hero.
