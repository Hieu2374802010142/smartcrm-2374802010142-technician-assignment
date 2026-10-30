
import argparse
import sqlite3
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[2]
DEFAULT_DB_PATH = ROOT_DIR / "smartcrm-sprint1.db"

SCHEMA_PATH = (
    ROOT_DIR / "docs" / "database" / "schema-l04.sql"
)

REQUIRED_TABLES = {
    "khach_hang",
    "phieu_bao_hanh",
    "ky_thuat_vien",
    "phan_cong_ky_thuat_vien",
    "lich_hen",
}

REQUIRED_INDEXES = {
    "idx_phan_cong_active",
    "idx_phieu_trang_thai",
    "idx_phieu_khach_hang",
    "idx_phan_cong_ky_thuat_vien",
    "idx_lich_hen_thoi_gian",
}


def migrate_database(db_path=DEFAULT_DB_PATH):
    db_path = Path(db_path).resolve()

    if not SCHEMA_PATH.is_file():
        raise FileNotFoundError(
            f"Khong tim thay schema: {SCHEMA_PATH}"
        )

    db_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    conn = sqlite3.connect(db_path)

    try:
        conn.execute("PRAGMA foreign_keys = ON")

        existing_tables = {
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master "
                "WHERE type = 'table'"
            )
        }

        if not existing_tables:
            schema = SCHEMA_PATH.read_text(
                encoding="utf-8"
            )

            # Tao schema khi database moi hoan toan
            conn.executescript(schema)

            print("Da tao schema database.")

        elif REQUIRED_TABLES.issubset(existing_tables):
            print(
                "Database da co du 5 bang, "
                "khong tao lai."
            )

        else:
            missing = REQUIRED_TABLES - existing_tables

            raise RuntimeError(
                "Database da ton tai nhung thieu bang: "
                + ", ".join(sorted(missing))
            )

        tables = {
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master "
                "WHERE type = 'table'"
            )
        }

        indexes = {
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master "
                "WHERE type = 'index'"
            )
        }

        missing_tables = REQUIRED_TABLES - tables
        missing_indexes = REQUIRED_INDEXES - indexes

        if missing_tables or missing_indexes:
            raise RuntimeError(
                "Schema chua day du. "
                f"Thieu bang: {sorted(missing_tables)}; "
                f"thieu index: {sorted(missing_indexes)}"
            )

        print("Migration thanh cong.")
        print(f"Database: {db_path}")

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

    migrate_database(args.db)
