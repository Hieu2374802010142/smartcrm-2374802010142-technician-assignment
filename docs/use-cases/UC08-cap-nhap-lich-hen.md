### UC08 – CẬP NHẬT LỊCH HẸN

**Actor chính:** Quản lý trung tâm

**Mục tiêu:**
Cho phép quản lý trung tâm cập nhật ngày, giờ hoặc hình thức giao–nhận máy khi lịch hẹn thay đổi.

**Điều kiện trước:**

* Quản lý trung tâm đã đăng nhập và có quyền cập nhật lịch hẹn.
* Phiếu bảo hành tồn tại trong hệ thống.
* Phiếu đã có lịch hẹn.
* Thông tin lịch hẹn mới được cung cấp.

**Điều kiện sau:**

* Lịch hẹn được cập nhật thành công.
* Ngày, giờ và hình thức giao–nhận mới được lưu vào hệ thống.
* Lịch hẹn mới không bị trùng với lịch làm việc của kỹ thuật viên.

**Liên quan:** US04
**Mức ưu tiên:** SHOULD

### LUỒNG CHÍNH

1. Quản lý trung tâm chọn chức năng **“Cập nhật lịch hẹn”**.
2. Hệ thống hiển thị thông tin lịch hẹn hiện tại.
3. Quản lý nhập thông tin lịch hẹn mới.
4. Hệ thống kiểm tra tính hợp lệ của thông tin lịch hẹn.
5. Hệ thống kiểm tra trùng lịch với lịch làm việc của kỹ thuật viên.
6. Hệ thống hiển thị thông tin lịch hẹn mới để quản lý xác nhận.
7. Quản lý xác nhận cập nhật.
8. Hệ thống lưu thông tin lịch hẹn mới.
9. Hệ thống thông báo **“Cập nhật lịch hẹn thành công”**.

### LUỒNG NGOẠI LỆ

**1a. Phiếu chưa có lịch hẹn**

* Hệ thống thông báo: **“Phiếu chưa có lịch hẹn.”**
* Quản lý có thể chuyển sang chức năng đặt lịch hẹn mới.

**4a. Thông tin lịch hẹn không hợp lệ**

* Hệ thống thông báo lỗi thông tin lịch hẹn.
* Quản lý nhập lại thông tin.
* Quay lại bước 3 của luồng chính.

**5a. Lịch hẹn bị trùng**

* Hệ thống thông báo: **“Lịch hẹn bị trùng.”**
* Quản lý chọn thời gian khác.
* Quay lại bước 3 của luồng chính.

**8a. Lỗi khi lưu lịch hẹn**

* Hệ thống thông báo lỗi khi lưu dữ liệu.
* Lịch hẹn cũ vẫn được giữ nguyên.
* Quản lý có thể thực hiện lại thao tác.

### QUY TẮC NGHIỆP VỤ LIÊN QUAN

* **BR10:** Ngày và giờ lịch hẹn phải hợp lệ.
* **BR11:** Lịch hẹn mới không được trùng với lịch làm việc của kỹ thuật viên.
* **BR12:** Khi cập nhật thành công, lịch hẹn mới thay thế lịch hẹn cũ.
* **BR05:** Hệ thống phải kiểm tra trùng lịch trước khi lưu lịch hẹn.
* **BR06:** Chỉ **Quản lý trung tâm** được thực hiện cập nhật lịch hẹn.
