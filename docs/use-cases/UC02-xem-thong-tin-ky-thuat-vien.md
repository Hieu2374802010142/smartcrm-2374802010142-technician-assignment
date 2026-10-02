### UC02 – XEM THÔNG TIN KỸ THUẬT VIÊN

**Actor chính:** Quản lý trung tâm

**Mục tiêu:**
Cho phép quản lý trung tâm xem thông tin kỹ thuật viên để lựa chọn kỹ thuật viên phù hợp cho phiếu bảo hành.

**Điều kiện trước:**

* Quản lý trung tâm đã đăng nhập và có quyền xem thông tin kỹ thuật viên.
* Hệ thống có dữ liệu kỹ thuật viên.

**Điều kiện sau:**

* Thông tin kỹ thuật viên được hiển thị.
* Quản lý có đủ thông tin để lựa chọn kỹ thuật viên phù hợp.

**Liên quan:** US02
**Mức ưu tiên:** MUST

### LUỒNG CHÍNH

1. Quản lý trung tâm chọn chức năng **“Xem thông tin kỹ thuật viên”**.
2. Hệ thống lấy danh sách kỹ thuật viên.
3. Hệ thống hiển thị thông tin kỹ thuật viên.
4. Quản lý xem thông tin và trạng thái làm việc của kỹ thuật viên.
5. Quản lý có thể chọn kỹ thuật viên phù hợp để thực hiện phân công.

### LUỒNG NGOẠI LỆ

**2a. Không có kỹ thuật viên**

* Hệ thống thông báo: **“Không có kỹ thuật viên.”**
* Quản lý quay lại màn hình trước.

**3a. Kỹ thuật viên không khả dụng**

* Hệ thống hiển thị trạng thái không khả dụng của kỹ thuật viên.
* Quản lý không thể chọn kỹ thuật viên này để phân công.
* Quản lý chọn kỹ thuật viên khác.

### QUY TẮC NGHIỆP VỤ LIÊN QUAN

* **BR04:** Thông tin kỹ thuật viên phải bao gồm trạng thái khả dụng.
* **BR05:** Kỹ thuật viên không khả dụng không được phân công cho phiếu.
* **BR06:** Chỉ **Quản lý trung tâm** được xem thông tin kỹ thuật viên phục vụ việc phân công.
