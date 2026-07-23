# Vinalink Doanh Chủ Portal - Hướng dẫn Triển khai & Tài nguyên

Website Portal này phục vụ việc quản lý tài liệu, khảo sát ý kiến và chạy bộ giả lập dòng tiền tối ưu cho Doanh chủ Vinalink, được thiết kế nâng cấp kế thừa từ template chuyên nghiệp **adminHMD v1.0.0**.

---

## 1. Cấu trúc Triển khai trên Web

Toàn bộ các trang hoạt động tĩnh được chia nhỏ theo mô hình đa trang (Multi-page App):
* [index.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/index.html) - Dashboard tổng quan & Lộ trình 3 năm.
* [html/documents.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/html/documents.html) - Thư viện tài liệu nghiên cứu và biểu mẫu.
* [html/visualizer.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/html/visualizer.html) - Bản đồ thấu cảm & Kịch bản F1 Archetypes.
* [html/simulator.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/html/simulator.html) - Bộ giả lập 7 nguồn thu nhập và dòng tiền 36 tháng.
* [html/feedback.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/html/feedback.html) - Form khảo sát Doanh chủ 22 trường dữ liệu.
* [html/settings.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/html/settings.html) - Cài đặt API kết nối Google Sheets (Dành riêng cho Cố vấn).
* [html/login.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/html/login.html) - Xác thực quyền quản trị Cố vấn Lean Startup.

---

## 2. Thư viện Tài liệu Chuẩn hóa (Consolidated Master Docs)

Toàn bộ tài liệu phân tích, khảo sát và đặc tả thuật toán được lưu trữ tập trung tại thư mục [docs/](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/docs/) gồm 4 tệp Master duy nhất:

1. **[01-master-business-policy.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/docs/01-master-business-policy.md)**
   * Hợp nhất trọn vẹn chính sách trả thưởng 7 nguồn thu nhập Vinalink Group, nghiên cứu công ty mẹ và chuẩn mực vận hành "Một Nghĩa".
2. **[02-doanh-chu-audit-report.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/docs/02-doanh-chu-audit-report.md)**
   * Hợp nhất bộ checklist khảo sát tầm nhìn/năng lực doanh chủ (MILP inputs) và bản đồ 3 thị trường khách hàng mục tiêu downline.
3. **[03-vinalink-simulator-fsd.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/docs/03-vinalink-simulator-fsd.md)**
   * Tài liệu Đặc tả Chức năng FSD cho bộ mô phỏng (flowchart, DFD Level 1, 6 spec chức năng, ma trận kiểm thử).
4. **[04-vinalink-simulator-srd.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/docs/04-vinalink-simulator-srd.md)**
   * Tài liệu Yêu cầu Hệ thống SRD (mô hình toán tăng trưởng S-curve Logistic, ma trận trực hệ và Khung bài toán Quy hoạch Tuyến tính / Tối ưu Kép).

---

## 3. Hướng dẫn Chạy Bộ Mô phỏng CLI Python

Bên cạnh giao diện Web UI, bộ mô phỏng backend được viết bằng Python chuẩn (Zero-Dependency) nằm tại tệp [vinalink-simulator.py](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/scripts/vinalink-simulator.py).

### Cú pháp Lệnh
```bash
python scripts/vinalink-simulator.py [tham_so]
```

### Các Tham số Tùy chọn (Arguments)
* `--size SIZE`: Quy mô mạng lưới tối đa (Mặc định: `10000`).
* `--retention RETENTION`: Tỷ lệ giữ chân NPP hoạt động, từ 0.05 đến 1.0 (Mặc định: `0.3`).
* `--split SPLIT`: Tỷ lệ phân bổ nhánh mạnh, từ 0.5 đến 0.95 (Mặc định: `0.7`).
* `--rank RANK`: Cấp bậc cá nhân của Doanh chủ (`BRONZE` / `SILVER` / `GOLD`, Mặc định: `GOLD`).
* `--f1 F1`: Số lượng F1 nòng cốt giả lập (Mặc định: `3`).
* `--dup DUP`: Hệ số nhân bản chiều sâu (Mặc định: `2`).
* `--f1-share SHARE`: Tỷ lệ doanh số nhánh do F1 mạnh nhất gánh, từ 0.1 đến 0.9 (Mặc định: `0.5`).
* `--dynamic`: Kích hoạt chế độ mô phỏng động chuỗi thời gian 36 tháng (Logistic S-curve).

### Ví dụ Chạy Mô phỏng Động 36 Tháng
```bash
python scripts/vinalink-simulator.py --size 10000 --retention 0.3 --split 0.7 --rank GOLD --f1 3 --dynamic
```

---

## 4. Tài nguyên Chưa Sử dụng (Hidden / Unused Assets) từ adminHMD

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
