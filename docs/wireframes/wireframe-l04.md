
# WIREFRAME – SMARTCRM L04
## Phân công kỹ thuật viên và lịch hẹn

**Dự án:** SmartCRM – Mekong Mobile
**Track:** SE – Software Engineering
**Luồng:** L04 – Phân công kỹ thuật viên và lịch hẹn

---

## 1. Màn hình: Danh sách phiếu chưa phân công

### Mục đích
Cho phép Quản lý trung tâm xem, tìm kiếm và lựa chọn các phiếu bảo hành chưa được phân công kỹ thuật viên.

### Thành phần giao diện
- Tiêu đề: Phiếu bảo hành chưa phân công
- Ô tìm kiếm: Mã phiếu / Số điện thoại khách hàng
- Bộ lọc trạng thái phiếu
- Bảng danh sách phiếu bảo hành

### Wireframe

```text
+------------------------------------------------------------+
| SMARTCRM - DANH SACH PHIEU CHUA PHAN CONG                  |
+------------------------------------------------------------+
| Tim kiem: [Ma phieu / So dien thoai........] [Tim kiem]    |
| Trang thai: [Moi v]                                       |
+------------------------------------------------------------+
| Ma phieu | Khach hang   | Thiet bi   | Trang thai | Thao tac|
| PB001    | Nguyen Van A | iPhone 15  | Moi        | Phan cong|
| PB002    | Tran Van B   | Samsung S24| Moi        | Phan cong|
+------------------------------------------------------------+
```

### Nút thao tác
- [Tìm kiếm]: Tìm phiếu bảo hành theo mã hoặc số điện thoại.
- [Phân công]: Chuyển sang màn hình phân công kỹ thuật viên.

### Quy tắc xử lý
- Chỉ hiển thị phiếu chưa có phân công đang hoạt động.
- Quản lý trung tâm được xem và thực hiện phân công.
- Danh sách phiếu được phân trang để hỗ trợ NFR01.

### Use Case liên quan
- UC01 – Xem phiếu chưa phân công
- UC03 – Phân công kỹ thuật viên

---

## 2. Màn hình: Phân công kỹ thuật viên và đặt lịch

### Mục đích
Cho phép Quản lý trung tâm chọn kỹ thuật viên phù hợp, phân công công việc, đặt lịch hẹn, cập nhật lịch hẹn và hủy phân công khi cần thiết.

### Thông tin phiếu bảo hành
- Mã phiếu
- Tên khách hàng
- Số điện thoại khách hàng
- Tên thiết bị
- Trạng thái phiếu

### Thông tin kỹ thuật viên
- Mã kỹ thuật viên
- Họ tên kỹ thuật viên
- Chuyên môn
- Trạng thái hoạt động
- Lịch hẹn hiện có

### Thông tin phân công
- Kỹ thuật viên được chọn
- Ngày phân công
- Trạng thái phân công: Đang phân công / Đã hủy

### Thông tin lịch hẹn
- Ngày hẹn
- Giờ bắt đầu
- Giờ kết thúc
- Loại lịch hẹn: Giao máy / Nhận máy
- Trạng thái lịch hẹn: Đã đặt / Đã hủy

### Wireframe

```text
+------------------------------------------------------------+
| SMARTCRM - PHAN CONG KY THUAT VIEN VA DAT LICH             |
+------------------------------------------------------------+
| THONG TIN PHIEU BAO HANH                                  |
| Ma phieu: PB001                                            |
| Khach hang: Nguyen Van A                                   |
| So dien thoai: 0901000001                                  |
| Thiet bi: iPhone 15                                        |
| Trang thai: Moi                                            |
+------------------------------------------------------------+
| THONG TIN PHAN CONG                                        |
| Ky thuat vien: [Chon ky thuat vien v]                      |
| Chuyen mon: Phan cung                                      |
| Trang thai hoat dong: Dang hoat dong                       |
| Trang thai phan cong: Dang phan cong                       |
+------------------------------------------------------------+
| THONG TIN LICH HEN                                         |
| Ngay hen: [30/09/2026]                                     |
| Gio bat dau: [09:00]                                       |
| Gio ket thuc: [10:00]                                      |
| Loai lich hen: [Nhan may v]                                |
| Trang thai lich hen: Da dat                                |
|                                                            |
| [Kiem tra trung lich]                                      |
| Ket qua: Khong trung lich                                  |
+------------------------------------------------------------+
| [Phan cong] [Dat lich] [Cap nhat lich hen]                 |
| [Huy phan cong] [Quay lai]                                 |
+------------------------------------------------------------+
```

### Nút thao tác
- [Phân công]: Lưu thông tin phân công kỹ thuật viên.
- [Đặt lịch]: Tạo lịch hẹn giao hoặc nhận máy.
- [Kiểm tra trùng lịch]: Kiểm tra lịch của kỹ thuật viên.
- [Cập nhật lịch hẹn]: Thay đổi ngày, giờ hoặc loại lịch hẹn.
- [Hủy phân công]: Hủy phân công đang hoạt động.
- [Quay lại]: Trở về danh sách phiếu.

### Quy tắc xử lý
- Chỉ Quản lý trung tâm có quyền phân công, cập nhật lịch và hủy phân công.
- Kỹ thuật viên phải đang hoạt động mới được chọn.
- Giờ kết thúc phải lớn hơn giờ bắt đầu.
- Khi đặt hoặc cập nhật lịch, hệ thống kiểm tra trùng lịch trước khi lưu.
- Hai lịch đang có hiệu lực của cùng kỹ thuật viên không được chồng lấn thời gian.
- Khi hủy phân công, trạng thái phân công chuyển thành Đã hủy.
- Phiếu không còn kỹ thuật viên được gán đang hoạt động và trạng thái phiếu trở về Mới.
- Lịch sử phân công đã hủy vẫn được lưu để truy vết.
- Khi hủy phân công, các lịch hẹn còn hiệu lực liên quan phải được hủy trong cùng giao dịch.
- Khi lưu phân công và lịch hẹn cùng lúc, hệ thống sử dụng transaction để tránh dữ liệu không đầy đủ.
- Các thao tác cập nhật chỉ khả dụng khi bản ghi ở trạng thái phù hợp.

### Thông báo
- Thành công: Phân công kỹ thuật viên thành công.
- Thành công: Đặt lịch hẹn thành công.
- Thành công: Cập nhật lịch hẹn thành công.
- Thành công: Hủy phân công thành công.
- Lỗi: Kỹ thuật viên đã có lịch trong khoảng thời gian này.
- Lỗi: Giờ kết thúc phải lớn hơn giờ bắt đầu.
- Lỗi: Bạn không có quyền thực hiện thao tác.

### Use Case liên quan
- UC02 – Xem thông tin kỹ thuật viên
- UC03 – Phân công kỹ thuật viên
- UC04 – Đặt lịch hẹn
- UC05 – Kiểm tra trùng lịch
- UC07 – Hủy phân công kỹ thuật viên
- UC08 – Cập nhật lịch hẹn

---

## 3. Màn hình: Công việc được phân công

### Mục đích
Cho phép Kỹ thuật viên xem danh sách công việc và lịch hẹn được phân công cho mình.

### Thành phần giao diện
- Tiêu đề: Công việc được phân công
- Bộ lọc theo ngày
- Bộ lọc trạng thái
- Danh sách công việc
- Nút xem chi tiết

### Thông tin công việc
- Mã phiếu
- Tên khách hàng
- Số điện thoại khách hàng
- Thiết bị
- Ngày hẹn
- Giờ bắt đầu và giờ kết thúc
- Loại lịch hẹn
- Trạng thái phân công
- Trạng thái lịch hẹn

### Wireframe

```text
+------------------------------------------------------------+
| SMARTCRM - CONG VIEC DUOC PHAN CONG                        |
+------------------------------------------------------------+
| Ngay: [30/09/2026]  Trang thai: [Tat ca v] [Loc]          |
+------------------------------------------------------------+
| Ma phieu | Thiet bi   | Ngay hen   | Gio   | Trang thai    |
| PB001    | iPhone 15  | 30/09/2026 | 09:00 | Da phan cong  |
| PB002    | Samsung S24| 30/09/2026 | 14:00 | Da phan cong  |
+------------------------------------------------------------+
| CHI TIET CONG VIEC                                         |
| Ma phieu: PB001                                            |
| Khach hang: Nguyen Van A                                   |
| Thiet bi: iPhone 15                                        |
| Ngay hen: 30/09/2026                                       |
| Gio hen: 09:00 - 10:00                                     |
| Loai lich: Nhan may                                        |
| Trang thai phan cong: Dang phan cong                       |
| Trang thai lich hen: Da dat                                |
+------------------------------------------------------------+
| [Xem chi tiet]                                             |
+------------------------------------------------------------+
```

### Nút thao tác
- [Lọc]: Lọc công việc theo ngày và trạng thái.
- [Xem chi tiết]: Hiển thị thông tin công việc.

### Quy tắc xử lý
- Kỹ thuật viên chỉ được xem công việc được phân công cho mình.
- Kỹ thuật viên không được tự thay đổi phân công hoặc lịch hẹn.
- Các phân công đã hủy không xuất hiện trong danh sách công việc đang hoạt động.

### Use Case liên quan
- UC06 – Xem công việc được phân công

---

## 4. Đối chiếu Wireframe với ERD

| Trường giao diện | Bảng dữ liệu | Thuộc tính |
|---|---|---|
| Mã phiếu | PHIẾU BẢO HÀNH | ma_phieu |
| Tên khách hàng | KHÁCH HÀNG | ho_ten |
| Số điện thoại khách hàng | KHÁCH HÀNG | so_dien_thoai |
| Thiết bị | PHIẾU BẢO HÀNH | ten_thiet_bi |
| Trạng thái phiếu | PHIẾU BẢO HÀNH | trang_thai |
| Ngày tạo phiếu | PHIẾU BẢO HÀNH | ngay_tao |
| Mã kỹ thuật viên | KỸ THUẬT VIÊN | ma_ky_thuat_vien |
| Tên kỹ thuật viên | KỸ THUẬT VIÊN | ho_ten |
| Chuyên môn | KỸ THUẬT VIÊN | chuyen_mon |
| Trạng thái hoạt động | KỸ THUẬT VIÊN | dang_hoat_dong |
| Ngày phân công | PHÂN CÔNG KỸ THUẬT VIÊN | ngay_phan_cong |
| Trạng thái phân công | PHÂN CÔNG KỸ THUẬT VIÊN | trang_thai_phan_cong |
| Ngày hẹn | LỊCH HẸN | ngay_hen |
| Giờ bắt đầu | LỊCH HẸN | gio_bat_dau |
| Giờ kết thúc | LỊCH HẸN | gio_ket_thuc |
| Loại lịch hẹn | LỊCH HẸN | loai_lich_hen |
| Trạng thái lịch hẹn | LỊCH HẸN | trang_thai_lich_hen |

### Các trường tính toán hoặc hiển thị
- Mã PB001 là cách hiển thị có tiền tố PB từ ma_phieu.
- Lịch làm việc được tổng hợp từ các lịch hẹn hiện có của kỹ thuật viên.
- Kết quả kiểm tra trùng lịch được tính từ các khoảng thời gian đã đặt, không cần lưu thành cột riêng.
- Trạng thái "Đã phân công" trên danh sách công việc được suy ra từ trạng thái phân công đang hoạt động.

---

## 5. Kết luận

Hệ thống SmartCRM L04 được thiết kế với 3 màn hình chính:
1. Danh sách phiếu chưa phân công.
2. Phân công kỹ thuật viên và đặt lịch.
3. Công việc được phân công.

Ba màn hình hỗ trợ 8 Use Case từ UC01 đến UC08 và sử dụng dữ liệu từ 5 bảng trong ERD.

Các chức năng kiểm tra trùng lịch, phân quyền và lưu dữ liệu nhất quán được bổ sung để đáp ứng các yêu cầu phi chức năng của hệ thống.