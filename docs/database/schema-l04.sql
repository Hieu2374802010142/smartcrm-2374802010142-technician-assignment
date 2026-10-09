
-- SMART CRM L04
-- Phan cong ky thuat vien va lich hen
-- Database: SQLite

PRAGMA foreign_keys = ON;

CREATE TABLE khach_hang (
    ma_khach_hang INTEGER PRIMARY KEY,
    ho_ten TEXT NOT NULL,
    so_dien_thoai TEXT NOT NULL
);

CREATE TABLE phieu_bao_hanh (
    ma_phieu INTEGER PRIMARY KEY,
    ma_khach_hang INTEGER NOT NULL,
    ten_thiet_bi TEXT NOT NULL,
    trang_thai TEXT NOT NULL DEFAULT 'Mới'
        CHECK (trang_thai IN (
            'Mới', 'Đã phân công',
            'Đang xử lý', 'Hoàn tất'
        )),
    ngay_tao DATETIME NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (ma_khach_hang)
        REFERENCES khach_hang(ma_khach_hang)
);

CREATE TABLE ky_thuat_vien (
    ma_ky_thuat_vien INTEGER PRIMARY KEY,
    ho_ten TEXT NOT NULL,
    so_dien_thoai TEXT,
    chuyen_mon TEXT,
    dang_hoat_dong INTEGER NOT NULL DEFAULT 1
        CHECK (dang_hoat_dong IN (0, 1))
);

CREATE TABLE phan_cong_ky_thuat_vien (
    ma_phan_cong INTEGER PRIMARY KEY,
    ma_phieu INTEGER NOT NULL,
    ma_ky_thuat_vien INTEGER NOT NULL,
    ngay_phan_cong DATETIME NOT NULL
        DEFAULT CURRENT_TIMESTAMP,
    trang_thai_phan_cong TEXT NOT NULL
        DEFAULT 'Đang hoạt động'
        CHECK (trang_thai_phan_cong IN (
            'Đang hoạt động', 'Đã hủy'
        )),

    FOREIGN KEY (ma_phieu)
        REFERENCES phieu_bao_hanh(ma_phieu),

    FOREIGN KEY (ma_ky_thuat_vien)
        REFERENCES ky_thuat_vien(ma_ky_thuat_vien)
);

-- Moi phieu chi co toi da mot phan cong dang hoat dong
CREATE UNIQUE INDEX idx_phan_cong_active
ON phan_cong_ky_thuat_vien(ma_phieu)
WHERE trang_thai_phan_cong = 'Đang hoạt động';

CREATE TABLE lich_hen (
    ma_lich_hen INTEGER PRIMARY KEY,
    ma_phan_cong INTEGER NOT NULL,
    ngay_hen DATE NOT NULL,
    gio_bat_dau TIME NOT NULL,
    gio_ket_thuc TIME NOT NULL,
    loai_lich_hen TEXT NOT NULL,
    trang_thai_lich_hen TEXT NOT NULL
        DEFAULT 'Còn hiệu lực'
        CHECK (trang_thai_lich_hen IN (
            'Còn hiệu lực', 'Đã hủy', 'Hoàn tất'
        )),
    ngay_tao DATETIME NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    CHECK (gio_ket_thuc > gio_bat_dau),

    FOREIGN KEY (ma_phan_cong)
        REFERENCES phan_cong_ky_thuat_vien(ma_phan_cong)
);

CREATE INDEX idx_phieu_trang_thai
ON phieu_bao_hanh(trang_thai);

CREATE INDEX idx_phieu_khach_hang
ON phieu_bao_hanh(ma_khach_hang);

CREATE INDEX idx_phan_cong_ky_thuat_vien
ON phan_cong_ky_thuat_vien(ma_ky_thuat_vien);

CREATE INDEX idx_lich_hen_thoi_gian
ON lich_hen(ngay_hen, gio_bat_dau, gio_ket_thuc);
