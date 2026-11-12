
# BUG LOG – BÀI TẬP 3
## Dự án SmartCRM – MEKONG MOBILE
**Luồng:** L04 – Phân công kỹ thuật viên và lịch hẹn  
**Ngày kiểm thử:** 06/11/2026  
**Trạng thái:** 3 lỗi đã sửa, kiểm thử hồi quy thành công

---

## 1. Tổng hợp lỗi

| Mã lỗi | Mức độ | Mô tả | Trạng thái | Commit |
|---|---|---|---|---|
| BUG-01 | Major | API danh sách phân công thiếu xác thực | Fixed | c8c966d |
| BUG-02 | Major | API phiếu chưa phân công thiếu xác thực | Fixed | b50ce78 |
| BUG-03 | Major | API danh sách kỹ thuật viên thiếu xác thực | Fixed | a4651d7 |

## 2. Chi tiết lỗi

### BUG-01 – API danh sách phân công thiếu xác thực

- **Severity:** Major
- **Endpoint:** GET /api/tickets/assignments
- **Mô tả:** Người dùng chưa đăng nhập vẫn có thể xem danh sách phân công kỹ thuật viên.
- **Bước tái hiện:** Gửi GET request đến endpoint mà không cung cấp token.
- **Kết quả thực tế:** HTTP 200, trả về dữ liệu phân công.
- **Kết quả mong đợi:** HTTP 401 Unauthorized.
- **Nguyên nhân:** Endpoint chưa khai báo Depends(check_manager).
- **Cách sửa:** Bổ sung kiểm tra xác thực và quyền quản lý bằng Depends(check_manager).
- **Kiểm thử hồi quy:** test_assignments_requires_authentication – PASS.
- **Trạng thái:** Fixed.
- **Commit:** https://github.com/Hieu2374802010142/smartcrm-2374802010142-technician-assignment/commit/c8c966d
- **Ảnh minh chứng:** [Bug01.png](screenshots/Bug01.png)

### BUG-02 – API phiếu chưa phân công thiếu xác thực

- **Severity:** Major
- **Endpoint:** GET /api/tickets/unassigned
- **Mô tả:** Người dùng chưa đăng nhập vẫn có thể xem các phiếu bảo hành chưa phân công, bao gồm thông tin khách hàng.
- **Bước tái hiện:** Gửi GET request đến endpoint mà không cung cấp token.
- **Kết quả thực tế:** HTTP 200, trả về dữ liệu phiếu bảo hành.
- **Kết quả mong đợi:** HTTP 401 Unauthorized.
- **Nguyên nhân:** Endpoint chưa khai báo Depends(check_manager).
- **Cách sửa:** Bổ sung Depends(check_manager) vào hàm get_unassigned_tickets.
- **Kiểm thử hồi quy:** test_unassigned_tickets_requires_authentication – PASS.
- **Trạng thái:** Fixed.
- **Commit:** https://github.com/Hieu2374802010142/smartcrm-2374802010142-technician-assignment/commit/b50ce78
- **Ảnh minh chứng:** [Bug02.png](screenshots/Bug02.png)

### BUG-03 – API danh sách kỹ thuật viên thiếu xác thực

- **Severity:** Major
- **Endpoint:** GET /api/technicians
- **Mô tả:** Người dùng chưa đăng nhập vẫn có thể xem họ tên, số điện thoại, chuyên môn và trạng thái của kỹ thuật viên.
- **Bước tái hiện:** Gửi GET request đến endpoint mà không cung cấp token.
- **Kết quả thực tế:** HTTP 200, trả về danh sách 9 kỹ thuật viên.
- **Kết quả mong đợi:** HTTP 401 Unauthorized.
- **Nguyên nhân:** Hàm get_technicians chưa khai báo Depends(check_manager).
- **Cách sửa:** Bổ sung Depends(check_manager) để yêu cầu quyền quản lý.
- **Kiểm thử hồi quy:** test_technicians_requires_authentication – PASS.
- **Trạng thái:** Fixed.
- **Commit:** https://github.com/Hieu2374802010142/smartcrm-2374802010142-technician-assignment/commit/a4651d7
- **Ảnh minh chứng:** [Bug03.png](screenshots/Bug03.png)

---

## 3. Kết quả kiểm thử sau khi sửa

- BUG-01: Regression test PASS.
- BUG-02: Regression test PASS.
- BUG-03: Regression test PASS.
- Toàn bộ dự án: **32/32 test PASS**.
- Lệnh kiểm thử: `python3 -m pytest -q`.
- Kết quả gần nhất: `32 passed in 0.30s`.

## 4. Kết luận

Trong quá trình thực hiện BT3, đã phát hiện và sửa 3 lỗi liên quan đến xác thực và phân quyền API.

Mỗi lỗi được tái hiện bằng kiểm thử thất bại trước khi sửa, sau đó bổ sung kiểm tra quyền và chạy lại kiểm thử thành công.

Ba lỗi có ba commit sửa riêng biệt trên GitHub. Kết quả kiểm thử cuối cùng đạt 32/32 PASS.
