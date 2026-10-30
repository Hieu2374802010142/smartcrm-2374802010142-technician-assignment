
import sqlite3

import pytest
from unittest.mock import patch
from types import SimpleNamespace

from src.backend.services import technician_service
from src.backend.services.technician_service import TechnicianError


# ==========================================
# DU LIEU MAU
# ==========================================

def sample_technician():
    return SimpleNamespace(
        ho_ten="Nguyen Van A",
        so_dien_thoai="0901234567",
        chuyen_mon="Sua dien thoai",
        dang_hoat_dong=True
    )


# ==========================================
# TC01 - LAY DANH SACH KY THUAT VIEN
# ==========================================

def test_get_technicians_success():
    sample = [
        {
            "ma_ky_thuat_vien": 1,
            "ho_ten": "Nguyen Van A",
            "dang_hoat_dong": 1
        },
        {
            "ma_ky_thuat_vien": 2,
            "ho_ten": "Tran Van B",
            "dang_hoat_dong": 1
        }
    ]

    with patch.object(
        technician_service.repo,
        "get_all_technicians",
        return_value=sample
    ):
        result = technician_service.get_technicians()

    assert len(result["technicians"]) == 2
    assert result["technicians"][0]["ho_ten"] == "Nguyen Van A"


# ==========================================
# TC02 - THEM KY THUAT VIEN THANH CONG
# ==========================================

def test_create_technician_success():
    data = sample_technician()

    with patch.object(
        technician_service.repo,
        "insert_technician",
        return_value=10
    ) as mock_insert:
        result = technician_service.create_technician(data)

    assert result["ma_ky_thuat_vien"] == 10
    assert result["message"] == "Them ky thuat vien thanh cong"
    mock_insert.assert_called_once_with(data)


# ==========================================
# TC03 - CAP NHAT KY THUAT VIEN THANH CONG
# ==========================================

def test_update_technician_success():
    data = sample_technician()

    with patch.object(
        technician_service.repo,
        "update_technician",
        return_value=1
    ) as mock_update:
        result = technician_service.update_technician(1, data)

    assert result["ma_ky_thuat_vien"] == 1
    assert result["message"] == "Cap nhat ky thuat vien thanh cong"
    mock_update.assert_called_once_with(1, data)


# ==========================================
# TC04 - CAP NHAT KY THUAT VIEN KHONG TON TAI
# ==========================================

def test_update_technician_not_found():
    data = sample_technician()

    with patch.object(
        technician_service.repo,
        "update_technician",
        return_value=0
    ):
        with pytest.raises(TechnicianError) as error:
            technician_service.update_technician(999, data)

    assert error.value.code == "NOT_FOUND"


# ==========================================
# TC05 - NGUNG HOAT DONG KY THUAT VIEN
# ==========================================

def test_delete_technician_success():
    with patch.object(
        technician_service.repo,
        "deactivate_technician",
        return_value=1
    ) as mock_delete:
        result = technician_service.delete_technician(1)

    assert result["ma_ky_thuat_vien"] == 1
    assert result["message"] == "Da ngung hoat dong ky thuat vien"
    mock_delete.assert_called_once_with(1)


# ==========================================
# TC06 - NGUNG HOAT DONG KTV KHONG TON TAI
# ==========================================

def test_delete_technician_not_found():
    with patch.object(
        technician_service.repo,
        "deactivate_technician",
        return_value=0
    ):
        with pytest.raises(TechnicianError) as error:
            technician_service.delete_technician(999)

    assert error.value.code == "NOT_FOUND"


# ==========================================
# TC07 - MA KY THUAT VIEN KHONG HOP LE
# ==========================================

def test_update_technician_invalid_id():
    data = sample_technician()

    with patch.object(
        technician_service.repo,
        "update_technician"
    ) as mock_update:
        with pytest.raises(TechnicianError) as error:
            technician_service.update_technician(0, data)

    assert error.value.code == "INVALID_DATA"
    mock_update.assert_not_called()


# ==========================================
# TC08 - LOI CO SO DU LIEU
# ==========================================

def test_create_technician_database_error():
    data = sample_technician()

    with patch.object(
        technician_service.repo,
        "insert_technician",
        side_effect=sqlite3.OperationalError("database locked")
    ):
        with pytest.raises(TechnicianError) as error:
            technician_service.create_technician(data)

    assert error.value.code == "DATABASE_ERROR"
