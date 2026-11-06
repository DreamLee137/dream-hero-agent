#!/usr/bin/env python3
"""Tạo CLAUDE.md + STATUS.md + files/{inbox,output} cho mỗi dự án. KHÔNG ghi đè file đã có.
Cách dùng: python3 tao_khung.py [dự-án ...]"""
import os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cau_hinh import DU_AN, mac_dir, od_moi, OD

HOM_NAY = datetime.date.today().strftime("%d/%m/%Y")

RIENG = {
 "lina": ("Lina / SentinelLog — outsourcing khách Hàn, **ưu tiên số 1**.",
   "- `Lina-Security-Backend/`, `Lina-Security-Manager/` (FE) — 🔒 **CHỈ ĐỌC tuyệt đối**: không sửa, commit, tạo nhánh, push (push đã bị khoá ở git). Đề xuất sửa → viết tài liệu vào `files/output/` cho dev dự án.\n"
   "- Tài liệu chung của công ty: SharePoint `TOWNSOFTVINA / General / [0] Project / [2] SentinelLog - Lina Life Insurrance /` (Release/, Tham khảo/) — đọc qua connector Microsoft 365, không chép đè.\n"
   "- Bản dịch tiếng Hàn lưu `files/output/`. Lịch deploy & Release Note: xem STATUS.md."),
 "nhalo": ("NhàLo — app quản lý nhà trọ (bản Lite).",
   "- `biztown-rent/` (app Flutter + Mini App), `biztown-rent_Backend/`, `e2e-src/` — ✏️ làm trên `feature/nhalo-lite`; `main` = bản trên store, chỉ merge khi Hero duyệt. Hồ sơ sản phẩm: `biztown-rent/docs/` (CURRENT_STATUS, DECISIONS, OPEN-QUESTIONS, LINKS).\n"
   "- Release AAB/IPA, video, test-runs → `files/output/`. Marketing chung công ty: SharePoint `General/[0] Project/[7] NhàLo/Marketing/`."),
 "balheh": ("Balheh — sản phẩm công ty thay Discord + Trello.",
   "- `Balheh-Project/` (docs), `Balheh_PJT_BackEnd/`, `Balheh_PJT_FrontEnd/`, `Balheh_PJT_Mobile/`, `Balheh_Storage/` — 📝 Hero làm BA/PM/thiết kế/test/marketing: **chỉ sửa docs, không sửa src**."),
 "chinchu": ("ChinChu — dự án sắp làm.",
   "- `biztown-Chinchu-FrontEnd/` (web, quankd làm chính), `biztown-Chinchu-BackEnd/` (NestJS) — ✏️ Hero thỉnh thoảng sửa: luôn nhánh riêng + PR cho quankd.\n"
   "- Cặp với NhàLo: xem mục \"Dự án liên quan\"."),
 "homepages": ("Homepages — biztown-web (BizTown, NhàLo, Balheh, privacy/support/delete-account) và trang Townsoft.",
   "- `biztown-web/`, `townsoft-homepage/` — 📝→✏️ làm trên nhánh riêng + PR, Hero duyệt trước khi merge/deploy."),
 "noi-tro": ("Hành chính, nhân sự, chấm công, lương, hoá đơn, mua hàng.",
   "- Không có code. Mọi con số lấy từ file Excel thật; **không sửa file gốc**, bản tính mới để `files/output/YYYY-MM/`.\n"
   "- STATUS.md chỉ ghi việc/tiến độ, KHÔNG ghi số lương hay thông tin cá nhân. Không gửi email cho kế toán/nhân viên, chỉ soạn nháp. Skill: townsoft-cham-cong-thang, townsoft-phieu-luong."),
 "phien-dich": ("Phiên dịch Việt ⇄ Hàn ⇄ Anh.",
   "- Không có code. Bản dịch của một dự án để **trong thư mục dự án đó** (`files/output/`, hậu tố _KO/_VI/_EN); ở đây chỉ để bảng thuật ngữ, văn phong, bản dịch lẻ.\n"
   "- 합니다체 với khách/sếp, 해요체 với dev. Giữ nguyên thuật ngữ kỹ thuật, tên màn hình, mã. Không gửi bản dịch cho khách."),
 "team": ("Đội agent Hero, Sidekick, quy trình, báo cáo ngày.",
   "- Luật & skill đội: `~/Projects/dream-hero-agent/` (repo GitHub DreamLee137/dream-hero-agent).\n"
   "- Báo cáo ngày: `files/output/bao-cao-ngay/YYYY-MM-DD-{sang,chieu}.md`. Bảng việc tổng: `~/Projects/BANG-VIEC.md` (tự sinh).\n"
   "- Sổ cấp quyền truy cập + khoá: chỉ trên OneDrive `0. Báo cáo Agent/Quản trị truy cập/` — không chép về đây."),
 "nha-liu-lo": ("Nhà Líu Lo — app chia việc nhà (🏡 cá nhân).",
   "- `biztown-nhaliulo/` ✏️ — GitHub `DreamLee137`. Theo thêm `~/Projects/dream-hero-agent/PERSONAL.md`.\n"
   "- 🚫 Không mang code/dữ liệu/chìa khoá công ty vào đây và ngược lại."),
 "cong-ty-huong-noi": ("Công ty Hướng Nội — kênh video TikTok (🏡 cá nhân).",
   "- Chưa có repo. Theo `~/Projects/dream-hero-agent/PERSONAL.md`.\n"
   "- 🚫 Không mang dữ liệu/chìa khoá công ty vào đây và ngược lại."),
}

CLAUDE = """# {ten} — thư mục dự án

{mota}

**Đây là nơi DUY NHẤT chứa mọi thứ của dự án** (code, tài liệu, ảnh, video, trạng thái). Đọc/ghi ở đây, không đi tìm ở OneDrive hay Project claude.ai.
Phạm vi: chỉ làm trong thư mục này. Cần dự án khác → hỏi Hero. Luật chung: `~/Projects/dream-hero-agent/CLAUDE.md`.

## Đọc trước khi làm
1. `STATUS.md` — trạng thái + **Bảng việc**.
2. Tài liệu sản phẩm trong repo (nếu có, vd. `docs/`).

## Cấu trúc
- `STATUS.md` — sổ trạng thái (sửa tại chỗ, mới nhất ở trên).
- `files/inbox/` — tài liệu **Hero đưa** (tham khảo, yêu cầu). File Hero gửi trong chat → lưu vào `files/inbox/YYYY-MM-DD_<tên>`.
- `files/output/` — mọi thứ **Claude tạo ra** → `files/output/YYYY-MM/<tên>`. Bản cũ để `_luu-tru/`.
- Các thư mục repo — code (xem dưới).

## Bảng việc (bắt buộc với mọi việc Hero giao)
| Trạng thái | Khi nào |
|---|---|
| 🔵 Đang làm | vừa nhận việc |
| 🔴 Cần Hero | vướng, cần quyết, cần quyền/chìa khoá — ghi rõ **cần gì** |
| 👀 Chờ Hero xem | làm xong — ghi **link file trong files/output/** hoặc PR |
| ⏸ Đang chờ | chờ người khác/bên ngoài |
| ✅ Xong | Hero đã duyệt (giữ tối đa 10 dòng, cũ hơn chuyển xuống "Đã xong gần đây") |

- ID: `<MÃ>-<ddmm>-<số>` (vd. `{ma}-0611-1`). Đổi trạng thái → sửa đúng dòng + ngày cập nhật + dòng "Cập nhật lần cuối".
- Chuyển sang 🔴/👀 → nếu phiên có công cụ thông báo đẩy (PushNotification) thì gửi 1 dòng. Discord kênh `can-hero` tự nhắn trong ≤ 1 giờ.

## Đồng bộ OneDrive (để chia sẻ)
`files/` ⇄ OneDrive `{od}` — mỗi giờ, file mới hơn thắng, **không bao giờ xoá**.
Hero nhắn "kéo về" / "đẩy lên" → chạy `python3 ~/Projects/dream-hero-agent/tools/mot-nha/dong_bo.py {key}` (cần shell thật trên Mac: Claude Code hoặc Desktop Commander).

## Repo & quyền
{repo}

## Luôn hỏi Hero
Push/merge `main`, deploy, nộp store, xoá file/nhánh, gửi email/tin thật, thanh toán, dùng API Console.
"""

STATUS = """# STATUS — {ten}

Cập nhật lần cuối: {ngay} — Sidekick (chuyển nhà)

## Tóm tắt
- (Sidekick điền từ sổ cũ)

## Bảng việc
| ID | Việc | Trạng thái | Cần Hero gì / Kết quả ở đâu | Cập nhật |
|---|---|---|---|---|

## Quyết định gần đây

## Câu hỏi mở

## Đã xong gần đây

## Lịch sử
- Sổ cũ (OneDrive TRANG-THAI.md, tới {ngay}): `files/output/_luu-tru/TRANG-THAI-truoc-*.md`
"""

MA = {"lina": "LN", "nhalo": "NL", "balheh": "BH", "chinchu": "CC", "homepages": "HP", "noi-tro": "NT",
      "phien-dich": "PD", "team": "SK", "nha-liu-lo": "LL", "cong-ty-huong-noi": "HN"}

for k in (sys.argv[1:] or DU_AN):
    md = mac_dir(k); ten = DU_AN[k][2]
    for sub in ("files/inbox", "files/output/_luu-tru"):
        os.makedirs(os.path.join(md, sub), exist_ok=True)
    mota, repo = RIENG[k]
    od = od_moi(k).replace(OD + "/", "")
    for fn, body in (("CLAUDE.md", CLAUDE.format(ten=ten, mota=mota, ma=MA[k], od=od, key=k, repo=repo)),
                     ("STATUS.md", STATUS.format(ten=ten, ngay=HOM_NAY))):
        p = os.path.join(md, fn)
        if os.path.exists(p):
            print(f"giữ nguyên {p}"); continue
        open(p, "w", encoding="utf-8").write(body); print(f"tạo {p}")
