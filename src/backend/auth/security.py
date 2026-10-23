
import secrets
from datetime import datetime, timedelta, timezone

from fastapi import Header, HTTPException


# Thoi gian het han token: 60 phut
TOKEN_LIFETIME_MINUTES = 60

# Luu phien dang nhap trong bo nho
sessions = {}


def create_token(username: str, role: str):
    token = secrets.token_urlsafe(32)

    expires_at = datetime.now(timezone.utc) + timedelta(
        minutes=TOKEN_LIFETIME_MINUTES
    )

    sessions[token] = {
        "username": username,
        "role": role,
        "expires_at": expires_at
    }

    return token


def get_current_user(authorization: str | None = Header(default=None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Chua dang nhap"
        )

    token = authorization.removeprefix("Bearer ").strip()
    session = sessions.get(token)

    if session is None:
        raise HTTPException(
            status_code=401,
            detail="Token khong hop le"
        )

    if datetime.now(timezone.utc) >= session["expires_at"]:
        sessions.pop(token, None)
        raise HTTPException(
            status_code=401,
            detail="Phien dang nhap da het han"
        )

    return {
        "username": session["username"],
        "role": session["role"]
    }


def require_manager(
    user: dict
):
    if user["role"] != "manager":
        raise HTTPException(
            status_code=403,
            detail="Ban khong co quyen thuc hien"
        )

    return user
