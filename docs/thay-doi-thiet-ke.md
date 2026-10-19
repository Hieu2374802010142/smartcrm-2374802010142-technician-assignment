# NHẬT KÝ THAY ĐỔI THIẾT KẾ – SMARTCRM L04

**Dự án:** SmartCRM – Mekong Mobile  
**Luồng nghiệp vụ:** L04 – Phân công kỹ thuật viên và lịch hẹn  
**Sinh viên:** Nguyễn Ngọc Hiếu  
**MSSV:** 2374802010142  
**Track:** SE – Software Engineering  
**Giai đoạn:** Rà soát Bài tập 1 và chuẩn bị Sprint 1 – Buổi 8

---

## 1. Mục đích

Tài liệu ghi nhận những thay đổi trong quá trình hoàn thiện thiết kế SmartCRM L04 sau khi nhận phản hồi từ giảng viên về Bài tập 1.

Các thay đổi được trình bày theo ba nội dung chính:

- Thay đổi gì?
- Vì sao cần thay đổi?
- Thay đổi ảnh hưởng đến tài liệu hoặc thành phần nào?

Nhật ký giúp theo dõi quá trình cải tiến thiết kế và bảo đảm sự nhất quán giữa yêu cầu, Use Case, kiến trúc, cơ sở dữ liệu và giao diện.

## 2. Tổng hợp phản hồi Bài tập 1

**Kết quả Bài tập 1: 5,5/10.**

Các tiêu chí được đánh giá:

| Tiêu chí | Điểm |
|---|---:|
| Tính đầy đủ | 6,5 |
| Tính kỹ thuật | 4,25 |
| Tính nhất quán | 6,0 |
| Trình bày | 6,5 |

Giảng viên ghi nhận việc xây dựng các yêu cầu chức năng FR01–FR08, khả năng truy vết và thiết kế ERD có lưu lịch sử phân công.

Tuy nhiên, bài làm cần tiếp tục cải thiện về đặc tả Use Case, chú giải sơ đồ, cách diễn giải NFR, phạm vi SRS và sự thống nhất giữa các tài liệu.

## 3. Nhật ký thay đổi thiết kế

### TD-01 – Bổ sung chú giải cho các sơ đồ

**Thay đổi gì?**

Rà soát sơ đồ Use Case, kiến trúc hệ thống và ERD. Bổ sung phần giải thích các ký hiệu, mối quan hệ và thành phần nằm trong hoặc ngoài phạm vi hệ thống.

**Vì sao cần thay đổi?**

Các sơ đồ cần được trình bày rõ ràng để người đọc hiểu đúng ý nghĩa mà không phải suy đoán.

**Ảnh hưởng đến đâu?**

- `use-case-l04.puml`
- `docs/architecture/architecture-l04.puml`
- `docs/database/erd-l04.puml`
- Các hình PNG tương ứng.

**Trạng thái:** Cần kiểm tra và hoàn thiện.

### TD-02 – Chuẩn hóa thuật ngữ và phạm vi SRS

**Thay đổi gì?**

Rà soát các thuật ngữ nghiệp vụ gồm Phiếu bảo hành, Kỹ thuật viên, Phân công, Lịch hẹn và Trùng lịch.

Làm rõ phạm vi không thực hiện (WON'T), bao gồm các chức năng ngoài luồng L04 như tiếp nhận phiếu, quản lý linh kiện, thanh toán và báo cáo tổng hợp.

**Vì sao cần thay đổi?**

Giúp phân biệt phạm vi của luồng L04 với toàn bộ hệ thống SmartCRM, tránh mở rộng chức năng ngoài yêu cầu.

**Ảnh hưởng đến đâu?**

- `srs.md`
- Tài liệu yêu cầu và các Use Case liên quan.

**Trạng thái:** Cần đối chiếu nội dung hiện có.

### TD-03 – Hoàn thiện đặc tả UC03 và cơ sở dữ liệu

**Thay đổi gì?**

Kiểm tra đặc tả UC03 – Phân công kỹ thuật viên, bảo đảm có đầy đủ:

- Tác nhân: Quản lý trung tâm.
- Điều kiện trước: Phiếu bảo hành ở trạng thái Mới.
- Luồng chính: Chọn phiếu, xem kỹ thuật viên, chọn kỹ thuật viên, kiểm tra điều kiện và lưu phân công.
- Luồng ngoại lệ: Phiếu không hợp lệ, kỹ thuật viên không phù hợp hoặc thao tác lưu thất bại.
- Điều kiện sau: Phân công được lưu và phiếu chuyển sang trạng thái Đã phân công.

Bổ sung SQL DDL triển khai cơ sở dữ liệu theo ERD L04.

**Vì sao cần thay đổi?**

Đặc tả chi tiết giúp lập trình viên hiểu rõ cách hệ thống xử lý nghiệp vụ. SQL DDL giúp chuyển thiết kế dữ liệu thành các bảng thực tế.

**Ảnh hưởng đến đâu?**

- `docs/use-cases/UC03-phan-cong-ky-thuat-vien.md`
- `docs/database/erd-l04.puml`
- `docs/database/schema-l04.sql`

**Trạng thái:** Đã bổ sung SQL DDL; cần kiểm tra đặc tả UC03.

### TD-04 – Làm rõ NFR và quyết định kiến trúc

**Thay đổi gì?**

Rà soát các yêu cầu phi chức năng đã xác định:

- NFR01 – Hiệu năng: Hiển thị danh sách phiếu chưa phân công trong tối đa 2 giây với 10.000 phiếu.
- NFR02 – Khả dụng: Người dùng được hướng dẫn cơ bản hoàn thành phân công và đặt lịch trong tối đa 3 phút.
- NFR03 – Bảo mật: Kiểm tra quyền đối với các thao tác phân công và đặt lịch.
- NFR04 – Tin cậy: Sử dụng transaction để tránh dữ liệu phân công hoặc lịch hẹn không đầy đủ.

Đối chiếu các NFR với giải pháp kiến trúc, đồng thời bổ sung giải thích về lựa chọn kỹ thuật và đánh đổi.

**Vì sao cần thay đổi?**

Các yêu cầu phi chức năng phải có tiêu chí đo lường và được liên kết với giải pháp kỹ thuật cụ thể.

**Ảnh hưởng đến đâu?**

- `srs.md`
- `docs/architecture/architecture-explanation.md`
- `docs/architecture/architecture-l04.puml`

**Trạng thái:** Đã xác định NFR; cần kiểm tra phần giải thích và minh chứng.

### TD-05 – Đồng bộ Wireframe với Use Case

**Thay đổi gì?**

Rà soát ba màn hình giao diện:

1. Danh sách phiếu chưa phân công.
2. Phân công kỹ thuật viên.
3. Đặt lịch hẹn.

Đặc biệt, màn hình Đặt lịch hẹn cần thể hiện ngày hẹn, giờ bắt đầu, giờ kết thúc, loại lịch hẹn và thông báo khi xảy ra trùng lịch.

**Vì sao cần thay đổi?**

Giao diện cần thể hiện đầy đủ các thao tác được mô tả trong Use Case để bảo đảm có thể triển khai chức năng.

**Ảnh hưởng đến đâu?**

- `docs/wireframes/wireframe-l04.md`
- UC03, UC04 và UC05.

**Trạng thái:** Đã có ba Wireframe; cần kiểm tra tính nhất quán.

### TD-06 – Kiểm tra truy vết yêu cầu

**Thay đổi gì?**

Rà soát sự liên kết giữa:

**User Story → Functional Requirement → Use Case → Test Case**

Kiểm tra mã định danh, tên chức năng, điều kiện nghiệp vụ và các trường hợp ngoại lệ.

**Vì sao cần thay đổi?**

Giúp phát hiện những yêu cầu chưa có chức năng tương ứng hoặc chưa có trường hợp kiểm thử.

**Ảnh hưởng đến đâu?**

- SRS.
- Bảng truy vết yêu cầu.
- Các file đặc tả UC01–UC08.
- Các Test Case TC01–TC16.

**Trạng thái:** Đã xây dựng cấu trúc truy vết; cần rà soát tính đầy đủ.

### TD-07 – Chuẩn hóa cấu trúc tài liệu và mã nguồn

**Thay đổi gì?**

Sắp xếp tài liệu theo các thư mục riêng cho Use Case, kiến trúc, cơ sở dữ liệu và Wireframe.

Bổ sung README hướng dẫn cài đặt, khởi tạo dữ liệu và chạy Backend.

**Vì sao cần thay đổi?**

Giúp giảng viên dễ tìm kiếm tài liệu, đồng thời hỗ trợ người khác tải mã nguồn về và chạy thử.

**Ảnh hưởng đến đâu?**

- `README.md`
- `docs/use-cases/`
- `docs/architecture/`
- `docs/database/`
- `docs/wireframes/`

**Trạng thái:** Đã cập nhật README và tổ chức thư mục dự án.

### TD-08 – Minh bạch việc sử dụng AI và kiểm chứng

**Thay đổi gì?**

Chuẩn bị nội dung khai báo việc sử dụng công cụ AI trong quá trình hỗ trợ phân tích yêu cầu, xây dựng tài liệu và lập trình.

Việc khai báo cần nêu công cụ sử dụng, mục đích, nội dung được hỗ trợ và cách sinh viên kiểm tra kết quả.

**Vì sao cần thay đổi?**

Bảo đảm tính minh bạch và trách nhiệm của sinh viên đối với tài liệu và mã nguồn được nộp.

**Ảnh hưởng đến đâu?**

- Phụ lục báo cáo.
- Tài liệu khai báo sử dụng AI theo yêu cầu giảng viên.

**Trạng thái:** Cần bổ sung và đối chiếu yêu cầu nộp bài.

## 4. Bảng tổng hợp trạng thái

| Mã | Nội dung | Trạng thái |
|---|---|---|
| TD-01 | Chú giải sơ đồ | Cần hoàn thiện |
| TD-02 | Thuật ngữ và WON'T | Cần kiểm tra |
| TD-03 | UC03 và SQL DDL | Hoàn thành một phần |
| TD-04 | NFR và kiến trúc | Cần kiểm tra |
| TD-05 | Wireframe | Cần kiểm tra |
| TD-06 | Truy vết yêu cầu | Cần kiểm tra |
| TD-07 | Cấu trúc tài liệu | Đã thực hiện |
| TD-08 | Khai báo AI | Cần bổ sung |

## 5. Kết luận

Sau khi nhận phản hồi Bài tập 1, dự án SmartCRM L04 đã xác định tám nhóm thay đổi nhằm cải thiện chất lượng phân tích và thiết kế.

Trong quá trình chuẩn bị Sprint 1, dự án đã bổ sung SQL DDL, tổ chức mã nguồn và cập nhật README. Những nội dung còn lại sẽ được tiếp tục kiểm tra và hoàn thiện để bảo đảm tính thống nhất giữa yêu cầu, thiết kế và triển khai.

Nhật ký này sẽ được cập nhật trạng thái sau khi từng thay đổi được kiểm chứng và hoàn tất.