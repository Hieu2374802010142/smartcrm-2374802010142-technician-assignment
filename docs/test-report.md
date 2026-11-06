# TEST REPORT – SMARTCRM L04

**Chức năng:** Phân công kỹ thuật viên và lịch hẹn  
**Giai đoạn:** Buổi 14 – Kiểm thử hệ thống  
**Công cụ:** Python 3.12.0, pytest 9.1.1, SQLite  
**Ngày thực hiện:** 06/11/2026

## 1. Kết quả kiểm thử tổng quan

- Tổng số bài kiểm thử tự động ở lần chạy toàn bộ gần nhất: 29
- PASS: 29
- FAIL: 0
- Thời gian thực thi toàn bộ: 0.27 giây
- Số test case đã chọn và ghi nhận trong báo cáo: 12
- Boundary Testing: 2 PASS
- Security Testing: 2 PASS
- Invalid Input Testing: 3 PASS
- Happy Path Testing: 4 PASS
- Reproducibility Testing: 1 PASS

## 2. Test Case – Boundary Testing

| ID | Điều kiện trước | Các bước thực hiện | Dữ liệu kiểm thử | Kết quả mong đợi | Mức ưu tiên | Kết quả thực tế | Trạng thái |
|---|---|---|---|---|---|---|---|
| TC-B01 | Có phân công đang hoạt động và lịch 09:00–10:00 | Chạy `test_appointment_adjacent_boundary` | Ngày 10/11/2026, lịch mới 10:00–11:00 | Tạo lịch thành công, trả về `SUCCESS` | High | Repository trả về `SUCCESS`; pytest PASSED | PASS |
| TC-B02 | Có phân công đang hoạt động và lịch 09:00–10:00 | Chạy `test_appointment_overlap_one_minute` | Ngày 10/11/2026, lịch mới 09:59–11:00 | Từ chối lịch trùng, trả về `APPOINTMENT_OVERLAP` | High | Repository trả về `APPOINTMENT_OVERLAP`; pytest PASSED | PASS |

## 3. Test Case – Security Testing

| ID | Điều kiện trước | Các bước thực hiện | Dữ liệu kiểm thử | Kết quả mong đợi | Mức ưu tiên | Kết quả thực tế | Trạng thái |
|---|---|---|---|---|---|---|---|
| TC-S01 | API phân công kỹ thuật viên đã được cấu hình xác thực | Chạy `test_assign_without_token`, gửi POST đến `/api/tickets/0/assign` không kèm token | `{"ma_ky_thuat_vien": 1}`, không có Authorization header | HTTP 401 Unauthorized | High | HTTP 401; pytest PASSED | PASS |
| TC-S02 | API có kiểm tra vai trò người dùng | Chạy `test_assign_without_manager_role`, gửi POST đến `/api/tickets/0/assign` bằng token technician | `{"ma_ky_thuat_vien": 1}`, token có role technician | HTTP 403 Forbidden | High | HTTP 403; pytest PASSED | PASS |

## 4. Test Case – Invalid Input Testing

| ID | Điều kiện trước | Các bước thực hiện | Dữ liệu kiểm thử | Kết quả mong đợi | Mức ưu tiên | Kết quả thực tế | Trạng thái |
|---|---|---|---|---|---|---|---|
| TC-I01 | Service đặt lịch hẹn đã được khởi tạo | Gọi `create_appointment()` với giờ kết thúc trước giờ bắt đầu | Phân công ID 2, ngày 28/10/2026, 10:00–09:00 | Phát sinh `TicketError` với mã `INVALID_DATA`, không gọi Repository | High | `INVALID_DATA`, Repository không được gọi; pytest PASSED | PASS |
| TC-I02 | Repository được giả lập trả trạng thái `TICKET_NOT_NEW` | Gọi `assign_technician()` cho phiếu không còn trạng thái Mới | Phiếu ID 1, kỹ thuật viên ID 2 | Phát sinh `TicketError` với mã `CONFLICT` | High | `CONFLICT`, thông báo chứa `Moi`; pytest PASSED | PASS |
| TC-I03 | Service tạo phiếu bảo hành đã được khởi tạo | Gọi `create_ticket()` với tên thiết bị chỉ chứa khoảng trắng | Khách hàng ID 1, tên thiết bị `"   "` | Phát sinh `TicketError` với mã `INVALID_DATA` | High | `INVALID_DATA`; pytest PASSED | PASS |

## 5. Test Case – Happy Path Testing

| ID | Điều kiện trước | Các bước thực hiện | Dữ liệu kiểm thử | Kết quả mong đợi | Mức ưu tiên | Kết quả thực tế | Trạng thái |
|---|---|---|---|---|---|---|---|
| TC-H01 | Service lấy danh sách phiếu chưa phân công hoạt động; Repository được giả lập trả về 2 phiếu | Chạy `test_get_unassigned_tickets`, gọi `get_unassigned_tickets()` | Phiếu ID 2 – Samsung Galaxy S22; phiếu ID 3 – OPPO Reno 8; trạng thái Mới | `total = 2`, danh sách có 2 phiếu với ID 2 và 3 | High | Trả về đúng 2 phiếu và mã phiếu; pytest PASSED | PASS |
| TC-H02 | Repository được giả lập trả trạng thái `SUCCESS` và mã phân công 10 | Chạy `test_assign_technician_success`, gọi `assign_technician()` | Phiếu ID 2, kỹ thuật viên ID 1 | Trả mã phân công 10, mã phiếu 2, mã kỹ thuật viên 1 và thông báo thành công | High | Trả đúng dữ liệu và thông báo `Phan cong ky thuat vien thanh cong`; pytest PASSED | PASS |
| TC-H03 | Repository được giả lập tạo lịch thành công với mã lịch hẹn 10 | Chạy `test_create_appointment_success`, gọi `create_appointment()` | Phân công ID 2, ngày 28/10/2026, 09:00–10:00, loại lịch `Nhan thiet bi` | Trả mã lịch hẹn 10, mã phân công 2, thông báo thành công; Repository nhận đúng tham số | High | Trả đúng dữ liệu và thông báo `Dat lich hen thanh cong`; Repository được gọi một lần với đúng tham số; pytest PASSED | PASS |
| TC-H04 | Repository được giả lập xác nhận khách hàng tồn tại và trả mã phiếu 101 | Chạy `test_create_ticket_success`, gọi `create_ticket()` | Khách hàng ID 1, thiết bị `iPhone 13` | Trả về mã phiếu bảo hành 101 | High | `ma_phieu = 101`; pytest PASSED | PASS |

## 6. Test Case – Reproducibility Testing

| ID | Điều kiện trước | Các bước thực hiện | Dữ liệu kiểm thử | Kết quả mong đợi | Mức ưu tiên | Kết quả thực tế | Trạng thái |
|---|---|---|---|---|---|---|---|
| TC-R01 | Có quyền tạo SQLite database thử nghiệm tại thư mục `/tmp`; database chưa tồn tại trước lần chạy đầu | Chạy `python3 -m src.backend.seed --db /tmp/smartcrm-bt3-repro-test.db` hai lần liên tiếp, sau đó truy vấn số lượng bản ghi | Database `smartcrm-bt3-repro-test.db`; dữ liệu mẫu gồm 3 khách hàng, 3 kỹ thuật viên và 3 phiếu bảo hành | Migration và seed đều thành công; lần thứ hai không thêm bản ghi mới; mỗi bảng dữ liệu mẫu có 3 bản ghi | High | Lần đầu thêm 3 khách hàng, 3 kỹ thuật viên, 3 phiếu; lần hai thêm 0 bản ghi; truy vấn SQLite xác nhận mỗi bảng có 3 bản ghi | PASS |

## 7. Minh chứng kiểm thử

### 7.1. Boundary Testing

**Test case:** TC-B01 và TC-B02

**Ảnh minh chứng:** [Boundary Testing](screenshots/TC-B01-TC-B02-boundary.png)

**Lệnh thực thi:**

`python3 -m pytest tests/test_appointment_boundary.py -v`

**Kết quả:** 2 passed.

### 7.2. Security Testing

**Test case:** TC-S01 và TC-S02

**Ảnh minh chứng:** [Security Testing](screenshots/TC-S01-TC-S02-security.png)

**Lệnh thực thi:**

`python3 -m pytest tests/test_auth.py::test_assign_without_token tests/test_auth.py::test_assign_without_manager_role -v`

**Kết quả:** 2 passed in 0.23s.

### 7.3. Invalid Input Testing

**Test case:** TC-I01, TC-I02 và TC-I03

**Ảnh minh chứng:** [Invalid Input Testing](screenshots/TC-I01-TC-I03-invalid.png)

**Lệnh thực thi:**

`python3 -m pytest tests/test_ticket_service.py::test_create_appointment_invalid_time tests/test_ticket_service.py::test_assign_technician_ticket_not_new tests/test_ticket_crud.py::test_create_ticket_empty_device -v`

**Kết quả:** 3 passed in 0.02s.

### 7.4. Happy Path Testing

**Test case:** TC-H01, TC-H02, TC-H03 và TC-H04

**Ảnh minh chứng:** [Happy Path Testing](screenshots/TC-H01-TC-H04-happy-path.png)

**Lệnh thực thi:**

`python3 -m pytest tests/test_ticket_service.py::test_get_unassigned_tickets tests/test_ticket_service.py::test_assign_technician_success tests/test_ticket_service.py::test_create_appointment_success tests/test_ticket_crud.py::test_create_ticket_success -v`

**Kết quả:** 4 passed in 0.02s.

### 7.5. Reproducibility Testing

**Test case:** TC-R01

**Ảnh minh chứng:** [Reproducibility Testing](screenshots/TC-R01-reproducibility.png)

**Lệnh thực thi:**

`python3 -m src.backend.seed --db /tmp/smartcrm-bt3-repro-test.db`

Lệnh được thực hiện hai lần liên tiếp trên cùng một SQLite database thử nghiệm.

**Kết quả lần thứ nhất:**

- Migration thành công, tạo cấu trúc database.
- Khách hàng mới: 3.
- Kỹ thuật viên mới: 3.
- Phiếu bảo hành mới: 3.
- Seed thành công.

**Kết quả lần thứ hai:**

- Database đã có đủ 5 bảng, không tạo lại.
- Migration thành công.
- Khách hàng mới: 0.
- Kỹ thuật viên mới: 0.
- Phiếu bảo hành mới: 0.
- Seed thành công.

**Kiểm tra SQLite sau lần chạy thứ hai:**

- Khách hàng: 3 bản ghi.
- Kỹ thuật viên: 3 bản ghi.
- Phiếu bảo hành: 3 bản ghi.

**Trạng thái:** PASS.

## 8. Nhận xét và đánh giá

### 8.1. Boundary Testing

Hai trường hợp Boundary Testing đều PASS. Hệ thống cho phép tạo lịch mới ngay khi lịch cũ kết thúc và từ chối lịch có thời gian chồng lấn một phút.

Các bài kiểm thử sử dụng cơ sở dữ liệu SQLite tạm, không làm thay đổi dữ liệu vận hành của SmartCRM.

### 8.2. Security Testing

Hai trường hợp Security Testing đều PASS. API phân công kỹ thuật viên từ chối yêu cầu chưa xác thực bằng HTTP 401 và từ chối người dùng không có quyền quản lý bằng HTTP 403.

Các bài kiểm thử sử dụng FastAPI TestClient.

### 8.3. Invalid Input Testing

Ba trường hợp Invalid Input Testing đều PASS.

- Hệ thống từ chối thời gian đặt lịch không hợp lệ.
- Hệ thống từ chối phân công phiếu bảo hành không còn trạng thái Mới.
- Hệ thống từ chối tạo phiếu bảo hành có tên thiết bị chỉ chứa khoảng trắng.

Các trường hợp này được kiểm thử tại tầng Service.

### 8.4. Happy Path Testing

Bốn trường hợp Happy Path Testing đều PASS.

- Service trả về đúng danh sách phiếu chưa phân công.
- Service xử lý thành công kết quả phân công kỹ thuật viên.
- Service xử lý thành công kết quả tạo lịch hẹn.
- Service xử lý thành công kết quả tạo phiếu bảo hành.

Các bài kiểm thử sử dụng Repository giả lập để xác nhận logic xử lý của Service, chưa kiểm tra việc ghi dữ liệu thực tế vào SQLite.

### 8.5. Reproducibility Testing

TC-R01 đã PASS. Hệ thống thực hiện migration và seed hai lần thành công trên cùng một SQLite database thử nghiệm.

Trong lần chạy thứ hai, chương trình không thêm khách hàng, kỹ thuật viên hoặc phiếu bảo hành mới. Kết quả truy vấn SQLite xác nhận số lượng dữ liệu mẫu vẫn là 3 khách hàng, 3 kỹ thuật viên và 3 phiếu bảo hành.

Điều này cho thấy quá trình khởi tạo database và dữ liệu mẫu có thể chạy lặp lại mà không tạo dữ liệu mẫu trùng trong trường hợp đã kiểm thử.

## 9. Kết luận

Tại thời điểm thực hiện kiểm thử, toàn bộ 29 bài kiểm thử tự động hiện có của SmartCRM L04 đều PASS.

Báo cáo đã lựa chọn, thực thi và ghi nhận đầy đủ 12 test case thuộc 5 nhóm:

- Boundary Testing: 2 PASS.
- Security Testing: 2 PASS.
- Invalid Input Testing: 3 PASS.
- Happy Path Testing: 4 PASS.
- Reproducibility Testing: 1 PASS.

**Tổng kết: 12/12 test case PASS, 0 FAIL.**

Các trường hợp kiểm thử đã có minh chứng bằng kết quả pytest, lệnh chạy migration/seed và truy vấn SQLite.

Các kiểm thử Happy Path và Invalid Input chủ yếu xác nhận logic Service với Repository giả lập; Boundary Testing sử dụng SQLite tạm; Security Testing sử dụng FastAPI TestClient. Vì vậy, kết quả trên phản ánh phạm vi kiểm thử đã thực hiện, không đồng nghĩa với việc toàn bộ hệ thống đã được kiểm thử end-to-end.

Kết quả kiểm thử là cơ sở để tiếp tục hoàn thiện Test Plan, Bug Log và các tài liệu phục vụ nộp BT3.