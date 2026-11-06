
import sqlite3

import pytest

from src.backend.migrate import migrate_database
from src.backend.repositories import ticket_repository


@pytest.fixture
def appointment_db(tmp_path, monkeypatch):
    # Tao database rieng cho moi test
    db_path = tmp_path / "smartcrm-test.db"
    migrate_database(db_path)

    def test_connection():
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        return conn

    # Repository se su dung database test
    monkeypatch.setattr(
        ticket_repository,
        "get_db_connection",
        test_connection
    )

    conn = test_connection()

    try:
        # Tao khach hang
        conn.execute(
            """
            INSERT INTO khach_hang
                (ma_khach_hang, ho_ten, so_dien_thoai)
            VALUES (1, 'Khach hang test', '0900000000')
            """
        )

        # Tao phieu bao hanh
        conn.execute(
            """
            INSERT INTO phieu_bao_hanh
                (ma_phieu, ma_khach_hang, ten_thiet_bi)
            VALUES (1, 1, 'Samsung Galaxy S22')
            """
        )

        # Tao ky thuat vien
        conn.execute(
            """
            INSERT INTO ky_thuat_vien
                (ma_ky_thuat_vien, ho_ten)
            VALUES (1, 'Ky thuat vien test')
            """
        )

        # Tao phan cong dang hoat dong
        conn.execute(
            """
            INSERT INTO phan_cong_ky_thuat_vien
                (ma_phan_cong, ma_phieu, ma_ky_thuat_vien)
            VALUES (1, 1, 1)
            """
        )

        # Lich hen co san: 09:00 - 10:00
        conn.execute(
            """
            INSERT INTO lich_hen
                (ma_phan_cong, ngay_hen,
                 gio_bat_dau, gio_ket_thuc,
                 loai_lich_hen)
            VALUES (
                1, '2026-11-10',
                '09:00:00', '10:00:00',
                'Nhan thiet bi'
            )
            """
        )

        conn.commit()
    finally:
        conn.close()

    return db_path


# TC-B01: Lich moi bat dau dung luc lich cu ket thuc
def test_appointment_adjacent_boundary(appointment_db):
    result = ticket_repository.create_appointment(
        assignment_id=1,
        ngay_hen="2026-11-10",
        gio_bat_dau="10:00:00",
        gio_ket_thuc="11:00:00",
        loai_lich_hen="Tra thiet bi"
    )

    assert result["status"] == "SUCCESS"
    assert result["ma_lich_hen"] > 0


# TC-B02: Lich moi bat dau som hon 1 phut
def test_appointment_overlap_one_minute(appointment_db):
    result = ticket_repository.create_appointment(
        assignment_id=1,
        ngay_hen="2026-11-10",
        gio_bat_dau="09:59:00",
        gio_ket_thuc="11:00:00",
        loai_lich_hen="Tra thiet bi"
    )

    assert result["status"] == "APPOINTMENT_OVERLAP"
