# BÁO CÁO KHẢO SÁT VÀ CHÂN DUNG KHÁCH HÀNG DOANH CHỦ (AUDIT REPORT & PERSONA)

> **Tài liệu hợp nhất:**
> - Checklist Khảo sát Tầm nhìn & Mục tiêu Doanh chủ Vinalink
> - Bản đồ 3 Thị trường Khách hàng Mục tiêu Vinalink
> 
> *Ý nghĩa: Tài liệu này cung cấp bộ câu hỏi khảo sát chẩn đoán 7 phần dành cho Doanh chủ và bản phân tích thấu cảm 3 thị trường khách hàng mục tiêu để phục vụ việc lập Kế hoạch Kinh doanh 3 năm.*

---

# PHẦN I. CHECKLIST KHẢO SÁT TẦM NHÌN & MỤC TIÊU DOANH CHỦ

> [!IMPORTANT]
> **QUY ƯỚC ĐỊNH DẠNG KHÓA (KHÔNG ĐƯỢC THAY ĐỔI):**
> 1. Đối với các câu hỏi tự luận/điền số: Chỉ điền câu trả lời của anh sau dấu mũi tên `->`. Không sửa đổi nhãn mã biến dạng `[ma_bien: kieu_du_lieu]`.
> 2. Đối với các câu hỏi lựa chọn: Đánh dấu `[x]` vào ô trống tương ứng `[ ]`.

---

## 1. Tầm nhìn & Mục tiêu Tài chính (Phần 1)
- **Mức thu nhập thụ động kỳ vọng qua các năm là bao nhiêu?**
  - Thu nhập năm 1 (VNĐ/tháng): [thu_nhap_nam_1: currency_vnd] -> ........................
  - Thu nhập năm 2 (VNĐ/tháng): [thu_nhap_nam_2: currency_vnd] -> ........................
  - Thu nhập năm 3 (VNĐ/tháng): [thu_nhap_nam_3: currency_vnd] -> ........................
- **Động lực lớn nhất khiến anh/chị quyết định xây dựng hệ thống đa cấp tại Vinalink là gì?** (Tự do tài chính, phát triển bản thân, giúp đỡ cộng đồng, hay tạo lập tài sản kế thừa?).
  - Trả lời: [dong_luc_lon_nhat: select("Tự do tài chính"|"Phát triển bản thân"|"Giúp đỡ cộng đồng"|"Tạo lập tài sản kế thừa")] -> ................................................................................

## 2. Quy mô & Cấu trúc Hệ thống mong muốn (Phần 2)
- **Số lượng nhân sự nòng cốt (Key Leaders - F1 trực tiếp) anh/chị muốn đồng hành và chuyển giao công nghệ là bao nhiêu người?**
  - Trả lời (người): [so_luong_f1_nong_cot: select(3|4|5)] -> ........................
- **Tổng số lượng thành viên/nhà phân phối hoạt động trong mạng lưới sau 3 năm mong muốn là bao nhiêu?**
  - Trả lời (người): [tong_quy_mo_he_thong: integer] -> ........................
- **Tỷ lệ phân bổ giữa "Nhà tiêu dùng thông minh" và "Nhà phân phối kinh doanh chuyên nghiệp" anh/chị hướng tới trong hệ thống của mình là gì?** (Ví dụ: 80% tiêu dùng - 20% kinh doanh).
  - Trả lời (% tiêu dùng - % kinh doanh): [ty_le_phan_bo: select("80% tiêu dùng - 20% kinh doanh"|"70% tiêu dùng - 30% kinh doanh"|"90% tiêu dùng - 10% kinh doanh")] -> ........................................................

## 3. Định hình Văn hóa Đội nhóm Tinh gọn & Giá trị Cốt lõi (Phần 3)
- **3 tính từ mô tả văn hóa làm việc mà anh/chị muốn định hình cho đội nhóm của mình là gì?** (Ví dụ: Tinh gọn, Kỷ luật, Nhân văn, Tốc độ, Học hỏi...).
  - Trả lời: [tinh_tu_van_hoa: text] -> ................................................................................
- **Phong cách lãnh đạo anh/chị hướng tới là gì?** (Lãnh đạo phục vụ, Lãnh đạo truyền cảm hứng, hay Lãnh đạo huấn luyện?).
  - Trả lời: [phong_cach_lanh_dao: select("Lãnh đạo phục vụ (Servant Leadership)"|"Lãnh đạo truyền cảm hứng"|"Lãnh đạo huấn luyện")] -> ................................................................................

### Trụ cột 3.1: Ánh xạ Nỗi đau Vận hành thành Giá trị Cốt lõi (Tầng Chìm)
*Hướng dẫn: Đánh dấu [x] vào các ô tương ứng dưới đây để xác định những "nỗi đau" vận hành anh/chị lo ngại nhất, từ đó hệ thống định vị Giá trị Cốt lõi cần tập trung xây dựng.*

- `[ ]` **Quá tải thời gian:** Lo sợ bản thân kiệt sức vì làm việc 12-14h/ngày để liên tục đi hỗ trợ trực tiếp từ xa $\rightarrow$ Giá trị cốt lõi tương ứng: **Tối giản Tinh gọn (Lean)** [cult_pain_burnout: checkbox]
- `[ ]` **Dumping & Mất lòng tin:** Lo sợ thành viên tuyến dưới bị ép số, ôm hàng chôn vốn dẫn đến bán cắt lỗ/phá giá $\rightarrow$ Giá trị cốt lõi tương ứng: **Chính trực Minh bạch (Integrity)** [cult_pain_dumping: checkbox]
- `[ ]` **Gãy rụng tuyến dưới:** Lo sợ tuyển được người mới nhưng không ai đồng hành dẫn dắt, làm họ nản lòng bỏ cuộc sau 30 ngày $\rightarrow$ Giá trị cốt lõi tương ứng: **Đồng hành Dụng tâm (Servant Leadership)** [cult_pain_churn: checkbox]
- `[ ]` **Mất bản sao quy trình:** Lo sợ các nhánh bên dưới tự làm một kiểu, truyền đạt sai quy chuẩn giáo án $\rightarrow$ Giá trị cốt lõi tương ứng: **Tôn trọng Nguyên bản (Duplication)** [cult_pain_disrespect: checkbox]

### Trụ cột 3.2: Cam kết Thiết lập Hành vi Thực hành Hằng ngày (Tầng Nổi)
*Hướng dẫn: Điền thông số cam kết của anh/chị và Ban điều hành F1 vào sau dấu mũi tên `->`.*

* **Nghi thức họp Daily Power 15 phút đầu ngày:**
  - Khung giờ họp cố định hằng ngày (ví dụ: 08:00 - 08:15): [cult_daily_time: time] -> ........................
  - Kênh họp trực tuyến chính thức (ví dụ: Zoom, Google Meet, Zalo): [cult_daily_channel: text] -> ........................
  - Mức gieo hạt tài chính phạt đi muộn (VNĐ/lần): [cult_daily_fine: currency_vnd] -> ........................
* **Quy chế giao tiếp & Họp tuần:**
  - Kênh nhắn tin công việc chính thức (ví dụ: Zalo, Discord): [cult_comm_channel: text] -> ........................
  - Thời hạn phản hồi tin nhắn tối đa (ví dụ: 4 giờ): [cult_comm_response_limit: integer] -> ........................
  - Lịch họp tuần Ban điều hành cố định (ví dụ: Tối chủ nhật): [cult_weekly_meeting_day: select("Thứ hai"|"Thứ ba"|"Thứ tư"|"Thứ năm"|"Thứ sáu"|"Thứ bảy"|"Chủ nhật")] -> ........................
* **Quy tắc xử lý sự cố nhánh gãy rụng:**
  - `[ ]` Cam kết tuyệt đối không đổ lỗi cá nhân, tập trung phân tích số liệu từ bộ mô phỏng [cult_trouble_no_blame: checkbox]
  - `[ ]` Cam kết đồng hành cùng F1-Hacker huấn luyện lại kỹ năng thực chiến bị thiếu hụt cho nhánh bị yếu [cult_trouble_retrain: checkbox]

## 4. Đánh giá Nguồn lực Đầu vào & Tự Chẩn đoán Năng lực (Phần 4)
- **Thời gian anh/chị có thể cam kết đầu tư cho việc phát triển hệ thống này mỗi ngày là bao nhiêu tiếng?**
  - Trả lời (giờ/ngày): [thoi_gian_cam_ket: select(4|5|6|7|8)] -> ........................
- **Ngân sách dự kiến đầu tư cho các hoạt động tiếp cận khách hàng, hội thảo, đào tạo ban đầu là bao nhiêu?**
  - Trả lời (VNĐ): [ngan_sach_ban_dau: currency_vnd] -> ........................
- **Anh/Chị đã có sẵn kỹ năng hoặc kinh nghiệm gì có thể tận dụng ngay?** (Kỹ năng thuyết trình, đào tạo sản phẩm, telesale, marketing online...).
  - Trả lời: [ky_nang_san_co: text] -> ................................................................................

  * **Ma trận Năng lực & Định hướng Kỹ năng Doanh chủ (Skill Matrix):**
    *Hướng dẫn: Đánh dấu `[x]` vào ô **"Đã có"** cho các kỹ năng anh/chị TỰ TIN đang nắm vững. Phần còn lại trống = ưu tiên phát triển.*

    | # | Tuyển dụng & Kết nối | Đã có | Đào tạo & Sao chép hệ thống | Đã có | Công nghệ & Truyền thông | Đã có | Vận hành & Chăm sóc | Đã có |
    | :---: | :--- | :---: | :--- | :---: | :--- | :---: | :--- | :---: |
    | 1 | Thu hút, giao tiếp với người lạ & xây dựng niềm tin nhanh `[sm_recruit_trust: checkbox]` | `[ ]` | Đóng gói quy trình phức tạp thành các bước đơn giản dễ sao chép `[sm_train_simplify: checkbox]` | `[ ]` | Thiết lập trang đích cá nhân hoá & phễu tuyển dụng tự động `[sm_funnel_tech: checkbox]` | `[ ]` | Vận hành văn phòng trực tuyến, đặt hàng & quản lý mã số `[sm_vpol_operation: checkbox]` | `[ ]` |
    | 2 | Thuyết trình cơ hội hợp tác thuyết phục & xử lý từ chối hiệu quả `[sm_opp_present: checkbox]` | `[ ]` | Thiết kế giáo trình, kèm cặp thực chiến & đào tạo sản phẩm `[sm_emc_training: checkbox]` | `[ ]` | Viết bài mạng xã hội thu hút & xây dựng thương hiệu cá nhân `[sm_brand_content: checkbox]` | `[ ]` | Phân tích số liệu nhánh mạnh/yếu, tỷ lệ giữ chân & cân bằng nhánh `[sm_data_analysis: checkbox]` | `[ ]` |
    | 3 | Thiết lập cuộc hẹn, gọi điện tư vấn & chốt đối tác tiềm năng `[sm_appointment_sales: checkbox]` | `[ ]` | Truyền cảm hứng, tạo động lực & dẫn dắt theo phong cách lãnh đạo phục vụ `[sm_servant_lead: checkbox]` | `[ ]` | Thành thạo công cụ thiết kế, dựng video để làm tài liệu tiếp thị `[sm_design_tool: checkbox]` | `[ ]` | Sử dụng bộ mô phỏng dự phóng tài chính để kiểm soát trần hoa hồng `[sm_sim_usage: checkbox]` | `[ ]` |
    | 4 | Tuyển chọn, chuyển giao & giữ chân nhân sự nòng cốt tuyến dưới `[sm_team_recruit: checkbox]` | `[ ]` | | | Định vị giá trị cá nhân & thấu cảm chân dung tuyến dưới mục tiêu `[sm_brand_persona: checkbox]` | `[ ]` | Lập kế hoạch kinh doanh & thiết lập mục tiêu hệ thống theo từng giai đoạn `[sm_strat_plan: checkbox]` | `[ ]` |
    | 5 | | | | | | | Tối ưu hoá cơ chế trả thưởng & kiểm soát trần hoa hồng hệ thống `[sm_scheme_opt: checkbox]` | `[ ]` |

### 4.1 Bảng Tự Đánh giá Mức độ Kỹ năng (Dành cho việc chẩn đoán co-founder F1)
*Hướng dẫn: Tự chấm điểm khả năng thực tế của bản thân theo thang điểm từ **1** (Yếu/Chưa biết làm) đến **5** (Rất mạnh/Tự tin giảng dạy) sau dấu mũi tên `->`.*

* **Nhóm 1: Kết nối & Tuyển dụng (Hustler)**
  - Tự tin thu hút, giao tiếp với người lạ và thiết lập niềm tin nhanh chóng: [self_hustler_1: select(1|2|3|4|5)] -> ........................
  - Kỹ năng thuyết trình OPP thuyết phục, xử lý từ chối hiệu quả: [self_hustler_2: select(1|2|3|4|5)] -> ........................
  - Uy tín cá nhân cao, có tầm ảnh hưởng trong vòng quan hệ xã hội: [self_hustler_3: select(1|2|3|4|5)] -> ........................
* **Nhóm 2: Đào tạo & Huấn luyện (Hacker)**
  - Khả năng đóng gói quy trình phức tạp thành các bước 1-2-3 đơn giản: [self_hacker_1: select(1|2|3|4|5)] -> ........................
  - Tự tin làm chủ sân khấu, đứng lớp chuyển giao kỹ năng cho người mới: [self_hacker_2: select(1|2|3|4|5)] -> ........................
  - Kỹ năng thiết kế slide bài giảng, giáo trình thực chiến và hướng dẫn SOP: [self_hacker_3: select(1|2|3|4|5)] -> ........................
* **Nhóm 3: Công nghệ & Truyền thông (Hipster)**
  - Thành thạo công cụ thiết kế, dựng video cơ bản (Canva, CapCut): [self_hipster_1: select(1|2|3|4|5)] -> ........................
  - Khả năng viết bài chia sẻ MXH thu hút, xây dựng thương hiệu cá nhân: [self_hipster_2: select(1|2|3|4|5)] -> ........................
  - Tự thiết lập Landing Page và phễu tuyển dụng tự động trên internet: [self_hipster_3: select(1|2|3|4|5)] -> ........................
* **Nhóm 4: Quản trị & Vận hành (Operator)**
  - Khả năng đọc hiểu bảng số liệu doanh số nhánh mạnh/yếu, tính năng động: [self_operator_1: select(1|2|3|4|5)] -> ........................
  - Sự tỉ mỉ trong việc quản trị đơn hàng, kết nối tổng kho xử lý sự cố giao nhận: [self_operator_2: select(1|2|3|4|5)] -> ........................
  - Kỹ năng tổ chức họp hành tinh gọn, kiểm soát nhịp kỷ luật của đội nhóm: [self_operator_3: select(1|2|3|4|5)] -> ........................

## 5. Khảo sát Hiện trạng Hệ thống Doanh nghiệp (Phần 5)
- **Quy mô tổng thành viên hiện tại của hệ thống (người):** [hien_tai_quy_mo_tong: integer] -> ........................
- **Số lượng NPP hoạt động thực tế hiện tại (người):** [hien_tai_npp_hoat_dong: integer] -> ........................
- **Số lượng KHTT hoạt động thực tế hiện tại (người):** [hien_tai_khtt_hoat_dong: integer] -> ........................
- **Cấp bậc cá nhân hiện tại của Doanh chủ (BRONZE/SILVER/GOLD):** [hien_tai_cap_bac_ca_nhan: select("BRONZE"|"SILVER"|"GOLD")] -> ........................
- **Danh hiệu nhóm hiện tại của Doanh chủ (NPP_THUONG/M/SM/DIR/RUBY/EME/DIA/BD/BKD/CD/AMB):** [hien_tai_danh_hieu: select("NPP_THUONG"|"M"|"SM"|"DIR"|"RUBY"|"EME"|"DIA"|"BD"|"BKD"|"CD"|"AMB")] -> ........................
- **Doanh số phát sinh hàng tháng hiện tại của toàn hệ thống (CV):** [hien_tai_doanh_so_cv: integer] -> ........................
- **Doanh số nhánh yếu hàng tháng hiện tại (CV):** [hien_tai_nhanh_yeu_cv: integer] -> ........................
- **Tỷ lệ giữ chân NPP hoạt động thực tế hiện tại (%):** [hien_tai_ty_le_giu_chan: integer] -> ........................
- **Điểm tràn từ Upline hàng tháng hiện tại (CV):** [hien_tai_diem_tran_cv: integer] -> ........................
- **Số lượng F1 nòng cốt đã tuyển dụng thành công hiện tại (người):** [hien_tai_f1_nong_cot: integer] -> ........................

## 6. Khung Định vị Tuyển dụng Tuyến dưới Tinh gọn (Phần 6)

### Trụ cột A: Định vị Giá trị của Doanh chủ (Leader Value Proposition - LVP)
- **Câu hỏi A1**: Anh/Chị sẽ hỗ trợ trực tiếp điều gì cho người mới trong 30 ngày đầu tiên tham gia?
  - `[ ]` Quy trình chuyển giao giáo trình đào tạo sản phẩm & sức khỏe chủ động từ Vinalink [lvp_a1_giao_trinh: checkbox]
  - `[ ]` Cầm tay chỉ việc hướng dẫn kỹ năng thiết lập cuộc hẹn và tuyển dụng thực chiến [lvp_a1_cam_tay: checkbox]
  - `[ ]` Đồng hành chia sẻ trực tiếp (OPP 2-1) hỗ trợ chốt khách cho họ [lvp_a1_opp_21: checkbox]
  - `[ ]` Cung cấp công cụ số hóa, tài liệu tiếp thị và văn phòng trực tuyến (VPOL) [lvp_a1_vpol: checkbox]
- **Câu hỏi A2**: Điểm khác biệt lớn nhất trong phong cách dẫn dắt đội nhóm của anh/chị so với các hệ thống đa cấp truyền thống là gì?
  - Trả lời: [lvp_a2_phong_cach: text] -> ................................................................................
- **Câu hỏi A3 (Lợi thế cạnh tranh nội bộ Vinalink - Intra-system)**: Giữa vô số các Upline và đội nhóm khác cũng đang phân phối Vinalink ngoài thị trường, tại sao một người mới lại nên chọn gia nhập hệ thống của riêng anh/chị?
  - `[ ]` **Quy trình EMC cải tiến**: Giáo trình đào tạo được đơn giản hóa tối đa, giúp người mới học nhanh, làm được ngay [lvp_a3_emc: checkbox]
  - `[ ]` **Công nghệ và Công cụ hỗ trợ**: Cung cấp phễu tuyển dụng, Landing Page cá nhân hóa và VPOL [lvp_a3_tech: checkbox]
  - `[ ]` **Văn hóa "An vui & Tinh gọn"**: Không ép doanh số cá nhân, không ôm hàng [lvp_a3_culture: checkbox]
  - `[ ]` **Sự cố cố vấn cá nhân**: Lộ trình 3 năm rõ ràng cho từng F1 nòng cốt [lvp_a3_mentor: checkbox]
  - Khác: [lvp_a3_khac: text] -> ................................................................................
- **Câu hỏi A4 (Lợi thế cạnh tranh ngoại bộ - Inter-system)**: Khi ứng viên đang cân nhắc giữa Vinalink và các công ty khác (Amway, Herbalife, Nuskin...):
  - `[ ]` **Lợi thế "Thuần Việt" của sản phẩm**: Sản phẩm IMC y học cổ truyền giá hợp lý (1.000 VNĐ = 2,5 CV) [lvp_a4_product: checkbox]
  - `[ ]` **Chính sách nhị phân lai mặt trời**: Cộng dồn doanh số trọn đời, không hạ cấp bậc, năng động cực thấp và không ly khai [lvp_a4_scheme: checkbox]
  - `[ ]` **Giá trị thừa kế pháp lý vững chắc**: Hoạt động 100% hợp pháp tại Việt Nam theo Nghị định 40 [lvp_a4_legal: checkbox]
  - Khác: [lvp_a4_khac: text] -> ................................................................................
- **Câu hỏi A5 (Định vị Thương hiệu cá nhân của Doanh chủ)**:
  - Trả lời: [lvp_a5_brand: text] -> ................................................................................

### Trụ cột B: Xác định Chân dung Phân khúc Tuyến dưới Ưu tiên (Ideal Downline Profiling - IDP)
- **Câu hỏi B1**: Trong 3 nhóm đối tượng dưới đây, anh/chị muốn ưu tiên phân bổ nguồn lực tuyển dụng vào nhóm nào nhất?
  - `[ ]` **Nhóm 1: Người làm thêm kiếm thu nhập thụ động** (Mẹ bỉm sữa, dân văn phòng có thời gian rảnh 2-3h/ngày, mong muốn kiếm 5 - 10 triệu/tháng) [idp_b1_nhom1: checkbox]
  - `[ ]` **Nhóm 2: Người tiêu dùng chuyển đổi** (Người yêu thích thảo dược Việt Nam công nghệ cao, muốn dùng giá sỉ hoặc miễn phí) [idp_b1_nhom2: checkbox]
  - `[ ]` **Nhóm 3: Nhà xây dựng hệ thống chuyên nghiệp/Doanh chủ hệ thống** (Tham vọng lớn, muốn xây dựng dòng tiền thụ động tỷ đồng lên Diamond/Ambassador) [idp_b1_nhom3: checkbox]
- **Câu hỏi B2**: Phân khúc nghề nghiệp và độ tuổi nào dễ kết nối nhất?
  - Trả lời: [idp_b2_demographic: text] -> ................................................................................

### Trụ cột C: Bộ lọc Tuyển dụng Nòng cốt (Qualification Filters)
- **Câu hỏi C1**: Đâu là 3 tiêu chí bắt buộc phải có ở một ứng viên để đầu tư thời gian hỗ trợ 2-1?
  - `[ ]` Khát khao & Động lực lớn [qf_c1_desire: checkbox]
  - `[ ]` Tinh thần học hỏi (Coachability) [qf_c1_coachable: checkbox]
  - `[ ]` Uy tín cá nhân (Trustworthiness) [qf_c1_trust: checkbox]
  - `[ ]` Cam kết thời gian (2-3h/ngày) [qf_c1_time: checkbox]
  - `[ ]` Năng lực đầu vào (giao tiếp, thuyết trình) [qf_c1_skill: checkbox]
- **Câu hỏi C2**: Bài test hoặc hành động cụ thể để kiểm tra cam kết của người mới:
  - Trả lời: [qf_c2_test: text] -> ................................................................................

## 7. Các Tham số Định lượng Chuẩn hóa cho Mô hình Tối ưu 3 năm (Phần 7)
- **Mục tiêu chính:** Tối đa hóa tổng giá trị hiện tại ròng của thu nhập (NPV) tích lũy trong 3 năm (36 tháng).
- **KHTT - Thời gian tuyển dụng:** [opt_time_recruit_consumer: integer] -> ........................
- **KHTT - Chi phí tiếp thị bình quan:** [opt_cost_recruit_consumer: currency_vnd] -> ........................
- **NPP - Thời gian tuyển dụng:** [opt_time_recruit_distributor: integer] -> ........................
- **NPP - Chi phí tiếp thị bình quan:** [opt_cost_recruit_distributor: currency_vnd] -> ........................
- **Thời gian kèm cặp NPP mới tháng đầu (giờ):** [opt_time_train_first_month: integer] -> ........................
- **Thời gian hỗ trợ duy trì NPP cũ các tháng sau (giờ/tháng):** [opt_time_support_monthly: integer] -> ........................
- **Tỷ lệ hao hụt KHTT & NPP hàng tháng (%/tháng):** [opt_churn_rate: float] -> ........................

---

# PHẦN II. BẢN ĐỒ 3 THỊ TRƯỜNG KHÁCH HÀNG MỤC TIÊU VINALINK

## 1. Thị trường 1: Nhóm Người làm thêm kiếm thu nhập thụ động
* **Định vị:** Nhóm tìm kiếm nguồn thu nhập phụ linh hoạt (5 - 10 triệu/tháng) bằng thời gian rảnh rỗi 2-3h/ngày.
* **Nỗi đau lớn nhất:** Sợ bị lừa đảo đa cấp biến tướng, sợ bị ép ôm hàng chôn vốn, sợ không bán được hàng.
* **Thông điệp tiếp cận:** *"Kinh doanh không ôm hàng - Quy trình EMC tối giản có sẵn, cầm tay chỉ việc từ xa."*
* **Lộ trình tiếp cận:** Tiếp cận hội nhóm online $\rightarrow$ Đăng bài chia sẻ giá trị $\rightarrow$ Gửi lời mời trải nghiệm thử không bỏ vốn.
* **Quy trình bán hàng:** Đăng ký KHTT giá sỉ $\rightarrow$ Kích hoạt gói khởi động nhỏ (800k - 1.6M) $\rightarrow$ Chuyển giao bài đăng EMC mẫu $\rightarrow$ Vận hành giao hàng tự động qua VPOL.

## 2. Thị trường 2: Nhóm Khách hàng tiêu dùng chuyển đổi
* **Định vị:** Người dùng có trải nghiệm tốt với sản phẩm thảo dược sinh học Vinalink, muốn tối ưu chi phí sử dụng hàng tháng.
* **Nỗi đau lớn nhất:** Chi phí dùng sản phẩm đều đặn hàng tháng cao, ngại mang tiếng lôi kéo bạn bè kiếm lời.
* **Thông điệp tiếp cận:** *"Giải pháp bảo vệ sức khỏe chủ động cho gia đình - Chia sẻ câu chuyện thật, nhận hoa hồng tự nhiên hướng tới dùng sản phẩm miễn phí."*
* **Lộ trình tiếp cận:** Chăm sóc định kỳ $\rightarrow$ Kích hoạt chia sẻ câu chuyện thật $\rightarrow$ Kết nối cộng đồng sống khỏe.
* **Quy trình bán hàng:** Chuyển đổi KHTT mua giá sỉ $\rightarrow$ Hướng dẫn Storytelling tự nhiên $\rightarrow$ Hỗ trợ tư vấn 2-1 trực tiếp $\rightarrow$ Khấu trừ hoa hồng đạt trạng thái dùng sản phẩm miễn phí (Free Product).

## 3. Thị trường 3: Nhóm Doanh chủ hệ thống / Leader chuyên nghiệp
* **Định vị:** Người có tư tư duy làm chủ, kinh nghiệm MLM/Bảo hiểm/Sale, muốn thiết lập sự nghiệp dòng tiền thụ động tỷ đồng thừa kế.
* **Nỗi đau lớn nhất:** Sợ sơ đồ ly khai tách nhánh làm mất công đào tạo; áp lực doanh số cá nhân ép ôm hàng phá giá; rủi ro pháp lý.
* **Thông điệp tiếp cận:** *"Sự nghiệp dòng tiền thụ động bền vững trọn đời - Sơ đồ trả thưởng không ly khai, cộng dồn doanh số trọn đời - Hệ thống số hóa giải phóng sức lao động."*
* **Lộ trình tiếp cận:** Tiếp cận vai trò Cố vấn Quản trị Tinh gọn $\rightarrow$ Phỏng vấn thấu cảm sâu $\rightarrow$ Phản biện định lượng bằng bộ mô phỏng đưa mục tiêu năm 3 về mốc Diamond (150M VNĐ/tháng).
* **Quy trình bán hàng:** Đăng ký NPP chính thức & hoàn thành khóa học pháp lý 3 ngày $\rightarrow$ Phân tích Matching Bonus F1-F5 bảo toàn dòng tiền $\rightarrow$ Chuyển giao VPOL & Landing Page $\rightarrow$ Đồng kiến tạo Master Plan 3 năm.
