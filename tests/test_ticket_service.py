
import pytest
from unittest.mock import patch

from src.backend.services import ticket_service
from src.backend.services.ticket_service import TicketError


# ==========================================
# TC01 - XEM PHIEU CHUA PHAN CONG
# ==========================================

def test_get_unassigned_tickets():
    sample_tickets = [
        {
            "ma_phieu": 2,
            "ten_thiet_bi": "Samsung Galaxy S22",
            "trang_thai": "Mới"
        },
        {
            "ma_phieu": 3,
            "ten_thiet_bi": "OPPO Reno 8",
            "trang_thai": "Mới"
        }
    ]

    with patch.object(
        ticket_service.repo,
        "get_unassigned_tickets",
        return_value=sample_tickets
    ):
        result = ticket_service.get_unassigned_tickets()

    assert result["total"] == 2
    assert len(result["tickets"]) == 2
    assert result["tickets"][0]["ma_phieu"] == 2
    assert result["tickets"][1]["ma_phieu"] == 3


# ==========================================
# TC02 - PHAN CONG KY THUAT VIEN THANH CONG
# ==========================================

def test_assign_technician_success():
    mock_result = {
        "status": "SUCCESS",
        "ma_phan_cong": 10
    }

    with patch.object(
        ticket_service.repo,
        "assign_technician",
        return_value=mock_result
    ):
        result = ticket_service.assign_technician(
            ticket_id=2,
            technician_id=1
        )

    assert result["ma_phan_cong"] == 10
    assert result["ma_phieu"] == 2
    assert result["ma_ky_thuat_vien"] == 1
    assert result["message"] == "Phan cong ky thuat vien thanh cong"


# ==========================================
# TC03 - TU CHOI PHIEU KHONG CON TRANG THAI MOI
# ==========================================

def test_assign_technician_ticket_not_new():
    mock_result = {
        "status": "TICKET_NOT_NEW"
    }

    with patch.object(
        ticket_service.repo,
        "assign_technician",
        return_value=mock_result
    ):
        with pytest.raises(TicketError) as error:
            ticket_service.assign_technician(
                ticket_id=1,
                technician_id=2
            )

    assert error.value.code == "CONFLICT"
    assert "Moi" in error.value.message


# ==========================================
# TC04 - DAT LICH HEN THANH CONG
# ==========================================

def test_create_appointment_success():
    mock_result = {
        "status": "SUCCESS",
        "ma_lich_hen": 10
    }

    with patch.object(
        ticket_service.repo,
        "create_appointment",
        return_value=mock_result
    ) as mock_create:
        result = ticket_service.create_appointment(
            assignment_id=2,
            ngay_hen="2026-10-28",
            gio_bat_dau="09:00:00",
            gio_ket_thuc="10:00:00",
            loai_lich_hen="Nhan thiet bi"
        )

    assert result["ma_lich_hen"] == 10
    assert result["ma_phan_cong"] == 2
    assert result["message"] == "Dat lich hen thanh cong"

    mock_create.assert_called_once_with(
        2,
        "2026-10-28",
        "09:00:00",
        "10:00:00",
        "Nhan thiet bi"
    )


# ==========================================
# TC05 - TU CHOI LICH HEN BI TRUNG
# ==========================================

def test_create_appointment_overlap():
    mock_result = {
        "status": "APPOINTMENT_OVERLAP"
    }

    with patch.object(
        ticket_service.repo,
        "create_appointment",
        return_value=mock_result
    ):
        with pytest.raises(TicketError) as error:
            ticket_service.create_appointment(
                assignment_id=2,
                ngay_hen="2026-10-27",
                gio_bat_dau="09:00:00",
                gio_ket_thuc="10:00:00",
                loai_lich_hen="Nhan thiet bi"
            )

    assert error.value.code == "CONFLICT"
    assert "trung" in error.value.message.lower()


# ==========================================
# TC06 - TU CHOI THOI GIAN KHONG HOP LE
# ==========================================

def test_create_appointment_invalid_time():
    with patch.object(
        ticket_service.repo,
        "create_appointment"
    ) as mock_create:
        with pytest.raises(TicketError) as error:
            ticket_service.create_appointment(
                assignment_id=2,
                ngay_hen="2026-10-28",
                gio_bat_dau="10:00:00",
                gio_ket_thuc="09:00:00",
                loai_lich_hen="Nhan thiet bi"
            )

    assert error.value.code == "INVALID_DATA"

    # Du lieu sai khong duoc gui xuong Repository
    mock_create.assert_not_called()
