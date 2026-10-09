# SRS RÚT GỌN – L04: PHÂN CÔNG KỸ THUẬT VIÊN VÀ LỊCH HẸN

**Học phần:** Chuyên đề tốt nghiệp 1
**Case Study:** Smart CRM – Mekong Mobile
**Luồng nghiệp vụ:** L04 – Phân công kỹ thuật viên và lịch hẹn
**Track:** SE
**Sinh viên:** Nguyễn Ngọc Hiếu
**MSSV:** 2374802010142

---

# 1. GIỚI THIỆU VÀ PHẠM VI

## 1.1. Bối cảnh

Mekong Mobile cần quản lý việc phân công kỹ thuật viên và sắp xếp lịch hẹn cho các phiếu bảo hành. Trong phạm vi luồng L04, Quản lý trung tâm cần xem các phiếu bảo hành chưa được phân công, xem thông tin và lịch làm việc của kỹ thuật viên, thực hiện phân công, đặt lịch hẹn và kiểm tra trùng lịch. Sau khi được phân công, Kỹ thuật viên có thể xem các công việc được giao.

Luồng nghiệp vụ được giới hạn ở việc **phân công kỹ thuật viên và quản lý lịch hẹn**, không đặc tả toàn bộ quy trình bảo hành của Mekong Mobile.

## 1.2. Phạm vi thực hiện

Luồng L04 bao gồm:

1. Xem phiếu bảo hành chưa phân công.
2. Xem thông tin và lịch làm việc của kỹ thuật viên.
3. Phân công kỹ thuật viên cho phiếu bảo hành.
4. Đặt lịch hẹn giao hoặc nhận máy.
5. Kiểm tra trùng lịch trước khi lưu lịch hẹn.
6. Kỹ thuật viên xem các công việc được phân công.

7. Hủy phân công kỹ thuật viên.

8. Cập nhật lịch hẹn.

## 1.3. Nội dung chủ ý không thực hiện – WON'T

Các nội dung sau **không thuộc phạm vi của L04**:

* Tiếp nhận và tạo mới phiếu bảo hành.
* Quản lý thông tin khách hàng.
* Phân loại lỗi hoặc chẩn đoán lỗi thiết bị.
* Quản lý linh kiện và tồn kho.
* Thực hiện sửa chữa thiết bị.
* Thanh toán chi phí sửa chữa.
* Báo cáo thống kê tổng thể của trung tâm.
* Gửi thông báo SMS hoặc email cho khách hàng.
* Quản lý toàn bộ hệ thống nhân sự và chấm công.

Các nội dung trên có thể được xem xét ở các luồng hoặc phiên bản khác.

## 1.4. Bảng thuật ngữ

| Thuật ngữ         | Định nghĩa                                                             |
| ----------------- | ---------------------------------------------------------------------- |
| Phiếu bảo hành    | Bản ghi yêu cầu bảo hành của khách hàng cần được xử lý                 |
| Kỹ thuật viên     | Nhân viên thực hiện công việc bảo hành được phân công                  |
| Quản lý trung tâm | Người quản lý việc phân công kỹ thuật viên và lịch hẹn                 |
| Phân công         | Việc gán một kỹ thuật viên cho một phiếu bảo hành                      |
| Lịch hẹn          | Thông tin về thời gian giao hoặc nhận máy liên quan đến phiếu bảo hành |
| Trùng lịch        | Trường hợp một kỹ thuật viên có hai lịch bị chồng lấn về thời gian     |
| Công việc         | Phiếu bảo hành đã được phân công cho một kỹ thuật viên                 |
| Trạng thái phiếu  | Trạng thái xử lý của phiếu bảo hành trong quy trình                    |

Trong toàn bộ tài liệu, các thuật ngữ trên được sử dụng thống nhất.

---

# 2. CÁC BÊN LIÊN QUAN VÀ VAI TRÒ NGƯỜI DÙNG

## 2.1. Các vai trò

| Vai trò           | Trách nhiệm trong phạm vi L04                                                                                       | Không thực hiện trong phạm vi L04                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Quản lý trung tâm | Xem phiếu chưa phân công, xem thông tin kỹ thuật viên, phân công kỹ thuật viên, đặt lịch hẹn và kiểm tra trùng lịch | Không thực hiện sửa chữa hoặc quản lý toàn bộ thông tin bảo hành                        |
| Kỹ thuật viên     | Xem các phiếu và lịch hẹn được phân công cho mình                                                                   | Không tự phân công phiếu cho bản thân hoặc kỹ thuật viên khác; không thay đổi phân công |

## 2.2. Actor chính

**Quản lý trung tâm** là actor chính của luồng L04 vì thực hiện các thao tác từ xem phiếu đến phân công và đặt lịch.

**Kỹ thuật viên** là actor sử dụng hệ thống để xem các công việc đã được phân công.


# 3. YÊU CẦU CHỨC NĂNG

## 3.1. Danh sách yêu cầu chức năng

### FR01 – Xem phiếu chưa phân công

Hệ thống phải cho phép Quản lý trung tâm xem danh sách các phiếu bảo hành đang ở trạng thái **Mới** và chưa được phân công kỹ thuật viên.

### FR02 – Xem thông tin kỹ thuật viên

Hệ thống phải cho phép Quản lý trung tâm xem thông tin và lịch làm việc của kỹ thuật viên trước khi thực hiện phân công.

### FR03 – Phân công kỹ thuật viên

Hệ thống phải cho phép Quản lý trung tâm chọn một kỹ thuật viên và phân công kỹ thuật viên đó cho một phiếu bảo hành chưa được phân công.

Sau khi phân công thành công, trạng thái phiếu phải được cập nhật từ **Mới** sang **Đã phân công**.

### FR04 – Đặt lịch hẹn

Hệ thống phải cho phép Quản lý trung tâm tạo lịch hẹn cho phiếu bảo hành với các thông tin cần thiết gồm ngày, thời gian và loại lịch hẹn.

### FR05 – Kiểm tra trùng lịch

Hệ thống phải kiểm tra lịch làm việc của kỹ thuật viên trước khi lưu lịch hẹn.

Nếu thời gian mới bị trùng với lịch hiện có của cùng kỹ thuật viên, hệ thống phải từ chối lưu lịch hẹn và thông báo cho Quản lý trung tâm.

### FR06 – Kỹ thuật viên xem công việc

Hệ thống phải cho phép Kỹ thuật viên xem danh sách các phiếu bảo hành và lịch hẹn được phân công cho chính mình.

### FR07 – Hủy phân công kỹ thuật viên

Hệ thống phải cho phép Quản lý trung tâm hủy phân công kỹ thuật viên đối với phiếu bảo hành chưa hoàn tất.

Sau khi hủy phân công thành công, kỹ thuật viên được gán cho phiếu phải được xóa và trạng thái phiếu được cập nhật về **Mới** để có thể phân công lại.

### FR08 – Cập nhật lịch hẹn

Hệ thống phải cho phép Quản lý trung tâm cập nhật ngày, thời gian và loại lịch hẹn của một phiếu bảo hành đã có lịch hẹn.

Trước khi lưu thông tin mới, hệ thống phải kiểm tra trùng lịch của kỹ thuật viên.

---

## 3.2. User Story và mức ưu tiên MoSCoW

### US01 – Xem phiếu chưa phân công

**Là Quản lý trung tâm, tôi muốn xem danh sách các phiếu bảo hành chưa được phân công để biết những phiếu cần được xử lý.**

**MoSCoW: MUST**

### US02 – Xem thông tin kỹ thuật viên

**Là Quản lý trung tâm, tôi muốn xem thông tin và lịch làm việc của kỹ thuật viên để lựa chọn kỹ thuật viên phù hợp cho phiếu bảo hành.**

**MoSCoW: MUST**

### US03 – Phân công kỹ thuật viên

**Là Quản lý trung tâm, tôi muốn phân công một kỹ thuật viên cho phiếu bảo hành để xác định người chịu trách nhiệm xử lý phiếu.**

**MoSCoW: MUST**

### US04 – Đặt lịch hẹn

**Là Quản lý trung tâm, tôi muốn đặt lịch hẹn cho phiếu bảo hành để xác định thời gian giao hoặc nhận máy của khách hàng.**

**MoSCoW: MUST**

### US05 – Kiểm tra trùng lịch

**Là Quản lý trung tâm, tôi muốn hệ thống kiểm tra trùng lịch của kỹ thuật viên trước khi lưu lịch hẹn để tránh đặt hai lịch bị trùng thời gian cho cùng một kỹ thuật viên.**

**MoSCoW: MUST**

### US06 – Kỹ thuật viên xem công việc

**Là Kỹ thuật viên, tôi muốn xem các phiếu bảo hành và lịch hẹn được phân công cho mình để biết những công việc cần thực hiện.**

**MoSCoW: SHOULD**

### US07 – Hủy phân công kỹ thuật viên

**Là Quản lý trung tâm, tôi muốn hủy phân công kỹ thuật viên đối với phiếu chưa hoàn tất để có thể phân công lại khi cần thiết.**

**MoSCoW: SHOULD**

### US08 – Cập nhật lịch hẹn

**Là Quản lý trung tâm, tôi muốn cập nhật ngày, thời gian và loại lịch hẹn để điều chỉnh lịch giao hoặc nhận máy khi có thay đổi.**

**MoSCoW: SHOULD**

---

## 3.3. Tiêu chí chấp nhận

### US01 – Xem phiếu chưa phân công

**AC01**

* **Given:** Có phiếu bảo hành đang ở trạng thái Mới và chưa được phân công.
* **When:** Quản lý trung tâm mở chức năng xem phiếu chưa phân công.
* **Then:** Hệ thống hiển thị danh sách các phiếu phù hợp.

**AC02**

* **Given:** Không có phiếu nào chưa được phân công.
* **When:** Quản lý trung tâm mở danh sách.
* **Then:** Hệ thống thông báo không có phiếu chưa phân công.

### US02 – Xem thông tin kỹ thuật viên

**AC01**

* **Given:** Có kỹ thuật viên đang hoạt động.
* **When:** Quản lý trung tâm mở danh sách kỹ thuật viên.
* **Then:** Hệ thống hiển thị thông tin của các kỹ thuật viên.

**AC02**

* **Given:** Kỹ thuật viên có các lịch làm việc đã được ghi nhận.
* **When:** Quản lý trung tâm xem thông tin kỹ thuật viên.
* **Then:** Hệ thống hiển thị các lịch liên quan để hỗ trợ việc phân công.

### US03 – Phân công kỹ thuật viên

**AC01**

* **Given:** Phiếu đang ở trạng thái Mới và chưa được phân công.
* **When:** Quản lý trung tâm chọn kỹ thuật viên và xác nhận phân công.
* **Then:** Hệ thống lưu thông tin phân công và chuyển trạng thái phiếu thành Đã phân công.

**AC02**

* **Given:** Quản lý trung tâm chưa chọn kỹ thuật viên.
* **When:** Quản lý xác nhận phân công.
* **Then:** Hệ thống không lưu và yêu cầu chọn kỹ thuật viên.

### US04 – Đặt lịch hẹn

**AC01**

* **Given:** Phiếu bảo hành đã được phân công kỹ thuật viên.
* **When:** Quản lý trung tâm nhập đầy đủ thông tin ngày, thời gian và loại lịch hẹn.
* **Then:** Hệ thống kiểm tra điều kiện lịch và cho phép lưu nếu không có trùng lịch.

**AC02**

* **Given:** Ngày hoặc thời gian lịch hẹn chưa được nhập.
* **When:** Quản lý trung tâm thực hiện lưu lịch.
* **Then:** Hệ thống không lưu và yêu cầu bổ sung thông tin còn thiếu.

### US05 – Kiểm tra trùng lịch

**AC01**

* **Given:** Kỹ thuật viên đã có lịch hẹn bị chồng lấn với thời gian mới.
* **When:** Quản lý trung tâm thực hiện lưu lịch hẹn mới.
* **Then:** Hệ thống thông báo trùng lịch và không lưu lịch mới.

**AC02**

* **Given:** Kỹ thuật viên không có lịch bị chồng lấn.
* **When:** Quản lý trung tâm xác nhận lịch hẹn.
* **Then:** Hệ thống cho phép lưu lịch hẹn.

### US06 – Kỹ thuật viên xem công việc

**AC01**

* **Given:** Kỹ thuật viên đã được phân công ít nhất một phiếu.
* **When:** Kỹ thuật viên mở danh sách công việc.
* **Then:** Hệ thống hiển thị các phiếu được phân công cho kỹ thuật viên đó.

**AC02**

* **Given:** Kỹ thuật viên chưa được phân công phiếu nào.
* **When:** Kỹ thuật viên mở danh sách công việc.
* **Then:** Hệ thống thông báo chưa có công việc được phân công.

### US07 – Hủy phân công kỹ thuật viên

**AC01**

* **Given:** Phiếu bảo hành đã được phân công và chưa hoàn tất.
* **When:** Quản lý trung tâm chọn chức năng hủy phân công và xác nhận.
* **Then:** Hệ thống hủy phân công, xóa kỹ thuật viên được gán và chuyển trạng thái phiếu về Mới.

**AC02**

* **Given:** Phiếu bảo hành đã hoàn tất.
* **When:** Quản lý trung tâm thực hiện hủy phân công.
* **Then:** Hệ thống không cho phép hủy và thông báo phiếu đã hoàn tất.

### US08 – Cập nhật lịch hẹn

**AC01**

* **Given:** Phiếu bảo hành đã có lịch hẹn.
* **When:** Quản lý trung tâm thay đổi ngày, thời gian hoặc loại lịch hẹn và xác nhận cập nhật.
* **Then:** Hệ thống kiểm tra trùng lịch và cập nhật lịch hẹn nếu hợp lệ.

**AC02**

* **Given:** Thời gian mới bị trùng với lịch hiện có của kỹ thuật viên.
* **When:** Quản lý trung tâm xác nhận cập nhật lịch.
* **Then:** Hệ thống thông báo trùng lịch và không lưu thông tin mới.

---

---

# 4. YÊU CẦU PHI CHỨC NĂNG

| Mã    | Loại      | Yêu cầu                                                                                                                                                                                    |
| ----- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| NFR01 | Hiệu năng | Danh sách phiếu chưa phân công phải hiển thị trong **không quá 2 giây** với dữ liệu tối đa **10.000 phiếu** trong điều kiện kiểm thử được xác định trước.                                  |
| NFR02 | Khả dụng  | Người dùng đã được hướng dẫn cơ bản phải hoàn thành thao tác phân công kỹ thuật viên và đặt lịch hẹn cho một phiếu trong **không quá 3 phút**.                                             |
| NFR03 | Bảo mật   | **100%** các yêu cầu thực hiện phân công kỹ thuật viên và đặt lịch hẹn phải được kiểm tra quyền truy cập; chỉ tài khoản có vai trò Quản lý trung tâm được phép thực hiện các thao tác này. |
| NFR04 | Tin cậy   | Khi lưu phân công hoặc lịch hẹn, hệ thống phải hoàn tất thao tác theo một giao dịch; trong **100% trường hợp lỗi khi lưu**, không được tạo bản ghi phân công hoặc lịch hẹn không đầy đủ.   |

Các NFR trên được sử dụng làm cơ sở cho việc lựa chọn kiến trúc ở phần thiết kế. Các ngưỡng có thể được điều chỉnh nếu giảng viên yêu cầu theo dữ liệu hoặc môi trường kiểm thử cụ thể.

---

---

# 5. RÀNG BUỘC VÀ QUY TẮC NGHIỆP VỤ

### BR01 – Trạng thái phiếu

Chỉ phiếu bảo hành đang ở trạng thái **Mới** và chưa có kỹ thuật viên được phân công mới được thực hiện phân công trong phạm vi L04.

### BR02 – Một kỹ thuật viên cho một phiếu

Tại một thời điểm, mỗi phiếu bảo hành chỉ được gán cho **một kỹ thuật viên**.

### BR03 – Cập nhật trạng thái sau phân công

Khi phân công kỹ thuật viên thành công, trạng thái phiếu được chuyển từ:

**Mới → Đã phân công**

### BR04 – Kiểm tra trùng lịch

Hệ thống phải kiểm tra lịch hiện có của kỹ thuật viên trước khi lưu lịch hẹn mới.

### BR05 – Không lưu lịch bị trùng

Nếu lịch hẹn mới bị chồng lấn với lịch đã tồn tại của cùng kỹ thuật viên, hệ thống không được lưu lịch hẹn mới.

### BR06 – Quyền thực hiện phân công

Chỉ **Quản lý trung tâm** được thực hiện thao tác phân công kỹ thuật viên và đặt lịch hẹn trong phạm vi L04.

### BR07 – Phạm vi xem công việc của kỹ thuật viên

Kỹ thuật viên chỉ được xem các công việc và lịch hẹn được phân công cho chính mình.

---

### BR08 – Hủy phân công kỹ thuật viên

Quản lý trung tâm được hủy phân công đối với phiếu chưa hoàn tất.

Khi hủy phân công:
- Chuyển trạng thái phân công thành Đã hủy.
- Phiếu không còn kỹ thuật viên đang được gán.
- Chuyển trạng thái phiếu về Mới.
- Hủy các lịch hẹn còn hiệu lực liên quan.
- Lưu các thay đổi trong cùng một transaction.

### BR09 – Cập nhật lịch hẹn

Chỉ Quản lý trung tâm được cập nhật lịch hẹn.
Hệ thống kiểm tra trùng lịch trước khi lưu.
Nếu lịch mới bị trùng, hệ thống từ chối cập nhật
và giữ nguyên dữ liệu cũ.


---

# 6. BẢNG TRUY VẾT YÊU CẦU

| Mã FR | Yêu cầu chức năng                                                        | User Story | Use Case                           | MoSCoW | Test Case  |
| ----- | ------------------------------------------------------------------------ | ---------- | ---------------------------------- | ------ | ---------- |
| FR01  | Xem danh sách phiếu bảo hành chưa được phân công                         | US01       | UC01 – Xem phiếu chưa phân công    | MUST   | TC01, TC02 |
| FR02  | Xem thông tin và lịch làm việc của kỹ thuật viên                         | US02       | UC02 – Xem thông tin kỹ thuật viên | MUST   | TC03, TC04 |
| FR03  | Phân công kỹ thuật viên cho phiếu và cập nhật trạng thái                 | US03       | UC03 – Phân công kỹ thuật viên     | MUST   | TC05, TC06 |
| FR04  | Tạo lịch hẹn với ngày, thời gian và loại lịch hẹn                        | US04       | UC04 – Đặt lịch hẹn                | MUST   | TC07, TC08 |
| FR05  | Kiểm tra trùng lịch trước khi lưu lịch hẹn                               | US05       | UC05 – Kiểm tra trùng lịch         | MUST   | TC09, TC10 |
| FR06  | Cho phép kỹ thuật viên xem các công việc được phân công                  | US06       | UC06 – Xem công việc               | SHOULD | TC11, TC12 |
| FR07  | Cho phép quản lý hủy phân công kỹ thuật viên đối với phiếu chưa hoàn tất | US07       | UC07 – Hủy phân công kỹ thuật viên | SHOULD | TC13, TC14 |
| FR08  | Cho phép quản lý cập nhật ngày, thời gian và loại lịch hẹn               | US08       | UC08 – Cập nhật lịch hẹn           | SHOULD | TC15, TC16 |

## 6.1. Kiểm tra truy vết

* FR01 → US01 → UC01 → TC01, TC02
* FR02 → US02 → UC02 → TC03, TC04
* FR03 → US03 → UC03 → TC05, TC06
* FR04 → US04 → UC04 → TC07, TC08
* FR05 → US05 → UC05 → TC09, TC10
* FR06 → US06 → UC06 → TC11, TC12
* FR07 → US07 → UC07 → TC13, TC14
* FR08 → US08 → UC08 → TC15, TC16

Mỗi yêu cầu chức năng đều có User Story, Use Case và các Test Case tương ứng. Các yêu cầu FR07 và FR08 được bổ sung nhằm đặc tả đầy đủ chức năng **hủy phân công** và **cập nhật lịch hẹn** trong phạm vi L04.

---

---

# KẾT LUẬN PHẠM VI

SRS này đặc tả luồng **L04 – Phân công kỹ thuật viên và lịch hẹn** trong Smart CRM – Mekong Mobile.

Phạm vi bao gồm 8 Use Case:

1. **UC01 – Xem phiếu chưa phân công**
2. **UC02 – Xem thông tin kỹ thuật viên**
3. **UC03 – Phân công kỹ thuật viên**
4. **UC04 – Đặt lịch hẹn**
5. **UC05 – Kiểm tra trùng lịch**
6. **UC06 – Xem công việc**
7. **UC07 – Hủy phân công kỹ thuật viên**
8. **UC08 – Cập nhật lịch hẹn**



---
