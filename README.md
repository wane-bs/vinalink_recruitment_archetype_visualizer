# Vinalink Doanh Chủ Portal - Hướng dẫn Triển khai & Tài nguyên

Website Portal này phục vụ việc quản lý tài liệu, xác định văn hóa đội ngũ, khảo sát ý kiến và chạy bộ giả lập dòng tiền tối ưu cho Doanh chủ Vinalink, được nâng cấp kế thừa từ template chuyên nghiệp **adminHMD v1.0.0**.

---

## 1. Cấu trúc Triển khai trên Web (Multi-Page App)

Toàn bộ các trang hoạt động tĩnh được chia nhỏ theo mô hình đa trang:
* [index.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/index.html) - Dashboard tổng quan & Lộ trình 3 năm.
* [html/documents.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/html/documents.html) - Thư viện tài liệu nghiên cứu, bộ công cụ văn hóa và kịch bản thuyết minh slide.
* [html/visualizer.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/html/visualizer.html) - Bộ Công Cụ Xác Định Tầm Nhìn & Văn Hóa Cốt Lõi Đội Ngũ (Lean Culture Toolkit).
* [html/simulator.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/html/simulator.html) - Bộ giả lập 7 nguồn thu nhập và dòng tiền 36 tháng.
* [html/feedback.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/html/feedback.html) - Form khảo sát Doanh chủ 22 trường dữ liệu.
* [html/settings.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/html/settings.html) - Cài đặt API kết nối Google Sheets (Dành riêng cho Cố vấn).
* [html/login.html](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/html/login.html) - Xác thực quyền quản trị Cố vấn Lean Startup.

---

## 2. Thư viện Tài liệu Chuẩn hóa (Consolidated Master Docs)

Toàn bộ tài liệu phân tích, đặc tả thuật toán và bộ công cụ được lưu trữ tập trung tại thư mục [docs/](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/docs/) gồm 6 tệp Master duy nhất:

1. **[01-master-business-policy.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/docs/01-master-business-policy.md)**
   * Hợp nhất trọn vẹn chính sách trả thưởng 7 nguồn thu nhập Vinalink Group, nghiên cứu công ty mẹ và chuẩn mực vận hành "Một Nghĩa".
2. **[02-doanh-chu-audit-report.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/docs/02-doanh-chu-audit-report.md)**
   * Hợp nhất bộ checklist khảo sát tầm nhìn/năng lực doanh chủ (MILP inputs) và bản đồ 3 thị trường khách hàng mục tiêu downline.
3. **[03-vinalink-simulator-fsd.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/docs/03-vinalink-simulator-fsd.md)**
   * Tài liệu Đặc tả Chức năng FSD cho bộ mô phỏng (flowchart, DFD Level 1, 6 spec chức năng, ma trận kiểm thử).
4. **[04-vinalink-simulator-srd.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/docs/04-vinalink-simulator-srd.md)**
   * Tài liệu Yêu cầu Hệ thống SRD (mô hình toán tăng trưởng S-curve Logistic, ma trận trực hệ và Khung bài toán Quy hoạch Tuyến tính / Tối ưu Kép).
5. **[05-bo-cong-cu-tam-nhin-van-hoa.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/docs/05-bo-cong-cu-tam-nhin-van-hoa.md)**
   * Bộ công cụ Xác định Tầm nhìn & Văn hóa Cốt lõi Đội ngũ (10 câu phỏng vấn Founder, Tảng băng 3 giá trị, Quy chế Zero Tolerance Anti-Dumping và Bộ lọc QF Checklist).
6. **[06-thuyet-minh-slide-de-xuat.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/docs/06-thuyet-minh-slide-de-xuat.md)**
   * Kịch bản Thuyết minh Chi tiết từng trang Slide ghép cặp 1:1 (Word-by-Slide Presenter Script) dành cho Cố vấn báo cáo trực tiếp với Doanh chủ Lê Thị Hồng Minh.

---

## 3. Tiến độ & Kế hoạch Triển khai (1 Tháng)

| Nội dung Công việc | Thời gian | Trạng thái | Tiến độ |
| :--- | :--- | :---: | :---: |
| **1. Nghiên cứu nền tảng & Khảo sát Doanh chủ** | Tuần 29/2026 | `Hoàn thành` | **100%** |
| **2. Xây dựng Bộ Công Cụ Văn Hóa & Tầm Nhìn (Lean Toolkit)** | Tuần 30/2026 | `Hoàn thành` | **100%** |
| **3. Tái cấu trúc mục tiêu & Mô phỏng dòng tiền 36 tháng (Simulator)** | 23/07 - 26/07 | `Hoàn thành` | **100%** |
| **4. Bộ Slide Đề Xuất & Tài Liệu Thuyết Minh Word-by-Slide** | 27/07 - 02/08 | `Đang thực hiện` | **85%** |
| **5. Hoàn thiện Kế hoạch 3 năm & Đồng hành 30 ngày đầu với Doanh chủ** | Tuần 32/2026 | `Kế hoạch` | **0%** |

---

## 4. Hướng dẫn Chạy Bộ Mô phỏng CLI Python

Bộ mô phỏng backend được viết bằng Python chuẩn (Zero-Dependency) nằm tại tệp [scripts/vinalink-simulator.py](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/scripts/vinalink-simulator.py).

### Cú pháp Lệnh
```bash
python scripts/vinalink-simulator.py --size 10000 --retention 0.3 --split 0.7 --rank GOLD --f1 3 --dynamic
```

### Sinh Bộ Slide PPTX McKinsey kèm Speaker Notes
```bash
python scripts/generate_proposal_ppt.py
```

---

## 5. Tài nguyên Chưa Sử dụng (Hidden / Unused Assets) từ adminHMD

Theo nguyên tắc tối giản, các trang mẫu của `adminhmd-1.0.0` được **ẩn khỏi thanh điều hướng chính** và lưu trữ dự phòng:
* `html/users.html`, `html/user-details.html`, `html/add-user.html`, `html/create-agent.html`, `html/profile.html` (Quản lý Nhân sự).
* `html/charts.html`, `html/tables.html`, `html/forms.html`, `html/components.html`, `html/alerts.html`, `html/modals.html` (Mẫu UI Elements).
* `html/404.html`, `html/500.html` (Trang lỗi).
