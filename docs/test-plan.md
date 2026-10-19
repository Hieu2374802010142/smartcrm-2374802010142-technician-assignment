# KẾ HOẠCH KIỂM THỬ – SMARTCRM L04

**Dự án:** SmartCRM – Mekong Mobile  
**Luồng:** L04 – Phân công kỹ thuật viên và lịch hẹn  
**Sinh viên:** Nguyễn Ngọc Hiếu  
**MSSV:** 2374802010142  
**Track:** SE – Software Engineering  
**Giai đoạn:** Sprint 1 – Buổi 8

---

## 1. Mục đích

Tài liệu mô tả kế hoạch kiểm thử Backend SmartCRM L04 nhằm xác minh các chức năng đã triển khai hoạt động đúng yêu cầu.

Trong Sprint 1, phạm vi kiểm thử tập trung vào CRUD kỹ thuật viên thông qua FastAPI và SQLite.

## 2. Phạm vi kiểm thử

### 2.1. Chức năng được kiểm thử

- GET danh sách kỹ thuật viên.
- POST thêm kỹ thuật viên.
- PUT cập nhật thông tin kỹ thuật viên.
- DELETE ngừng hoạt động kỹ thuật viên (xóa mềm).
- Kiểm tra kết nối cơ sở dữ liệu.
- Kiểm tra chương trình khởi tạo dữ liệu mẫu.

### 2.2. Ngoài phạm vi Sprint 1

Các chức năng sau thuộc thiết kế L04 nhưng chưa triển khai đầy đủ:

- Phân công kỹ thuật viên cho phiếu bảo hành.
- Đặt lịch hẹn giao – nhận thiết bị.
- Kiểm tra trùng lịch.
- Hủy phân công.
- Cập nhật lịch hẹn.

Những chức năng này sẽ được kiểm thử trong các Sprint tiếp theo.

## 3. Môi trường kiểm thử

| Thành phần | Công nghệ |
|---|---|
| Ngôn ngữ | Python 3.12 |
| Backend | FastAPI |
| Database | SQLite |
| Công cụ kiểm thử thủ công | Swagger UI |
| Hệ điều hành | macOS |
| API Base URL | http://127.0.0.1:8000 |

## 4. Phương pháp kiểm thử

Áp dụng kiểm thử hộp đen (Black-box Testing) thông qua API.

Các nhóm trường hợp kiểm thử:

- **Positive Testing:** Dữ liệu hợp lệ, thao tác thành công.
- **Negative Testing:** Dữ liệu không hợp lệ hoặc tài nguyên không tồn tại.
- **Boundary Testing:** Kiểm tra giá trị biên của các trường dữ liệu theo ràng buộc thực tế.
- **Database Verification:** Kiểm tra dữ liệu sau khi thực hiện thao tác.
- **Regression Testing:** Kiểm tra lại các API sau khi thay đổi mã nguồn.

## 5. Danh sách Test Case

| Mã TC | Chức năng | Dữ liệu hoặc tình huống | Kết quả mong đợi |
|---|---|---|---|
| TC-S1-01 | GET kỹ thuật viên | Gửi GET `/api/technicians` | HTTP 200, trả về danh sách |
| TC-S1-02 | POST kỹ thuật viên | Gửi dữ liệu hợp lệ | HTTP 201, thêm thành công |
| TC-S1-03 | PUT kỹ thuật viên | Cập nhật ID tồn tại | HTTP 200, dữ liệu được cập nhật |
| TC-S1-04 | DELETE kỹ thuật viên | Ngừng hoạt động ID tồn tại | HTTP 200, trạng thái hoạt động thay đổi |
| TC-S1-05 | POST dữ liệu thiếu | Thiếu trường bắt buộc | Trả về lỗi xác thực dữ liệu |
| TC-S1-06 | PUT ID không tồn tại | Sử dụng ID không có trong database | Trả về lỗi phù hợp, không cập nhật dữ liệu |
| TC-S1-07 | DELETE ID không tồn tại | Sử dụng ID không có trong database | Trả về lỗi phù hợp, không thay đổi dữ liệu |
| TC-S1-08 | Seed database | Chạy trên database mới | Tạo 5 bảng và thêm 3 kỹ thuật viên mẫu |
| TC-S1-09 | Seed chạy lại | Chạy seed trên database đã có dữ liệu | Không thêm trùng dữ liệu mẫu |
| TC-S1-10 | Kiểm tra database | Gửi GET `/db-test` | Kết nối SQLite thành công |

**Lưu ý:** TC-S1-05 đến TC-S1-07 là các trường hợp dự kiến cần thực thi và xác nhận mã lỗi thực tế. Chưa kết luận Pass nếu chưa kiểm thử.

## 6. Tiêu chí đánh giá

Một Test Case được đánh giá:

- **PASS:** Kết quả thực tế phù hợp kết quả mong đợi.
- **FAIL:** Kết quả thực tế không phù hợp kết quả mong đợi.
- **BLOCKED:** Không thể thực hiện do thiếu dữ liệu hoặc môi trường.
- **NOT RUN:** Chưa thực hiện.

Điều kiện hoàn thành kế hoạch kiểm thử Sprint 1:

- Thực thi các Test Case thuộc phạm vi đã triển khai.
- Ghi nhận kết quả thực tế và trạng thái từng Test Case.
- Lưu minh chứng kiểm thử.
- Ghi nhận lỗi phát hiện được để theo dõi xử lý.

## 7. Minh chứng kiểm thử hiện có

Các ảnh Swagger đã lưu tại `docs/api-tests/`:

- `get-technicians.png`
- `post-technician.png`
- `put-technician.png`
- `delete-technician.png`

Các minh chứng này phục vụ xác nhận bốn thao tác CRUD đã được kiểm thử thủ công.

## 8. Rủi ro kiểm thử

| Rủi ro | Biện pháp |
|---|---|
| Database chứa dữ liệu từ lần kiểm thử trước | Sử dụng dữ liệu kiểm thử riêng |
| Trùng mã kỹ thuật viên | Kiểm tra dữ liệu trước khi thêm |
| Thao tác xóa mềm ảnh hưởng kết quả GET | Kiểm tra trạng thái hoạt động sau DELETE |
| API thay đổi trong quá trình phát triển | Thực hiện kiểm thử hồi quy |
| Thiếu minh chứng cho trường hợp lỗi | Bổ sung kiểm thử âm và lưu kết quả |

## 9. Kết luận

Kế hoạch kiểm thử Sprint 1 tập trung xác minh chức năng CRUD kỹ thuật viên, kết nối SQLite và khởi tạo dữ liệu mẫu.

Bốn thao tác CRUD đã có minh chứng kiểm thử Swagger. Các trường hợp kiểm thử âm, giá trị biên và kiểm thử hồi quy sẽ được tiếp tục thực hiện, ghi nhận trong `test-report.md`.

Kế hoạch này là cơ sở để theo dõi chất lượng Backend và mở rộng kiểm thử các chức năng phân công kỹ thuật viên, lịch hẹn trong những Sprint tiếp theo.