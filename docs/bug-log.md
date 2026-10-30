# NHẬT KÝ LỖI VÀ KHẮC PHỤC – SMARTCRM L04 (BT2)

**Sinh viên:** Nguyễn Ngọc Hiếu
**MSSV:** 2374802010142
**Dự án:** SmartCRM – L04: Phân công kỹ thuật viên và lịch hẹn
**Ngày tổng hợp:** 30/10/2026

## 1. Mục đích

Tài liệu ghi nhận các vấn đề kỹ thuật đã gặp hoặc được kiểm tra trong quá trình phát triển và kiểm thử SmartCRM L04, giúp theo dõi nguyên nhân, cách xử lý và kết quả xác minh.

## 2. Nhật ký lỗi và vấn đề kỹ thuật

### BUG-01 – Cổng chạy FastAPI đã được sử dụng

**Hiện tượng:** Khi khởi động FastAPI, Terminal xuất hiện thông báo `Address already in use`.

**Nguyên nhân:** Cổng 8000 đã có tiến trình sử dụng.

**Cách xử lý:** Kiểm tra tiến trình đang chạy hoặc sử dụng cổng khác khi cần chạy bản thử nghiệm độc lập.

**Kết quả:** Bản Clean Clone đã khởi động thành công trên cổng 8001.

**Trạng thái:** Đã xử lý.

### BUG-02 – Cần thiết lập thông tin đăng nhập khi Clean Clone

**Vấn đề:** File `.env` không được đưa lên GitHub vì chứa thông tin cấu hình xác thực. Do đó, bản clone mới cần được thiết lập tài khoản quản lý riêng.

**Cách xử lý:** Bổ sung chương trình `src/backend/setup_admin.py` để thiết lập tài khoản và tạo cấu hình môi trường.

**Kết quả:** Đã đăng nhập thành công vào giao diện SmartCRM trên bản Clean Clone.

**Trạng thái:** Đã xác minh.

### BUG-03 – Nguy cơ dữ liệu mẫu bị trùng khi chạy Seed nhiều lần

**Vấn đề:** Nếu chương trình Seed luôn thêm dữ liệu mới, việc chạy lại có thể tạo bản ghi trùng lặp.

**Cách xử lý:** Cải tiến Seed để kiểm tra dữ liệu đã tồn tại trước khi thêm.

**Kết quả kiểm tra:**

| Loại dữ liệu | Chạy lần 1 | Chạy lần 2 |
|---|---:|---:|
| Khách hàng | 3 | 0 |
| Kỹ thuật viên | 3 | 0 |
| Phiếu bảo hành | 3 | 0 |

**Trạng thái:** Đã xác minh.

### BUG-04 – Cần kiểm soát lỗi nghiệp vụ độc lập với HTTP

**Vấn đề thiết kế:** Nếu Service phụ thuộc trực tiếp vào HTTP response, việc kiểm thử và tái sử dụng logic nghiệp vụ trở nên khó khăn.

**Cách xử lý:** Sử dụng `TicketError` tại Service và chuyển đổi lỗi thành HTTP response tại Routes.

**Kết quả:** Các bài kiểm thử Service và CRUD đã chạy thành công trong bộ 27 bài kiểm thử.

**Trạng thái:** Đã cải tiến kiến trúc.

### BUG-05 – Cần kiểm tra khả năng triển khai từ GitHub

**Vấn đề:** Một dự án chạy được trên máy phát triển chưa đủ chứng minh có thể cài đặt lại từ mã nguồn GitHub.

**Cách xử lý:** Thực hiện Clean Clone, Migration, Seed, cấu hình tài khoản, chạy API và kiểm thử.

**Kết quả:** Bản Clean Clone chạy thành công, 27/27 bài kiểm thử PASS; giao diện đăng nhập, phân công và đặt lịch hoạt động.

**Trạng thái:** Đã xác minh.

## 3. Tổng kết

Các vấn đề đã được xử lý hoặc kiểm chứng thông qua cải tiến kiến trúc, cấu hình môi trường, Migration, Seed và kiểm thử tự động.

Lưu ý: BUG-02 đến BUG-05 bao gồm cả rủi ro và vấn đề thiết kế được phòng ngừa, không có nghĩa tất cả đều từng gây lỗi thực tế trong lúc chạy chương trình.

**Kết quả kiểm thử tại thời điểm tổng hợp:** 27/27 PASS.

**Phiên bản mã nguồn được kiểm tra:** `f54f007` – tag `v0.2`.
## 4. Truy vết commit và bằng chứng kiểm chứng

Các liên kết dưới đây ghi nhận những commit triển khai hoặc cải tiến thành phần liên quan. Không phải mọi mục đều là lỗi đã phát sinh trong quá trình chạy chương trình.

| Mã | Phân loại | Commit liên quan | Bằng chứng |
|---|---|---|---|
| BUG-01 | Lỗi môi trường chạy thực tế | Chưa xác định commit sửa lỗi | FastAPI khởi động thành công trên cổng 8001 |
| BUG-02 | Vấn đề cấu hình triển khai | `f54f007` | Thiết lập tài khoản và đăng nhập thành công trên Clean Clone |
| BUG-03 | Rủi ro dữ liệu trùng | `7377515`, `f54f007` | Seed lần đầu thêm 3/3/3, lần hai thêm 0/0/0 |
| BUG-04 | Cải tiến kiến trúc | `25c91bc`, `f54f007` | Bộ kiểm thử Service và CRUD PASS |
| BUG-05 | Kiểm chứng khả năng triển khai | `f54f007` | Clean Clone và 27/27 bài kiểm thử PASS |

### 4.1. Liên kết commit GitHub

**Commit f54f007 – Hoàn thiện BT2**

https://github.com/Hieu2374802010142/smartcrm-2374802010142-technician-assignment/commit/f54f007

**Commit 25c91bc – API phân công và lịch hẹn**

https://github.com/Hieu2374802010142/smartcrm-2374802010142-technician-assignment/commit/25c91bc

**Commit 7377515 – Seed dữ liệu ban đầu**

https://github.com/Hieu2374802010142/smartcrm-2374802010142-technician-assignment/commit/7377515

### 4.2. Lệnh kiểm chứng

**Kiểm tra Migration:**

```bash
python3 -m src.backend.migrate
```

**Kiểm tra Seed:**

```bash
python3 -m src.backend.seed
python3 -m src.backend.seed
```

**Kiểm tra toàn bộ bộ kiểm thử:**

```bash
python3 -m pytest -q
```

**Chạy hệ thống trên cổng 8001:**

```bash
python3 -m uvicorn src.backend.main:app --reload --port 8001
```

Các lệnh trên được sử dụng trong quá trình kiểm chứng bản Clean Clone. Kết quả đã ghi nhận là 27/27 bài kiểm thử PASS, Seed không tạo thêm bản ghi mẫu ở lần chạy thứ hai và luồng đăng nhập, phân công, đặt lịch hoạt động thành công.

### 4.3. Giới hạn của nhật ký

BUG-01 là sự cố môi trường đã quan sát được. Các mục BUG-02 đến BUG-05 là vấn đề cấu hình, rủi ro hoặc cải tiến được kiểm chứng.

Chưa có đủ bằng chứng để khẳng định cả năm mục đều là lỗi mã nguồn đã được sửa trong Giai đoạn 2. Khi có thêm lỗi thực tế, cần ghi riêng thời điểm phát hiện, bước tái hiện, nguyên nhân, thay đổi mã nguồn, commit sửa và kết quả kiểm thử lại.
