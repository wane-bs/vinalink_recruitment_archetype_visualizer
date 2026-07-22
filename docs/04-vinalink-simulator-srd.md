# SYSTEM REQUIREMENT DOCUMENT (SRD)
## MÔ HÌNH TOÁN HỌC & YÊU CẦU KỸ THUẬT BỘ MÔ PHỎNG VINALINK GROUP 36 THÁNG

**Mã tài liệu:** VNL-2026-SRD-04  
**Dự án:** Lập Kế hoạch Kinh doanh 3 năm - Doanh chủ Vinalink  
**Đơn vị xây dựng:** SIHUB Lean Startup Team  
**Ngày phát hành:** 22-07-2026  
**Trạng thái:** Chính thức phê duyệt  

---

## 1. YÊU CẦU KỸ THUẬT TỔNG THỂ (OVERALL SYSTEM REQUIREMENTS)

### 1.1 Môi trường Thực thi (Execution Environment)
1. **Backend Simulation Engine:** Python 3.10+ (Standard Library, Zero-Dependency Architecture).
2. **Frontend Visualizer UI:** Single-page Web Application (HTML5, Vanilla JavaScript ES6, Bootstrap 5.3 CSS, Bootstrap Icons, Local State Engine).

### 1.2 Yêu cầu Phi chức năng (Non-Functional Requirements - NFR)
* Hiệu năng: Thời gian thực thi $\le 50\text{ ms}$ cho toàn bộ chuỗi 36 tháng.
* Độ chính xác: Sai số quy đổi dòng tiền $< 1\text{ VNĐ}$.
* Tương thích: Hoạt động mượt mà trên Chrome, Firefox, Safari, Edge (Desktop & Mobile).

---

## 2. MÔ HÌNH TOÁN HỌC HỆ THỐNG (MATHEMATICAL SYSTEM MODEL)

### 2.1 Phương trình Tăng trưởng Mạng lưới S-curve (Logistic Growth)
$$N(t) = N_{start} + \frac{N_{total} - N_{start}}{1 + e^{-c \cdot (t - t_0)}}$$
*Trong đó $N_{start}$ là Quy mô mạng lưới hiện tại (nhập từ Baseline), $N_{total}$ là Quy mô mạng lưới mục tiêu sau 36 tháng, $t_0 = 18$, $c = 0.25$.*

### 2.2 Cấu trúc Ma trận Trực hệ F1–F5
$$N_{npp}(k) = n_{f1} \times dup\_factor^{k-1}$$
$$N_{active}(k) = \min(N_{npp}(k), \text{round}(N_{npp}(k) \times R_{retention}))$$

---

## 3. KHUNG BÀI TOÁN QUY HOẠCH TUYẾN TÍNH / TỐI ƯU KÉP (LINEAR & DUAL-OBJECTIVE PROGRAMMING FRAMEWORK)

### 3.1 Véc-tơ Biến Quyết định (Decision Variables)
$$X(t) = \begin{bmatrix} NewF1(t) \\ V_{retail}(t) \\ Hours(t) \end{bmatrix}$$

### 3.2 Hàm Mục tiêu Kép (Dual-Objective Functions)
1. **Tối đa hóa Tổng Thu nhập Thụ động 36 Tháng:**
   $$\max Z_1 = \sum_{t=1}^{36} Income_{total}(X(t))$$
2. **Tối thiểu hóa Áp lực Nguồn lực & Năng lượng Làm việc:**
   $$\min Z_2 = \sum_{t=1}^{36} (Hours(t) - 4)^2 + \lambda \cdot BurnoutRisk(X(t))$$

### 3.3 Hệ Bất phương trình Ràng buộc (Constraints Matrix)
1. **Trần thời gian làm việc:** $4 \le Hours(t) \le 6$ tiếng/ngày, $\forall t \in [1, 36]$.
2. **Giới hạn quản trị F1 nòng cốt:** $\sum_{\tau = \max(1, t-5)}^{t} NewF1(\tau) \le 4$, $\forall t \in [1, 36]$.
3. **Duy trì năng động cá nhân:** $V_{personal}(t) \ge 2.000\text{ CV/tháng}$, $\forall t \in [1, 36]$.
4. **Tăng trưởng mạng lưới S-curve MLM.**

### 3.4 Giải thuật Quy hoạch Tuyến KPIs và Thời gian Làm việc Tối ưu hằng tháng
1. **Giải thuật Phân bổ Tuyển dụng F1 ($NewF1(t)$):**
   $$NewF1(t) = NewDistributors(t) \times \frac{n\_f1\_target - f1\_start}{N_{active\_npp\_target} - npp\_start}$$
   Trong đó:
   * $NewDistributors(t) = N_{active\_distributors}(t) - N_{active\_distributors}(t-1)$
   * $n\_f1\_target$: Mục tiêu F1 nòng cốt sau 3 năm.
   * $f1\_start$: Số lượng F1 nòng cốt hiện tại Baseline.
   * $N_{active\_npp\_target}$: Mục tiêu tổng số NPP hoạt động sau 3 năm.
   * $npp\_start$: Số lượng NPP hoạt động hiện tại Baseline.
2. **Giải thuật Tối ưu Hóa Thời gian làm việc ($Hours(t)$):**
   $$Hours(t) = 4 + 0.5 \times NewF1(t) + 0.1 \times \log_2(N_{active\_distributors}(t))$$
   Với ràng buộc trần:
   $$Hours(t) = \max(4.0, \min(6.0, Hours(t)))$$
   Phương trình này giải quyết bài toán tối ưu hóa nguồn lực: Doanh chủ làm việc tối thiểu 4 tiếng/ngày, tăng thêm 30 phút cho mỗi F1 mới cần bảo trợ, và tăng dần theo quy mô quản lý mạng lưới (logarithm cơ số 2), khống chế tối đa 6 tiếng/ngày để phòng ngừa burnout.
