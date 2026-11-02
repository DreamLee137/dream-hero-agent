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

## 💳 API Console — chỉ dùng khi được Hero duyệt
Mặc định **mọi việc chạy bằng gói Claude**, không dùng API. Claude Code luôn đăng nhập bằng tài khoản Claude, không bằng API key.
Khi một việc thực sự cần API, agent gửi đề xuất cho Hero (qua `#📢-can-hero`):
- Việc gì, vì sao gói Claude không làm được
- Model dùng (ưu tiên Haiku/Sonnet) + Batch API / prompt caching nếu áp dụng
- Ước tính chi phí/tháng + giới hạn chi tiêu đặt trong workspace
- Phương án thay thế không dùng API
Hero duyệt → ghi `docs/DECISIONS.md` của sản phẩm + đăng ký key trong `SECRETS.md`.

## Sidekick
| Công cụ | Dùng cho |
|---|---|
| 🔌 Microsoft 365: OneDrive/SharePoint | Thư mục báo cáo: bảng tổng hợp Excel + file báo cáo |
| 🔌 Outlook | Email cho Hero **2 lần/ngày**: 8:00 (kế hoạch hôm nay, ngắn) · 17:30 (tổng kết: đã làm · cần làm · đang chặn · cần Hero quyết) |
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

## Thợ xây — RULE: bộ cố định + bộ theo loại sản phẩm
**Rule:** Thợ xây luôn dùng **Bộ cố định**, cộng thêm **đúng 1 bộ theo loại** cho mỗi phần của sản phẩm (một sản phẩm có thể gồm nhiều phần, vd. NhàLo = Mobile + Backend + Zalo Mini App).
- Loại của từng phần ghi trong `docs/product/tech.md` ngay giai đoạn 0.
- Dùng công cụ **ngoài** danh sách này → hỏi Hero trước, được duyệt thì thêm vào đây.
- Stack mặc định là chuẩn công ty. Sản phẩm muốn khác → Hero chốt ở giai đoạn 2, ghi `docs/DECISIONS.md`.

### Bộ cố định (mọi sản phẩm)
| Công cụ | Dùng cho |
|---|---|
| Claude Code trên Mac mini | Viết code, chạy lệnh |
| Git + GitHub (`gh`) | Nhánh `feature/*`, Pull Request, Issues |
| GitHub Actions | CI: lint + test + build mỗi PR; deploy có duyệt (xem Gác cổng) |
| 🔌 Figma `get_design_context` | Lấy thiết kế theo node ID |
| `openapi.yaml` (hợp đồng API) | Giao tiếp FE ↔ BE |
| Docker | DB/Redis/dịch vụ chạy local |
| `.env` + `SECRETS.md` | Cấu hình và chìa khoá |
| `changelog/YYYY-MM-DD.md` | Nhật ký thay đổi |

### Bộ theo loại sản phẩm
| Loại | Stack mặc định | Build & chạy | Test (cùng Thợ săn) | Theo dõi lỗi sau phát hành | Phát hành |
|---|---|---|---|---|---|
| **Mobile app** | Flutter + Riverpod + go_router | Android Studio, Xcode, máy ảo + thiết bị thật | `flutter test`, Maestro | Firebase Crashlytics 🆓 *(đề xuất)* | Fastlane → TestFlight / Google Play |
| **Backend / API** | Java 21 + Spring Boot + PostgreSQL + Redis + Flyway | Maven, Docker | JUnit + test với DB tạm trong CI | Log server + Sentry Free *(đề xuất)* | GitHub Actions → server (AWS) |
| **Web app / trang quản trị** | React + Vite + Tailwind *(đề xuất)* | Node.js | Vitest, Playwright | Sentry Free *(đề xuất)* | GitHub Actions → hosting |
| **Landing page / website tĩnh** | HTML/Tailwind hoặc Astro *(đề xuất)* | Node.js | Playwright (kiểm link, form, mobile) | Google Search Console 🆓 | GitHub Actions → hosting |
| **Zalo Mini App** | React + Vite + Tailwind + zmp-ui | Zalo Mini App CLI/Studio | Playwright + máy thật trong Zalo | Log backend | Gửi Zalo duyệt 🖐️ |

*(đề xuất)* = chưa dùng ở công ty; lần đầu áp dụng cần Hero duyệt, sau đó bỏ chữ "đề xuất".

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

## Nội trợ
| Công cụ | Dùng cho |
|---|---|
| 🔌 Outlook | Lọc email hoá đơn, soạn email gửi kế toán (Hero duyệt) |
| 🔌 OneDrive/SharePoint | Lưu chứng từ, bảng theo dõi Excel |
| 🔌 Lịch Outlook | Hạn nộp, hạn thanh toán, gia hạn |

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

**Tài khoản Facebook:** đang dùng tài khoản số 1 của Hero làm admin. Muốn tách riêng → thêm người/tài khoản thứ 2 làm admin trong **Meta Business Portfolio** (không tạo tài khoản ảo, Meta có thể khoá).

**Sản xuất**
| Loại | Công cụ (thử nghiệm để chọn) |
|---|---|
| Ảnh | 🔌 Higgsfield · 🔌 Canva · Google AI Pro (Imagen) |
| Video | 🔌 Higgsfield · Google AI Pro (Veo/Flow, xem hạn mức của gói) · CapCut Free 🖐️ |
| Giọng đọc | ElevenLabs 💳 · Gemini TTS (Google AI Pro) · **đề xuất thêm:** Vbee / FPT.AI (giọng Việt tự nhiên, hợp người lớn tuổi) |
| Slide, tài liệu | 🔌 Gamma Free · Canva |

**Thử nghiệm công cụ (vòng 1, 2 tuần) · Ngân sách: chỉ dùng đồ miễn phí + đã có** (Higgsfield Plus, Google AI Pro, bản Free/dùng thử của Canva, CapCut, Gamma, ElevenLabs, Vbee)
- Cùng 1 kịch bản → làm bằng 2–3 công cụ/tổ hợp (vd. Higgsfield + ElevenLabs vs. Veo + Vbee).
- Chấm điểm: chất lượng (Hero chấm 1–5) · thời gian làm · chi phí/video · kết quả thật (lượt xem, tỉ lệ xem hết, bình luận).
- Ghi vào bảng Excel trên OneDrive → chọn tổ hợp thắng làm mặc định, lặp lại mỗi quý.
