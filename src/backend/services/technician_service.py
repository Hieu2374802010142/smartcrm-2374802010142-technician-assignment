
import sqlite3

from src.backend.repositories import technician_repository as repo


# ==========================================
# LOI NGHIEP VU - KHONG PHU THUOC FASTAPI
# ==========================================

class TechnicianError(Exception):
    """Loi nghiep vu lien quan den ky thuat vien."""

    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(message)


# ==========================================
# READ - DANH SACH KY THUAT VIEN
# ==========================================

def get_technicians():
    try:
        technicians = repo.get_all_technicians()

        return {
            "technicians": technicians
        }

    except sqlite3.Error as exc:
        raise TechnicianError(
            "DATABASE_ERROR",
            "Khong the lay danh sach ky thuat vien"
        ) from exc


# ==========================================
# CREATE - THEM KY THUAT VIEN
# ==========================================

def create_technician(data):
    try:
        technician_id = repo.insert_technician(data)

        return {
            "message": "Them ky thuat vien thanh cong",
            "ma_ky_thuat_vien": technician_id
        }

    except sqlite3.IntegrityError as exc:
        raise TechnicianError(
            "CONFLICT",
            "Du lieu ky thuat vien khong hop le hoac bi trung"
        ) from exc

    except sqlite3.Error as exc:
        raise TechnicianError(
            "DATABASE_ERROR",
            "Khong the them ky thuat vien"
        ) from exc


# ==========================================
# UPDATE - CAP NHAT KY THUAT VIEN
# ==========================================

def update_technician(technician_id, data):
    if technician_id <= 0:
        raise TechnicianError(
            "INVALID_DATA",
            "Ma ky thuat vien khong hop le"
        )

    try:
        affected_rows = repo.update_technician(
            technician_id,
            data
        )

        if affected_rows == 0:
            raise TechnicianError(
                "NOT_FOUND",
                "Khong tim thay ky thuat vien"
            )

        return {
            "message": "Cap nhat ky thuat vien thanh cong",
            "ma_ky_thuat_vien": technician_id
        }

    except sqlite3.IntegrityError as exc:
        raise TechnicianError(
            "CONFLICT",
            "Du lieu cap nhat khong hop le hoac bi trung"
        ) from exc

    except sqlite3.Error as exc:
        raise TechnicianError(
            "DATABASE_ERROR",
            "Khong the cap nhat ky thuat vien"
        ) from exc


# ==========================================
# DELETE - NGUNG HOAT DONG KY THUAT VIEN
# ==========================================

def delete_technician(technician_id):
    if technician_id <= 0:
        raise TechnicianError(
            "INVALID_DATA",
            "Ma ky thuat vien khong hop le"
        )

    try:
        affected_rows = repo.deactivate_technician(
            technician_id
        )

        if affected_rows == 0:
            raise TechnicianError(
                "NOT_FOUND",
                "Khong tim thay ky thuat vien"
            )

        return {
            "message": "Da ngung hoat dong ky thuat vien",
            "ma_ky_thuat_vien": technician_id
        }

    except sqlite3.IntegrityError as exc:
        raise TechnicianError(
            "CONFLICT",
            "Khong the ngung hoat dong ky thuat vien do du lieu lien quan"
        ) from exc

    except sqlite3.Error as exc:
        raise TechnicianError(
            "DATABASE_ERROR",
            "Khong the ngung hoat dong ky thuat vien"
        ) from exc
