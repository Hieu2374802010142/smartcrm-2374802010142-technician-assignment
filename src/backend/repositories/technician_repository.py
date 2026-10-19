
import sqlite3
from pathlib import Path

# Duong dan database Sprint 1
DB_PATH = Path(__file__).resolve().parents[3] / "smartcrm-sprint1.db"


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


# Lay danh sach ky thuat vien
def get_all_technicians():
    conn = get_db_connection()
    try:
        cursor = conn.execute("""
            SELECT ma_ky_thuat_vien, ho_ten,
                   so_dien_thoai, chuyen_mon, dang_hoat_dong
            FROM ky_thuat_vien
            ORDER BY ma_ky_thuat_vien
        """)
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


# Them ky thuat vien
def insert_technician(data):
    conn = get_db_connection()
    try:
        cursor = conn.execute("""
            INSERT INTO ky_thuat_vien
                (ho_ten, so_dien_thoai, chuyen_mon, dang_hoat_dong)
            VALUES (?, ?, ?, ?)
        """, (
            data.ho_ten,
            data.so_dien_thoai,
            data.chuyen_mon,
            int(data.dang_hoat_dong),
        ))

        conn.commit()
        return cursor.lastrowid

    except sqlite3.Error:
        conn.rollback()
        raise
    finally:
        conn.close()


# Cap nhat ky thuat vien
def update_technician(technician_id, data):
    conn = get_db_connection()
    try:
        cursor = conn.execute("""
            UPDATE ky_thuat_vien
            SET ho_ten = ?,
                so_dien_thoai = ?,
                chuyen_mon = ?,
                dang_hoat_dong = ?
            WHERE ma_ky_thuat_vien = ?
        """, (
            data.ho_ten,
            data.so_dien_thoai,
            data.chuyen_mon,
            int(data.dang_hoat_dong),
            technician_id,
        ))

        conn.commit()
        return cursor.rowcount

    except sqlite3.Error:
        conn.rollback()
        raise
    finally:
        conn.close()


# Ngung hoat dong ky thuat vien (Soft Delete)
def deactivate_technician(technician_id):
    conn = get_db_connection()
    try:
        cursor = conn.execute("""
            UPDATE ky_thuat_vien
            SET dang_hoat_dong = 0
            WHERE ma_ky_thuat_vien = ?
        """, (technician_id,))

        conn.commit()
        return cursor.rowcount

    except sqlite3.Error:
        conn.rollback()
        raise
    finally:
        conn.close()
