# UC06 – XEM CÔNG VIỆC ĐƯỢC PHÂN CÔNG

**Actor chính:** Kỹ thuật viên

**Mục tiêu:**

Cho phép kỹ thuật viên xem các phiếu bảo hành và lịch hẹn được phân công cho mình.

**Điều kiện trước:**

* Kỹ thuật viên đã đăng nhập vào hệ thống.
* Tài khoản kỹ thuật viên đang hoạt động.
* Kỹ thuật viên đã được phân công ít nhất một phiếu hoặc có thể chưa có công việc được phân công.

**Điều kiện sau:**

* Kỹ thuật viên xem được danh sách công việc được phân công cho mình.
* Thông tin phiếu bảo hành và lịch hẹn liên quan được hiển thị.
* Kỹ thuật viên không xem được công việc được phân công cho kỹ thuật viên khác.

**Liên quan:** US06

**Mức ưu tiên:** SHOULD

## LUỒNG CHÍNH

1. Kỹ thuật viên chọn chức năng **“Công việc được phân công”**.
2. Hệ thống xác định tài khoản kỹ thuật viên đang đăng nhập.
3. Hệ thống lấy danh sách các phiếu bảo hành được phân công cho kỹ thuật viên.
4. Hệ thống lấy thông tin lịch hẹn liên quan đến các phiếu được phân công.
5. Hệ thống hiển thị danh sách công việc gồm thông tin phiếu, khách hàng, lịch hẹn và trạng thái.
6. Kỹ thuật viên chọn một công việc để xem chi tiết.
7. Hệ thống hiển thị thông tin chi tiết của công việc được chọn.

## LUỒNG NGOẠI LỆ

**1a. Phiên đăng nhập không hợp lệ**

* Hệ thống phát hiện phiên đăng nhập không hợp lệ hoặc đã hết hạn.
* Hệ thống yêu cầu kỹ thuật viên đăng nhập lại.
* Không hiển thị dữ liệu công việc.

**3a. Không có công việc được phân công**

* Hệ thống không tìm thấy phiếu bảo hành nào được phân công cho kỹ thuật viên.
* Hệ thống thông báo **“Bạn chưa có công việc được phân công.”**
* Kỹ thuật viên có thể quay lại trang chính.

**3b. Lỗi khi tải dữ liệu**

* Hệ thống không thể lấy danh sách công việc.
* Hệ thống thông báo lỗi tải dữ liệu.
* Kỹ thuật viên có thể thực hiện lại thao tác.

**6a. Công việc không còn được phân công**

* Hệ thống phát hiện công việc đã được thay đổi hoặc không còn thuộc kỹ thuật viên đang đăng nhập.
* Hệ thống không hiển thị thông tin chi tiết công việc đó.
* Hệ thống thông báo **“Công việc không còn được phân công cho bạn.”**
* Kỹ thuật viên quay lại danh sách công việc.

## QUY TẮC NGHIỆP VỤ LIÊN QUAN

* **BR02:** Một phiếu chỉ có một kỹ thuật viên được phân công tại một thời điểm.
* **BR07:** Kỹ thuật viên chỉ được xem các công việc được phân công cho chính mình.
