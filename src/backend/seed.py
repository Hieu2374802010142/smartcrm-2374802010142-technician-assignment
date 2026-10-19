
import sqlite3
from pathlib import Path

# Thu muc goc cua du an
ROOT_DIR = Path(__file__).resolve().parents[2]

DB_PATH = ROOT_DIR / "smartcrm-sprint1.db"
SCHEMA_PATH = ROOT_DIR / "docs" / "database" / "schema-l04.sql"


def seed_database():
    # Kiem tra file SQL
    if not SCHEMA_PATH.exists():
        print("Loi: Khong tim thay file schema-l04.sql")
        return

    # Ket noi database
    conn = sqlite3.connect(DB_PATH)

    try:
        # Kiem tra cac bang hien co
        existing_tables = {
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master "
                "WHERE type = 'table'"
            ).fetchall()
        }

        required_tables = {
            "khach_hang",
            "phieu_bao_hanh",
            "ky_thuat_vien",
            "phan_cong_ky_thuat_vien",
            "lich_hen",
        }

        # Tao bang khi database hoan toan moi
        if not existing_tables:
            schema = SCHEMA_PATH.read_text(encoding="utf-8")
            conn.executescript(schema)
            print("Da tao cac bang database.")

        # Neu database da co bang thi khong tao lai
        elif required_tables.issubset(existing_tables):
            print("Database da co day du bang, bo qua tao bang.")

        else:
            missing_tables = required_tables - existing_tables
            print("Loi: Database thieu bang:", missing_tables)
            print("Khong thay doi database.")
            return

        # Du lieu ky thuat vien mau
        technicians = [
            ("Nguyen Van An", "0901234567", "Phan cung", 1),
            ("Tran Minh Binh", "0912345678", "Phan mem", 1),
            ("Le Quoc Cuong", "0923456789", "Dien thoai", 1),
        ]

        # Kiem tra du lieu hien co
        count = conn.execute(
            "SELECT COUNT(*) FROM ky_thuat_vien"
        ).fetchone()[0]

        if count == 0:
            conn.executemany(
                """
                INSERT INTO ky_thuat_vien
                (ho_ten, so_dien_thoai, chuyen_mon, dang_hoat_dong)
                VALUES (?, ?, ?, ?)
                """,
                technicians,
            )
            conn.commit()
            print("Da them 3 ky thuat vien mau.")
        else:
            print(
                f"Bang da co {count} ky thuat vien, "
                "khong them trung."
            )

        print("Khoi tao database thanh cong!")

    except sqlite3.Error as error:
        conn.rollback()
        print(f"Loi SQLite: {error}")

    finally:
        conn.close()


if __name__ == "__main__":
    seed_database()
