
import os
import hashlib
import hmac

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from src.backend.auth.security import create_token


router = APIRouter(prefix="/api/auth", tags=["Authentication"])


class LoginRequest(BaseModel):
    username: str
    password: str


def hash_password(password: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        600000
    )


@router.post("/login")
def login(data: LoginRequest):
    username = os.getenv("SMARTCRM_ADMIN_USER")
    password_hash = os.getenv("SMARTCRM_ADMIN_PASSWORD_HASH")
    password_salt = os.getenv("SMARTCRM_ADMIN_PASSWORD_SALT")

    if not username or not password_hash or not password_salt:
        raise HTTPException(
            status_code=503,
            detail="Tai khoan quan ly chua duoc cau hinh"
        )

    try:
        expected_hash = bytes.fromhex(password_hash)
        salt = bytes.fromhex(password_salt)
    except ValueError:
        raise HTTPException(
            status_code=503,
            detail="Cau hinh tai khoan khong hop le"
        )

    actual_hash = hash_password(data.password, salt)

    if (
        not hmac.compare_digest(data.username, username)
        or not hmac.compare_digest(actual_hash, expected_hash)
    ):
        raise HTTPException(
            status_code=401,
            detail="Sai ten dang nhap hoac mat khau"
        )

    token = create_token(username, "manager")

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": "manager"
    }
