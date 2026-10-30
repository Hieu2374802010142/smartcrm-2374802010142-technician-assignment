
import argparse
import sqlite3
from pathlib import Path

from src.backend.migrate import (
    DEFAULT_DB_PATH,
    migrate_database,
)


CUSTOMERS = [
    ("Nguyen Van Nam", "0909000001"),
    ("Tran Thi Hoa", "0909000002"),
    ("Le Minh Tuan", "0909000003"),
]

TECHNICIANS = [
    ("Nguyen Van An", "0901234567", "Phan cung", 1),
    ("Tran Minh Binh", "0912345678", "Phan mem", 1),
    ("Le Quoc Cuong", "0923456789", "Dien thoai", 1),
]

TICKETS = [
    ("0909000001", "iPhone 13 - Demo"),
    ("0909000002", "Samsung Galaxy S22 - Demo"),
    ("0909000003", "OPPO Reno 8 - Demo"),
]


def seed_database(db_path=DEFAULT_DB_PATH):
    db_path = Path(db_path).resolve()

    # Tao schema neu database chua ton tai
    migrate_database(db_path)

    conn = sqlite3.connect(db_path)

    try:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute("BEGIN")

        inserted_customers = 0
        inserted_technicians = 0
        inserted_tickets = 0

        # 1. Seed khach hang
        for name, phone in CUSTOMERS:
            existing = conn.execute(
                """
                SELECT ma_khach_hang
                FROM khach_hang
                WHERE so_dien_thoai = ?
                LIMIT 1
                """,
                (phone,)
            ).fetchone()

            if existing is None:
                conn.execute(
                    """
                    INSERT INTO khach_hang
                    (ho_ten, so_dien_thoai)
                    VALUES (?, ?)
                    """,
                    (name, phone)
                )
                inserted_customers += 1

        # 2. Seed ky thuat vien
        for name, phone, specialty, active in TECHNICIANS:
            existing = conn.execute(
                """
                SELECT ma_ky_thuat_vien
                FROM ky_thuat_vien
                WHERE so_dien_thoai = ?
                LIMIT 1
                """,
                (phone,)
            ).fetchone()

            if existing is None:
                conn.execute(
                    """
                    INSERT INTO ky_thuat_vien
                    (
                        ho_ten,
                        so_dien_thoai,
                        chuyen_mon,
                        dang_hoat_dong
                    )
                    VALUES (?, ?, ?, ?)
                    """,
                    (name, phone, specialty, active)
                )
                inserted_technicians += 1

        # 3. Seed phieu bao hanh
        for phone, device in TICKETS:
            customer = conn.execute(
                """
                SELECT ma_khach_hang
                FROM khach_hang
                WHERE so_dien_thoai = ?
                LIMIT 1
                """,
                (phone,)
            ).fetchone()

            if customer is None:
                raise RuntimeError(
                    f"Khong tim thay khach hang: {phone}"
                )

            customer_id = customer[0]

            existing = conn.execute(
                """
                SELECT ma_phieu
                FROM phieu_bao_hanh
                WHERE ma_khach_hang = ?
                  AND ten_thiet_bi = ?
                LIMIT 1
                """,
                (customer_id, device)
            ).fetchone()

            if existing is None:
                conn.execute(
                    """
                    INSERT INTO phieu_bao_hanh
                    (
                        ma_khach_hang,
                        ten_thiet_bi,
                        trang_thai
                    )
                    VALUES (?, ?, 'Mới')
                    """,
                    (customer_id, device)
                )
                inserted_tickets += 1

        conn.commit()

        print("\n=== KET QUA SEED ===")
        print(f"Khach hang moi: {inserted_customers}")
        print(f"Ky thuat vien moi: {inserted_technicians}")
        print(f"Phieu bao hanh moi: {inserted_tickets}")
        print("Seed thanh cong!")

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--db",
        default=str(DEFAULT_DB_PATH),
        help="Duong dan SQLite database"
    )

    args = parser.parse_args()

    seed_database(args.db)
