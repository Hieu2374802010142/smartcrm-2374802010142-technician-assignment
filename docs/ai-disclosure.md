# KHAI BÁO SỬ DỤNG AI – SMARTCRM L04 (BT2)

**Sinh viên:** Nguyễn Ngọc Hiếu
**MSSV:** 2374802010142
**Dự án:** SmartCRM – L04: Phân công kỹ thuật viên và lịch hẹn
**Ngày khai báo:** 30/10/2026

## 1. Công cụ AI sử dụng

Trong quá trình thực hiện Bài tập 2, sinh viên có sử dụng ChatGPT của OpenAI làm công cụ hỗ trợ học tập, lập trình, kiểm thử và soạn thảo tài liệu.

## 2. Phạm vi sử dụng AI

| Nội dung | Hình thức hỗ trợ |
|---|---|
| Kiến trúc phần mềm | Gợi ý tổ chức mã nguồn theo Routes, Services và Repositories |
| Backend FastAPI | Hỗ trợ viết, giải thích và điều chỉnh mã nguồn |
| CRUD | Hỗ trợ xây dựng và kiểm tra các chức năng quản lý dữ liệu |
| SQLite | Hướng dẫn Migration và Seed dữ liệu mẫu |
| Kiểm thử | Hỗ trợ xây dựng và sửa các bài kiểm thử bằng pytest |
| Git và GitHub | Hướng dẫn kiểm tra thay đổi, commit, push và tạo tag |
| Clean Clone | Hướng dẫn cài đặt và chạy dự án trên bản clone độc lập |
| Tài liệu | Hỗ trợ soạn báo cáo thay đổi thiết kế và nhật ký lỗi |

## 3. Cách kiểm chứng kết quả AI

Các nội dung do AI đề xuất được kiểm tra bằng cách:

1. Xem xét mã nguồn trong Visual Studio Code.
2. Chạy chương trình trên môi trường Python và FastAPI.
3. Thực hiện Migration và Seed trên database SQLite.
4. Chạy kiểm thử tự động bằng pytest.
5. Thử đăng nhập và thao tác trên giao diện SmartCRM.
6. Kiểm tra trạng thái Git và kết quả push lên GitHub.

Kết quả xác minh đã ghi nhận:

- 27/27 bài kiểm thử PASS.
- Migration tạo thành công năm bảng.
- Seed chạy hai lần mà không tạo thêm dữ liệu mẫu trùng lặp.
- Clean Clone chạy thành công trên cổng 8001.
- Đăng nhập, phân công kỹ thuật viên và đặt lịch hẹn thành công.
- Mã nguồn được lưu tại commit `f54f007`, tag `v0.2`.

## 4. Trách nhiệm của sinh viên

AI được sử dụng như công cụ hỗ trợ, không thay thế hoàn toàn việc thực hiện và kiểm chứng bài tập.

Sinh viên chịu trách nhiệm đối với mã nguồn, kết quả kiểm thử, tài liệu và nội dung trình bày trong báo cáo.

Các thông tin nhạy cảm như mật khẩu quản lý, file `.env` và database cục bộ không được đưa lên GitHub.

## 5. Giới hạn của việc sử dụng AI

Nội dung AI đề xuất có thể chưa chính xác hoặc chưa phù hợp hoàn toàn với yêu cầu giảng viên. Vì vậy, cần đối chiếu với mã nguồn thực tế, kết quả kiểm thử và tài liệu yêu cầu trước khi sử dụng.

Việc 27 bài kiểm thử PASS không đồng nghĩa hệ thống đã được kiểm chứng đầy đủ về bảo mật, hiệu năng và khả năng vận hành thực tế.

## 6. Kết luận

ChatGPT đã được sử dụng để hỗ trợ quá trình phát triển SmartCRM L04 BT2, đặc biệt trong việc tổ chức kiến trúc, lập trình, kiểm thử và chuẩn bị tài liệu.

Các kết quả kỹ thuật được trình bày dựa trên những thao tác và kiểm thử đã thực hiện trên dự án.
