from unittest.mock import patch

from fastapi.testclient import TestClient

from src.backend.main import app
from src.backend.auth.security import create_token
from src.backend.services import ticket_service


client = TestClient(app)
URL = "/api/tickets/0/assign"
DATA = {"ma_ky_thuat_vien": 1}


# TC07 - Chua dang nhap
def test_assign_without_token():
    response = client.post(URL, json=DATA)
    assert response.status_code == 401


# TC08 - Token khong hop le
def test_assign_invalid_token():
    response = client.post(
        URL,
        json=DATA,
        headers={"Authorization": "Bearer token-sai"}
    )
    assert response.status_code == 401


# TC09 - Khong co quyen manager
def test_assign_without_manager_role():
    token = create_token("technician", "technician")

    response = client.post(
        URL,
        json=DATA,
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 403


# TC10 - Manager duoc phep phan cong
def test_assign_with_manager_role():
    token = create_token("manager", "manager")

    with patch.object(
        ticket_service,
        "assign_technician",
        return_value={"message": "Phan cong thanh cong"}
    ) as mock_assign:
        response = client.post(
            URL,
            json=DATA,
            headers={"Authorization": f"Bearer {token}"}
        )

    assert response.status_code == 200
    mock_assign.assert_called_once_with(0, 1)