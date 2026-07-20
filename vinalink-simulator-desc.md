# GIẢI THUẬT VÀ MÔ TẢ BỘ MÔ PHỎNG KẾ HOẠCH KINH DOANH VINALINK 3 NĂM

**Tài liệu mã số:** VNL-2026-SIM-01
**Dự án:** Lập Kế hoạch Kinh doanh 3 năm - Doanh chủ Vinalink
**Mô phỏng bằng mã nguồn:** [vinalink-simulator.py](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/vinalink-simulator.py)
**Đơn vị phát triển:** SIHUB Lean Startup Team

---

## I. MỤC TIÊU BỘ MÔ PHỎNG
Bộ mô phỏng tài chính được xây dựng nhằm mục đích phản biện định lượng tính khả thi của các mục tiêu tài chính mà Doanh chủ đặt ra trong kế hoạch 3 năm. Thay vì dựa trên các con số dự phóng cảm tính, bộ mô phỏng áp dụng trực tiếp các quy tắc và điều khoản thực tế của **Sơ đồ trả thưởng Vinalink Group** đã được Bộ Công Thương phê duyệt, kết hợp với các tham số hao hụt tự nhiên của mô hình kinh doanh hệ thống (MLM).

---

## II. CÁC THAM SỐ ĐẦU VÀO (INPUT VARIABLES)
Bộ mô phỏng cho phép cố vấn cấu hình các tham số thực tế của mạng lưới bao gồm:

1. **Quy mô hệ thống tối đa ($N_{total}$):** Tổng số lượng thành viên trong mạng lưới tích lũy sau 3 năm.
2. **Tỷ lệ phân bổ Khách hàng / Nhà phân phối:**
   * Tỷ lệ Khách hàng thân thiết tiêu dùng ($P_{consumer}$): Mặc định là $80\%$.
   * Tỷ lệ Nhà phân phối kinh doanh ($P_{distributor}$): Mặc định là $20\%$.
3. **Tỷ lệ giữ chân Nhà phân phối ($R_{retention}$):** Tỷ lệ NPP duy trì hoạt động năng động hàng tháng thực tế (dao động từ $30\% - 50\%$ do hao hụt tự nhiên).
4. **Mức tiêu dùng trung bình hàng tháng:**
   * Doanh số KHTT tiêu dùng trung bình ($V_{consumer\_cv}$): Mặc định là $1.000\text{ CV/tháng}$ ($\approx 2.500.000\text{ VNĐ}$).
   * Doanh số NPP năng động trung bình ($V_{distributor\_cv}$): Mặc định là $2.000\text{ CV/tháng}$ ($\approx 5.000.000\text{ VNĐ}$).
5. **Tỷ lệ lệch nhánh Nhị phân ($R_{split}$):** Tỷ lệ phân bổ doanh số giữa nhánh Mạnh và nhánh Yếu (ví dụ: tỷ lệ lệch $70/30$ tương đương $R_{split} = 0.7$ cho nhánh Mạnh).
6. **Cấp bậc cá nhân của Doanh chủ ($Rank_{personal}$):** Có 3 cấp bậc là Đồng (Bronze), Bạc (Silver), và Vàng/VIP (Gold).

---

## III. GIẢI THUẬT VÀ CÔNG THỨC TOÁN HỌC ĐỊNH LƯỢNG

### 1. Số lượng thành viên hoạt động thực tế
* Số lượng Khách hàng thân thiết hoạt động:
  $$N_{consumer} = N_{total} \times P_{consumer}$$
* Số lượng Nhà phân phối hoạt động thực tế hàng tháng:
  $$N_{active\_distributor} = (N_{total} \times P_{distributor}) \times R_{retention}$$

### 2. Tổng doanh số phát sinh hàng tháng ($CV_{total}$)
Tổng doanh số phát sinh hàng tháng (tính theo đơn vị điểm CV - Commission Volume):
$$CV_{total} = (N_{consumer} \times V_{consumer\_cv}) + (N_{active\_distributor} \times V_{distributor\_cv})$$

### 3. Doanh số nhánh Yếu ($CV_{weak}$) và nhánh Mạnh ($CV_{strong}$)
Dựa trên tỷ lệ lệch nhánh nhị phân $R_{split}$ (trong đó $R_{split} \ge 0.5$):
$$CV_{strong} = CV_{total} \times R_{split}$$
$$CV_{weak} = CV_{total} \times (1 - R_{split})$$

### 4. Tính toán Hoa hồng Chu kỳ nhóm (Group Volume Commission - GVC)
Mô hình trả thưởng nhị phân của Vinalink quy định:
* **Điều kiện thăng chức danh:** Danh hiệu được thăng cấp dựa trên tổng doanh số nhóm tích lũy lũy kế ($CV_{accumulated} = CV_{total} \times 12$ tháng).
* **Định nghĩa chu kỳ cân nhánh:**
  * Nếu chưa đạt danh hiệu Director ($CV_{accumulated} < 550.000\text{ CV}$): Chu kỳ cân nhánh là $3.000\text{ CV}$ nhánh yếu, hoa hồng nhận được cho mỗi chu kỳ là $300.000\text{ VNĐ}$ (tương đương $10\%$ doanh số nhánh yếu).
  * Nếu đạt danh hiệu Director trở lên ($CV_{accumulated} \ge 550.000\text{ CV}$): Chu kỳ cân nhánh là $7.000\text{ CV}$ nhánh yếu, hoa hồng nhận được cho mỗi chu kỳ là $560.000\text{ VNĐ}$ (tương đương $8\%$ doanh số nhánh yếu).
* **Công thức tính số chu kỳ ($C$):**
  $$C = \lfloor \frac{CV_{weak}}{CV_{cycle}} \rfloor$$
  *Trong đó $CV_{cycle} \in \{3000, 7000\}$ tùy thuộc vào danh hiệu.*
* **Hoa hồng Chu kỳ thô:**
  $$Income_{gvc\_raw} = C \times Bonus_{cycle}$$
  *Trong đó $Bonus_{cycle} \in \{300000, 560000\}\text{ VNĐ}$.*

### 5. Áp dụng Trần hoa hồng chu kỳ (Maxout Limit)
Để bảo toàn quỹ thưởng công ty, Vinalink áp dụng trần hoa hồng chu kỳ hàng tháng dựa trên Cấp bậc cá nhân (Bronze, Silver, Gold) và Danh hiệu thăng cấp (Senior Manager, Director, Ruby, Emerald, Diamond, v.v.):
$$Income_{gvc} = \min(Income_{gvc\_raw}, Limit_{maxout}(Title, Rank_{personal}))$$

*Ví dụ: Trần Maxout của danh hiệu Ruby tương ứng với các cấp bậc cá nhân là:*
* *Bronze:* $150.000.000\text{ VNĐ/tháng}$
* *Silver:* $300.000.000\text{ VNĐ/tháng}$
* *Gold:* $600.000.000\text{ VNĐ/tháng}$

### 6. Tính toán Thưởng duy trì doanh số (Qualify Volume Bonus)
Khoản thưởng này được chi trả hàng tháng dựa trên các mốc doanh số nhánh yếu thực tế đạt được trong tháng đó. Doanh nghiệp được cộng gộp tất cả các mốc đạt được (mức cộng dồn lũy kế tối đa 1 chu kỳ reset):
$$Income_{qualify} = \sum_{m \in M} Bonus_{qualify}(m, Rank_{personal}) \times 1.000\text{ VNĐ}$$
*Trong đó $M = \{80.000, 240.000, 550.000\}$ là các mốc doanh số nhánh yếu tính theo CV.*

*Bảng tra cứu điểm thưởng Qualify Bonus theo mốc doanh số nhánh yếu hàng tháng:*
| Cấp bậc cá nhân | Mốc 80.000 CV | Mốc 240.000 CV | Mốc 550.000 CV | Tổng cộng nhận được |
| :--- | :---: | :---: | :---: | :---: |
| **Bronze** | 5.000 CV | 10.000 CV | 25.000 CV | **40.000 CV** ($\approx 40\text{ triệu VNĐ}$) |
| **Silver** | 10.000 CV | 15.000 CV | 30.000 CV | **55.000 CV** ($\approx 55\text{ triệu VNĐ}$) |
| **Gold** | 10.000 CV | 22.000 CV | 38.000 CV | **70.000 CV** ($\approx 70\text{ triệu VNĐ}$) |

### 7. Tính các khoản hoa hồng khác và Tổng thu nhập thụ động
Các khoản hoa hồng khác (Bảo trợ trực tiếp Sponsor Bonus, Hoa hồng cộng hưởng Matching Bonus hưởng sâu F1 - F5 từ thu nhập chu kỳ của tuyến dưới, Quỹ Lãnh đạo toàn quốc) được ước tính bằng $30\%$ hoa hồng chu kỳ nhóm thực tế nhận được:
$$Income_{others} = Income_{gvc} \times 0.30$$
Tổng thu nhập thụ động hàng tháng ước tính:
$$Income_{total} = Income_{gvc} + Income_{qualify} + Income_{others}$$

---

## IV. CẤU TRÚC MÃ NGUỒN PYTHON
Tệp [vinalink-simulator.py](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/vinalink-simulator.py) triển khai giải thuật trên qua 2 hàm chính:
* `simulate(...)`: Nhận các tham số đầu vào và trả về một từ điển (`dict`) kết quả định lượng chi tiết.
* `main()`: Cung cấp giao diện CLI (Command Line Interface) sử dụng thư viện `argparse` để chạy mô phỏng trực tiếp từ terminal.

### Cách chạy mô phỏng từ dòng lệnh:
Chạy với các tham số mặc định (Quy mô 10.000 người, tỷ lệ giữ chân 30%, lệch nhánh 70/30, cấp bậc Vàng):
```bash
python vinalink-simulator.py
```

Chạy với các cấu hình tùy biến (ví dụ: Quy mô 5.000 người, tỷ lệ giữ chân 50%, lệch nhánh cân bằng hơn 60/40, cấp bậc Bạc):
```bash
python vinalink-simulator.py --size 5000 --retention 0.5 --split 0.6 --rank SILVER
```
