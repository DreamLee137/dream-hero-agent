# Bộ công cụ của đội

Ký hiệu: 🔌 đã kết nối với Claude (MCP) · 🌐 làm qua Chrome · 🖐️ Hero tự làm (agent chuẩn bị) · 🆓 miễn phí · 💳 trả phí
Công cụ mới → thêm vào đây + ghi `CHANGELOG.md`.

## Nguyên tắc chọn cách làm (tiết kiệm lượt dùng)
1. **Ưu tiên MCP/API** khi có. Lưu ý: làm qua Chrome thường **tốn hơn** MCP, vì agent phải chụp và đọc màn hình liên tục.
2. Chrome chỉ dùng khi không có kết nối (Facebook, Zalo OA, store...).
3. Việc lặp lại, đơn giản (đăng bài, điền form, đổi tên file) → dùng model nhẹ (Sonnet/Haiku). Việc cần suy nghĩ (spec, kiến trúc, review) → model mạnh.
4. Gom việc: làm một lần cho cả lô (10 bài, 20 ảnh) thay vì từng cái.
5. Có kết quả đo được thì mới đổi sang công cụ trả phí.

---

## Sidekick
| Công cụ | Dùng cho |
|---|---|
| 🔌 Microsoft 365: OneDrive/SharePoint | Thư mục báo cáo: bảng tổng hợp Excel + file báo cáo |
| 🔌 Outlook | Email hằng ngày cho Hero: việc đã làm · việc cần làm · đang chặn · cần Hero quyết |
| Scheduled tasks (Cowork) | Lịch báo cáo ngày/tuần |
| GitHub | Đọc git log, issue, PR để tổng hợp |

## Hoa tiêu
| Công cụ | Dùng cho |
|---|---|
| Claude tìm web 🆓 | Nghiên cứu chính, có nguồn + ngày |
| Gemini Deep Research (Google AI Pro) 🖐️ | Đối chiếu chéo các báo cáo lớn |
| Google Trends 🆓🌐 | Mức quan tâm theo từ khoá, khu vực, mùa |
| Đánh giá App Store / Google Play 🆓🌐 | Review của mình + đối thủ, tổng hợp hằng tháng |
| **Đề xuất thêm:** Meta Ad Library 🆓🌐 | Xem quảng cáo đang chạy của đối thủ (nội dung, thời gian chạy) |
| **Đề xuất thêm:** Google Maps 🆓🌐 | Đếm/khảo sát đối tượng theo khu vực (vd. nhà trọ quanh trường) |
| **Đề xuất thêm:** Hội nhóm Facebook, Voz, Tinhte 🆓🌐 | Nghe người dùng thật nói gì, dùng từ ngữ gì (chỉ đọc) |

## Kiến trúc sư
| Công cụ | Dùng cho |
|---|---|
| Repo `docs/` | Nguồn chính của spec, rule, quyết định |
| 🔌 FigJam | Sơ đồ luồng, scope map |
| 🔌 OneDrive / Gamma | Bản xuất đẹp gửi sếp/khách (Word, PDF, slide) |

## Thợ may
| Công cụ | Dùng cho |
|---|---|
| 🔌 Figma | UI/UX, prototype, ảnh store |
| 🔌 FigJam | Luồng màn hình |
| 🔌 Canva (Free → cân nhắc Pro) | Ảnh mạng xã hội, banner nhanh |
| 🔌 Higgsfield | Ảnh minh hoạ, mascot, tách nền, upscale |
| Google AI Pro (Gemini, Imagen) 🖐️ | Phương án tạo ảnh thứ hai để so sánh |
| **Đề xuất thêm:** Google Fonts, Lucide/Material icons, Coolors 🆓 | Font, icon, bảng màu |

## Thợ xây
| Công cụ | Dùng cho |
|---|---|
| Claude Code (Mac mini) | Code chính |
| GitHub | Repo, PR, Actions (CI) |
| 🔌 Figma `get_design_context` | Lấy thiết kế chính xác để code |
| Android Studio, Xcode, Docker | Build, máy ảo, chạy BE local |

## Thợ săn — chọn theo loại sản phẩm
| Loại sản phẩm | Test tự động | Test tay |
|---|---|---|
| App mobile | Maestro e2e + unit/widget test | Thiết bị thật iOS + Android |
| Web / trang quản trị / landing | Playwright | Chrome + điện thoại |
| Backend / API | Unit + integration test chạy trong GitHub Actions | Swagger/Postman |

Ghi chép: **GitHub Issues** (mỗi lỗi 1 issue, gắn nhãn mức độ) + **bảng Excel trên OneDrive** (test case, tỉ lệ đạt, gửi sếp). Excel lấy số liệu từ Issues, không ghi tay hai nơi.

## Gác cổng — tự deploy sau khi Hero duyệt
Đề xuất: **deploy qua GitHub Actions có bước duyệt**, không đưa khoá server trực tiếp cho agent.
1. Gác cổng chạy checklist → tạo tag phiên bản → GitHub Actions chuẩn bị deploy.
2. GitHub dừng chờ duyệt (environment `production` có người duyệt là Hero).
3. Hero bấm **Approve** (được cả trên GitHub Mobile) → tự deploy.
4. Lỗi → Gác cổng chạy rollback về tag trước.
Cần phối hợp anh Tính để dựng pipeline lần đầu. Store: Fastlane + App Store Connect API Key + Google Play service account.

## Hát rong
**Kênh**
| Kênh | Cách làm |
|---|---|
| Facebook Fanpage | Meta Business Suite 🌐: Hát rong soạn + lên lịch, Hero duyệt |
| Quảng cáo Facebook | Ads Manager 🌐: Hát rong chuẩn bị nội dung, tệp đối tượng, ngân sách, chỉ số dừng → **Hero bấm chạy và trả tiền** 🖐️ |
| Hội nhóm Facebook | **Hát rong soạn bài, Hero/CTV tự đăng** 🖐️ (xem lưu ý bên dưới) |
| Zalo OA | Trang quản lý OA 🌐: bài viết, tin chào, menu. Tin ZNS gửi qua backend |
| TikTok, YouTube | Hát rong viết kịch bản + chuẩn bị video, Hero duyệt rồi đăng |

⚠️ **Hội nhóm Facebook:** dùng công cụ tự động đăng bài hàng loạt vào nhóm của người khác vi phạm quy định của Meta, dễ bị khoá tài khoản cá nhân lẫn Fanpage. Cách bền vững:
- Lập **nhóm riêng của sản phẩm** (vd. "Cộng đồng chủ trọ"), Fanpage làm admin → Hát rong lên nội dung cho nhóm này.
- Nhóm của người khác: Hát rong soạn bài hữu ích (không quảng cáo lộ liễu) + danh sách nhóm phù hợp, người thật đăng và trả lời bình luận.

**Sản xuất**
| Loại | Công cụ (thử nghiệm để chọn) |
|---|---|
| Ảnh | 🔌 Higgsfield · 🔌 Canva · Google AI Pro (Imagen) |
| Video | 🔌 Higgsfield · Google AI Pro (Veo/Flow, xem hạn mức của gói) · CapCut Free 🖐️ |
| Giọng đọc | ElevenLabs 💳 · Gemini TTS (Google AI Pro) · **đề xuất thêm:** Vbee / FPT.AI (giọng Việt tự nhiên, hợp người lớn tuổi) |
| Slide, tài liệu | 🔌 Gamma Free · Canva |

**Thử nghiệm công cụ (vòng 1, 2 tuần)**
- Cùng 1 kịch bản → làm bằng 2–3 công cụ/tổ hợp (vd. Higgsfield + ElevenLabs vs. Veo + Vbee).
- Chấm điểm: chất lượng (Hero chấm 1–5) · thời gian làm · chi phí/video · kết quả thật (lượt xem, tỉ lệ xem hết, bình luận).
- Ghi vào bảng Excel trên OneDrive → chọn tổ hợp thắng làm mặc định, lặp lại mỗi quý.
