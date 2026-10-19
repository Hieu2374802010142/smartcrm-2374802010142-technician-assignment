
from fastapi import APIRouter
from pydantic import BaseModel, Field

from src.backend.services import technician_service

router = APIRouter(prefix="/api/technicians", tags=["Technicians"])


class TechnicianCreate(BaseModel):
    ho_ten: str = Field(min_length=1)
    so_dien_thoai: str | None = None
    chuyen_mon: str | None = None
    dang_hoat_dong: bool = True


@router.get("")
def get_technicians():
    return technician_service.get_technicians()


@router.post("", status_code=201)
def create_technician(data: TechnicianCreate):
    return technician_service.create_technician(data)


@router.put("/{technician_id}")
def update_technician(technician_id: int, data: TechnicianCreate):
    return technician_service.update_technician(technician_id, data)


@router.delete("/{technician_id}")
def delete_technician(technician_id: int):
    return technician_service.delete_technician(technician_id)
