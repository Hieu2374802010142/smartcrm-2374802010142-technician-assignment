# SMARTCRM – MEKONG MOBILE

**Luồng L04:** Phân công kỹ thuật viên và lịch hẹn
**Track:** Software Engineering (SE)
**Sinh viên:** Nguyễn Ngọc Hiếu
**MSSV:** 2374802010142
**Bài tập:** BT3 – Kiểm thử, đóng gói và triển khai phần mềm

## 1. Giới thiệu dự án

SmartCRM L04 là ứng dụng web hỗ trợ trung tâm bảo hành Mekong Mobile quản lý phiếu bảo hành, kỹ thuật viên và lịch hẹn.

Các chức năng chính:

- Đăng nhập bằng tài khoản quản lý.
- Xem danh sách phiếu bảo hành chưa phân công.
- Thêm, xem, cập nhật và xóa phiếu bảo hành.
- Quản lý thông tin kỹ thuật viên.
- Phân công kỹ thuật viên cho phiếu bảo hành.
- Đặt lịch hẹn nhận hoặc trả thiết bị.
- Kiểm tra trùng lịch hẹn của kỹ thuật viên.
- Kiểm tra xác thực và phân quyền truy cập API.

## 2. Công nghệ sử dụng

| Thành phần | Công nghệ |
|---|---|
| Ngôn ngữ | Python 3.12 |
| Backend | FastAPI |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite |
| Container | Docker, Docker Compose |
| API Documentation | Swagger UI |
| Automated Testing | pytest |
| Quản lý mã nguồn | Git, GitHub |

Kiến trúc hệ thống:

**Frontend → Routes → Services → Repositories → SQLite**

- **Routes:** Tiếp nhận HTTP request, kiểm tra quyền và trả HTTP response.
- **Services:** Xử lý nghiệp vụ và kiểm tra dữ liệu.
- **Repositories:** Truy vấn và cập nhật SQLite.
- **Frontend:** Tương tác với backend thông qua REST API.

## 3. Yêu cầu môi trường

### Triển khai bằng Docker (khuyến nghị)

- Docker Desktop có hỗ trợ Docker Compose.
- Git.
- Trình duyệt web.

### Chạy trực tiếp bằng Python

- Python 3.12.
- Git.
- Trình duyệt web.
- Visual Studio Code (khuyến nghị).

## 4. Docker Quickstart – Hướng dẫn chạy BT3

### Bước 1. Clone repository

```bash
git clone https://github.com/Hieu2374802010142/smartcrm-2374802010142-technician-assignment.git
cd smartcrm-2374802010142-technician-assignment
```

Để kiểm tra đúng phiên bản được đánh dấu cho bài nộp:

```bash
git checkout v1.0
```

**Lưu ý:** Tag `v1.0` hiện có trên GitHub nhưng chưa được xác nhận chứa toàn bộ thay đổi BT3 mới nhất. Cần hoàn tất kiểm tra phiên bản trước khi nộp.

### Bước 2. Chuẩn bị cấu hình môi trường

```bash
cp .env.example .env
```

File `.env.example` cung cấp cấu hình tài khoản demo phục vụ kiểm thử học phần.

Không sử dụng tài khoản demo này trong môi trường production. Không commit file `.env` lên GitHub.

### Bước 3. Build và khởi động ứng dụng

```bash
docker compose up -d --build
```

Docker sẽ thực hiện:

1. Build image sử dụng Python 3.12.
2. Cài đặt các thư viện trong `requirements.txt`.
3. Sao chép mã nguồn backend và database schema.
4. Chạy module seed để chuẩn bị database.
5. Khởi động FastAPI trên cổng `8000`.

### Bước 4. Kiểm tra trạng thái

```bash
docker compose ps
```

Container hoạt động bình thường khi có trạng thái `healthy`.

Các địa chỉ truy cập:

- **Ứng dụng:** http://127.0.0.1:8000/app
- **Swagger UI:** http://127.0.0.1:8000/docs
- **Health API:** http://127.0.0.1:8000/health
- **Database check:** http://127.0.0.1:8000/db-test

### Bước 5. Dừng ứng dụng

```bash
docker compose down
```

Dữ liệu SQLite được lưu trong Docker named volume `smartcrm_data`, giúp duy trì dữ liệu giữa các lần khởi động thông thường.

**Lưu ý:** Quy trình chạy từ bản clone sạch của tag `v1.0` cần được xác minh lại trước khi nộp chính thức.

## 5. Hướng dẫn chạy trực tiếp bằng Python

### Bước 1. Tạo môi trường

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

### Bước 2. Khởi tạo database

```bash
python3 -m src.backend.migrate
python3 -m src.backend.seed
```

### Bước 3. Thiết lập tài khoản quản lý

```bash
python3 -m src.backend.setup_admin
```

Sau khi thiết lập `.env`, nạp biến môi trường:

```bash
set -a
source .env
set +a
```

### Bước 4. Khởi động FastAPI

```bash
python3 -m uvicorn src.backend.main:app --reload --port 8000
```

Truy cập http://127.0.0.1:8000/app.

**Lưu ý:** Không chạy Uvicorn và Docker Compose đồng thời trên cùng cổng `8000`.

## 6. Hướng dẫn sử dụng

### 6.1. Đăng nhập

Mở giao diện `/app` và đăng nhập bằng tài khoản quản lý đã cấu hình.

### 6.2. Xem phiếu chưa phân công

Hệ thống hiển thị các phiếu bảo hành đang ở trạng thái `Mới` và chưa có phân công hoạt động.

### 6.3. Phân công kỹ thuật viên

1. Chọn phiếu bảo hành chưa phân công.
2. Chọn kỹ thuật viên đang hoạt động.
3. Nhấn nút phân công.
4. Hệ thống kiểm tra điều kiện nghiệp vụ và lưu kết quả.

### 6.4. Đặt lịch hẹn

1. Chọn phân công đang hoạt động.
2. Chọn ngày hẹn.
3. Nhập giờ bắt đầu và giờ kết thúc.
4. Chọn loại lịch hẹn.
5. Lưu lịch hẹn.

Hệ thống kiểm tra thời gian hợp lệ và từ chối lịch hẹn trùng với lịch đã có của cùng kỹ thuật viên.

## 7. Các API chính

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
| GET | `/health` | Kiểm tra trạng thái backend và database |

Các API quản lý được bảo vệ bằng cơ chế xác thực và kiểm tra quyền theo cấu hình hệ thống.

Tài liệu API chi tiết: `docs/api-documentation-bt3.md`.

## 8. Kiểm thử Bài tập 3

Chạy toàn bộ bài kiểm thử tự động:

```bash
python3 -m pytest -q
```

**Kết quả kiểm thử gần nhất trên máy phát triển:**

- Tổng số bài kiểm thử: **32**
- PASS: **32**
- FAIL: **0**
- Thời gian thực thi: **0.43 giây**
- Tỷ lệ PASS: **100%**

Bộ kiểm thử bao gồm các chức năng xác thực, quản lý kỹ thuật viên, phiếu bảo hành và xử lý nghiệp vụ.

Báo cáo BT3 cũng ghi nhận 12 test case được lựa chọn để trình bày minh chứng theo năm nhóm:

- Happy Path
- Boundary
- Invalid Data
- Security
- Reproducibility

Tài liệu:

- Test Plan: `docs/test-plan-bt3.md`
- Test Report: `docs/test-report.md`
- Docker Test Report: `docs/test-report-docker.md`
- Test Evidence: `docs/screenshots/`

## 9. Bug Log và các bản sửa lỗi

Trong quá trình kiểm thử BT3, ba lỗi phân quyền đã được ghi nhận và sửa:

| Mã lỗi | Nội dung | Commit sửa |
|---|---|---|
| BUG-01 | API danh sách phân công chưa kiểm tra xác thực | `c8c966d` |
| BUG-02 | API phiếu chưa phân công chưa kiểm tra xác thực | `b50ce78` |
| BUG-03 | API danh sách kỹ thuật viên chưa kiểm tra xác thực | `a4651d7` |

Chi tiết các bước tái hiện, mức độ nghiêm trọng, cách sửa và minh chứng:

`docs/bug-log-bt3.md`

## 10. Triển khai và kiểm tra bảo mật

Dự án sử dụng Docker Compose để đóng gói backend FastAPI cùng database SQLite.

Các thành phần triển khai:

- Dockerfile sử dụng `python:3.12-slim`.
- Docker Compose ánh xạ cổng local `127.0.0.1:8000`.
- Database được lưu trong named volume.
- Healthcheck kiểm tra kết nối đến endpoint `/db-test`.
- Cấu hình quản lý được nạp từ file `.env`.
- Có file `.env.example` để hỗ trợ tạo môi trường demo.

Các nội dung kiểm tra bảo mật bao gồm xác thực, phân quyền, bảo vệ dữ liệu cấu hình và kiểm tra thư viện phụ thuộc.

Kết quả kiểm tra phụ thuộc và ảnh minh chứng được ghi nhận trong tài liệu BT3. Chưa xác nhận hoàn tất kiểm tra lỗ hổng toàn bộ Docker image.

Tài liệu:

- Deployment Guide: `docs/deployment-guide.md`
- Security Checklist: `docs/checklist-bao-mat.md`
- Security Evidence: `docs/screenshots/`

## 11. Migration và Seed

Database SQLite gồm năm bảng chính:

1. `khach_hang`
2. `phieu_bao_hanh`
3. `ky_thuat_vien`
4. `phan_cong_ky_thuat_vien`
5. `lich_hen`

Schema: `docs/database/schema-l04.sql`

Các module:

- Migration: `src/backend/migrate.py`
- Seed: `src/backend/seed.py`

Có thể chạy trên database thử nghiệm riêng:

```bash
python3 -m src.backend.migrate --db /tmp/smartcrm-demo.db
python3 -m src.backend.seed --db /tmp/smartcrm-demo.db
```

Seed được thiết kế để hỗ trợ kiểm tra khả năng chạy lặp lại trên dữ liệu mẫu.

## 12. Tổ chức mã nguồn

```text
smartcrm-2374802010142-technician-assignment/
├── docs/
│   ├── architecture/
│   ├── database/
│   ├── screenshots/
│   ├── use-cases/
│   ├── wireframes/
│   ├── test-plan-bt3.md
│   ├── test-report.md
│   ├── test-report-docker.md
│   ├── bug-log-bt3.md
│   ├── deployment-guide.md
│   ├── checklist-bao-mat.md
│   ├── api-documentation-bt3.md
│   └── ai-disclosure.md
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
├── .env.example
├── .gitignore
├── Dockerfile
├── compose.yaml
├── requirements.txt
├── README.md
└── srs.md
```

## 13. Tài liệu thiết kế và minh chứng

- Đặc tả yêu cầu: `srs.md`
- Use Case: `docs/use-cases/`
- Kiến trúc: `docs/architecture/`
- ERD và SQL DDL: `docs/database/`
- Wireframe: `docs/wireframes/`
- Nhật ký thay đổi thiết kế: `docs/thay-doi-thiet-ke.md`
- Ảnh minh chứng BT3: `docs/screenshots/`
- Khai báo sử dụng AI: `docs/ai-disclosure.md`

## 14. Phạm vi và giới hạn

Dự án tập trung vào luồng L04 – Phân công kỹ thuật viên và lịch hẹn.

Các chức năng quản lý kho, thanh toán, bảo hành toàn hệ thống và quản trị nhiều chi nhánh không thuộc phạm vi triển khai.

Phiên đăng nhập được lưu trong bộ nhớ backend, có thời hạn 60 phút và có thể mất khi khởi động lại server.

SQLite được sử dụng phục vụ mục đích học tập, kiểm thử và demo.

## 15. GitHub và phiên bản nộp bài

**Repository:**

https://github.com/Hieu2374802010142/smartcrm-2374802010142-technician-assignment

**Nhánh chính:** `main`

**Tag theo yêu cầu BT3:** `v1.0`

**Trạng thái:** Tag `v1.0` đã tồn tại; cần xác nhận và chốt nội dung phiên bản nộp sau khi hoàn thiện tài liệu.

---

**Sinh viên thực hiện:** Nguyễn Ngọc Hiếu
**MSSV:** 2374802010142
