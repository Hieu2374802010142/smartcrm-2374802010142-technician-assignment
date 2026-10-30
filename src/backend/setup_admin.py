
import hashlib
import secrets
import getpass
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
ENV_FILE = ROOT_DIR / ".env"

def main():
    print("=== SmartCRM L04 - Cai dat tai khoan quan ly ===")

    username = input("Ten dang nhap [manager]: ").strip() or "manager"

    password = getpass.getpass("Mat khau: ")
    confirm = getpass.getpass("Nhap lai mat khau: ")

    if not password:
        print("Loi: Mat khau khong duoc de trong.")
        return

    if password != confirm:
        print("Loi: Hai mat khau khong khop.")
        return

    salt = secrets.token_bytes(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        600000
    )

    content = (
        f"SMARTCRM_ADMIN_USER={username}\n"
        f"SMARTCRM_ADMIN_PASSWORD_SALT={salt.hex()}\n"
        f"SMARTCRM_ADMIN_PASSWORD_HASH={password_hash.hex()}\n"
    )

    if ENV_FILE.exists():
        answer = input(".env da ton tai. Ghi de? (y/N): ")
        if answer.strip().lower() != "y":
            print("Da huy. Khong thay doi .env.")
            return

    ENV_FILE.write_text(content, encoding="utf-8")
    try:
        ENV_FILE.chmod(0o600)
    except OSError:
        pass

    print("Da tao file .env.")
    print("Khong dua file .env len GitHub.")
    print("De nap cau hinh, chay: set -a; source .env; set +a")

if __name__ == "__main__":
    main()
