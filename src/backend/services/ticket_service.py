
import sqlite3

from fastapi import HTTPException

from src.backend.repositories import ticket_repository as repo


# Lay danh sach phieu bao hanh chua phan cong
def get_unassigned_tickets():
    try:
        tickets = repo.get_unassigned_tickets()

        return {
            "tickets": tickets,
            "total": len(tickets)
        }

    except sqlite3.Error:
        raise HTTPException(
            status_code=500,
            detail="Khong the lay danh sach phieu chua phan cong"
        )

# UC03 - Phan cong ky thuat vien
def assign_technician(ticket_id, technician_id):
    try:
        result = repo.assign_technician(
            ticket_id, technician_id
        )

        status = result["status"]

        if status == "TICKET_NOT_FOUND":
            raise HTTPException(
                status_code=404,
                detail="Khong tim thay phieu bao hanh"
            )

        if status == "TICKET_NOT_NEW":
            raise HTTPException(
                status_code=409,
                detail="Phieu khong o trang thai Moi"
            )

        if status == "TECHNICIAN_NOT_FOUND":
            raise HTTPException(
                status_code=404,
                detail="Khong tim thay ky thuat vien"
            )

        if status == "TECHNICIAN_INACTIVE":
            raise HTTPException(
                status_code=409,
                detail="Ky thuat vien da ngung hoat dong"
            )

        return {
            "message": "Phan cong ky thuat vien thanh cong",
            "ma_phan_cong": result["ma_phan_cong"],
            "ma_phieu": ticket_id,
            "ma_ky_thuat_vien": technician_id
        }

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=409,
            detail="Du lieu phan cong khong hop le hoac bi trung"
        )

    except sqlite3.Error:
        raise HTTPException(
            status_code=500,
            detail="Khong the phan cong ky thuat vien"
        )

# UC04 - Dat lich hen va UC05 - Kiem tra trung lich
def create_appointment(
    assignment_id,
    ngay_hen,
    gio_bat_dau,
    gio_ket_thuc,
    loai_lich_hen
):
    # Kiem tra thoi gian hop le
    if gio_ket_thuc <= gio_bat_dau:
        raise HTTPException(
            status_code=400,
            detail="Gio ket thuc phai sau gio bat dau"
        )

    # Kiem tra loai lich hen
    if not loai_lich_hen.strip():
        raise HTTPException(
            status_code=400,
            detail="Loai lich hen khong duoc de trong"
        )

    try:
        result = repo.create_appointment(
            assignment_id,
            ngay_hen,
            gio_bat_dau,
            gio_ket_thuc,
            loai_lich_hen
        )

        status = result["status"]

        if status == "ASSIGNMENT_NOT_FOUND":
            raise HTTPException(
                status_code=404,
                detail="Khong tim thay phan cong dang hoat dong"
            )

        if status == "APPOINTMENT_OVERLAP":
            raise HTTPException(
                status_code=409,
                detail="Lich hen bi trung voi lich cua ky thuat vien"
            )

        return {
            "message": "Dat lich hen thanh cong",
            "ma_lich_hen": result["ma_lich_hen"],
            "ma_phan_cong": assignment_id
        }

    except sqlite3.IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Du lieu lich hen khong hop le"
        )

    except sqlite3.Error:
        raise HTTPException(
            status_code=500,
            detail="Khong the luu lich hen"
        )

# Lay danh sach phan cong dang hoat dong
def get_active_assignments():
    try:
        assignments = repo.get_active_assignments()

        return {
            "assignments": assignments,
            "total": len(assignments)
        }

    except sqlite3.Error:
        raise HTTPException(
            status_code=500,
            detail="Khong the tai danh sach phan cong"
        )
