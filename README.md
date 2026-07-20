# Vinalink Doanh Chủ Portal - Hướng dẫn Triển khai & Tài nguyên

Website Portal này phục vụ việc quản lý tài liệu, khảo sát ý kiến và chạy bộ giả lập dòng tiền tối ưu cho Doanh chủ Vinalink, được thiết kế nâng cấp kế thừa từ template chuyên nghiệp **adminHMD v1.0.0**.

---

## 1. Cấu trúc Triển khai trên Web

Toàn bộ các trang hoạt động tĩnh được chia nhỏ theo mô hình đa trang (Multi-page App):
* [index.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/index.html) - Dashboard tổng quan & Lộ trình 3 năm.
* [documents.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/documents.html) - Thư viện tài liệu nghiên cứu.
* [visualizer.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/visualizer.html) - Bản đồ thấu cảm & Kịch bản F1 Archetypes.
* [simulator.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/simulator.html) - Bộ giả lập cân nhánh và dòng tiền nhị phân Vinalink.
* [feedback.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/feedback.html) - Form khảo sát Doanh chủ 22 trường dữ liệu.
* [settings.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/settings.html) - Cài đặt API kết nối Google Sheets (Dành riêng cho Cố vấn).
* [login.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/login.html) - Xác thực quyền quản trị Cố vấn SIHUB.

---

## 2. Tài nguyên Chưa Sử dụng (Hidden / Unused Assets) từ adminHMD

Theo nguyên tắc tối giản và tập trung nghiệp vụ hiện tại, các trang mẫu và tính năng của `adminhmd-1.0.0` dưới đây đã được **ẩn khỏi thanh điều hướng chính** và chưa được sử dụng đến trong website Vinalink Portal. Chúng được lưu trữ làm tài nguyên dự phòng để mở rộng tính năng quản trị sau này:

### A. Quản lý Nhân sự & Phân quyền
* `html/users.html` - Danh sách nhà quản lý/người dùng hệ thống.
* `html/user-details.html` - Chi tiết thông tin chi tiết của người dùng.
* `html/add-user.html` - Giao diện biểu mẫu thêm mới người dùng.
* `html/create-agent.html` - Giao diện tạo robot/agent quản trị.
* `html/profile.html` - Trang cá nhân của Admin.

### B. Mẫu Tiện ích & UI Elements
* `html/charts.html` - Biểu đồ thống kê mẫu sử dụng Chart.js.
* `html/tables.html` - Các kiểu bảng biểu mẫu (bảng cơ bản, bảng sọc, bảng hover).
* `html/forms.html` - Các phần tử input, select, textarea mẫu.
* `html/components.html` - Các thành phần giao diện mẫu (Buttons, Badges, Accordion, Progress, Pagination).
* `html/alerts.html` - Các loại thông báo nổi, cảnh báo lỗi.
* `html/modals.html` - Giao diện các popup modal hội thoại.
* `html/blank.html` - Trang trống mẫu làm khung phát triển trang mới.

### C. Giao diện Xác thực dự phòng
* `html/forgot-password.html` - Trang khôi phục mật khẩu.
* `html/register.html` - Trang đăng ký tài khoản mới.

### D. Trang Lỗi Hệ thống
* `html/404.html` - Trang thông báo không tìm thấy đường dẫn (Page Not Found).
* `html/500.html` - Trang thông báo lỗi máy chủ nội bộ.

### E. Tài liệu & Mã nguồn Stylesheets gốc
* `documentation/docs.html` - Tài liệu kỹ thuật lập trình gốc của template `adminHMD`.
* `assets/scss/` - Các tệp nguồn SASS phục vụ tùy biến màu sắc và lưới (đã biên dịch tĩnh ra `assets/css/style.css`).

---

## 3. Bảo mật Thông tin Nhạy cảm

Tệp tin phản biện và đối chiếu dữ liệu nhạy cảm **`doi-chieu-bao-cao.md`** chứa thông tin nội bộ của cố vấn. Tệp này đã được đưa vào cấu hình `.gitignore` và **không được đẩy lên hosting tĩnh** dưới bất kỳ hình thức nào để bảo mật tuyệt đối dữ liệu doanh nghiệp và khách hàng.
