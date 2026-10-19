
import sqlite3

from fastapi import HTTPException

from src.backend.repositories import technician_repository as repo


# Lay danh sach ky thuat vien
def get_technicians():
    try:
        return {"technicians": repo.get_all_technicians()}
    except sqlite3.Error:
        raise HTTPException(
            status_code=500,
            detail="Khong the lay danh sach ky thuat vien"
        )


# Them ky thuat vien
def create_technician(data):
    try:
        technician_id = repo.insert_technician(data)

        return {
            "message": "Them ky thuat vien thanh cong",
            "ma_ky_thuat_vien": technician_id
        }

    except sqlite3.Error:
        raise HTTPException(
            status_code=500,
            detail="Khong the them ky thuat vien"
        )


# Cap nhat ky thuat vien
def update_technician(technician_id, data):
    try:
        affected_rows = repo.update_technician(
            technician_id, data
        )

        if affected_rows == 0:
            raise HTTPException(
                status_code=404,
                detail="Khong tim thay ky thuat vien"
            )

        return {
            "message": "Cap nhat ky thuat vien thanh cong",
            "ma_ky_thuat_vien": technician_id
        }

    except sqlite3.Error:
        raise HTTPException(
            status_code=500,
            detail="Khong the cap nhat ky thuat vien"
        )


# Ngung hoat dong ky thuat vien
def delete_technician(technician_id):
    try:
        affected_rows = repo.deactivate_technician(
            technician_id
        )

        if affected_rows == 0:
            raise HTTPException(
                status_code=404,
                detail="Khong tim thay ky thuat vien"
            )

        return {
            "message": "Da ngung hoat dong ky thuat vien",
            "ma_ky_thuat_vien": technician_id
        }

    except sqlite3.Error:
        raise HTTPException(
            status_code=500,
            detail="Khong the ngung hoat dong ky thuat vien"
        )
