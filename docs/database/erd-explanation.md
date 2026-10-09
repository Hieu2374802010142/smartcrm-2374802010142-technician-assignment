# GIẢI THÍCH ERD VÀ CHUẨN HÓA 3NF – SMARTCRM L04

**Dự án:** SmartCRM – Mekong Mobile
**Track:** SE – Software Engineering
**Luồng:** L04 – Phân công kỹ thuật viên và lịch hẹn

## 1. Mục đích thiết kế cơ sở dữ liệu

Cơ sở dữ liệu được thiết kế để hỗ trợ quản lý phiếu bảo hành, phân công kỹ thuật viên, đặt lịch hẹn, kiểm tra trùng lịch, hủy phân công và cập nhật lịch hẹn.

Mô hình gồm 5 bảng dữ liệu chính.

## 2. Mô tả các bảng dữ liệu

### 2.1. KHÁCH HÀNG

- Khóa chính: ma_khach_hang
- Thuộc tính: ho_ten, so_dien_thoai
- Chức năng: Lưu thông tin cơ bản của khách hàng có phiếu bảo hành.

### 2.2. PHIẾU BẢO HÀNH

- Khóa chính: ma_phieu
- Khóa ngoại: ma_khach_hang
- Thuộc tính: ten_thiet_bi, trang_thai, ngay_tao
- Chức năng: Lưu thông tin phiếu bảo hành và trạng thái xử lý.

### 2.3. KỸ THUẬT VIÊN

- Khóa chính: ma_ky_thuat_vien
- Thuộc tính: ho_ten, so_dien_thoai, chuyen_mon, dang_hoat_dong
- Chức năng: Lưu thông tin kỹ thuật viên phục vụ phân công.

### 2.4. PHÂN CÔNG KỸ THUẬT VIÊN

- Khóa chính: ma_phan_cong
- Khóa ngoại: ma_phieu, ma_ky_thuat_vien
- Thuộc tính: ngay_phan_cong, trang_thai_phan_cong
- Chức năng: Ghi nhận việc phân công kỹ thuật viên cho phiếu bảo hành và lưu lịch sử phân công.

### 2.5. LỊCH HẸN

- Khóa chính: ma_lich_hen
- Khóa ngoại: ma_phan_cong
- Thuộc tính: ngay_hen, gio_bat_dau, gio_ket_thuc, loai_lich_hen, trang_thai_lich_hen, ngay_tao
- Chức năng: Quản lý lịch hẹn gắn với từng lần phân công.

## 3. Mối quan hệ giữa các bảng

| Quan hệ | Kiểu | Giải thích |
|---|---|---|
| KHÁCH HÀNG – PHIẾU BẢO HÀNH | 1:N | Một khách hàng có thể có nhiều phiếu bảo hành. |
| PHIẾU BẢO HÀNH – PHÂN CÔNG | 1:N | Một phiếu có thể có nhiều lần phân công trong lịch sử. |
| KỸ THUẬT VIÊN – PHÂN CÔNG | 1:N | Một kỹ thuật viên có thể nhận nhiều phiếu. |
| PHÂN CÔNG – LỊCH HẸN | 1:N | Một lần phân công có thể có nhiều lịch hẹn. |

## 4. Kiểm tra chuẩn hóa cơ sở dữ liệu

### 4.1. Chuẩn 1NF

Mỗi bảng có khóa chính xác định từng bản ghi.

Các thuộc tính được thiết kế để lưu giá trị đơn, không sử dụng nhóm thuộc tính lặp trong cùng một bản ghi.

Vì vậy, mô hình được thiết kế theo nguyên tắc 1NF.

### 4.2. Chuẩn 2NF

Cả 5 bảng đều sử dụng khóa chính đơn.

Các thuộc tính không khóa phụ thuộc vào toàn bộ khóa chính của bảng tương ứng, không tồn tại phụ thuộc bộ phận vào khóa chính ghép.

Vì vậy, mô hình được thiết kế theo nguyên tắc 2NF.

### 4.3. Chuẩn 3NF

Các thông tin được phân tách theo đúng đối tượng nghiệp vụ:

- Thông tin khách hàng được lưu trong bảng KHÁCH HÀNG.
- Thông tin phiếu được lưu trong bảng PHIẾU BẢO HÀNH.
- Thông tin kỹ thuật viên được lưu trong bảng KỸ THUẬT VIÊN.
- Thông tin phân công được lưu trong bảng PHÂN CÔNG KỸ THUẬT VIÊN.
- Thông tin lịch hẹn được lưu trong bảng LỊCH HẸN.

Ví dụ, bảng PHÂN CÔNG chỉ lưu mã kỹ thuật viên thay vì sao chép họ tên và số điện thoại kỹ thuật viên.

Bảng LỊCH HẸN chỉ lưu mã phân công thay vì sao chép thông tin khách hàng, phiếu và kỹ thuật viên.

Theo các phụ thuộc chức năng nghiệp vụ đã giả định, thuộc tính không khóa không phụ thuộc bắc cầu vào khóa chính thông qua một thuộc tính không khóa khác.

Do đó, mô hình được thiết kế hướng đến chuẩn 3NF. Việc xác nhận đầy đủ cần kiểm tra thêm các phụ thuộc chức năng và ràng buộc khi triển khai cơ sở dữ liệu.

## 5. Ràng buộc nghiệp vụ

### 5.1. Phân công kỹ thuật viên

- Mỗi phiếu chỉ có tối đa một phân công đang hoạt động tại một thời điểm.
- Kỹ thuật viên phải đang hoạt động khi được phân công.
- Sau khi phân công, trạng thái phiếu chuyển từ Mới sang Đã phân công.

### 5.2. Hủy phân công – UC07

- Chỉ được hủy phân công khi phiếu chưa hoàn tất.
- Trạng thái phân công được chuyển thành Đã hủy.
- Phiếu không còn phân công đang hoạt động và trạng thái phiếu trở về Mới.
- Các lịch hẹn còn hiệu lực liên quan được chuyển thành Đã hủy.
- Toàn bộ thao tác phải thực hiện trong cùng một transaction.
- Lịch sử phân công được giữ lại để truy vết.

### 5.3. Cập nhật lịch hẹn – UC08

- Chỉ được cập nhật lịch hẹn hợp lệ và còn hiệu lực.
- Giờ kết thúc phải lớn hơn giờ bắt đầu.
- Phải kiểm tra trùng lịch của kỹ thuật viên trước khi lưu.
- Khi cập nhật bị lỗi, dữ liệu lịch hẹn cũ phải được giữ nguyên.

### 5.4. Kiểm tra trùng lịch – UC05

Hai lịch hẹn còn hiệu lực của cùng một kỹ thuật viên không được chồng lấn thời gian.

Điều kiện trùng lịch:

gio_bat_dau_moi < gio_ket_thuc_cu
AND
gio_ket_thuc_moi > gio_bat_dau_cu

Điều kiện được xét cho các lịch cùng ngày, cùng kỹ thuật viên và còn hiệu lực.

## 6. Kết luận

Mô hình ERD gồm 5 bảng và 4 quan hệ một-nhiều, đáp ứng các nhu cầu lưu trữ chính của luồng SmartCRM L04.

Thiết kế tách riêng khách hàng, phiếu bảo hành, kỹ thuật viên, phân công và lịch hẹn nhằm giảm trùng lặp dữ liệu, hỗ trợ truy vết lịch sử và hướng đến chuẩn hóa 3NF.

Các ràng buộc nghiệp vụ cần được hiện thực và kiểm thử ở tầng cơ sở dữ liệu và tầng xử lý nghiệp vụ.
