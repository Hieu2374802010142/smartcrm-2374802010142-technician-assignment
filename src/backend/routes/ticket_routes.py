
from datetime import date, time

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from src.backend.services import ticket_service
from src.backend.services.ticket_service import TicketError
from src.backend.auth.security import get_current_user, require_manager


# ==========================================
# ROUTER - PHIEU BAO HANH SMARTCRM L04
# ==========================================

router = APIRouter(
    prefix="/api/tickets",
    tags=["Tickets"]
)


# ==========================================
# KIEM TRA QUYEN QUAN LY
# ==========================================

def check_manager(user: dict = Depends(get_current_user)):
    return require_manager(user)


# ==========================================
# XU LY LOI TAI TANG ROUTES
# ==========================================

def handle_ticket_error(error: TicketError):
    status_codes = {
        "NOT_FOUND": 404,
        "INVALID_DATA": 400,
        "CONFLICT": 409,
        "DATABASE_ERROR": 500
    }

    raise HTTPException(
        status_code=status_codes.get(error.code, 500),
        detail=error.message
    )


# ==========================================
# CAC MODEL DU LIEU DAU VAO
# ==========================================

class TechnicianAssignment(BaseModel):
    ma_ky_thuat_vien: int = Field(gt=0)


class AppointmentCreate(BaseModel):
    ma_phan_cong: int = Field(gt=0)
    ngay_hen: date
    gio_bat_dau: time
    gio_ket_thuc: time
    loai_lich_hen: str = Field(min_length=1)


class TicketData(BaseModel):
    ma_khach_hang: int = Field(gt=0)
    ten_thiet_bi: str = Field(min_length=1)


# ==========================================
# UC01 - XEM PHIEU CHUA PHAN CONG
# ==========================================

@router.get("/unassigned")
def get_unassigned_tickets():
    try:
        return ticket_service.get_unassigned_tickets()
    except TicketError as error:
        handle_ticket_error(error)


# ==========================================
# UC03 - PHAN CONG KY THUAT VIEN
# ==========================================

@router.post("/{ticket_id}/assign")
def assign_technician(
    ticket_id: int,
    data: TechnicianAssignment,
    manager: dict = Depends(check_manager)
):
    try:
        return ticket_service.assign_technician(
            ticket_id,
            data.ma_ky_thuat_vien
        )
    except TicketError as error:
        handle_ticket_error(error)


# ==========================================
# UC04 - DAT LICH HEN
# UC05 - KIEM TRA TRUNG LICH
# ==========================================

@router.post("/appointments")
def create_appointment(
    data: AppointmentCreate,
    manager: dict = Depends(check_manager)
):
    try:
        return ticket_service.create_appointment(
            data.ma_phan_cong,
            data.ngay_hen.isoformat(),
            data.gio_bat_dau.isoformat(),
            data.gio_ket_thuc.isoformat(),
            data.loai_lich_hen
        )
    except TicketError as error:
        handle_ticket_error(error)


# ==========================================
# XEM DANH SACH PHAN CONG
# ==========================================

@router.get("/assignments")
def get_active_assignments():
    try:
        return ticket_service.get_active_assignments()
    except TicketError as error:
        handle_ticket_error(error)


# ==========================================
# CRUD PHIEU BAO HANH - BT2
# ==========================================

# READ - Danh sach tat ca phieu
@router.get("")
def get_all_tickets(
    manager: dict = Depends(check_manager)
):
    try:
        return ticket_service.get_all_tickets()
    except TicketError as error:
        handle_ticket_error(error)


# READ - Chi tiet phieu
@router.get("/{ticket_id}")
def get_ticket_by_id(
    ticket_id: int,
    manager: dict = Depends(check_manager)
):
    try:
        return ticket_service.get_ticket_by_id(ticket_id)
    except TicketError as error:
        handle_ticket_error(error)


# CREATE - Tao phieu
@router.post("", status_code=201)
def create_ticket(
    data: TicketData,
    manager: dict = Depends(check_manager)
):
    try:
        return ticket_service.create_ticket(
            data.ma_khach_hang,
            data.ten_thiet_bi
        )
    except TicketError as error:
        handle_ticket_error(error)


# UPDATE - Cap nhat phieu
@router.put("/{ticket_id}")
def update_ticket(
    ticket_id: int,
    data: TicketData,
    manager: dict = Depends(check_manager)
):
    try:
        return ticket_service.update_ticket(
            ticket_id,
            data.ma_khach_hang,
            data.ten_thiet_bi
        )
    except TicketError as error:
        handle_ticket_error(error)


# DELETE - Xoa phieu
@router.delete("/{ticket_id}")
def delete_ticket(
    ticket_id: int,
    manager: dict = Depends(check_manager)
):
    try:
        return ticket_service.delete_ticket(ticket_id)
    except TicketError as error:
        handle_ticket_error(error)
