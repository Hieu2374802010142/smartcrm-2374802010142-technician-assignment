# UC01 – XEM PHIẾU CHƯA PHÂN CÔNG

**Actor chính:** Quản lý trung tâm

**Mục tiêu:**  
Cho phép quản lý trung tâm xem danh sách các phiếu bảo hành đang ở trạng thái **Mới** và chưa được phân công kỹ thuật viên.

**Điều kiện trước:**

- Quản lý trung tâm đã đăng nhập và có quyền xem phiếu bảo hành.
- Hệ thống có dữ liệu phiếu bảo hành.

**Điều kiện sau:**

- Danh sách các phiếu chưa phân công được hiển thị.
- Quản lý có thể chọn một phiếu để xem thông tin chi tiết và thực hiện phân công.

**Liên quan:** US01  
**Mức ưu tiên:** MUST

## LUỒNG CHÍNH

1. Quản lý trung tâm chọn chức năng **“Xem phiếu chưa phân công”**.
2. Hệ thống lấy danh sách các phiếu bảo hành.
3. Hệ thống lọc các phiếu đang ở trạng thái **Mới** và chưa có kỹ thuật viên.
4. Hệ thống hiển thị danh sách phiếu chưa phân công.
5. Quản lý chọn một phiếu để xem thông tin chi tiết.
6. Hệ thống hiển thị thông tin của phiếu được chọn.

## LUỒNG NGOẠI LỆ

### 2a. Không có phiếu chưa phân công

- Hệ thống không tìm thấy phiếu nào đang ở trạng thái **Mới** và chưa được phân công.
- Hệ thống hiển thị thông báo: **“Không có phiếu chưa phân công.”**
- Quản lý có thể quay lại màn hình chính.

### 5a. Phiếu không còn tồn tại

- Phiếu được chọn không còn tồn tại trong hệ thống.
- Hệ thống thông báo: **“Phiếu không tồn tại hoặc đã được xóa.”**
- Quản lý quay lại danh sách phiếu.

## QUY TẮC NGHIỆP VỤ LIÊN QUAN

- **BR01:** Chỉ phiếu ở trạng thái **Mới** và chưa được phân công mới xuất hiện trong danh sách.
- **BR02:** Phiếu đã được phân công không được hiển thị trong danh sách phiếu chưa phân công.
- **BR06:** Chỉ **Quản lý trung tâm** được xem danh sách phiếu chưa phân công.
