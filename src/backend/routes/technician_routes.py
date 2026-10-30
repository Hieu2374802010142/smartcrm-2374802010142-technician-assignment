
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from src.backend.auth.security import (
    get_current_user,
    require_manager,
)
from src.backend.services import technician_service
from src.backend.services.technician_service import TechnicianError


router = APIRouter(
    prefix="/api/technicians",
    tags=["Technicians"]
)


class TechnicianCreate(BaseModel):
    ho_ten: str = Field(min_length=1)
    so_dien_thoai: str | None = None
    chuyen_mon: str | None = None
    dang_hoat_dong: bool = True


def check_manager(
    user: dict = Depends(get_current_user)
):
    return require_manager(user)


def handle_technician_error(error: TechnicianError):
    status_codes = {
        "INVALID_DATA": 400,
        "NOT_FOUND": 404,
        "CONFLICT": 409,
        "DATABASE_ERROR": 500,
    }

    raise HTTPException(
        status_code=status_codes.get(error.code, 500),
        detail=error.message
    ) from error


# Lay danh sach ky thuat vien
@router.get("")
def get_technicians():
    try:
        return technician_service.get_technicians()
    except TechnicianError as error:
        handle_technician_error(error)


# Them ky thuat vien - chi quan ly
@router.post("", status_code=201)
def create_technician(
    data: TechnicianCreate,
    user: dict = Depends(check_manager)
):
    try:
        return technician_service.create_technician(data)
    except TechnicianError as error:
        handle_technician_error(error)


# Cap nhat ky thuat vien - chi quan ly
@router.put("/{technician_id}")
def update_technician(
    technician_id: int,
    data: TechnicianCreate,
    user: dict = Depends(check_manager)
):
    try:
        return technician_service.update_technician(
            technician_id, data
        )
    except TechnicianError as error:
        handle_technician_error(error)


# Ngung hoat dong ky thuat vien - chi quan ly
@router.delete("/{technician_id}")
def delete_technician(
    technician_id: int,
    user: dict = Depends(check_manager)
):
    try:
        return technician_service.delete_technician(
            technician_id
        )
    except TechnicianError as error:
        handle_technician_error(error)
