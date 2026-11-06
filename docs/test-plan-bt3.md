# TEST PLAN – SMARTCRM L04 – BT3

**Dự án:** SmartCRM – Mekong Mobile  
**Luồng:** L04 – Phân công kỹ thuật viên và lịch hẹn  
**Sinh viên:** Nguyễn Ngọc Hiếu  
**MSSV:** 2374802010142  
**Track:** SE – Software Engineering  
**Giai đoạn:** Buổi 13–14 – Kiểm thử hệ thống  
**Ngày:** 06/11/2026

## 1. Mục tiêu và phạm vi kiểm thử

### 1.1. Mục tiêu

Kiểm tra các chức năng đã triển khai trong SmartCRM L04 nhằm xác nhận hệ thống xử lý đúng các trường hợp nghiệp vụ thông thường, dữ liệu không hợp lệ, thời gian trùng lịch và quyền truy cập API.

Đồng thời, kiểm tra khả năng khởi tạo lại cơ sở dữ liệu và dữ liệu mẫu mà không phát sinh bản ghi trùng.

### 1.2. Phạm vi

Thực hiện 12 test case thuộc 5 nhóm:

- **Happy Path (4 TC):** Lấy danh sách phiếu chưa phân công, phân công kỹ thuật viên, tạo lịch hẹn và tạo phiếu bảo hành.
- **Boundary Testing (2 TC):** Kiểm tra hai lịch liền kề và hai lịch chồng lấn một phút.
- **Invalid Input Testing (3 TC):** Kiểm tra giờ hẹn không hợp lệ, phiếu không còn trạng thái Mới và tên thiết bị chỉ chứa khoảng trắng.
- **Security Testing (2 TC):** Kiểm tra API phân công khi thiếu token và khi người dùng không có quyền quản lý.
- **Reproducibility Testing (1 TC):** Chạy migration và seed hai lần trên cùng một database SQLite.

Các bài kiểm thử tự động tập trung vào tầng Service, Repository và API. Chưa xác nhận toàn bộ luồng thao tác giao diện đến database bằng kiểm thử end-to-end.

## 2. Phương pháp kiểm thử

Áp dụng các phương pháp:

- **Positive Testing:** Kiểm tra dữ liệu hợp lệ và kết quả thành công.
- **Negative Testing:** Kiểm tra dữ liệu sai và trạng thái nghiệp vụ không hợp lệ.
- **Boundary Testing:** Kiểm tra ranh giới thời gian đặt lịch.
- **Security Testing:** Kiểm tra xác thực và phân quyền.
- **Reproducibility Testing:** Kiểm tra khả năng chạy lại migration và seed.
- **Regression Testing:** Chạy lại bộ kiểm thử tự động sau khi thay đổi mã nguồn.

Các trường hợp được triển khai bằng pytest, kết hợp Repository giả lập, SQLite tạm và FastAPI TestClient tùy theo mục tiêu kiểm thử.

## 3. Môi trường và dữ liệu kiểm thử

| Thành phần | Công nghệ |
|---|---|
| Hệ điều hành | macOS |
| Ngôn ngữ | Python 3.12.0 |
| Backend | FastAPI |
| Database | SQLite |
| Công cụ kiểm thử | pytest 9.1.1 |
| Kiểm thử API | FastAPI TestClient |
| Kiểm thử nghiệp vụ | Service và Repository |
| Dữ liệu mẫu | Phiếu bảo hành, kỹ thuật viên, phân công và lịch hẹn |
| Lưu minh chứng | `docs/screenshots/` |

**Các lệnh kiểm thử chính:**

Chạy toàn bộ bộ kiểm thử tự động:

`python3 -m pytest -q`

Chạy Boundary Testing:

`python3 -m pytest tests/test_appointment_boundary.py -v`

Kiểm tra khả năng khởi tạo dữ liệu mẫu:

`python3 -m src.backend.seed --db /tmp/smartcrm-bt3-repro-test.db`

Lệnh seed được thực hiện hai lần trên cùng database thử nghiệm, sau đó kiểm tra số lượng bản ghi bằng SQLite.

## 4. Tiêu chí hoàn thành và quản lý kết quả

### 4.1. Tiêu chí đánh giá

- **PASS:** Kết quả thực tế phù hợp với kết quả mong đợi.
- **FAIL:** Kết quả thực tế khác kết quả mong đợi.
- **BLOCKED:** Không thể kiểm thử do thiếu môi trường hoặc dữ liệu.
- **NOT RUN:** Trường hợp chưa được thực thi.

### 4.2. Điều kiện hoàn thành

- Thực thi và ghi nhận đầy đủ 12 test case.
- Ghi rõ dữ liệu đầu vào, kết quả mong đợi và kết quả thực tế.
- Lưu ảnh minh chứng cho các nhóm kiểm thử.
- Chạy lại bộ kiểm thử tự động để phát hiện lỗi hồi quy.
- Ghi nhận các lỗi thực tế và liên kết commit sửa lỗi trong Bug Log nếu có.

### 4.3. Tài liệu kết quả

- **Test Report:** `docs/test-report.md`
- **Ảnh minh chứng:** `docs/screenshots/`
- **Bug Log:** `docs/bug-log.md`

Test Report ghi nhận 12/12 test case PASS. Bộ kiểm thử tự động gần nhất có 29/29 bài kiểm thử PASS. Trường hợp Reproducibility được thực hiện riêng bằng Terminal và SQLite.

Các kết quả này xác nhận phạm vi kiểm thử đã thực hiện, không thay thế việc kiểm thử end-to-end toàn bộ hệ thống.