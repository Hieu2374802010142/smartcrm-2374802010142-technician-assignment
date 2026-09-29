### UC03 – PHÂN CÔNG KỸ THUẬT VIÊN

**Actor chính:** Quản lý trung tâm

**Mục tiêu:**
Cho phép quản lý trung tâm chọn và phân công một kỹ thuật viên phù hợp cho phiếu bảo hành chưa được phân công.

**Điều kiện trước:**

* Quản lý trung tâm đã đăng nhập và có quyền phân công.
* Phiếu bảo hành tồn tại trong hệ thống.
* Phiếu đang ở trạng thái **Mới** và chưa được phân công kỹ thuật viên.

**Điều kiện sau:**

* Phiếu bảo hành được gán cho một kỹ thuật viên.
* Trạng thái phiếu được cập nhật từ **Mới** thành **Đã phân công**.
* Thông tin phân công được lưu thành công trong hệ thống.

**Liên quan:** US03
**Mức ưu tiên:** MUST

### LUỒNG CHÍNH

1. Quản lý trung tâm chọn chức năng **“Xem phiếu chưa phân công”**.
2. Hệ thống hiển thị danh sách các phiếu bảo hành đang ở trạng thái **Mới** và chưa có kỹ thuật viên.
3. Quản lý chọn một phiếu cần phân công.
4. Hệ thống hiển thị thông tin chi tiết của phiếu và danh sách kỹ thuật viên.
5. Quản lý chọn kỹ thuật viên phù hợp.
6. Hệ thống kiểm tra điều kiện phân công của phiếu và kỹ thuật viên.
7. Hệ thống lưu thông tin phân công.
8. Hệ thống cập nhật trạng thái phiếu từ **Mới** thành **Đã phân công**.
9. Hệ thống thông báo **“Phân công kỹ thuật viên thành công”**.

### LUỒNG NGOẠI LỆ

**3a. Phiếu đã được phân công**

* Khi quản lý chọn phiếu nhưng phiếu đã được phân công cho kỹ thuật viên khác, hệ thống không cho phép tiếp tục phân công.
* Hệ thống thông báo: **“Phiếu đã được phân công.”**
* Quản lý quay lại danh sách phiếu chưa phân công.

**5a. Kỹ thuật viên không phù hợp hoặc không khả dụng**

* Khi kỹ thuật viên được chọn không đáp ứng điều kiện phân công, hệ thống thông báo lý do.
* Hệ thống yêu cầu quản lý chọn kỹ thuật viên khác.
* Quay lại bước 5 của luồng chính.

**7a. Lỗi khi lưu thông tin phân công**

* Hệ thống thông báo lỗi lưu dữ liệu.
* Thông tin phân công không được lưu không đầy đủ.
* Trạng thái phiếu vẫn giữ nguyên là **Mới**.
* Quản lý có thể thực hiện lại thao tác phân công.

### QUY TẮC NGHIỆP VỤ LIÊN QUAN

* **BR01:** Chỉ phiếu ở trạng thái **Mới** và chưa được phân công mới được phân công.
* **BR02:** Một phiếu chỉ có một kỹ thuật viên được phân công tại một thời điểm.
* **BR03:** Khi phân công thành công, trạng thái phiếu chuyển từ **Mới** sang **Đã phân công**.
* **BR06:** Chỉ **Quản lý trung tâm** được thực hiện phân công kỹ thuật viên.
