# SMARTCRM – MEKONG MOBILE

**Luồng L04:** Phân công kỹ thuật viên và lịch hẹn  
**Track:** SE – Software Engineering  
**Sinh viên:** Nguyễn Ngọc Hiếu  
**MSSV:** 2374802010142

## 1. Giới thiệu dự án

SmartCRM L04 hỗ trợ Quản lý trung tâm xem phiếu bảo hành chưa phân công, lựa chọn kỹ thuật viên, thực hiện phân công và quản lý lịch hẹn giao – nhận thiết bị.

Hệ thống kiểm tra trùng lịch trước khi lưu lịch hẹn. Kỹ thuật viên có thể xem công việc được phân công cho mình.

## 2. Môi trường và hướng dẫn chạy

### 2.1. Công nghệ sử dụng

- Ngôn ngữ: Python 3.12
- Backend: FastAPI
- Database: SQLite
- API Documentation: Swagger UI
- Công cụ phát triển: Visual Studio Code
- Quản lý phiên bản: Git và GitHub

### 2.2. Cài đặt thư viện

Tại thư mục gốc của dự án, chạy:

```bash
python3 -m pip install -r requirements.txt
```

Đảm bảo môi trường đã cài đặt FastAPI và Uvicorn.

### 2.3. Khởi động Backend

```bash
python3 -m uvicorn src.backend.main:app --reload
```

Địa chỉ Backend:

`http://127.0.0.1:8000`

Swagger UI:

`http://127.0.0.1:8000/docs`

### 2.4. Cơ sở dữ liệu

File thiết kế SQL:

`docs/database/schema-l04.sql`

Tạo database Sprint 1 nếu chưa tồn tại:

```bash
sqlite3 smartcrm-sprint1.db < docs/database/schema-l04.sql
```

Backend sử dụng file `smartcrm-sprint1.db` tại thư mục gốc dự án.

Lưu ý: Không chạy lại lệnh tạo bảng trên một database đã có dữ liệu nếu chưa kiểm tra hoặc sao lưu.

## 3. Phạm vi chức năng

Các chức năng nghiệp vụ L04:

- UC01 – Xem phiếu chưa phân công
- UC02 – Xem thông tin kỹ thuật viên
- UC03 – Phân công kỹ thuật viên
- UC04 – Đặt lịch hẹn
- UC05 – Kiểm tra trùng lịch
- UC06 – Xem công việc được phân công
- UC07 – Hủy phân công kỹ thuật viên
- UC08 – Cập nhật lịch hẹn

Các chức năng trên là phạm vi thiết kế, không đồng nghĩa tất cả đã được lập trình.

## 4. Thiết kế hệ thống

- SRS: `srs.md`
- Use Case: `docs/use-cases/`
- Sơ đồ kiến trúc: `docs/architecture/`
- ERD và SQL DDL: `docs/database/`
- Wireframe: `docs/wireframes/`
- Nhật ký thay đổi thiết kế: `docs/thay-doi-thiet-ke.md`

## 5. API Sprint 1

| Phương thức | Endpoint | Chức năng |
|---|---|---|
| GET | `/` | Kiểm tra trang chủ |
| GET | `/db-test` | Kiểm tra kết nối SQLite |
| GET | `/api/technicians` | Xem danh sách kỹ thuật viên |
| POST | `/api/technicians` | Thêm kỹ thuật viên |
| PUT | `/api/technicians/{technician_id}` | Cập nhật kỹ thuật viên |
| DELETE | `/api/technicians/{technician_id}` | Ngừng hoạt động kỹ thuật viên (xóa mềm) |

## 6. Tiến độ Sprint 1 – Buổi 8

### Đã thực hiện

- Rà soát phản hồi BT1.
- Tạo nhật ký thay đổi thiết kế.
- Tạo cơ sở dữ liệu Sprint 1 theo SQL DDL.
- Tạo 5 bảng theo ERD L04.
- Thêm dữ liệu mẫu kỹ thuật viên.
- Khởi động Backend FastAPI thành công.
- Kiểm thử API GET danh sách kỹ thuật viên.
- Kiểm thử POST thêm kỹ thuật viên: HTTP 201.
- Kiểm thử PUT cập nhật kỹ thuật viên: HTTP 200.
- Kiểm tra xóa mềm qua dữ liệu GET.

### Cần tiếp tục

- Lưu ảnh minh chứng kiểm thử API vào thư mục `docs/`.
- Hoàn thiện tổ chức Backend theo các lớp kiến trúc.
- Bổ sung kiểm thử tự động và xử lý ngoại lệ.
- Xây dựng chức năng phân công kỹ thuật viên và đặt lịch hẹn.
- Kiểm tra tính nhất quán giữa mã nguồn và tài liệu thiết kế.

## 7. GitHub

Repository:

https://github.com/Hieu2374802010142/smartcrm-2374802010142-technician-assignment

Nhánh phát triển hiện tại: `main`.