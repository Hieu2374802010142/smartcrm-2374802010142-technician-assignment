# SMARTCRM – MEKONG MOBILE

**Luồng L04:** Phân công kỹ thuật viên và lịch hẹn  
**Track:** SE – Software Engineering  
**Sinh viên:** Nguyễn Ngọc Hiếu  
**MSSV:** 2374802010142

## 1. Giới thiệu dự án

SmartCRM L04 là hệ thống hỗ trợ quản lý quy trình phân công kỹ thuật viên và lịch hẹn trong trung tâm bảo hành thiết bị.

Hệ thống được thiết kế để hỗ trợ Quản lý trung tâm xem phiếu bảo hành chưa phân công, lựa chọn kỹ thuật viên phù hợp, thực hiện phân công và quản lý lịch hẹn giao – nhận thiết bị.

Trong **Sprint 1 – Buổi 8**, dự án tập trung xây dựng cơ sở dữ liệu, tổ chức kiến trúc Backend và triển khai CRUD cho thực thể Kỹ thuật viên.

## 2. Môi trường và hướng dẫn chạy

### 2.1. Công nghệ sử dụng

- Ngôn ngữ: Python 3.12
- Backend: FastAPI
- Database: SQLite
- API Documentation: Swagger UI
- Công cụ phát triển: Visual Studio Code
- Quản lý phiên bản: Git và GitHub

### 2.2. Cài đặt thư viện

Tại thư mục gốc dự án, chạy:

```bash
python3 -m pip install -r requirements.txt
```

### 2.3. Khởi tạo cơ sở dữ liệu

File SQL DDL:

`docs/database/schema-l04.sql`

Chạy lệnh sau để tạo database và thêm dữ liệu mẫu:

```bash
python3 -m src.backend.seed
```

Chương trình sẽ:

- Tạo database `smartcrm-sprint1.db` nếu chưa tồn tại.
- Khởi tạo 5 bảng theo ERD L04.
- Thêm 3 kỹ thuật viên mẫu nếu bảng kỹ thuật viên chưa có dữ liệu.
- Không thêm dữ liệu mẫu trùng khi chạy lại.
- Không ghi đè dữ liệu kỹ thuật viên hiện có.

Database SQLite được lưu tại thư mục gốc dự án và không đưa lên GitHub.

### 2.4. Khởi động Backend

```bash
python3 -m uvicorn src.backend.main:app --reload
```

Địa chỉ Backend:

http://127.0.0.1:8000

Swagger UI:

http://127.0.0.1:8000/docs

Truy cập Swagger UI để kiểm thử các API.

## 3. Phạm vi chức năng L04

Các Use Case thuộc phạm vi thiết kế:

- UC01 – Xem phiếu chưa phân công
- UC02 – Xem thông tin kỹ thuật viên
- UC03 – Phân công kỹ thuật viên
- UC04 – Đặt lịch hẹn
- UC05 – Kiểm tra trùng lịch
- UC06 – Xem công việc được phân công
- UC07 – Hủy phân công kỹ thuật viên
- UC08 – Cập nhật lịch hẹn

Các Use Case trên thuộc phạm vi thiết kế tổng thể. Trong Sprint 1, hệ thống mới triển khai CRUD kỹ thuật viên để làm nền tảng cho các chức năng nghiệp vụ tiếp theo.

## 4. Thiết kế và kiến trúc hệ thống

### 4.1. Tài liệu thiết kế

- SRS: `srs.md`
- Use Case: `docs/use-cases/`
- Sơ đồ kiến trúc: `docs/architecture/`
- ERD và SQL DDL: `docs/database/`
- Wireframe: `docs/wireframes/`
- Nhật ký thay đổi thiết kế: `docs/thay-doi-thiet-ke.md`

### 4.2. Kiến trúc Backend

Backend được tổ chức theo ba tầng:

**Routes → Service → Repository → SQLite**

- **Routes:** Tiếp nhận HTTP request và trả về response.
- **Service:** Xử lý logic nghiệp vụ và các trường hợp lỗi.
- **Repository:** Thực hiện truy vấn SQLite.
- **SQLite:** Lưu trữ dữ liệu của hệ thống.

Các file chính:

```text
src/backend/
├── main.py
├── seed.py
├── routes/
│   └── technician_routes.py
├── services/
│   └── technician_service.py
└── repositories/
    └── technician_repository.py
```

### 4.3. Cơ sở dữ liệu

Database gồm 5 bảng:

1. `khach_hang`
2. `phieu_bao_hanh`
3. `ky_thuat_vien`
4. `phan_cong_ky_thuat_vien`
5. `lich_hen`

Các bảng được xây dựng dựa trên ERD của luồng L04.

## 5. API Sprint 1

| Phương thức | Endpoint | Chức năng |
|---|---|---|
| GET | `/` | Kiểm tra trang chủ |
| GET | `/db-test` | Kiểm tra kết nối SQLite |
| GET | `/api/technicians` | Xem danh sách kỹ thuật viên |
| POST | `/api/technicians` | Thêm kỹ thuật viên |
| PUT | `/api/technicians/{technician_id}` | Cập nhật kỹ thuật viên |
| DELETE | `/api/technicians/{technician_id}` | Ngừng hoạt động kỹ thuật viên (xóa mềm) |

### Kiểm thử API

Đã kiểm thử bằng Swagger UI:

- GET danh sách kỹ thuật viên: HTTP 200.
- POST thêm kỹ thuật viên: HTTP 201.
- PUT cập nhật kỹ thuật viên: HTTP 200.
- DELETE ngừng hoạt động kỹ thuật viên: HTTP 200.

Ảnh minh chứng được lưu tại:

`docs/api-tests/`

Gồm các file:

- `get-technicians.png`
- `post-technician.png`
- `put-technician.png`
- `delete-technician.png`

## 6. Tiến độ Sprint 1 – Buổi 8

### 6.1. Đã hoàn thành

- Rà soát phản hồi Bài tập 1.
- Tạo nhật ký thay đổi thiết kế.
- Xây dựng SQL DDL gồm 5 bảng.
- Tổ chức Backend theo kiến trúc Routes → Service → Repository.
- Xây dựng CRUD kỹ thuật viên bằng FastAPI và SQLite.
- Kiểm thử các API GET, POST, PUT, DELETE.
- Lưu 4 ảnh minh chứng kiểm thử Swagger.
- Xây dựng chương trình tạo dữ liệu mẫu `seed.py`.
- Kiểm tra tạo thành công 5 bảng trên database mới.
- Kiểm tra thêm thành công 3 kỹ thuật viên mẫu.
- Sử dụng Conventional Commits.
- Commit và push mã nguồn lên GitHub nhánh `main`.

### 6.2. Công việc cần tiếp tục

- Bổ sung kiểm thử tự động và các trường hợp ngoại lệ.
- Xây dựng chức năng phân công kỹ thuật viên.
- Xây dựng chức năng đặt lịch hẹn.
- Triển khai kiểm tra trùng lịch trước khi lưu.
- Tiếp tục đối chiếu mã nguồn với tài liệu thiết kế.

## 7. GitHub

Repository:

https://github.com/Hieu2374802010142/smartcrm-2374802010142-technician-assignment

Nhánh phát triển: `main`.

Dự án sử dụng GitHub để quản lý mã nguồn, tài liệu thiết kế và minh chứng kiểm thử trong quá trình thực hiện Sprint 1.