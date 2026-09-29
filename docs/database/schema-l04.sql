-- =====================================================
-- SMARTCRM L04
-- Phân công kỹ thuật viên và lịch hẹn
-- =====================================================

CREATE TABLE khach_hang (
    ma_khach_hang INTEGER PRIMARY KEY,
    ho_ten TEXT NOT NULL,
    so_dien_thoai TEXT NOT NULL
);

CREATE TABLE phieu_bao_hanh (
    ma_phieu INTEGER PRIMARY KEY,
    ma_khach_hang INTEGER NOT NULL,
    ten_thiet_bi TEXT NOT NULL,
    trang_thai TEXT NOT NULL,
    ngay_tao DATETIME NOT NULL,

    FOREIGN KEY (ma_khach_hang)
        REFERENCES khach_hang(ma_khach_hang)
);

CREATE TABLE ky_thuat_vien (
    ma_ky_thuat_vien INTEGER PRIMARY KEY,
    ho_ten TEXT NOT NULL,
    so_dien_thoai TEXT,
    chuyen_mon TEXT,
    dang_hoat_dong BOOLEAN NOT NULL DEFAULT 1
);

CREATE TABLE phan_cong_ky_thuat_vien (
    ma_phan_cong INTEGER PRIMARY KEY,
    ma_phieu INTEGER NOT NULL UNIQUE,
    ma_ky_thuat_vien INTEGER NOT NULL,
    ngay_phan_cong DATETIME NOT NULL,

    FOREIGN KEY (ma_phieu)
        REFERENCES phieu_bao_hanh(ma_phieu),

    FOREIGN KEY (ma_ky_thuat_vien)
        REFERENCES ky_thuat_vien(ma_ky_thuat_vien)
);

CREATE TABLE lich_hen (
    ma_lich_hen INTEGER PRIMARY KEY,
    ma_phieu INTEGER NOT NULL,
    ma_ky_thuat_vien INTEGER NOT NULL,
    ngay_hen DATE NOT NULL,
    gio_bat_dau TIME NOT NULL,
    gio_ket_thuc TIME NOT NULL,
    loai_lich_hen TEXT NOT NULL,
    ngay_tao DATETIME NOT NULL,

    FOREIGN KEY (ma_phieu)
        REFERENCES phieu_bao_hanh(ma_phieu),

    FOREIGN KEY (ma_ky_thuat_vien)
        REFERENCES ky_thuat_vien(ma_ky_thuat_vien)
);

CREATE INDEX idx_phieu_trang_thai
ON phieu_bao_hanh(trang_thai);

CREATE INDEX idx_phieu_khach_hang
ON phieu_bao_hanh(ma_khach_hang);

CREATE INDEX idx_lich_hen_ky_thuat_vien
ON lich_hen(ma_ky_thuat_vien, ngay_hen);

CREATE INDEX idx_lich_hen_thoi_gian
ON lich_hen(
    ma_ky_thuat_vien,
    ngay_hen,
    gio_bat_dau,
    gio_ket_thuc
);