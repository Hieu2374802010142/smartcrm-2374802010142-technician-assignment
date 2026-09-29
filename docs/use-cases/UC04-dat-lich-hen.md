# UC04 – ĐẶT LỊCH HẸN

**Actor chính:** Quản lý trung tâm

**Mục tiêu:**

Cho phép quản lý trung tâm tạo lịch hẹn giao–nhận máy cho khách hàng đối với phiếu bảo hành đã được phân công kỹ thuật viên.

**Điều kiện trước:**

* Quản lý trung tâm đã đăng nhập và có quyền đặt lịch.
* Phiếu bảo hành tồn tại trong hệ thống.
* Phiếu đã được phân công kỹ thuật viên.
* Thông tin khách hàng và phiếu bảo hành đầy đủ.

**Điều kiện sau:**

* Lịch hẹn giao–nhận máy được tạo thành công.
* Thông tin ngày, giờ và loại lịch hẹn được lưu trong hệ thống.
* Lịch hẹn không bị trùng với lịch đã tồn tại của kỹ thuật viên.

**Liên quan:** US04

**Mức ưu tiên:** MUST

## LUỒNG CHÍNH

1. Quản lý trung tâm chọn một phiếu bảo hành đã được phân công.
2. Hệ thống hiển thị thông tin phiếu, khách hàng và kỹ thuật viên được phân công.
3. Quản lý chọn chức năng **“Đặt lịch hẹn”**.
4. Hệ thống hiển thị biểu mẫu nhập thông tin lịch hẹn.
5. Quản lý nhập ngày, giờ và loại lịch hẹn giao–nhận máy.
6. Hệ thống kiểm tra thông tin lịch hẹn và kiểm tra trùng lịch.
7. Hệ thống xác nhận lịch hẹn không bị trùng.
8. Hệ thống lưu thông tin lịch hẹn.
9. Hệ thống thông báo **“Đặt lịch hẹn thành công”**.

## LUỒNG NGOẠI LỆ

**5a. Thông tin lịch hẹn không hợp lệ**

* Khi ngày hoặc giờ hẹn không hợp lệ, hệ thống thông báo lỗi.
* Hệ thống yêu cầu quản lý nhập lại thông tin.
* Quay lại bước 5 của luồng chính.

**6a. Lịch hẹn bị trùng**

* Hệ thống phát hiện kỹ thuật viên đã có lịch trong khoảng thời gian được chọn.
* Hệ thống thông báo **“Kỹ thuật viên đã có lịch hẹn trong khoảng thời gian này.”**
* Lịch hẹn không được lưu.
* Quản lý chọn thời gian khác.
* Quay lại bước 5 của luồng chính.

**8a. Lỗi khi lưu lịch hẹn**

* Hệ thống thông báo lỗi lưu dữ liệu.
* Thông tin lịch hẹn không được lưu không đầy đủ.
* Quản lý có thể thực hiện lại thao tác đặt lịch.

## QUY TẮC NGHIỆP VỤ LIÊN QUAN

* **BR04:** Hệ thống phải kiểm tra trùng lịch trước khi lưu lịch hẹn.
* **BR05:** Không được lưu lịch hẹn nếu phát hiện thời gian bị trùng.
* **BR06:** Chỉ **Quản lý trung tâm** được thực hiện đặt lịch hẹn.
