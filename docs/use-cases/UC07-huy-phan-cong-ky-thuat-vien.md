### UC07 – HỦY PHÂN CÔNG KỸ THUẬT VIÊN

**Actor chính:** Quản lý trung tâm

**Mục tiêu:**
Cho phép quản lý trung tâm hủy phân công kỹ thuật viên đối với phiếu chưa hoàn tất để có thể phân công lại.

**Điều kiện trước:**

* Quản lý trung tâm đã đăng nhập và có quyền hủy phân công.
* Phiếu bảo hành tồn tại trong hệ thống.
* Phiếu đã được phân công kỹ thuật viên.
* Phiếu chưa hoàn tất.

**Điều kiện sau:**

* Phân công kỹ thuật viên được hủy.
* Phiếu không còn kỹ thuật viên được phân công.
* Trạng thái phiếu được chuyển về **Mới** để có thể phân công lại.

**Liên quan:** US03
**Mức ưu tiên:** SHOULD

### LUỒNG CHÍNH

1. Quản lý trung tâm chọn chức năng **“Xem phiếu đã phân công”**.
2. Hệ thống hiển thị danh sách các phiếu đã được phân công.
3. Quản lý chọn phiếu cần hủy phân công.
4. Hệ thống hiển thị thông tin phiếu và kỹ thuật viên đang được phân công.
5. Quản lý chọn chức năng **“Hủy phân công”**.
6. Hệ thống kiểm tra trạng thái của phiếu.
7. Hệ thống hiển thị yêu cầu xác nhận hủy phân công.
8. Quản lý xác nhận hủy phân công.
9. Hệ thống xóa thông tin phân công kỹ thuật viên.
10. Hệ thống cập nhật trạng thái phiếu về **Mới**.
11. Hệ thống thông báo **“Hủy phân công thành công”**.

### LUỒNG NGOẠI LỆ

**3a. Phiếu không tồn tại**

* Hệ thống thông báo: **“Phiếu không tồn tại hoặc đã được xóa.”**
* Quản lý quay lại danh sách phiếu.

**6a. Phiếu đã hoàn tất**

* Hệ thống thông báo: **“Không thể hủy phân công phiếu đã hoàn tất.”**
* Hệ thống không thực hiện thay đổi.
* Quản lý quay lại màn hình chi tiết phiếu.

**8a. Quản lý không xác nhận**

* Hệ thống hủy thao tác xác nhận.
* Thông tin phân công và trạng thái phiếu không thay đổi.

**9a. Lỗi khi lưu thông tin**

* Hệ thống thông báo lỗi khi hủy phân công.
* Thông tin phân công vẫn được giữ nguyên.
* Trạng thái phiếu không thay đổi.
* Quản lý có thể thực hiện lại thao tác.

### QUY TẮC NGHIỆP VỤ LIÊN QUAN

* **BR07:** Chỉ phiếu chưa hoàn tất mới được phép hủy phân công.
* **BR08:** Khi hủy phân công thành công, thông tin kỹ thuật viên được xóa khỏi phiếu.
* **BR09:** Sau khi hủy phân công thành công, trạng thái phiếu chuyển về **Mới**.
* **BR06:** Chỉ **Quản lý trung tâm** được thực hiện hủy phân công.
