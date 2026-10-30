
from src.backend.repositories.technician_repository import get_db_connection


# Lay danh sach phieu bao hanh chua phan cong
def get_unassigned_tickets():
    conn = get_db_connection()

    try:
        cursor = conn.execute("""
            SELECT
                p.ma_phieu,
                p.ten_thiet_bi,
                p.trang_thai,
                p.ngay_tao,
                k.ho_ten AS ten_khach_hang,
                k.so_dien_thoai
            FROM phieu_bao_hanh p
            JOIN khach_hang k
                ON p.ma_khach_hang = k.ma_khach_hang
            WHERE p.trang_thai = 'Mới'
              AND NOT EXISTS (
                  SELECT 1
                  FROM phan_cong_ky_thuat_vien pc
                  WHERE pc.ma_phieu = p.ma_phieu
                    AND pc.trang_thai_phan_cong = 'Đang hoạt động'
              )
            ORDER BY p.ngay_tao DESC, p.ma_phieu DESC
        """)

        return [dict(row) for row in cursor.fetchall()]

    finally:
        conn.close()

# UC03 - Phan cong ky thuat vien
def assign_technician(ticket_id, technician_id):
    conn = get_db_connection()

    try:
        conn.execute("BEGIN IMMEDIATE")

        # Kiem tra phieu bao hanh
        ticket = conn.execute("""
            SELECT trang_thai
            FROM phieu_bao_hanh
            WHERE ma_phieu = ?
        """, (ticket_id,)).fetchone()

        if ticket is None:
            return_result = "TICKET_NOT_FOUND"

        elif ticket["trang_thai"] != "Mới":
            return_result = "TICKET_NOT_NEW"

        else:
            # Kiem tra ky thuat vien
            technician = conn.execute("""
                SELECT dang_hoat_dong
                FROM ky_thuat_vien
                WHERE ma_ky_thuat_vien = ?
            """, (technician_id,)).fetchone()

            if technician is None:
                return_result = "TECHNICIAN_NOT_FOUND"

            elif technician["dang_hoat_dong"] != 1:
                return_result = "TECHNICIAN_INACTIVE"

            else:
                # Luu phan cong
                cursor = conn.execute("""
                    INSERT INTO phan_cong_ky_thuat_vien
                        (ma_phieu, ma_ky_thuat_vien)
                    VALUES (?, ?)
                """, (ticket_id, technician_id))

                # Cap nhat trang thai phieu
                conn.execute("""
                    UPDATE phieu_bao_hanh
                    SET trang_thai = 'Đã phân công'
                    WHERE ma_phieu = ?
                """, (ticket_id,))

                conn.commit()

                return {
                    "status": "SUCCESS",
                    "ma_phan_cong": cursor.lastrowid
                }

        conn.rollback()
        return {"status": return_result}

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()

# UC04 - Dat lich hen va UC05 - Kiem tra trung lich
def create_appointment(
    assignment_id,
    ngay_hen,
    gio_bat_dau,
    gio_ket_thuc,
    loai_lich_hen
):
    conn = get_db_connection()

    try:
        conn.execute("BEGIN IMMEDIATE")

        # Kiem tra phan cong co ton tai va dang hoat dong
        assignment = conn.execute("""
            SELECT ma_ky_thuat_vien
            FROM phan_cong_ky_thuat_vien
            WHERE ma_phan_cong = ?
              AND trang_thai_phan_cong = 'Đang hoạt động'
        """, (assignment_id,)).fetchone()

        if assignment is None:
            conn.rollback()
            return {"status": "ASSIGNMENT_NOT_FOUND"}

        # Kiem tra lich hen trung cua cung ky thuat vien
        overlap = conn.execute("""
            SELECT lh.ma_lich_hen
            FROM lich_hen lh
            JOIN phan_cong_ky_thuat_vien pc
                ON lh.ma_phan_cong = pc.ma_phan_cong
            WHERE pc.ma_ky_thuat_vien = ?
              AND lh.ngay_hen = ?
              AND lh.trang_thai_lich_hen = 'Còn hiệu lực'
              AND lh.gio_bat_dau < ?
              AND lh.gio_ket_thuc > ?
            LIMIT 1
        """, (
            assignment["ma_ky_thuat_vien"],
            ngay_hen,
            gio_ket_thuc,
            gio_bat_dau
        )).fetchone()

        if overlap is not None:
            conn.rollback()
            return {"status": "APPOINTMENT_OVERLAP"}

        # Luu lich hen moi
        cursor = conn.execute("""
            INSERT INTO lich_hen (
                ma_phan_cong,
                ngay_hen,
                gio_bat_dau,
                gio_ket_thuc,
                loai_lich_hen
            )
            VALUES (?, ?, ?, ?, ?)
        """, (
            assignment_id,
            ngay_hen,
            gio_bat_dau,
            gio_ket_thuc,
            loai_lich_hen
        ))

        conn.commit()

        return {
            "status": "SUCCESS",
            "ma_lich_hen": cursor.lastrowid
        }

    except Exception:
        conn.rollback()
        raise

    finally:
        conn.close()

# Lay danh sach phan cong dang hoat dong
def get_active_assignments():
    conn = get_db_connection()

    try:
        cursor = conn.execute("""
            SELECT
                pc.ma_phan_cong,
                pc.ma_phieu,
                p.ten_thiet_bi,
                pc.ma_ky_thuat_vien,
                ktv.ho_ten AS ten_ky_thuat_vien
            FROM phan_cong_ky_thuat_vien pc
            JOIN phieu_bao_hanh p
                ON pc.ma_phieu = p.ma_phieu
            JOIN ky_thuat_vien ktv
                ON pc.ma_ky_thuat_vien = ktv.ma_ky_thuat_vien
            WHERE pc.trang_thai_phan_cong = 'Đang hoạt động'
            ORDER BY pc.ma_phan_cong DESC
        """)

        return [dict(row) for row in cursor.fetchall()]

    finally:
        conn.close()

# ==========================================
# CRUD PHIEU BAO HANH - BT2 TRACK SE
# ==========================================

def get_all_tickets():
    conn = get_db_connection()
    try:
        rows = conn.execute("""
            SELECT p.ma_phieu, p.ma_khach_hang,
                   p.ten_thiet_bi, p.trang_thai,
                   p.ngay_tao,
                   k.ho_ten AS ten_khach_hang
            FROM phieu_bao_hanh p
            JOIN khach_hang k
              ON p.ma_khach_hang = k.ma_khach_hang
            ORDER BY p.ma_phieu DESC
        """).fetchall()

        return [dict(row) for row in rows]
    finally:
        conn.close()


def get_ticket_by_id(ticket_id):
    conn = get_db_connection()
    try:
        row = conn.execute("""
            SELECT ma_phieu, ma_khach_hang,
                   ten_thiet_bi, trang_thai, ngay_tao
            FROM phieu_bao_hanh
            WHERE ma_phieu = ?
        """, (ticket_id,)).fetchone()

        return dict(row) if row else None
    finally:
        conn.close()


def customer_exists(customer_id):
    conn = get_db_connection()
    try:
        row = conn.execute("""
            SELECT 1 FROM khach_hang
            WHERE ma_khach_hang = ?
        """, (customer_id,)).fetchone()

        return row is not None
    finally:
        conn.close()


def insert_ticket(customer_id, device_name):
    conn = get_db_connection()
    try:
        cursor = conn.execute("""
            INSERT INTO phieu_bao_hanh
                (ma_khach_hang, ten_thiet_bi)
            VALUES (?, ?)
        """, (customer_id, device_name))

        conn.commit()
        return cursor.lastrowid
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def update_ticket(ticket_id, customer_id, device_name):
    conn = get_db_connection()
    try:
        conn.execute("BEGIN IMMEDIATE")

        ticket = conn.execute("""
            SELECT trang_thai FROM phieu_bao_hanh
            WHERE ma_phieu = ?
        """, (ticket_id,)).fetchone()

        if ticket is None:
            conn.rollback()
            return "NOT_FOUND"

        assignment = conn.execute("""
            SELECT 1 FROM phan_cong_ky_thuat_vien
            WHERE ma_phieu = ?
            LIMIT 1
        """, (ticket_id,)).fetchone()

        if ticket["trang_thai"] != "Mới" or assignment:
            conn.rollback()
            return "NOT_EDITABLE"

        conn.execute("""
            UPDATE phieu_bao_hanh
            SET ma_khach_hang = ?, ten_thiet_bi = ?
            WHERE ma_phieu = ?
        """, (customer_id, device_name, ticket_id))

        conn.commit()
        return "SUCCESS"
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def delete_ticket(ticket_id):
    conn = get_db_connection()
    try:
        conn.execute("BEGIN IMMEDIATE")

        ticket = conn.execute("""
            SELECT trang_thai FROM phieu_bao_hanh
            WHERE ma_phieu = ?
        """, (ticket_id,)).fetchone()

        if ticket is None:
            conn.rollback()
            return "NOT_FOUND"

        assignment = conn.execute("""
            SELECT 1 FROM phan_cong_ky_thuat_vien
            WHERE ma_phieu = ?
            LIMIT 1
        """, (ticket_id,)).fetchone()

        if ticket["trang_thai"] != "Mới" or assignment:
            conn.rollback()
            return "NOT_DELETABLE"

        conn.execute("""
            DELETE FROM phieu_bao_hanh
            WHERE ma_phieu = ?
        """, (ticket_id,))

        conn.commit()
        return "SUCCESS"
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
