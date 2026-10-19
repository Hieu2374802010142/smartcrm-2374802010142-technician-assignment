
from pathlib import Path
import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="SmartCRM - L04")

# Duong dan database Sprint 1
DB_PATH = Path(__file__).resolve().parents[2] / "smartcrm-sprint1.db"


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


# Du lieu dau vao khi them ky thuat vien
class TechnicianCreate(BaseModel):
    ho_ten: str = Field(min_length=1)
    so_dien_thoai: str | None = None
    chuyen_mon: str | None = None
    dang_hoat_dong: bool = True


# API trang chu
@app.get("/")
def hello():
    return {"message": "Hello Smart CRM"}


# API kiem tra ket noi SQLite
@app.get("/db-test")
def db_test():
    conn = get_db_connection()
    try:
        conn.execute("SELECT 1")
        return {"message": "SQLite connection OK"}
    finally:
        conn.close()


# API xem danh sach ky thuat vien
@app.get("/api/technicians")
def get_technicians():
    conn = get_db_connection()

    try:
        cursor = conn.execute(
            """
            SELECT
                ma_ky_thuat_vien,
                ho_ten,
                so_dien_thoai,
                chuyen_mon,
                dang_hoat_dong
            FROM ky_thuat_vien
            ORDER BY ma_ky_thuat_vien
            """
        )

        technicians = [dict(row) for row in cursor.fetchall()]
        return {"technicians": technicians}

    finally:
        conn.close()


# API them ky thuat vien
@app.post("/api/technicians", status_code=201)
def create_technician(data: TechnicianCreate):
    conn = get_db_connection()

    try:
        cursor = conn.execute(
            """
            INSERT INTO ky_thuat_vien
                (ho_ten, so_dien_thoai, chuyen_mon, dang_hoat_dong)
            VALUES (?, ?, ?, ?)
            """,
            (
                data.ho_ten,
                data.so_dien_thoai,
                data.chuyen_mon,
                int(data.dang_hoat_dong),
            ),
        )

        conn.commit()

        return {
            "message": "Them ky thuat vien thanh cong",
            "ma_ky_thuat_vien": cursor.lastrowid,
        }

    except sqlite3.Error:
        conn.rollback()
        raise HTTPException(
            status_code=500,
            detail="Khong the them ky thuat vien",
        )

    finally:
        conn.close()

# API sua thong tin ky thuat vien
@app.put("/api/technicians/{technician_id}")
def update_technician(technician_id: int, data: TechnicianCreate):
    conn = get_db_connection()

    try:
        cursor = conn.execute(
            """
            UPDATE ky_thuat_vien
            SET ho_ten = ?,
                so_dien_thoai = ?,
                chuyen_mon = ?,
                dang_hoat_dong = ?
            WHERE ma_ky_thuat_vien = ?
            """,
            (
                data.ho_ten,
                data.so_dien_thoai,
                data.chuyen_mon,
                int(data.dang_hoat_dong),
                technician_id,
            ),
        )

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Khong tim thay ky thuat vien",
            )

        conn.commit()

        return {
            "message": "Cap nhat ky thuat vien thanh cong",
            "ma_ky_thuat_vien": technician_id,
        }

    except sqlite3.Error:
        conn.rollback()
        raise HTTPException(
            status_code=500,
            detail="Khong the cap nhat ky thuat vien",
        )

    finally:
        conn.close()

# API ngung hoat dong ky thuat vien (Soft Delete)
@app.delete("/api/technicians/{technician_id}")
def delete_technician(technician_id: int):
    conn = get_db_connection()

    try:
        cursor = conn.execute(
            """
            UPDATE ky_thuat_vien
            SET dang_hoat_dong = 0
            WHERE ma_ky_thuat_vien = ?
            """,
            (technician_id,),
        )

        if cursor.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail="Khong tim thay ky thuat vien",
            )

        conn.commit()

        return {
            "message": "Da ngung hoat dong ky thuat vien",
            "ma_ky_thuat_vien": technician_id,
        }

    except sqlite3.Error:
        conn.rollback()
        raise HTTPException(
            status_code=500,
            detail="Khong the ngung hoat dong ky thuat vien",
        )

    finally:
        conn.close()
