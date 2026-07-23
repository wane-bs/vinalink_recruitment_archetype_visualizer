# BẢN PHẢN HỒI CHECKLIST KHẢO SÁT TẦM NHÌN DOANH CHỦ VINALINK

**Doanh chủ thực hiện:** Doanh Chủ Vinalink (Mock Leader)
**Thời gian phản hồi:** 2026-07-22 21:19:58
**Trạng thái đồng bộ:** Đồng bộ tự động lúc 20:00

---

## PHẦN CHI TIẾT CÂU TRẢ LỜI KHẢO SÁT (TÍCH HỢP ĐỒNG BỘ MỚI)

### 1. Tầm nhìn & Mục tiêu Tài chính (Phần 1)
- **Thu nhập Năm 1 (VNĐ/tháng):** [thu_nhap_nam_1: currency_vnd] -> 15.000.000 VNĐ
- **Thu nhập Năm 2 (VNĐ/tháng):** [thu_nhap_nam_2: currency_vnd] -> 60.000.000 VNĐ
- **Thu nhập Năm 3 (VNĐ/tháng):** [thu_nhap_nam_3: currency_vnd] -> 1.500.000.000 VNĐ
- **Động lực lớn nhất:** [dong_luc_lon_nhat: select(...)] -> Tự do tài chính

### 2. Quy mô & Cấu trúc Hệ thống mong muốn (Phần 2)
- **Số lượng F1 nòng cốt thiết lập dẫn dắt:** [so_luong_f1_nong_cot: select(3|4|5)] -> 3 người
- **Tổng quy mo hệ thống (3 năm):** [tong_quy_mo_he_thong: integer] -> 1000 người
- **Tỷ lệ phân bổ định hướng:** [ty_le_phan_bo: select(...)] -> 80% tiêu dùng - 20% kinh doanh

### 3. Xác định Giá trị Cốt lõi & Văn hóa Đội nhóm (Phần 3)
- **3 tính từ văn hóa đội nhóm:** [tinh_tu_van_hoa: text] -> Tinh gọn, An vui, Cam kết
- **Phong cách lãnh đạo:** [phong_cach_lanh_dao: select(...)] -> Lãnh đạo phục vụ (Servant Leadership)

#### Trụ cột 3.1: Định vị Nỗi đau lo ngại nhất (Tầng Chìm)
- [x] **Quá tải thời gian (Lean):** [cult_pain_burnout: checkbox]
- [ ] **Dumping & Mất lòng tin (Integrity):** [cult_pain_dumping: checkbox]
- [x] **Gãy rụng tuyến dưới (Servant Leadership):** [cult_pain_churn: checkbox]
- [ ] **Mất bản sao quy trình (Duplication):** [cult_pain_disrespect: checkbox]

#### Trụ cột 3.2: Cam kết Hành vi Thực hành Hằng ngày (Tầng Nổi)
- **Khung giờ họp Daily Power:** [cult_daily_time: time] -> 08:00
- **Kênh họp Daily chính thức:** [cult_daily_channel: text] -> Zoom
- **Mức gieo hạt phạt đi muộn:** [cult_daily_fine: currency_vnd] -> 50.000 VNĐ
- **Kênh nhắn tin công việc:** [cult_comm_channel: text] -> Zalo
- **Thời hạn phản hồi tin nhắn tối đa:** [cult_comm_response_limit: integer] -> 4 giờ
- **Lịch họp tuần Ban điều hành F1:** [cult_weekly_meeting_day: select(...)] -> Chủ nhật
- [x] **KHÔNG đổ lỗi khi gãy nhánh:** [cult_trouble_no_blame: checkbox]
- [x] **Cùng Hacker đứng lớp huấn luyện lại:** [cult_trouble_retrain: checkbox]

### 4. Đánh giá Nguồn lực Đầu vào & Tự Chẩn đoán Năng lực (Phần 4)
- **Thời gian cam kết làm việc mỗi ngày:** [thoi_gian_cam_ket: select(...)] -> 4 giờ/ngày
- **Ngân sách đầu tư ban đầu:** [ngan_sach_ban_dau: currency_vnd] -> 5.000.000 VNĐ
- **Kỹ năng sẵn có sở hữu:** [ky_nang_san_co: text] -> ['sm_recruit_trust', 'sm_opp_present', 'sm_emc_training', 'sm_servant_lead', 'sm_brand_content', 'sm_vpol_operation']

- **Ma trận Năng lực & Định hướng Kỹ năng Doanh chủ (Skill Matrix):**

  | # | Tuyển dụng & Kết nối | Đã có | Đào tạo & Sao chép hệ thống | Đã có | Công nghệ & Truyền thông | Đã có | Vận hành & Chăm sóc | Đã có |
  | :---: | :--- | :---: | :--- | :---: | :--- | :---: | :--- | :---: |
  | 1 | Thu hút, giao tiếp với người lạ & xây dựng niềm tin nhanh `[sm_recruit_trust: checkbox]` | [x] | Đóng gói quy trình phức tạp thành các bước đơn giản dễ sao chép `[sm_train_simplify: checkbox]` | [ ] | Thiết lập trang đích cá nhân hoá & phễu tuyển dụng tự động `[sm_funnel_tech: checkbox]` | [ ] | Vận hành văn phòng trực tuyến, đặt hàng & quản lý mã số `[sm_vpol_operation: checkbox]` | [x] |
  | 2 | Thuyết trình cơ hội hợp tác thuyết phục & xử lý từ chối hiệu quả `[sm_opp_present: checkbox]` | [x] | Thiết kế giáo trình, kèm cặp thực chiến & đào tạo sản phẩm `[sm_emc_training: checkbox]` | [x] | Viết bài mạng xã hội thu hút & xây dựng thương hiệu cá nhân `[sm_brand_content: checkbox]` | [x] | Phân tích số liệu nhánh mạnh/yếu, tỷ lệ giữ chân & cân bằng nhánh `[sm_data_analysis: checkbox]` | [ ] |
  | 3 | Thiết lập cuộc hẹn, gọi điện tư vấn & chốt đối tác tiềm năng `[sm_appointment_sales: checkbox]` | [ ] | Truyền cảm hứng, tạo động lực & dẫn dắt theo phong cách lãnh đạo phục vụ `[sm_servant_lead: checkbox]` | [x] | Thành thạo công cụ thiết kế, dựng video để làm tài liệu tiếp thị `[sm_design_tool: checkbox]` | [ ] | Sử dụng bộ mô phỏng dự phóng tài chính để kiểm soát trần hoa hồng `[sm_sim_usage: checkbox]` | [ ] |
  | 4 | Tuyển chọn, chuyển giao & giữ chân nhân sự nòng cốt tuyến dưới `[sm_team_recruit: checkbox]` | [ ] | | | Định vị giá trị cá nhân & thấu cảm chân dung tuyến dưới mục tiêu `[sm_brand_persona: checkbox]` | [ ] | Lập kế hoạch kinh doanh & thiết lập mục tiêu hệ thống theo từng giai đoạn `[sm_strat_plan: checkbox]` | [ ] |
  | 5 | | | | | | | Tối ưu hoá cơ chế trả thưởng & kiểm soát trần hoa hồng hệ thống `[sm_scheme_opt: checkbox]` | [ ] |

#### Phần 4.1: Điểm tự đánh giá 12 năng lực quản trị (1-5)
* **Nhóm 1: Kết nối & Tuyển dụng (Hustler)**
  - Tự tin thu hút, giao tiếp người lạ: [self_hustler_1: select(1|2|3|4|5)] -> 3
  - Thuyết trình OPP & chốt khách: [self_hustler_2: select(1|2|3|4|5)] -> 3
  - Có tầm ảnh hưởng & uy tín lớn: [self_hustler_3: select(1|2|3|4|5)] -> 3
* **Nhóm 2: Đào tạo & Huấn luyện (Hacker)**
  - Đóng gói quy trình thành 1-2-3 đơn giản: [self_hacker_1: select(1|2|3|4|5)] -> 4
  - Tự tin đứng lớp, truyền lửa người mới: [self_hacker_2: select(1|2|3|4|5)] -> 3
  - Thiết kế slide, giáo trình & SOP: [self_hacker_3: select(1|2|3|4|5)] -> 3
* **Nhóm 3: Công nghệ & Truyền thông (Hipster)**
  - Sử dụng công cụ thiết kế Canva, CapCut: [self_hipster_1: select(1|2|3|4|5)] -> 2
  - Viết bài MXH, xây dựng thương hiệu: [self_hipster_2: select(1|2|3|4|5)] -> 3
  - Thiết lập Landing page & phễu tự động: [self_hipster_3: select(1|2|3|4|5)] -> 2
* **Nhóm 4: Quản trị & Vận hành (Operator)**
  - Đọc hiểu số cân nhánh nhị phân, năng động: [self_operator_1: select(1|2|3|4|5)] -> 3
  - Tỉ mỉ quản đơn hàng, kết nối tổng kho: [self_operator_2: select(1|2|3|4|5)] -> 4
  - Tổ chức họp tinh gọn, kiểm soát kỷ luật: [self_operator_3: select(1|2|3|4|5)] -> 3

### 5. Khảo sát Hiện trạng Hệ thống (Phần 5)
- **Quy mô tổng thành viên hiện tại:** [hien_tai_quy_mo_tong: integer] -> 50 người
- **Số NPP hoạt động thực tế:** [hien_tai_npp_hoat_dong: integer] -> 10 người
- **Số KHTT hoạt động thực tế:** [hien_tai_khtt_hoat_dong: integer] -> 30 người
- **Cấp bậc cá nhân hiện tại:** [hien_tai_cap_bac_ca_nhan: select(...)] -> GOLD
- **Danh hiệu nhóm hiện tại:** [hien_tai_danh_hieu: select(...)] -> SM
- **Doanh số phát sinh hàng tháng hiện tại (CV):** [hien_tai_doanh_so_cv: integer] -> 20000 CV
- **Doanh số nhánh yếu hàng tháng hiện tại (CV):** [hien_tai_nhanh_yeu_cv: integer] -> 8000 CV
- **Tỷ lệ giữ chân NPP hoạt động (%):** [hien_tai_ty_le_giu_chan: integer] -> 80 %
- **Điểm tràn từ Upline hàng tháng (CV):** [hien_tai_diem_tran_cv: integer] -> 0 CV
- **Số lượng F1 nòng cốt đã tuyển:** [hien_tai_f1_nong_cot: integer] -> 2 người

### 6. Khung Định vị Tuyển dụng Tuyến dưới Tinh gọn (Phần 6)

#### Trụ cột A: Định vị Giá trị của Doanh chủ (Leader Value Proposition - LVP)
- **Câu A1 (Hỗ trợ 30 ngày đầu):** Cầm tay chỉ việc hướng dẫn kỹ năng hẹn và tuyển thực chiến, Đồng hành OPP 2-1
- **Câu A2 (Phong cách dẫn dắt khác biệt):** [lvp_a2_phong_cach: text] -> Đào tạo thực chiến y học cổ truyền kết hợp phễu tự động.
- **Câu A3 (Lợi thế nội bộ - Intra-system):** Quy trình EMC cải tiến dễ sao chép, Văn hóa An vui & Tinh gọn
- **Câu A4 (Lợi thế ngoại bộ - Inter-system):** Lợi thế Thuần Việt giá bình dân, Trả thưởng Nhị phân lai không ly khai
- **Câu A5 (Hình ảnh thương hiệu cá nhân):** [lvp_a5_brand: text] -> Người dẫn đường tận tâm, cam kết hỗ trợ F1 thực chiến.

#### Trụ cột B: Xác định Chân dung Phân khúc Tuyến dưới Ưu tiên (IDP)
- **Câu B1 (Phân khúc ưu tiên tuyển dụng):** [idp_b1_prior: select(...)] -> nhom_3
- **Câu B2 (Nghề nghiệp & độ tuổi mục tiêu):** [idp_b2_demographic: text] -> Nhân viên văn phòng, người làm tự do 30-45 tuổi.

#### Trụ cột C: Bộ lọc Tuyển dụng Nòng cốt (Qualification Filters)
- **Câu C1 (3 tiêu chí bắt buộc):** Khát khao & Động lực lớn, Tinh thần học hỏi (Coachability), Cam kết thời gian
- **Câu C2 (Bài test hành động cam kết):** [qf_c2_test: text] -> Trải nghiệm ít nhất 1 sản phẩm & hoàn thành khóa học pháp lý cơ bản 3 ngày.
