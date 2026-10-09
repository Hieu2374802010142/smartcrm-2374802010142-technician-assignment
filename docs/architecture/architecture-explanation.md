# GIẢI THÍCH KIẾN TRÚC – SMARTCRM L04

## 1. Kiến trúc hệ thống

Hệ thống SmartCRM L04 sử dụng kiến trúc phân lớp gồm:

- Presentation Layer: Web UI sử dụng HTML/CSS.
- API Layer: FastAPI tiếp nhận và xử lý HTTP/JSON.
- Business Logic Layer: Xử lý phân công kỹ thuật viên, đặt lịch hẹn và kiểm tra trùng lịch.
- Data Access Layer: Thực hiện truy vấn và lưu dữ liệu.
- Database: SQLite lưu trữ thông tin khách hàng, phiếu bảo hành, kỹ thuật viên, phân công và lịch hẹn.

## 2. Giải thích lựa chọn kiến trúc theo NFR

### NFR01 – Hiệu năng

Vì NFR01 yêu cầu danh sách phiếu chưa phân công phản hồi không quá 2 giây với tối đa 10.000 phiếu, hệ thống sử dụng Data Access Layer để tập trung xử lý truy vấn và hỗ trợ phân trang. Đánh đổi là cần tối ưu câu truy vấn và xây dựng chỉ mục khi dữ liệu tăng.

### NFR03 – Bảo mật

Vì NFR03 yêu cầu kiểm tra quyền đối với 100% thao tác phân công và đặt lịch, hệ thống thực hiện xác thực và phân quyền tại API Layer. Đánh đổi là mỗi yêu cầu cần thêm bước kiểm tra quyền, làm tăng thời gian xử lý.

### NFR04 – Tin cậy

Vì NFR04 yêu cầu dữ liệu phân công và lịch hẹn được lưu nhất quán, hệ thống sử dụng transaction khi thực hiện các thao tác ghi dữ liệu. Nếu xảy ra lỗi, transaction được rollback để tránh tạo dữ liệu không đầy đủ. Đánh đổi là việc quản lý giao dịch phức tạp hơn.

## 3. Kết luận

Kiến trúc phân lớp giúp SmartCRM L04 dễ bảo trì, phân chia trách nhiệm rõ ràng và đáp ứng các yêu cầu về hiệu năng, bảo mật và độ tin cậy.

Các cơ chế phân trang, phân quyền và transaction là giải pháp thiết kế cần được hiện thực và kiểm thử để xác nhận đạt các ngưỡng NFR.
