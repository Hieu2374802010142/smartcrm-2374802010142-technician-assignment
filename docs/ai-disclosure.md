# KHAI BÁO SỬ DỤNG AI – SMARTCRM L04 (BT2 & BT3)

**Sinh viên:** Nguyễn Ngọc Hiếu
**MSSV:** 2374802010142
**Dự án:** SmartCRM – L04: Phân công kỹ thuật viên và lịch hẹn
**Ngày cập nhật:** 12/11/2026
**Công cụ AI:** ChatGPT – OpenAI

## 1. Công cụ AI sử dụng

Trong quá trình thực hiện Bài tập 2 và Bài tập 3 của dự án SmartCRM L04, sinh viên có sử dụng ChatGPT của OpenAI để hỗ trợ tìm hiểu kiến thức, lập trình, kiểm thử, phân tích lỗi, triển khai Docker và soạn thảo tài liệu.

AI đóng vai trò công cụ hỗ trợ. Sinh viên thực hiện các thao tác trên môi trường phát triển, kiểm tra kết quả và chịu trách nhiệm về sản phẩm nộp.

## 2. Phạm vi sử dụng AI

| Nội dung | Hình thức hỗ trợ |
|---|---|
| Kiến trúc phần mềm | Gợi ý và giải thích cấu trúc Routes, Services, Repositories |
| Backend FastAPI | Hỗ trợ viết, đọc hiểu, điều chỉnh và rà soát mã nguồn |
| CRUD | Hỗ trợ xây dựng và kiểm tra các chức năng quản lý kỹ thuật viên và phiếu bảo hành |
| SQLite | Hướng dẫn Migration, Seed và kiểm tra truy vấn dữ liệu |
| Kiểm thử | Hỗ trợ thiết kế test case, chạy pytest, phân tích lỗi và kiểm tra hồi quy |
| Bảo mật API | Hỗ trợ phát hiện và khắc phục các endpoint chưa được bảo vệ |
| Docker | Hướng dẫn cấu hình, build, chạy và kiểm tra container |
| Fresh Clone | Hướng dẫn kiểm tra khả năng triển khai từ bản clone độc lập |
| Git và GitHub | Hỗ trợ kiểm tra thay đổi, lịch sử commit, push và release tag |
| Tài liệu BT3 | Hỗ trợ soạn Test Plan, Test Report, Bug Log, Security Checklist, API Documentation và Deployment Guide |

## 3. Cách kiểm chứng kết quả AI

Sinh viên kiểm chứng các đề xuất của AI thông qua những hoạt động sau:

1. Đọc và đối chiếu mã nguồn thực tế trong Visual Studio Code.
2. Chạy chương trình FastAPI và kiểm tra các API.
3. Kiểm tra Migration, Seed và dữ liệu SQLite.
4. Chạy kiểm thử tự động bằng pytest.
5. Kiểm tra đăng nhập và các chức năng trên giao diện SmartCRM.
6. Kiểm tra các API được bảo vệ bằng Bearer token.
7. Build và chạy ứng dụng bằng Docker Compose.
8. Kiểm tra triển khai trên bản Fresh Clone độc lập.
9. Đối chiếu tài liệu với kết quả Terminal, mã nguồn và bằng chứng kiểm thử.
10. Kiểm tra trạng thái Git trước khi commit và push.

Các nội dung chưa được kiểm chứng đầy đủ phải được ghi nhận là giới hạn hoặc công việc cần tiếp tục, không trình bày như kết quả đã hoàn thành.

## 4. Kết quả kiểm chứng Bài tập 2

Trong giai đoạn BT2, các kết quả đã được ghi nhận gồm:

- 27/27 bài kiểm thử PASS.
- Migration tạo thành công năm bảng dữ liệu.
- Seed được kiểm tra để tránh tạo dữ liệu mẫu trùng lặp.
- Clean Clone chạy thành công trên cổng 8001.
- Đăng nhập, phân công kỹ thuật viên và đặt lịch hẹn được kiểm tra.
- Một mốc mã nguồn được ghi nhận tại commit `f54f007`, tag `v0.2`.

Đây là kết quả thuộc giai đoạn BT2, không phải số liệu kiểm thử cuối cùng của BT3.

## 5. Kết quả kiểm chứng Bài tập 3

### 5.1. Kiểm thử tự động

Sinh viên thực hiện kiểm thử bằng lệnh:

`python3 -m pytest -q`

Kết quả đã ghi nhận:

**32 bài kiểm thử PASS, 0 FAIL.**

Kết quả này phản ánh lần chạy kiểm thử đã được quan sát, không đồng nghĩa toàn bộ chức năng và tình huống vận hành đều được kiểm chứng.

### 5.2. Phát hiện và sửa lỗi bảo mật

Trong quá trình BT3, ba lỗi phân quyền truy cập API được ghi nhận và khắc phục:

| Mã lỗi | Nội dung | Commit sửa lỗi |
|---|---|---|
| BUG-01 | API danh sách phân công cho phép truy cập khi chưa xác thực | `c8c966d` |
| BUG-02 | API phiếu bảo hành chưa phân công cho phép truy cập khi chưa xác thực | `b50ce78` |
| BUG-03 | API danh sách kỹ thuật viên cho phép truy cập khi chưa xác thực | `a4651d7` |

Các endpoint liên quan đã được kiểm tra lại và trả về HTTP `401` khi không cung cấp Bearer token hợp lệ.

### 5.3. Kiểm tra Docker

Sinh viên đã thực hiện:

- Build Docker image.
- Khởi động container bằng Docker Compose.
- Kiểm tra trạng thái container.
- Truy cập giao diện `/app`.
- Kiểm tra endpoint `/health`.
- Kiểm tra đăng nhập bằng API.
- Chạy bộ kiểm thử tự động.

Kết quả xác nhận môi trường Docker có thể khởi động và phục vụ các chức năng cơ bản đã kiểm tra.

### 5.4. Kiểm tra Fresh Clone

Một bản clone độc lập được sử dụng để kiểm tra khả năng triển khai.

Thông tin xác minh:

- Release tag: `v1.0.1`.
- Thư mục kiểm tra: `smartcrm-bt3-fresh-clone`.
- Cổng truy cập: `8001`.
- Docker container đạt trạng thái healthy.
- Endpoint `/health` trả HTTP `200`.
- Giao diện `/app` trả HTTP `200`.
- API đăng nhập trả HTTP `200` với thông tin hợp lệ.

Các kết quả này chứng minh những bước kiểm tra triển khai cơ bản đã thành công trong môi trường thử nghiệm.

### 5.5. Rà soát bảo mật

Sinh viên đã rà soát:

- Việc bảo vệ file `.env` và thông tin bí mật.
- Cơ chế xác thực và phân quyền.
- Kiểm tra dữ liệu đầu vào.
- Sử dụng truy vấn SQL có tham số.
- Kiểm tra trùng lịch hẹn.
- Cách xử lý lỗi và thông tin ghi log.
- Các thư viện phụ thuộc.

Kết quả kiểm tra dependency bằng `pip-audit` tại thời điểm thực hiện không phát hiện lỗ hổng đã biết.

Một số nội dung chưa được kiểm chứng đầy đủ, bao gồm kiểm thử đồng thời, kiểm tra toàn diện log nhạy cảm và quét bảo mật Docker image.

### 5.6. Hỗ trợ soạn thảo tài liệu

ChatGPT được sử dụng để hỗ trợ chuẩn bị và rà soát:

- `docs/test-plan-bt3.md`
- `docs/test-report.md`
- `docs/test-report-docker.md`
- `docs/bug-log-bt3.md`
- `docs/checklist-bao-mat.md`
- `docs/api-documentation-bt3.md`
- `docs/deployment-guide.md`
- `docs/ai-disclosure.md`

Các tài liệu được đối chiếu với kết quả kiểm thử và mã nguồn đã kiểm tra. Việc soạn thảo tài liệu bằng AI không thay thế yêu cầu cung cấp bằng chứng thực tế.

## 6. Trách nhiệm của sinh viên

Sinh viên chịu trách nhiệm đối với:

- Tính chính xác của mã nguồn và tài liệu.
- Việc thực hiện và xác minh các bước kiểm thử.
- Kết quả triển khai được trình bày trong báo cáo.
- Các thay đổi được commit và push lên GitHub.
- Việc bảo vệ mật khẩu, token và cấu hình nhạy cảm.
- Việc tuân thủ yêu cầu của giảng viên và quy định học thuật.

Những nội dung AI đề xuất cần được kiểm tra trước khi sử dụng hoặc nộp.

## 7. Giới hạn của việc sử dụng AI

AI có thể đưa ra mã nguồn, hướng dẫn hoặc nhận định chưa chính xác. Vì vậy, sinh viên cần kiểm tra lại bằng mã nguồn thực tế, Terminal, kết quả kiểm thử và tài liệu yêu cầu.

Kết quả 32 bài kiểm thử PASS không chứng minh hệ thống đã được kiểm thử toàn diện về bảo mật, hiệu năng, khả năng chịu tải và vận hành thực tế.

Các nội dung chưa hoàn thành phải được phân biệt rõ với những kết quả đã kiểm chứng.

## 8. Kết luận

ChatGPT được sử dụng làm công cụ hỗ trợ trong quá trình phát triển SmartCRM L04 BT2 và BT3, đặc biệt ở các công việc lập trình, kiểm thử, khắc phục lỗi bảo mật, triển khai Docker và chuẩn bị tài liệu.

Các kết quả kỹ thuật được ghi nhận dựa trên những thao tác và bằng chứng đã thực hiện trong dự án.

Sinh viên chịu trách nhiệm cuối cùng về tính chính xác, trung thực và chất lượng của sản phẩm nộp.

**Người khai báo:** Nguyễn Ngọc Hiếu
**MSSV:** 2374802010142
**Ngày:** 12/11/2026