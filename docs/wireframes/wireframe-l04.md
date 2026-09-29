# WIREFRAME – SMARTCRM L04

## 1. Màn hình: Danh sách phiếu chưa phân công

### Mục đích
Cho phép Quản lý trung tâm xem các phiếu bảo hành đang ở trạng thái Mới
và chưa được phân công kỹ thuật viên.

### Thành phần giao diện

- Tiêu đề: Phiếu bảo hành chưa phân công
- Ô tìm kiếm: Mã phiếu / Số điện thoại khách hàng
- Bộ lọc trạng thái
- Bảng danh sách phiếu:

| Mã phiếu | Khách hàng | Thiết bị | Ngày tạo | Trạng thái | Thao tác |
|----------|------------|----------|----------|------------|----------|
| PB001 | Nguyễn Văn A | iPhone 15 | 29/09/2026 | Mới | Phân công |
| PB002 | Trần Văn B | Samsung S24 | 29/09/2026 | Mới | Phân công |

### Nút thao tác

[Phân công]

### Use Case liên quan

- UC01 – Xem phiếu chưa phân công
- UC03 – Phân công kỹ thuật viên


---

## 2. Màn hình: Phân công kỹ thuật viên và đặt lịch

### Mục đích
Cho phép Quản lý trung tâm chọn kỹ thuật viên và tạo lịch hẹn
giao–nhận máy cho khách hàng.

### Thông tin phiếu

- Mã phiếu
- Tên khách hàng
- Số điện thoại
- Thiết bị
- Trạng thái

### Thông tin kỹ thuật viên

| Kỹ thuật viên | Chuyên môn | Trạng thái | Lịch làm việc |
|---------------|------------|------------|---------------|
| Nguyễn Văn A | Phần cứng | Đang hoạt động | Xem lịch |
| Trần Văn B | Phần mềm | Đang hoạt động | Xem lịch |

### Chọn kỹ thuật viên

[Kỹ thuật viên ▼]

### Thông tin lịch hẹn

- Ngày hẹn: [__/__/____]
- Giờ bắt đầu: [__:__]
- Giờ kết thúc: [__:__]
- Loại lịch hẹn: [Giao máy / Nhận máy ▼]

### Kiểm tra lịch

[Kiểm tra trùng lịch]

Kết quả:

- Không trùng lịch → Có thể lưu
- Trùng lịch → Hiển thị thông báo lỗi

### Nút thao tác

[Phân công]    [Đặt lịch]    [Hủy]

### Use Case liên quan

- UC02 – Xem thông tin kỹ thuật viên
- UC03 – Phân công kỹ thuật viên
- UC04 – Đặt lịch hẹn
- UC05 – Kiểm tra trùng lịch


---

## 3. Màn hình: Công việc được phân công

### Mục đích
Cho phép Kỹ thuật viên xem các phiếu bảo hành và lịch hẹn
được phân công cho mình.

### Bộ lọc

- Ngày
- Trạng thái

### Danh sách công việc

| Mã phiếu | Khách hàng | Thiết bị | Ngày hẹn | Giờ | Loại lịch | Trạng thái |
|----------|------------|----------|----------|-----|-----------|------------|
| PB001 | Nguyễn Văn A | iPhone 15 | 30/09/2026 | 09:00 | Nhận máy | Đã phân công |
| PB002 | Trần Văn B | Samsung S24 | 30/09/2026 | 14:00 | Giao máy | Đã phân công |

### Chi tiết công việc

- Mã phiếu
- Khách hàng
- Số điện thoại
- Thiết bị
- Ngày hẹn
- Giờ hẹn
- Loại lịch
- Trạng thái

### Nút thao tác

[Xem chi tiết]

### Use Case liên quan

- UC06 – Xem công việc được phân công