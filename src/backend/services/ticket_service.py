
import sqlite3

from src.backend.repositories import ticket_repository as repo


# ==========================================
# LOI NGHIEP VU
# ==========================================

class TicketError(Exception):
    """Loi nghiep vu khong phu thuoc FastAPI."""

    def __init__(self, code, message):
        self.code = code
        self.message = message
        super().__init__(message)


# ==========================================
# UC01 - XEM PHIEU CHUA PHAN CONG
# ==========================================

def get_unassigned_tickets():
    try:
        tickets = repo.get_unassigned_tickets()
        return {
            "tickets": tickets,
            "total": len(tickets)
        }
    except sqlite3.Error as exc:
        raise TicketError(
            "DATABASE_ERROR",
            "Khong the lay danh sach phieu chua phan cong"
        ) from exc


# ==========================================
# UC03 - PHAN CONG KY THUAT VIEN
# ==========================================

def assign_technician(ticket_id, technician_id):
    try:
        result = repo.assign_technician(
            ticket_id, technician_id
        )

        status = result["status"]

        if status == "TICKET_NOT_FOUND":
            raise TicketError(
                "NOT_FOUND",
                "Khong tim thay phieu bao hanh"
            )

        if status == "TICKET_NOT_NEW":
            raise TicketError(
                "CONFLICT",
                "Phieu khong o trang thai Moi"
            )

        if status == "TECHNICIAN_NOT_FOUND":
            raise TicketError(
                "NOT_FOUND",
                "Khong tim thay ky thuat vien"
            )

        if status == "TECHNICIAN_INACTIVE":
            raise TicketError(
                "CONFLICT",
                "Ky thuat vien da ngung hoat dong"
            )

        if status != "SUCCESS":
            raise TicketError(
                "DATABASE_ERROR",
                "Khong the phan cong ky thuat vien"
            )

        return {
            "message": "Phan cong ky thuat vien thanh cong",
            "ma_phan_cong": result["ma_phan_cong"],
            "ma_phieu": ticket_id,
            "ma_ky_thuat_vien": technician_id
        }

    except sqlite3.IntegrityError as exc:
        raise TicketError(
            "CONFLICT",
            "Du lieu phan cong khong hop le hoac bi trung"
        ) from exc

    except sqlite3.Error as exc:
        raise TicketError(
            "DATABASE_ERROR",
            "Khong the phan cong ky thuat vien"
        ) from exc


# ==========================================
# UC04 - DAT LICH HEN
# UC05 - KIEM TRA TRUNG LICH
# ==========================================

def create_appointment(
    assignment_id,
    ngay_hen,
    gio_bat_dau,
    gio_ket_thuc,
    loai_lich_hen
):
    if gio_ket_thuc <= gio_bat_dau:
        raise TicketError(
            "INVALID_DATA",
            "Gio ket thuc phai sau gio bat dau"
        )

    if not loai_lich_hen.strip():
        raise TicketError(
            "INVALID_DATA",
            "Loai lich hen khong duoc de trong"
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
            raise TicketError(
                "NOT_FOUND",
                "Khong tim thay phan cong dang hoat dong"
            )

        if status == "APPOINTMENT_OVERLAP":
            raise TicketError(
                "CONFLICT",
                "Lich hen bi trung voi lich cua ky thuat vien"
            )

        if status != "SUCCESS":
            raise TicketError(
                "DATABASE_ERROR",
                "Khong the luu lich hen"
            )

        return {
            "message": "Dat lich hen thanh cong",
            "ma_lich_hen": result["ma_lich_hen"],
            "ma_phan_cong": assignment_id
        }

    except sqlite3.IntegrityError as exc:
        raise TicketError(
            "INVALID_DATA",
            "Du lieu lich hen khong hop le"
        ) from exc

    except sqlite3.Error as exc:
        raise TicketError(
            "DATABASE_ERROR",
            "Khong the luu lich hen"
        ) from exc


# ==========================================
# XEM DANH SACH PHAN CONG
# ==========================================

def get_active_assignments():
    try:
        assignments = repo.get_active_assignments()
        return {
            "assignments": assignments,
            "total": len(assignments)
        }
    except sqlite3.Error as exc:
        raise TicketError(
            "DATABASE_ERROR",
            "Khong the tai danh sach phan cong"
        ) from exc


# ==========================================
# CRUD PHIEU BAO HANH
# ==========================================

def get_all_tickets():
    try:
        tickets = repo.get_all_tickets()
        return {
            "tickets": tickets,
            "total": len(tickets)
        }
    except sqlite3.Error as exc:
        raise TicketError(
            "DATABASE_ERROR",
            "Khong the lay danh sach phieu bao hanh"
        ) from exc


def get_ticket_by_id(ticket_id):
    try:
        ticket = repo.get_ticket_by_id(ticket_id)

        if ticket is None:
            raise TicketError(
                "NOT_FOUND",
                "Khong tim thay phieu bao hanh"
            )

        return ticket

    except sqlite3.Error as exc:
        raise TicketError(
            "DATABASE_ERROR",
            "Khong the xem chi tiet phieu bao hanh"
        ) from exc


def create_ticket(customer_id, device_name):
    if customer_id <= 0:
        raise TicketError(
            "INVALID_DATA",
            "Ma khach hang khong hop le"
        )

    if not isinstance(device_name, str) or not device_name.strip():
        raise TicketError(
            "INVALID_DATA",
            "Ten thiet bi khong duoc de trong"
        )

    device_name = device_name.strip()

    try:
        if not repo.customer_exists(customer_id):
            raise TicketError(
                "NOT_FOUND",
                "Khong tim thay khach hang"
            )

        ticket_id = repo.insert_ticket(
            customer_id, device_name
        )

        return {
            "message": "Tao phieu bao hanh thanh cong",
            "ma_phieu": ticket_id
        }

    except sqlite3.IntegrityError as exc:
        raise TicketError(
            "INVALID_DATA",
            "Du lieu phieu bao hanh khong hop le"
        ) from exc

    except sqlite3.Error as exc:
        raise TicketError(
            "DATABASE_ERROR",
            "Khong the tao phieu bao hanh"
        ) from exc


def update_ticket(ticket_id, customer_id, device_name):
    if ticket_id <= 0 or customer_id <= 0:
        raise TicketError(
            "INVALID_DATA",
            "Ma phieu hoac ma khach hang khong hop le"
        )

    if not isinstance(device_name, str) or not device_name.strip():
        raise TicketError(
            "INVALID_DATA",
            "Ten thiet bi khong duoc de trong"
        )

    device_name = device_name.strip()

    try:
        if not repo.customer_exists(customer_id):
            raise TicketError(
                "NOT_FOUND",
                "Khong tim thay khach hang"
            )

        result = repo.update_ticket(
            ticket_id, customer_id, device_name
        )

        if result == "NOT_FOUND":
            raise TicketError(
                "NOT_FOUND",
                "Khong tim thay phieu bao hanh"
            )

        if result == "NOT_EDITABLE":
            raise TicketError(
                "CONFLICT",
                "Khong the sua phieu da duoc phan cong"
            )

        if result != "SUCCESS":
            raise TicketError(
                "DATABASE_ERROR",
                "Khong the cap nhat phieu bao hanh"
            )

        return {
            "message": "Cap nhat phieu thanh cong",
            "ma_phieu": ticket_id
        }

    except sqlite3.IntegrityError as exc:
        raise TicketError(
            "INVALID_DATA",
            "Du lieu cap nhat khong hop le"
        ) from exc

    except sqlite3.Error as exc:
        raise TicketError(
            "DATABASE_ERROR",
            "Khong the cap nhat phieu bao hanh"
        ) from exc


def delete_ticket(ticket_id):
    if ticket_id <= 0:
        raise TicketError(
            "INVALID_DATA",
            "Ma phieu khong hop le"
        )

    try:
        result = repo.delete_ticket(ticket_id)

        if result == "NOT_FOUND":
            raise TicketError(
                "NOT_FOUND",
                "Khong tim thay phieu bao hanh"
            )

        if result == "NOT_DELETABLE":
            raise TicketError(
                "CONFLICT",
                "Khong the xoa phieu da duoc phan cong"
            )

        if result != "SUCCESS":
            raise TicketError(
                "DATABASE_ERROR",
                "Khong the xoa phieu bao hanh"
            )

        return {
            "message": "Xoa phieu bao hanh thanh cong",
            "ma_phieu": ticket_id
        }

    except sqlite3.IntegrityError as exc:
        raise TicketError(
            "CONFLICT",
            "Phieu dang co du lieu lien quan, khong the xoa"
        ) from exc

    except sqlite3.Error as exc:
        raise TicketError(
            "DATABASE_ERROR",
            "Khong the xoa phieu bao hanh"
        ) from exc
