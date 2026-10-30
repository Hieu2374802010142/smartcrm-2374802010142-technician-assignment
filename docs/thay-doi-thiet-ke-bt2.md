# BÁO CÁO THAY ĐỔI THIẾT KẾ – SMARTCRM L04

**Sinh viên:** Nguyễn Ngọc Hiếu
**MSSV:** 2374802010142
**Dự án:** SmartCRM – L04: Phân công kỹ thuật viên và lịch hẹn
**Phiên bản:** v0.2
**Ngày cập nhật:** 30/10/2026

## 1. Mục đích

Tài liệu ghi nhận những thay đổi trong thiết kế và triển khai hệ thống SmartCRM L04 từ Bài tập 1 (BT1) sang Bài tập 2 (BT2).

Mục tiêu là cải thiện chất lượng mã nguồn, tăng khả năng kiểm thử, hỗ trợ cài đặt trên máy mới và hoàn thiện các chức năng quản lý phiếu bảo hành, phân công kỹ thuật viên và đặt lịch hẹn.

## 2. Các vấn đề được ghi nhận từ BT1

Trong BT1, hệ thống đã có các thành phần thiết kế cơ bản gồm SRS, Use Case, sơ đồ kiến trúc, ERD và Wireframe.

Kết quả đánh giá BT1 là **5,5/10**. Một số vấn đề cần cải thiện gồm:

- Sơ đồ còn thiếu chú thích ký hiệu.
- SRS chưa có bảng thuật ngữ và phần WON'T.
- Số lượng User Story chưa phù hợp giới hạn yêu cầu.
- Phần giải thích kiến trúc chưa làm rõ lựa chọn kỹ thuật theo NFR và các đánh đổi.
- Tài liệu nộp thiếu đặc tả chi tiết UC03 và mã SQL DDL.

Ngoài các nhận xét về tài liệu, trong BT2 hệ thống tiếp tục được hoàn thiện về mã nguồn, kiểm thử và khả năng triển khai.

## 3. Những thay đổi chính trong BT2

### 3.1. Cải thiện kiến trúc ba lớp

Backend được tổ chức theo ba lớp:

**Routes → Services → Repositories → Database**

- **Routes:** Tiếp nhận HTTP request, xác thực quyền truy cập và chuyển lỗi nghiệp vụ thành HTTP response.
- **Services:** Xử lý các quy tắc nghiệp vụ như kiểm tra dữ liệu, điều kiện phân công và lịch hẹn.
- **Repositories:** Thực hiện truy vấn và cập nhật dữ liệu SQLite.

Đối với chức năng phiếu bảo hành, Service sử dụng `TicketError` để biểu diễn lỗi nghiệp vụ, thay vì phụ thuộc trực tiếp vào `HTTPException` của FastAPI.

**Lợi ích:** Phân tách trách nhiệm giữa các lớp, giảm phụ thuộc vào framework và thuận tiện hơn khi viết Unit Test.

### 3.2. Bổ sung CRUD phiếu bảo hành

Hệ thống được bổ sung các API quản lý phiếu bảo hành:

| Phương thức | API | Chức năng |
|---|---|---|
| GET | `/api/tickets` | Lấy danh sách phiếu |
| POST | `/api/tickets` | Tạo phiếu |
| GET | `/api/tickets/{ticket_id}` | Xem chi tiết phiếu |
| PUT | `/api/tickets/{ticket_id}` | Cập nhật phiếu |
| DELETE | `/api/tickets/{ticket_id}` | Xóa phiếu |

Các thao tác được kiểm tra điều kiện nghiệp vụ, bao gồm tính hợp lệ của dữ liệu và trạng thái phiếu.

Trong quá trình thử nghiệm API, hệ thống đã tạo, đọc, cập nhật và xóa thành công một phiếu kiểm thử.

### 3.3. Hoàn thiện quản lý kỹ thuật viên

Hệ thống hỗ trợ:

- Xem danh sách kỹ thuật viên.
- Thêm kỹ thuật viên.
- Cập nhật thông tin kỹ thuật viên.
- Ngừng hoạt động kỹ thuật viên.

Các chức năng được tổ chức theo Routes, Services và Repositories.

### 3.4. Bổ sung Migration

File triển khai: `src/backend/migrate.py`

Migration hỗ trợ khởi tạo cấu trúc database SQLite gồm năm bảng:

1. `khach_hang`
2. `phieu_bao_hanh`
3. `ky_thuat_vien`
4. `phan_cong_ky_thuat_vien`
5. `lich_hen`

Migration có khả năng nhận biết database đã có đầy đủ bảng để tránh tạo lại cấu trúc không cần thiết.

Lệnh thực hiện:

```bash
python3 -m src.backend.migrate
```

### 3.5. Cải tiến Seed dữ liệu mẫu

File triển khai: `src/backend/seed.py`

Seed được thiết kế để có thể chạy nhiều lần mà không tạo dữ liệu mẫu trùng lặp.

Kết quả kiểm tra trên database mới:

| Dữ liệu | Lần chạy 1 | Lần chạy 2 |
|---|---:|---:|
| Khách hàng mới | 3 | 0 |
| Kỹ thuật viên mới | 3 | 0 |
| Phiếu bảo hành mới | 3 | 0 |

Lệnh thực hiện:

```bash
python3 -m src.backend.seed
```

**Lợi ích:** Thuận tiện khi triển khai hệ thống và chuẩn bị dữ liệu trình diễn.

### 3.6. Bổ sung thiết lập tài khoản quản lý

File triển khai: `src/backend/setup_admin.py`

Hệ thống hỗ trợ tạo cấu hình tài khoản quản lý bằng lệnh:

```bash
python3 -m src.backend.setup_admin
```

Thông tin cấu hình được lưu trong file `.env`, không đưa lên GitHub.

Việc này giúp triển khai trên máy mới mà không cần công khai mật khẩu quản lý trong mã nguồn.

### 3.7. Bổ sung kiểm thử tự động

BT2 bổ sung và cập nhật các bài kiểm thử cho:

- Xác thực và phân quyền.
- CRUD kỹ thuật viên.
- CRUD phiếu bảo hành.
- Phân công kỹ thuật viên.
- Đặt lịch hẹn và xử lý dữ liệu không hợp lệ.

Lệnh chạy:

```bash
python3 -m pytest -q
```

**Kết quả:** 27/27 bài kiểm thử PASS.

### 3.8. Kiểm tra Clean Clone

Dự án đã được clone từ GitHub vào thư mục thử nghiệm độc lập `smartcrm-bt2-clean-test`.

Các bước kiểm tra đã thực hiện thành công:

1. Clone đúng commit `f54f007`.
2. Khởi tạo database bằng Migration.
3. Seed dữ liệu mẫu hai lần mà không phát sinh bản ghi trùng.
4. Chạy 27 bài kiểm thử.
5. Thiết lập tài khoản quản lý.
6. Khởi động FastAPI trên cổng 8001.
7. Đăng nhập giao diện SmartCRM.
8. Phân công kỹ thuật viên thành công, mã phân công 1.
9. Đặt lịch nhận thiết bị thành công, mã lịch hẹn 1.

Kết quả này chứng minh luồng chức năng chính hoạt động trên bản clone mới.

## 4. Bảng so sánh BT1 và BT2

| Tiêu chí | BT1 | BT2 |
|---|---|---|
| Kiến trúc | Thiết kế phân lớp ban đầu | Hoàn thiện phân tách Routes, Services, Repositories |
| Phiếu bảo hành | Tập trung vào luồng phân công | Bổ sung CRUD |
| Kỹ thuật viên | Có chức năng quản lý cơ bản | Hoàn thiện Service và kiểm thử |
| Database | Có ERD và SQL DDL | Bổ sung Migration |
| Dữ liệu mẫu | Seed ban đầu | Seed chạy lặp không trùng |
| Xác thực | Có đăng nhập quản lý | Bổ sung công cụ thiết lập tài khoản |
| Kiểm thử | Có kế hoạch và báo cáo Sprint 1 | 27 bài kiểm thử tự động PASS |
| Triển khai | Chạy trên môi trường phát triển | Đã kiểm tra Clean Clone |
| Quản lý phiên bản | Commit trên GitHub | Commit `f54f007`, tag `v0.2` |

## 5. Đánh đổi và giới hạn

- **SQLite:** Dễ cài đặt và phù hợp quy mô bài tập, nhưng chưa hướng đến hệ thống có số lượng lớn người dùng đồng thời.
- **Giao diện HTML/CSS/JavaScript:** Dễ triển khai và trình diễn, nhưng chưa sử dụng framework frontend chuyên biệt.
- **Kiểm thử tự động:** Đã kiểm tra nhiều trường hợp nghiệp vụ, nhưng chưa thay thế hoàn toàn kiểm thử tích hợp, bảo mật và hiệu năng.
- **Clean Clone:** Đã xác nhận khả năng triển khai và luồng chính; chưa chứng minh hệ thống đáp ứng toàn bộ ngưỡng NFR trong môi trường thực tế.

## 6. Kết luận

Trong BT2, SmartCRM L04 được cải tiến từ bản thiết kế và triển khai ban đầu thành hệ thống có cấu trúc mã nguồn rõ ràng hơn, hỗ trợ CRUD, Migration, Seed, xác thực quản lý và kiểm thử tự động.

Kết quả 27/27 bài kiểm thử PASS cùng với việc chạy thành công trên bản Clean Clone là bằng chứng cho tiến độ hoàn thiện hệ thống.

Những cải tiến này tạo nền tảng cho việc tiếp tục bổ sung chức năng và nâng cao chất lượng phần mềm trong các giai đoạn sau.
