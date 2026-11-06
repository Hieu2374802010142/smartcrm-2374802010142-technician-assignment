# TEST REPORT – SMARTCRM L04

**Chức năng:** Phân công kỹ thuật viên và lịch hẹn  
**Giai đoạn:** Buổi 14 – Kiểm thử hệ thống  
**Công cụ:** Python 3.12.0, pytest 9.1.1, SQLite  
**Ngày thực hiện:** 06/11/2026

## 1. Kết quả kiểm thử tổng quan

- Tổng số bài kiểm thử tự động: 29
- PASS: 29
- FAIL: 0
- Thời gian thực thi toàn bộ: 0.27 giây
- Boundary Test bổ sung: 2/2 PASS

## 2. Test Case – Boundary Testing

| ID | Điều kiện trước | Các bước thực hiện | Dữ liệu kiểm thử | Kết quả mong đợi | Mức ưu tiên | Kết quả thực tế | Trạng thái |
|---|---|---|---|---|---|---|---|
| TC-B01 | Có phân công đang hoạt động và lịch 09:00–10:00 | Chạy `test_appointment_adjacent_boundary` | Ngày 10/11/2026, lịch mới 10:00–11:00 | Tạo lịch thành công, trả về SUCCESS | High | Repository trả về SUCCESS; pytest PASSED | PASS |
| TC-B02 | Có phân công đang hoạt động và lịch 09:00–10:00 | Chạy `test_appointment_overlap_one_minute` | Ngày 10/11/2026, lịch mới 09:59–11:00 | Từ chối lịch trùng, trả về APPOINTMENT_OVERLAP | High | Repository trả về APPOINTMENT_OVERLAP; pytest PASSED | PASS |

## 3. Minh chứng kiểm thử

**TC-B01 và TC-B02:** [Ảnh kết quả Boundary Test](screenshots/TC-B01-TC-B02-boundary.png)

Lệnh thực thi:

`python3 -m pytest tests/test_appointment_boundary.py -v`

Kết quả: **2 passed in 0.03s**

## 4. Nhận xét

Hai trường hợp kiểm thử giá trị biên đều đạt yêu cầu. Hệ thống cho phép đặt lịch mới ngay khi lịch cũ kết thúc và từ chối lịch có thời gian chồng lấn một phút.

Các kiểm thử được thực hiện trên cơ sở dữ liệu SQLite tạm, không làm thay đổi dữ liệu vận hành của SmartCRM.

**Kết luận:** Các trường hợp Boundary Test đã kiểm tra đều PASS. Cần tiếp tục hoàn thiện các nhóm kiểm thử khác để đáp ứng đầy đủ Test Report của BT3.