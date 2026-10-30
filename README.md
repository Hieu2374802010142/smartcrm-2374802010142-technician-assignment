# SMARTCRM – MEKONG MOBILE

**Luồng L04:** Phân công kỹ thuật viên và lịch hẹn
**Track:** Software Engineering (SE)
**Sinh viên:** Nguyễn Ngọc Hiếu
**MSSV:** 2374802010142
**Bài tập:** BT2 – Triển khai phần mềm

## 1. Giới thiệu dự án

SmartCRM L04 là ứng dụng web hỗ trợ trung tâm bảo hành Mekong Mobile quản lý phiếu bảo hành, kỹ thuật viên và lịch hẹn.

Các chức năng đã triển khai:

- Đăng nhập bằng tài khoản quản lý.
- Xem danh sách phiếu bảo hành chưa phân công.
- Thêm, xem, cập nhật và xóa phiếu bảo hành.
- Quản lý thông tin kỹ thuật viên.
- Phân công kỹ thuật viên cho phiếu bảo hành.
- Đặt lịch hẹn nhận hoặc trả thiết bị.
- Kiểm tra trùng lịch hẹn của kỹ thuật viên.
- Kiểm tra quyền truy cập đối với các API quản lý.

## 2. Công nghệ sử dụng

| Thành phần | Công nghệ |
|---|---|
| Ngôn ngữ | Python 3.12 |
| Backend | FastAPI |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite |
| API Documentation | Swagger UI |
| Automated Testing | pytest |
| Quản lý mã nguồn | Git, GitHub |

Hệ thống sử dụng kiến trúc phân lớp:

**Frontend → Routes → Services → Repositories → SQLite**

- **Routes:** Tiếp nhận yêu cầu HTTP, kiểm tra quyền và xử lý HTTP response.
- **Services:** Kiểm tra dữ liệu, xử lý nghiệp vụ và phát sinh lỗi nghiệp vụ.
- **Repositories:** Truy vấn và cập nhật dữ liệu SQLite.
- **Frontend:** Giao diện tương tác với backend thông qua REST API.

## 3. Yêu cầu môi trường

Máy tính cần cài đặt:

- Python 3.12
- Git
- Trình duyệt web
- Visual Studio Code (khuyến nghị)

## 4. Hướng dẫn cài đặt từ GitHub

### Bước 1. Clone dự án

Mở Terminal và chạy:

```bash
git clone https://github.com/Hieu2374802010142/smartcrm-2374802010142-technician-assignment.git

cd smartcrm-2374802010142-technician-assignment
```

### Bước 2. Tạo môi trường Python

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Cài đặt thư viện:

```bash
python3 -m pip install -r requirements.txt
```

### Bước 3. Khởi tạo database

Chạy Migration:

```bash
python3 -m src.backend.migrate
```

Chạy Seed:

```bash
python3 -m src.backend.seed
```

Chương trình sử dụng database `smartcrm-sprint1.db` tại thư mục gốc dự án.

Database gồm 5 bảng:

1. `khach_hang`
2. `phieu_bao_hanh`
3. `ky_thuat_vien`
4. `phan_cong_ky_thuat_vien`
5. `lich_hen`

Seed tạo dữ liệu mẫu:

- 3 khách hàng.
- 3 kỹ thuật viên.
- 3 phiếu bảo hành ở trạng thái `Mới`.

Migration và Seed có thể chạy lại mà không tạo trùng các dữ liệu mẫu trên database chưa bị chỉnh sửa.

### Bước 4. Thiết lập tài khoản quản lý

Chạy:

```bash
python3 -m src.backend.setup_admin
```

Nhập tên đăng nhập, mật khẩu và xác nhận mật khẩu theo hướng dẫn.

Chương trình tạo file `.env` chứa tên đăng nhập, salt và mã băm mật khẩu.

Nạp cấu hình:

```bash
set -a
source .env
set +a
```

**Lưu ý:** Không đưa `.env`, mật khẩu hoặc database cá nhân lên GitHub.

### Bước 5. Khởi động ứng dụng

```bash
python3 -m uvicorn src.backend.main:app --reload
```

Các đường dẫn:

- Giao diện ứng dụng: http://127.0.0.1:8000/app
- Swagger UI: http://127.0.0.1:8000/docs
- Kiểm tra backend: http://127.0.0.1:8000/
- Kiểm tra SQLite: http://127.0.0.1:8000/db-test

Để dừng backend, nhấn `Control + C` trong Terminal.

## 5. Hướng dẫn sử dụng

### 5.1. Đăng nhập

Truy cập:

http://127.0.0.1:8000/app

Đăng nhập bằng tài khoản quản lý đã tạo ở Bước 4.

Sau khi đăng nhập thành công, người quản lý có thể sử dụng các chức năng nghiệp vụ của hệ thống.

### 5.2. Xem phiếu chưa phân công

Ứng dụng tải danh sách các phiếu bảo hành đang ở trạng thái `Mới` và chưa được phân công kỹ thuật viên.

### 5.3. Phân công kỹ thuật viên

1. Chọn phiếu bảo hành chưa phân công.
2. Chọn kỹ thuật viên đang hoạt động.
3. Nhấn nút phân công.
4. Hệ thống kiểm tra điều kiện nghiệp vụ và lưu kết quả.

### 5.4. Đặt lịch hẹn

1. Chọn phân công đang hoạt động.
2. Chọn ngày hẹn.
3. Nhập giờ bắt đầu và kết thúc.
4. Chọn loại lịch hẹn.
5. Lưu lịch hẹn.

Hệ thống kiểm tra thời gian hợp lệ và phát hiện lịch trùng trước khi lưu.

## 6. Các API chính

| Phương thức | Endpoint | Chức năng |
|---|---|---|
| POST | `/api/auth/login` | Đăng nhập |
| GET | `/api/technicians` | Xem kỹ thuật viên |
| POST | `/api/technicians` | Thêm kỹ thuật viên |
| PUT | `/api/technicians/{technician_id}` | Cập nhật kỹ thuật viên |
| DELETE | `/api/technicians/{technician_id}` | Ngừng hoạt động kỹ thuật viên |
| GET | `/api/tickets` | Xem danh sách phiếu |
| POST | `/api/tickets` | Tạo phiếu |
| GET | `/api/tickets/{ticket_id}` | Xem chi tiết phiếu |
| PUT | `/api/tickets/{ticket_id}` | Cập nhật phiếu |
| DELETE | `/api/tickets/{ticket_id}` | Xóa phiếu |
| GET | `/api/tickets/unassigned` | Xem phiếu chưa phân công |
| POST | `/api/tickets/{ticket_id}/assign` | Phân công kỹ thuật viên |
| GET | `/api/tickets/assignments` | Xem danh sách phân công |
| POST | `/api/tickets/appointments` | Tạo lịch hẹn |

Các API thay đổi dữ liệu được bảo vệ bằng cơ chế xác thực và phân quyền quản lý theo cấu hình hiện tại.

## 7. Kiểm thử tự động

Chạy toàn bộ bài kiểm thử:

```bash
python3 -m pytest -v
```

Các nhóm kiểm thử:

| Nhóm | Số bài kiểm thử |
|---|---:|
| Authentication | 4 |
| Technician Service | 8 |
| Ticket CRUD | 9 |
| Ticket Service | 6 |
| **Tổng cộng** | **27** |

Kết quả kiểm thử gần nhất trong quá trình phát triển:

**27 passed in 0.24s**

Các bài kiểm thử sử dụng mock và dữ liệu thử nghiệm để xác minh nghiệp vụ mà không cần thao tác trực tiếp trên database sản xuất.

## 8. Migration và Seed

Migration sử dụng SQL DDL trong:

`docs/database/schema-l04.sql`

File thực thi:

`src/backend/migrate.py`

File tạo dữ liệu mẫu:

`src/backend/seed.py`

Có thể thử nghiệm trên database riêng:

```bash
python3 -m src.backend.migrate --db /tmp/smartcrm-demo.db
python3 -m src.backend.seed --db /tmp/smartcrm-demo.db
```

Chạy Seed lần thứ hai để kiểm tra tính lặp lại.

## 9. Tổ chức mã nguồn

```text
smartcrm-2374802010142-technician-assignment/
├── docs/
│   ├── architecture/
│   ├── database/
│   ├── use-cases/
│   └── wireframes/
├── src/
│   ├── backend/
│   │   ├── auth/
│   │   ├── repositories/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── main.py
│   │   ├── migrate.py
│   │   ├── seed.py
│   │   └── setup_admin.py
│   └── frontend/
│       └── index.html
├── tests/
│   ├── test_auth.py
│   ├── test_technician_service.py
│   ├── test_ticket_crud.py
│   └── test_ticket_service.py
├── .env.example
├── .gitignore
├── requirements.txt
├── README.md
└── srs.md
```

## 10. Tài liệu thiết kế

- Đặc tả yêu cầu: `srs.md`
- Use Case: `docs/use-cases/`
- Kiến trúc hệ thống: `docs/architecture/`
- ERD và SQL DDL: `docs/database/`
- Wireframe: `docs/wireframes/`
- Nhật ký thay đổi thiết kế: `docs/thay-doi-thiet-ke.md`

## 11. Phạm vi và giới hạn

Dự án tập trung triển khai luồng L04 – Phân công kỹ thuật viên và lịch hẹn.

Các chức năng như quản lý kho, thanh toán, bảo hành toàn hệ thống và quản trị nhiều chi nhánh không thuộc phạm vi triển khai BT2.

Phiên đăng nhập hiện được lưu trong bộ nhớ backend, có thời hạn 60 phút và sẽ mất khi khởi động lại server.

Ứng dụng sử dụng SQLite để phục vụ học tập, kiểm thử và demo.

## 12. GitHub

Repository:

https://github.com/Hieu2374802010142/smartcrm-2374802010142-technician-assignment

Nhánh chính: `main`

Mã nguồn, tài liệu thiết kế, kiểm thử tự động và hướng dẫn chạy được quản lý bằng Git và GitHub.

**Sinh viên thực hiện:** Nguyễn Ngọc Hiếu
**MSSV:** 2374802010142
