
from fastapi import APIRouter, Depends
from datetime import date, time
from pydantic import BaseModel, Field

from src.backend.services import ticket_service
from src.backend.auth.security import get_current_user, require_manager


router = APIRouter(
    prefix="/api/tickets",
    tags=["Tickets"]
)


# Kiem tra dang nhap va quyen Quan ly trung tam
def check_manager(user: dict = Depends(get_current_user)):
    return require_manager(user)


# UC01 - Xem danh sach phieu chua phan cong
@router.get("/unassigned")
def get_unassigned_tickets():
    return ticket_service.get_unassigned_tickets()


# Du lieu dau vao khi phan cong ky thuat vien
class TechnicianAssignment(BaseModel):
    ma_ky_thuat_vien: int = Field(gt=0)


# UC03 - Phan cong ky thuat vien
@router.post("/{ticket_id}/assign")
def assign_technician(
    ticket_id: int,
    data: TechnicianAssignment,
    manager: dict = Depends(check_manager)
):
    return ticket_service.assign_technician(
        ticket_id,
        data.ma_ky_thuat_vien
    )


# Du lieu dau vao khi dat lich hen
class AppointmentCreate(BaseModel):
    ma_phan_cong: int = Field(gt=0)
    ngay_hen: date
    gio_bat_dau: time
    gio_ket_thuc: time
    loai_lich_hen: str = Field(min_length=1)


# UC04 - Dat lich hen va UC05 - Kiem tra trung lich
@router.post("/appointments")
def create_appointment(
    data: AppointmentCreate,
    manager: dict = Depends(check_manager)
):
    return ticket_service.create_appointment(
        data.ma_phan_cong,
        data.ngay_hen.isoformat(),
        data.gio_bat_dau.isoformat(),
        data.gio_ket_thuc.isoformat(),
        data.loai_lich_hen
    )


# Lay danh sach phan cong dang hoat dong
@router.get("/assignments")
def get_active_assignments():
    return ticket_service.get_active_assignments()
