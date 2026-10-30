
import pytest

from src.backend.services import ticket_service


# Test 1: Lay danh sach phieu
def test_get_all_tickets(monkeypatch):
    sample = [
        {"ma_phieu": 1, "ten_thiet_bi": "iPhone 13"}
    ]

    monkeypatch.setattr(
        ticket_service.repo,
        "get_all_tickets",
        lambda: sample
    )

    result = ticket_service.get_all_tickets()

    assert result["total"] == 1
    assert result["tickets"][0]["ma_phieu"] == 1


# Test 2: Tao phieu thanh cong
def test_create_ticket_success(monkeypatch):
    monkeypatch.setattr(
        ticket_service.repo,
        "customer_exists",
        lambda customer_id: True
    )

    monkeypatch.setattr(
        ticket_service.repo,
        "insert_ticket",
        lambda customer_id, device_name: 101
    )

    result = ticket_service.create_ticket(
        1, "iPhone 13"
    )

    assert result["ma_phieu"] == 101


# Test 3: Ten thiet bi rong
def test_create_ticket_empty_device():
    with pytest.raises(ticket_service.TicketError) as exc:
        ticket_service.create_ticket(1, "   ")

    assert exc.value.code == "INVALID_DATA"


# Test 4: Khach hang khong ton tai
def test_create_ticket_customer_not_found(monkeypatch):
    monkeypatch.setattr(
        ticket_service.repo,
        "customer_exists",
        lambda customer_id: False
    )

    with pytest.raises(ticket_service.TicketError) as exc:
        ticket_service.create_ticket(999, "Samsung A54")

    assert exc.value.code == "NOT_FOUND"


# Test 5: Xem phieu khong ton tai
def test_get_ticket_not_found(monkeypatch):
    monkeypatch.setattr(
        ticket_service.repo,
        "get_ticket_by_id",
        lambda ticket_id: None
    )

    with pytest.raises(ticket_service.TicketError) as exc:
        ticket_service.get_ticket_by_id(999)

    assert exc.value.code == "NOT_FOUND"


# Test 6: Cap nhat phieu thanh cong
def test_update_ticket_success(monkeypatch):
    monkeypatch.setattr(
        ticket_service.repo,
        "customer_exists",
        lambda customer_id: True
    )

    monkeypatch.setattr(
        ticket_service.repo,
        "update_ticket",
        lambda ticket_id, customer_id, device_name: "SUCCESS"
    )

    result = ticket_service.update_ticket(
        1, 1, "iPhone 14"
    )

    assert result["ma_phieu"] == 1


# Test 7: Khong cho sua phieu da phan cong
def test_update_assigned_ticket(monkeypatch):
    monkeypatch.setattr(
        ticket_service.repo,
        "customer_exists",
        lambda customer_id: True
    )

    monkeypatch.setattr(
        ticket_service.repo,
        "update_ticket",
        lambda ticket_id, customer_id, device_name: "NOT_EDITABLE"
    )

    with pytest.raises(ticket_service.TicketError) as exc:
        ticket_service.update_ticket(
            1, 1, "iPhone 14"
        )

    assert exc.value.code == "CONFLICT"


# Test 8: Xoa phieu thanh cong
def test_delete_ticket_success(monkeypatch):
    monkeypatch.setattr(
        ticket_service.repo,
        "delete_ticket",
        lambda ticket_id: "SUCCESS"
    )

    result = ticket_service.delete_ticket(1)

    assert result["ma_phieu"] == 1


# Test 9: Khong cho xoa phieu da phan cong
def test_delete_assigned_ticket(monkeypatch):
    monkeypatch.setattr(
        ticket_service.repo,
        "delete_ticket",
        lambda ticket_id: "NOT_DELETABLE"
    )

    with pytest.raises(ticket_service.TicketError) as exc:
        ticket_service.delete_ticket(1)

    assert exc.value.code == "CONFLICT"
