# UC05 – KIỂM TRA TRÙNG LỊCH

**Actor chính:** Quản lý trung tâm

**Mục tiêu:**

Cho phép hệ thống kiểm tra kỹ thuật viên có lịch hẹn trùng với khoảng thời gian được chọn trước khi lưu lịch hẹn mới.

**Điều kiện trước:**

* Quản lý trung tâm đã đăng nhập và có quyền đặt lịch.
* Phiếu bảo hành đã được phân công kỹ thuật viên.
* Quản lý đã nhập ngày và giờ cho lịch hẹn.
* Thông tin kỹ thuật viên cần kiểm tra đã được xác định.

**Điều kiện sau:**

* Nếu không có lịch trùng, hệ thống xác nhận lịch hẹn hợp lệ và cho phép tiếp tục lưu lịch hẹn.
* Nếu có lịch trùng, hệ thống thông báo lỗi và không cho phép lưu lịch hẹn.
* Không tạo dữ liệu lịch hẹn không hợp lệ trong hệ thống.

**Liên quan:** US05

**Mức ưu tiên:** MUST

## LUỒNG CHÍNH

1. Quản lý trung tâm nhập hoặc chọn ngày và giờ của lịch hẹn.
2. Hệ thống xác định kỹ thuật viên được phân công cho phiếu bảo hành.
3. Hệ thống lấy các lịch hẹn hiện có của kỹ thuật viên trong khoảng thời gian liên quan.
4. Hệ thống so sánh khoảng thời gian lịch hẹn mới với các lịch hẹn đã tồn tại.
5. Hệ thống xác nhận không có lịch hẹn bị trùng.
6. Hệ thống thông báo lịch hẹn hợp lệ.
7. Hệ thống trả kết quả kiểm tra về chức năng **“Đặt lịch hẹn”** để tiếp tục lưu lịch.

## LUỒNG NGOẠI LỆ

**2a. Không xác định được kỹ thuật viên**

* Hệ thống không tìm thấy kỹ thuật viên được phân công cho phiếu.
* Hệ thống thông báo lỗi.
* Không cho phép tiếp tục tạo lịch hẹn.
* Quản lý quay lại thông tin phân công để kiểm tra.

**3a. Kỹ thuật viên chưa có lịch hẹn**

* Hệ thống không tìm thấy lịch hẹn nào của kỹ thuật viên trong khoảng thời gian liên quan.
* Hệ thống xác nhận không có lịch trùng.
* Tiếp tục bước 5 của luồng chính.

**4a. Phát hiện lịch hẹn bị trùng**

* Hệ thống phát hiện kỹ thuật viên đã có lịch hẹn trong khoảng thời gian được chọn.
* Hệ thống thông báo **“Kỹ thuật viên đã có lịch hẹn trong khoảng thời gian này.”**
* Hệ thống không cho phép lưu lịch hẹn mới.
* Quản lý chọn thời gian khác.
* Quay lại bước 1 của luồng chính.

**5a. Lỗi khi kiểm tra lịch**

* Hệ thống không thể truy vấn hoặc kiểm tra dữ liệu lịch hẹn.
* Hệ thống thông báo lỗi kiểm tra lịch.
* Hệ thống không cho phép lưu lịch hẹn.
* Quản lý có thể thực hiện lại thao tác.

## QUY TẮC NGHIỆP VỤ LIÊN QUAN

* **BR04:** Hệ thống phải kiểm tra trùng lịch trước khi lưu lịch hẹn.
* **BR05:** Không được lưu lịch hẹn nếu phát hiện thời gian bị trùng.
* **BR02:** Một phiếu chỉ có một kỹ thuật viên được phân công tại một thời điểm.
* **BR06:** Chỉ **Quản lý trung tâm** được thực hiện đặt lịch hẹn.
