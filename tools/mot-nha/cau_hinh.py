# Cấu hình "Một nhà = Mac mini" — danh sách dự án và nơi sao lưu trên OneDrive.
# Sửa ở đây khi thêm/bớt dự án. Không chứa bí mật.
import os

HOME = os.path.expanduser("~")
PROJECTS = os.path.join(HOME, "Projects")
OD = os.path.join(HOME, "Library/CloudStorage/OneDrive-TOWNSOFTVINA")

# Bản cũ (chỉ dùng khi chuyển nhà 06/11/2026)
OD_CU_CTY = os.path.join(OD, "[0] TOWNSOFT'S FILES/0. Project/0. Báo cáo Agent")
OD_CU_CANHAN = os.path.join(OD, "[1] PERSONAL/Heroes")

# Nơi sao lưu files/ mới (Mac -> OneDrive, để chia sẻ)
OD_MOI_CTY = os.path.join(OD, "[0] TOWNSOFT'S FILES/0. Project/0. Dự án Agent")
OD_MOI_CANHAN = os.path.join(OD, "[1] PERSONAL/Heroes - Dự án")

# key: (khu, thư mục Mac, tên hiển thị = tên thư mục OneDrive, nguồn cũ trên OneDrive)
DU_AN = {
    "lina":              ("company",  "company/lina",               "Lina",              [("Lina", "auto")]),
    "nhalo":             ("company",  "company/nhalo",              "NhàLo",             [("NhàLo", "auto")]),
    "balheh":            ("company",  "company/balheh",             "Balheh",            [("Balheh", "auto")]),
    "chinchu":           ("company",  "company/chinchu",            "ChinChu",           [("ChinChu", "auto")]),
    "homepages":         ("company",  "company/homepages",          "Homepages",         [("Homepages", "auto")]),
    "noi-tro":           ("company",  "company/noi-tro",            "Nội trợ",           [("Nội trợ", "auto")]),
    "phien-dich":        ("company",  "company/phien-dich",         "Phiên dịch",        [("Phiên dịch", "auto")]),
    "team":              ("company",  "company/team",               "team",              [("team", "auto"),
                                                                                           ("Báo cáo ngày", "output/bao-cao-ngay"),
                                                                                           ("Sổ giao việc.xlsx", "inbox/"),
                                                                                           ("Tệp giao việc", "inbox/")]),
    "nha-liu-lo":        ("personal", "personal/nha-liu-lo",        "Nhà Líu Lo",        [("Nhà Líu Lo", "auto")]),
    "cong-ty-huong-noi": ("personal", "personal/cong-ty-huong-noi", "Công ty Hướng Nội", [("Công ty Hướng Nội", "auto")]),
}

# Mục con có tên khớp -> inbox (tài liệu Hero đưa); còn lại -> output (Claude tạo ra)
INBOX_TEN = {"Giao việc", "Claude input", "Tệp giao việc", "Sổ giao việc.xlsx",
             "[Lina] CEO Claude 분석", "_video-tham-khao"}

# Không đưa lên OneDrive (tạo lại được, làm nghẽn OneDrive)
LOAI_TRU = ["node_modules", ".git", ".dart_tool", "build", ".gradle", "Pods",
            ".DS_Store", ".next", "dist", "__pycache__", "*.tmp", "~$*"]


def mac_dir(key):
    return os.path.join(PROJECTS, DU_AN[key][1])


def od_moi(key):
    khu, _, ten, _ = DU_AN[key]
    return os.path.join(OD_MOI_CTY if khu == "company" else OD_MOI_CANHAN, ten)


def od_cu(key, src):
    khu = DU_AN[key][0]
    return os.path.join(OD_CU_CTY if khu == "company" else OD_CU_CANHAN, src)
