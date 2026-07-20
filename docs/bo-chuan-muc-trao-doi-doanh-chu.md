# BỘ CHUẨN MỰC PHỐI HỢP VÀ THỐNG NHẤT KHÁI NIỆM TRONG LẬP KẾ HOẠCH KINH DOANH HỆ THỐNG

> **Tài liệu tham chiếu dự án:**
> - Nghiên cứu Công ty Mẹ Vinalink Group: [vinalink-parent-research.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/vinalink-parent-research.md)
> - Phân tích Cơ chế Kinh doanh EMC: [phan-tich-co-che-kinh-doanh.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/phan-tich-co-che-kinh-doanh.md)
> 
> *Ý nghĩa: Tài liệu này đóng vai trò là cơ sở đồng thuận về phương pháp luận và các định nghĩa chuẩn hóa giữa Đội ngũ Cố vấn và Doanh chủ hệ thống, làm nền tảng xây dựng Kế hoạch Kinh doanh 3 năm khả thi, bền vững.*

---

## I. NGUYÊN TẮC ĐỒNG THUẬN CỐT LÕI
Để xây dựng một lộ trình phát triển hệ thống 3 năm thực tế, tối ưu nguồn lực và tuân thủ chặt chẽ hành lang pháp lý (Nghị định 40/2018/NĐ-CP về quản lý hoạt động kinh doanh đa cấp), Đội ngũ Cố vấn và Doanh chủ thống nhất nguyên tắc: **Lập kế hoạch dựa trên dữ liệu thực tế và định nghĩa chuẩn hóa một nghĩa**. 

Mọi dự báo tài chính, quy mô đội nhóm và kế hoạch tuyển dụng sẽ được xây dựng trên các thông số đã đăng ký pháp lý của Vinalink Group với Bộ Công Thương (được cấp phép từ năm 2014 theo [vinalink-parent-research.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/vinalink-parent-research.md)) nhằm đảm bảo tính khả thi cao nhất khi triển khai.

---

## II. NGUYÊN TẮC "MỘT NGHĨA" VỀ CÁC THỰC THỂ HỆ THỐNG
Trong suốt quá trình trao đổi và lập kế hoạch, các thuật ngữ mô tả thành viên hệ thống bắt buộc phải tuân thủ đúng một nghĩa duy nhất được quy định trong chính sách của Vinalink Group. Tuyệt đối không đánh tráo khái niệm hoặc cộng gộp vai trò để tránh làm sai lệch mô hình tài chính.

1. **Nhà phân phối (NPP):** 
   - *Định nghĩa một nghĩa:* Cá nhân đã hoàn thành thủ tục đăng ký pháp lý, ký Hợp đồng bán hàng đa cấp với Vinalink Group để được quyền xây dựng hệ thống và nhận hoa hồng.
   - *Đặc trưng tài chính:* NPP có các cấp bậc cá nhân dựa trên doanh số tích lũy một lần duy nhất (Bronze: 2.000 CV; Silver: 4.000 CV; Gold/VIP: 10.000 CV theo [phan-tich-co-che-kinh-doanh.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/phan-tich-co-che-kinh-doanh.md#L11-L19)) nhằm quyết định tỷ lệ nhận hoa hồng bảo trợ trực tiếp và trần hoa hồng chu kỳ nhóm.
2. **Khách hàng thân thiết (KHTT):**
   - *Định nghĩa một nghĩa:* Cá nhân đăng ký tài khoản miễn phí để mua sản phẩm giá sỉ trực tiếp từ công ty để tiêu dùng, không ký hợp đồng đa cấp.
   - *Đặc trưng tài chính:* Doanh số mua hàng của KHTT được tính trực tiếp vào nhánh yếu của NPP giới thiệu và tính vào điểm năng động duy trì hàng tháng của NPP đó (theo [phan-tich-co-che-kinh-doanh.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/phan-tich-co-che-kinh-doanh.md#L88-L91)). KHTT không có quyền bảo trợ tuyến dưới và không được nhận bất kỳ loại hoa hồng nào từ hệ thống.
3. **Khách hàng lẻ (Retail Customer):**
   - *Định nghĩa một nghĩa:* Người tiêu dùng cuối cùng mua sản phẩm trực tiếp từ NPP theo mức giá bán lẻ niêm yết của công ty. Doanh số này mang lại lợi nhuận bán lẻ trực tiếp ngay lập tức cho NPP.

---

## III. CHỈ SỐ SỨC KHỎE HỆ THỐNG BỀN VỮNG
Mô hình phát triển hệ thống bền vững cần tối ưu hóa giữa việc phát triển mạng lưới phân phối và việc phân phối sản phẩm ra thị trường tiêu dùng thực tế. Sức khỏe tài chính của hệ thống sẽ được giám sát qua hai chỉ số cốt lõi:

1. **Tỷ lệ Tiêu dùng Thực tế (Real Consumption Ratio - RCR):**
   $$RCR = \frac{\text{Doanh số phát sinh từ KHTT} + \text{Doanh số bán lẻ của NPP}}{\text{Tổng doanh số toàn hệ thống (CV)}} \times 100\%$$
   * **Chuẩn mực:** Tỷ lệ $RCR$ tối thiểu cần duy trì ở mức **50%**. Chỉ số này phản ánh dòng tiền đổ vào hệ thống đến từ nhu cầu sử dụng sản phẩm thực sự của thị trường tự do, thay vì chỉ đến từ việc NPP tự mua hàng tích lũy danh hiệu.
2. **Tỷ lệ Giữ chân Nhà phân phối (NPP Retention Rate - RR):**
   Tỷ lệ NPP tiếp tục phát sinh điểm năng động hoặc tuyển dụng mới sau các mốc 3 tháng, 6 tháng và 12 tháng.
   * **Chuẩn mực:** Trong mô hình tài chính 3 năm, tỷ lệ giữ chân NPP sau 3 tháng đầu tiên sẽ được tính toán thực tế (giả định hao hụt từ $50\% - 70\%$ đối với nhóm NPP không phát triển được KHTT hoặc bán lẻ), tránh việc giả định hệ thống bảo toàn 100% quân số gây ảo tưởng về quy mô.

---

## IV. NGUYÊN TẮC PHẢN BIỆN KHOA HỌC VÀ THỰC TẾ
Để kế hoạch kinh doanh có giá trị thực thi cao, Đội ngũ Cố vấn và Doanh chủ thống nhất thảo luận dựa trên các quy luật vận hành và cơ chế trả thưởng thực tế của Vinalink:

### 1. Phân tích tính tương thích giữa vai trò NPP và Khách hàng tiêu dùng
* *Lập luận phổ biến:* Coi mỗi NPP mới gia nhập mặc định là một khách hàng tiêu dùng bền vũ trọn đời của hệ thống.
* *Dẫn chứng kiểm chứng:* 
  - Theo cơ chế trả thưởng tại [phan-tich-co-che-kinh-doanh.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/phan-tich-co-che-kinh-doanh.md#L72-L76), để nhận tối đa quyền lợi hoa hồng bảo trợ trực tiếp (Sponsor Bonus), NPP mới cần kích hoạt các gói tích lũy cá nhân có giá trị ban đầu lớn (ví dụ gói Gold/VIP là 10.000 CV, tương đương khoảng 4.000.000 VNĐ). 
  - Điều này đòi hỏi NPP phải chịu chi phí cơ hội về vốn và thời gian hoạt động. Nếu NPP không được đào tạo kỹ năng bán hàng và tuyển dụng đúng quy trình để tạo ra thu nhập bù đắp, họ sẽ dừng hoạt động và ngừng tiêu dùng để cắt lỗ. Do đó, doanh số tiêu dùng từ NPP chỉ được tính toán dựa trên mức năng động tối thiểu hàng tháng từ **1.000 CV - 2.000 CV/tháng**, không gộp chung với doanh số mua gói ban đầu của NPP mới trong dài hạn.

### 2. Đánh giá thực tế về tốc độ nhân bản hệ thống Nhị phân lai Mặt trời
* *Lập luận phổ biến:* Giả định hệ thống nhị phân sẽ nhân bản cân bằng tuyệt đối theo cấp số nhân ($2 \rightarrow 4 \rightarrow 8 \rightarrow 16 \dots$) để nhanh chóng đạt quy mô hàng ngàn thành viên.
* *Dẫn chứng kiểm chứng:*
  - Sơ đồ Vinalink chi trả hoa hồng chu kỳ nhóm dựa trên doanh số phát sinh tại **nhánh yếu hơn** (trước Director: chu kỳ 3.000 CV Trái - 3.000 CV Phải nhận 300.000 VNĐ; từ Director trở lên: chu kỳ 7.000 CV Trái - 7.000 CV Phải nhận 560.000 VNĐ theo [phan-tich-co-che-kinh-doanh.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/phan-tich-co-che-kinh-doanh.md#L62-L68)).
  - Trong thực tế vận hành, hiện tượng lệch nhánh (nhánh mạnh phát triển vượt trội so với nhánh yếu) là đặc tính cố hữu của sơ đồ nhị phân. Mặc dù doanh số dư ở nhánh mạnh được bảo lưu trọn đời, dòng tiền hoa hồng thực tế nhận được hàng tháng của doanh chủ hoàn toàn bị giới hạn bởi tốc độ phát triển của nhánh yếu.
  - **Quy ước:** Kế hoạch kinh doanh 3 năm sẽ sử dụng kịch bản lệch nhánh thực tế (tỷ lệ phân bổ doanh số Nhánh Mạnh/Nhánh Yếu là 70/30 hoặc 80/20) để tính toán thu nhập dòng tiền thực tế cho doanh chủ, thay vì giả định cân nhánh lý tưởng 50/50.

---

## V. QUY TRÌNH XÁC THỰC SỐ LIỆU ĐẦU VÀO KHI LẬP KẾ HOẠCH
Mọi số liệu lịch sử dùng làm điểm xuất phát cho kế hoạch 3 năm cần được Doanh chủ trích xuất trực tiếp từ Văn phòng trực tuyến (VPOL) của Vinalink để đảm bảo tính xác thực:
1. **Số lượng NPP hoạt động thực tế:** NPP có phát sinh điểm năng động cá nhân hoặc bảo trợ trực tiếp trong 3 tháng gần nhất.
2. **Doanh số phát sinh thực tế tại Nhánh Yếu hàng tháng** (CV/tháng).
3. **Tỷ lệ KHTT có mã số mua hàng hoạt động ổn định.**

*Trường hợp khởi nghiệp hệ thống mới (chưa có sẵn số liệu cũ):* Lộ trình 3 năm sẽ thiết lập 3 tháng đầu tiên là **Giai đoạn Kiểm chứng thực địa (Field Validation Phase)** nhằm đo lường năng lực bán lẻ và bảo trợ thực tế của chính doanh chủ trước khi áp dụng công thức nhân bản quy mô.

---

## VI. KHUNG HƯỚNG DẪN RÀNG BUỘC KHI TRẢ LỜI DOANH-CHU-CHECKLIST.MD
Mục này cung cấp hướng dẫn tư duy logic để Doanh chủ tự điền thông tin vào [doanh-chu-checklist.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/doanh-chu-checklist.md) một cách thực tế, tránh các mục tiêu mơ hồ hoặc không khả thi về mặt vận hành.

### 1. Ràng buộc Mục tiêu Tài chính (Phần 1 của Checklist)
* **Yêu cầu:** Khai báo mục tiêu thu nhập thụ động qua 3 năm (Năm 1, Năm 2, Năm 3).
* **Hướng dẫn logic:** Doanh chủ bắt buộc phải quy đổi mức thu nhập mong muốn thành **doanh số nhánh yếu (CV)** tương ứng dựa trên cơ chế trả thưởng chu kỳ nhóm.
* **Công thức đối chiếu nhanh:**
  $$\text{Doanh số nhánh yếu yêu cầu (CV/tháng)} \approx \frac{\text{Thu nhập mục tiêu (VNĐ/tháng)}}{560.000 \text{ VNĐ}} \times 7.000 \text{ CV}$$
  *(Công thức áp dụng đối với cấp bậc từ Director trở lên theo quy định tại [phan-tich-co-che-kinh-doanh.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/phan-tich-co-che-kinh-doanh.md#L66-L67))*
* **Ví dụ mẫu:** Để đạt mục tiêu thu nhập thụ động **50.000.000 VNĐ/tháng**:
  - Số chu kỳ cân nhánh yếu cần đạt mỗi tháng: $50.000.000 / 560.000 \approx 89 \text{ chu kỳ}$.
  - Doanh số bắt buộc phải phát sinh mới tại nhánh yếu: $89 \times 7.000 \text{ CV} = 623.000 \text{ CV/tháng}$ (tương đương khoảng **250.000.000 VNĐ** doanh số bán sản phẩm phát sinh ở nhánh yếu mỗi tháng).

### 2. Ràng buộc Quy mô & Cấu trúc Hệ thống (Phần 2 của Checklist)
* **Yêu cầu:** Xác định số lượng F1 nòng cốt (Key Leaders) và tổng quy mô mạng lưới.
* **Hướng dẫn logic:** 
  - **Giới hạn số F1 nòng cốt:** Doanh chủ chỉ nên đặt mục tiêu dẫn dắt sâu tối đa **3 - 5 F1 nòng cốt** trong giai đoạn đầu. Việc cố gắng hỗ trợ cùng lúc nhiều hơn 5 F1 sẽ dẫn đến quá tải năng lực cá nhân và làm giảm chất lượng chuyển đổi quy trình EMC.
  - **Cơ cấu phân bổ:** Nếu lựa chọn cơ cấu 80% tiêu dùng - 20% kinh doanh, kế hoạch kinh doanh bắt buộc phải phân bổ phần lớn nguồn lực cho chiến dịch marketing sản phẩm và phát triển hệ thống KHTT mua hàng tự động qua mã số giá sỉ.

### 3. Ràng buộc Nguồn lực Đầu vào (Phần 4 của Checklist)
* **Yêu cầu:** Khai báo thời gian cam kết mỗi ngày và ngân sách đầu tư ban đầu.
* **Hướng dẫn logic (Ma trận Tương xứng):**
  - **Thời gian:** Thời gian cam kết phải tương thích với mục tiêu chức danh nhóm (Group Title). Nếu thời gian cam kết $< 2$ giờ/ngày ($< 14$ giờ/tuần), mô hình sẽ được cố vấn định hình ở quy mô **Làm thêm/Tiêu dùng thông minh** (Thu nhập mục tiêu $< 10$ triệu/tháng). Để xây dựng hệ thống đạt danh hiệu từ Ruby trở lên (yêu cầu tích lũy tối thiểu 1.100.000 CV theo [phan-tich-co-che-kinh-doanh.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/phan-tich-co-che-kinh-doanh.md#L30)), doanh chủ cần cam kết tối thiểu từ $4$ giờ/ngày trở lên.
  - **Ngân sách:** Nếu ngân sách ban đầu là $0$ đồng, lộ trình tuyển dụng và marketing bắt buộc phải tối ưu hóa phương thức tiếp cận trực tiếp (Word of Mouth) hoặc tận dụng tài liệu miễn phí của Vinalink (VPOL), loại bỏ các kế hoạch chạy quảng cáo trả phí hoặc xây dựng phễu tự động hóa phức tạp.

### 4. Ràng buộc Khung Định vị Tuyển dụng Tinh gọn (Phần 5 của Checklist)
* **Trụ cột A (Leader Value Proposition - LVP - Câu A1):** Chỉ được chọn **tối đa 2 giá trị hỗ trợ cốt lõi** mà doanh chủ tự tin thực hiện tốt nhất cho người mới trong 30 ngày đầu tiên (ví dụ: quy trình EMC đào tạo sản phẩm hoặc đồng hành chia sẻ OPP 2-1). Việc chọn tất cả sẽ làm phân tán nguồn lực của doanh chủ.
* **Trụ cột B (Ideal Downline Profiling - IDP - Câu B1):** Bắt buộc **chọn duy nhất 1 phân khúc khách hàng/tuyến dưới mục tiêu ưu tiên** cho chiến dịch khởi động (ví dụ: chỉ tập trung vào nhóm Người làm thêm kiếm thu nhập thụ động). Việc định vị đa mục tiêu từ đầu sẽ làm loãng thông điệp tuyển dụng.
* **Trụ cột C (Qualification Filters - Câu C2):** Bắt buộc thiết lập **ít nhất 1 chỉ số hành động cụ thể** để lọc cam kết của thành viên mới trước khi chuyển giao sâu quy trình EMC (ví dụ: Hoàn thành khóa học pháp lý cơ bản của Bộ Công Thương đăng ký bởi Vinalink trong vòng 3 ngày theo [vinalink-parent-research.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/vinalink-parent-research.md#L13)).
