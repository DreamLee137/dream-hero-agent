# 🏡 Dự án cá nhân của Dream

Dùng chung toàn bộ quy trình (`PLAYBOOK.md`), đội agent, rule như dự án công ty, cộng thêm các luật dưới đây.

## 1. Ranh giới với công ty
- **Ưu tiên việc công ty.** Dự án cá nhân chỉ chạy khi không có việc công ty đang chờ, hoặc Hero chỉ định.
- Repo trên GitHub `DreamLee137`, thư mục `~/Projects/personal/`, chìa khoá ở `~/.secrets/personal/`, kênh Discord riêng.
- Không dùng code, dữ liệu, thiết kế, tài liệu, chìa khoá, tài khoản dịch vụ của công ty.
- ⚠️ Hero tự kiểm tra chính sách công ty về việc dùng máy Mac mini, gói Claude và ngân sách API của công ty cho dự án cá nhân. **Không dùng ngân sách API 220 USD của công ty cho dự án cá nhân.**

## 2. Giai đoạn demo: chạy miễn phí trên nền tảng online
| Phần | Nơi chạy demo miễn phí (gợi ý) |
|---|---|
| Web / landing | GitHub Pages, Cloudflare Pages, Vercel, Netlify (tên miền phụ miễn phí) |
| Backend / API | Supabase (Postgres), Cloudflare Workers, Render (gói free) |
| Lưu file/ảnh | Cloudflare R2 hoặc Supabase Storage (chuẩn S3) |
| App mobile | Bản web build, APK cài trực tiếp (TestFlight cần tài khoản Apple Developer trả phí) |
| Email gửi đi | Gói free của Resend / Brevo |
Giới hạn của gói free (ngủ khi không dùng, giới hạn dung lượng) ghi vào `tech.md` của dự án.

## 3. Thiết kế "sẵn sàng chuyển nhà" (bắt buộc từ ngày đầu)
1. **Mọi cấu hình qua biến môi trường** (`.env`): URL, domain, DB, khoá. Không viết cứng domain/URL trong code.
2. **`docker-compose.yml` chạy được toàn bộ** hệ thống trên một máy. Đây là "vali" để chuyển sang server riêng.
3. **Database chuẩn PostgreSQL**, migration nằm trong repo. Không phụ thuộc tính năng độc quyền của nhà cung cấp; nếu buộc phải dùng (auth, storage, realtime), bọc qua một lớp riêng trong code để sau thay được.
4. **Lưu file qua chuẩn S3**: đổi nhà cung cấp chỉ cần đổi `.env`.
5. **Đường dẫn tương đối** trong frontend; API base URL lấy từ cấu hình.
6. **Sao lưu định kỳ**: script xuất DB + file, chạy hằng tuần.
7. **`MIGRATION.md`** trong repo: các bước chuyển từ nền tảng free sang server + domain riêng (DNS, SSL, biến môi trường, chuyển dữ liệu, kiểm tra sau chuyển). Thợ xây cập nhật mỗi khi thêm dịch vụ mới.
8. Gác cổng chạy thử "chuyển nhà" bằng docker-compose trên Mac mini mỗi bản phát hành lớn, để chắc chắn vali còn dùng được.
