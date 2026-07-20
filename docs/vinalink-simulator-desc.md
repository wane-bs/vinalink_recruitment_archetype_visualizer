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

## III. CHI TIẾT GIẢI THUẬT VÀ CÔNG THỨC TOÁN HỌC

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

---

## IV. NỘI DUNG THĂNG CẤP DANH HIỆU

### 1. Điều kiện doanh số và ràng buộc danh hiệu F1
Cấp bậc cá nhân (Bronze, Silver, Gold) thể hiện mức tích lũy doanh số mua hàng cá nhân. Trong khi đó, **Danh hiệu** thể hiện mức tích lũy doanh số nhóm và cơ cấu phát triển tuyến dưới trực hệ:

* **Manager**: Doanh số tích lũy đạt $80.000\text{ CV}$.
* **Senior Manager**: Doanh số tích lũy đạt $240.000\text{ CV}$.
* **Director**: Doanh số tích lũy đạt $550.000\text{ CV}$.
* **Ruby**: Doanh số tích lũy đạt $1.100.000\text{ CV}$.
* **Emerald**: Doanh số tích lũy đạt $2.200.000\text{ CV}$.
* **Diamond**: Doanh số tích lũy đạt $4.400.000\text{ CV}$.
* **Blue Diamond**: Doanh số tích lũy đạt $6.600.000\text{ CV}$, đồng thời mỗi nhánh (Trái & Phải) phải có tối thiểu **01 F1** đạt danh hiệu **Diamond**.
* **Black Diamond**: Doanh số tích lũy đạt $10.000.000\text{ CV}$, đồng thời mỗi nhánh phải có tối thiểu **01 F1** đạt danh hiệu **Blue Diamond**.
* **Crown Diamond**: Doanh số tích lũy đạt $15.000.000\text{ CV}$, đồng thời mỗi nhánh phải có tối thiểu **01 F1** đạt danh hiệu **Black Diamond**.
* **Ambassador**: Doanh số tích lũy đạt $22.000.000\text{ CV}$, đồng thời mỗi nhánh phải có tối thiểu **01 F1** đạt danh hiệu **Crown Diamond**.

### 2. Mô phỏng cơ cấu F1 trong giải thuật
Trong mô phỏng vĩ mô của `vinalink-simulator.py`, doanh số tích lũy 1 năm của F1 mạnh nhất ở mỗi nhánh (nhánh yếu và nhánh mạnh) được giả lập đóng góp $50\%$ tổng doanh số tích lũy của nhánh đó:
$$CV_{weak\_accumulated\_F1} = (CV_{weak} \times 0.5) \times 12$$
$$CV_{strong\_accumulated\_F1} = (CV_{strong} \times 0.5) \times 12$$

Hàm `determine_final_title` sẽ duyệt qua danh sách danh hiệu từ thấp đến cao, tự động tra cứu danh hiệu của các F1 này. Nếu Doanh chủ đạt mốc doanh số của danh hiệu cao (từ Blue Diamond trở lên) nhưng F1 ở một trong hai nhánh không đạt danh hiệu kế cận tương ứng, danh hiệu của Doanh chủ sẽ bị **nghẽn (capped)** tại cấp bậc tối đa mà cấu trúc F1 đáp ứng được.

---

## V. HOA HỒNG DOANH SỐ NHÓM (GVC) & TRẦN MAXOUT

### 1. Chu kỳ cân nhánh nhóm
* **Dưới danh hiệu Director** ($CV_{accumulated} < 550.000\text{ CV}$): Chu kỳ cân nhánh là $3.000\text{ CV}$ nhánh yếu, hoa hồng nhận được cho mỗi chu kỳ là $300.000\text{ VNĐ}$ ($10\%$ doanh số nhánh yếu).
* **Đạt danh hiệu Director trở lên** ($CV_{accumulated} \ge 550.000\text{ CV}$): Chu kỳ cân nhánh là $7.000\text{ CV}$ nhánh yếu, hoa hồng nhận được cho mỗi chu kỳ là $560.000\text{ VNĐ}$ ($8\%$ doanh số nhánh yếu).
* **Số chu kỳ ($C$):** $C = \lfloor \frac{CV_{weak}}{CV_{cycle}} \rfloor$.
* **Hoa hồng Chu kỳ thô:** $Income_{gvc\_raw} = C \times Bonus_{cycle}$.

### 2. Trần hoa hồng chu kỳ nhóm (Maxout Limit)
Để bảo toàn quỹ thưởng, Vinalink áp dụng trần hoa hồng chu kỳ nhóm hàng tháng dựa trên Danh hiệu và Cấp bậc cá nhân:
$$Income_{gvc} = \min(Income_{gvc\_raw}, Limit_{maxout}(Title, Rank_{personal}))$$

---

## VI. HOA HỒNG CỘNG HƯỞNG (MATCHING BONUS)

### 1. Cơ sở tính Hoa hồng Cộng hưởng
Hoa hồng Cộng hưởng được tính toán dựa trên ba yếu tố:
1. Danh hiệu hiện tại của Doanh chủ.
2. Doanh số nhánh yếu thực tế phát sinh trong tháng làm điều kiện kích hoạt.
3. Hoa hồng chu kỳ nhóm của các thành viên trực hệ thuộc 5 tầng gần nhất (F1 - F5).

### 2. Cơ cấu phân bổ theo Danh hiệu và Doanh số nhánh yếu

* **Director, Ruby, Emerald:**
  * Điều kiện doanh số nhánh yếu tháng hiện tại đạt từ: **$85.000\text{ CV}$**.
  * Mức hưởng: **$10\%$** hoa hồng chu kỳ của tất cả F1 và F2.
* **Diamond, Blue Diamond, Black Diamond:**
  * Điều kiện doanh số nhánh yếu tháng hiện tại đạt từ: **$300.000\text{ CV}$**.
  * Mức hưởng: **$10\%$** của F1, F2 và cộng thêm **$5\%$** của F3.
* **Crown Diamond:**
  * Điều kiện doanh số nhánh yếu tháng hiện tại đạt từ: **$700.000\text{ CV}$**.
  * Mức hưởng: **$10\%$** của F1, F2 và cộng thêm **$5\%$** của F3, F4.
* **Ambassador:**
  * Điều kiện doanh số nhánh yếu tháng hiện tại đạt từ: **$3.000.000\text{ CV}$**.
  * Mức hưởng: **$10\%$** của F1, F2 và cộng thêm **$5\%$** của F3, F4, F5.

### 3. Mô phỏng thu nhập Matching Bonus F1-F5 trong giải thuật
Trong mô hình nhị phân phân rã trực hệ, số lượng NPP ở tầng $k$ ($k \in [1, 5]$) được giới hạn tối đa theo cấp số nhân nhị phân $2^k$:
$$N_{npp}(k) = 2^k \times R_{retention}$$

* Doanh số nhánh yếu trung bình của một NPP ở tầng $k$:
  $$CV_{weak}(k) = \frac{CV_{weak}}{2^k}$$
* Doanh số tích lũy 1 năm của NPP ở tầng $k$:
  $$CV_{accumulated}(k) = \frac{CV_{total}}{2^k} \times 12$$
  *Hệ thống dùng $CV_{accumulated}(k)$ để tra cứu danh hiệu của NPP tầng $k$, từ đó xác định kích thước chu kỳ ($CV_{cycle}(k)$) và trần Maxout tương ứng của họ.*
* Số chu kỳ trung bình của một NPP ở tầng $k$:
  $$C(k) = \lfloor \frac{CV_{weak}(k)}{CV_{cycle}(k)} \rfloor$$
* Hoa hồng chu kỳ nhóm nhận được của NPP ở tầng $k$ (sau khi áp trần Maxout):
  $$Income_{gvc}(k) = \min(C(k) \times Bonus_{cycle}(k), Limit_{maxout}(Title(k), Gold))$$
* Tổng Hoa hồng Cộng hưởng nhận được của Doanh chủ từ tất cả các tầng được hưởng:
  $$Income_{matching} = \sum_{k=1}^{5} N_{npp}(k) \times Income_{gvc}(k) \times Rate_{matching}(k)$$

---

## VII. THƯỞNG DUY TRÌ DOANH SỐ (QUALIFY BONUS)
Được chi trả hàng tháng dựa trên các mốc doanh số nhánh yếu thực tế đạt được trong tháng (cộng gộp tất cả các mốc đạt được, tối đa 1 chu kỳ reset):
$$Income_{qualify} = \sum_{m \in M} Bonus_{qualify}(m, Rank_{personal}) \times 1.000\text{ VNĐ}$$
*Trong đó $M = \{80.000, 240.000, 550.000\}$ CV.*

---

## VIII. TỔNG THU NHẬP ƯỚC TÍNH HÀNG THÁNG
Tổng thu nhập thụ động hàng tháng của Doanh chủ được tính bằng:
$$Income_{total} = Income_{gvc} + Income_{qualify} + Income_{matching} + (Income_{gvc} \times 0.10)$$
*(Trong đó khoản $Income_{gvc} \times 0.10$ ước tính cho các loại hoa hồng hỗ trợ bảo trợ trực tiếp và các quỹ toàn quốc khác).*
