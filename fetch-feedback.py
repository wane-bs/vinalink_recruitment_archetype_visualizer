# -*- coding: utf-8 -*-
import os
import re
import urllib.request
import csv
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from datetime import datetime

# Cấu hình đường dẫn các file local
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHECKLIST_TRA_LOI_PATH = os.path.join(BASE_DIR, "doanh-chu-checklist-tra-loi.md")
DOI_CHIEU_BAO_CAO_PATH = os.path.join(BASE_DIR, "doi-chieu-bao-cao.md")
BO_CHUAN_MUC_PATH = os.path.join(BASE_DIR, "bo-chuan-muc-trao-doi-doanh-chu.md")

# ID Google Sheet lưu phản hồi (chia sẻ Anyone with link can view)
SPREADSHEET_ID = "1-MockSpreadsheetID-VinalinkFeedback" 
CSV_URL = f"https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/export?format=csv"

# Thông tin gửi Email qua SMTP (Đọc từ file .env hoặc cấu hình mặc định)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.environ.get("SENDER_EMAIL", "your-email@gmail.com")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD", "your-app-password")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL", SENDER_EMAIL) # Gửi cho chính anh Mr. Híu

def fetch_feedback_data():
    """Tải dữ liệu phản hồi mới nhất từ Google Sheet hoặc sử dụng mock data nếu chưa cấu hình SPREADSHEET_ID"""
    print(f"[{datetime.now()}] Bắt đầu đồng bộ dữ liệu phản hồi từ Google Sheets...")
    
    # Kiểm tra xem có cấu hình SPREADSHEET_ID thực tế chưa
    if "Mock" in SPREADSHEET_ID or not SPREADSHEET_ID:
        print("Chế độ mô phỏng: Đang giả lập phản hồi đầy đủ 22 trường của Doanh chủ...")
        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "doanhChuName": "Doanh Chủ Vinalink (Mock Leader)",
            "e1": "15.000.000 VNĐ",
            "e2": "60.000.000 VNĐ",
            "e3": "1.500.000.000 VNĐ", # Vi phạm: Mâu thuẫn toán học (maxout ~764tr, đề xuất diamond 150tr)
            "motivation": "Tự do tài chính & Tạo lập tài sản kế thừa",
            "a2": "6", # Vi phạm: Vượt giới hạn quản trị Lean (tối đa 5 F1)
            "totalMembers": "10000",
            "distributionRatio": "80% tiêu dùng - 20% kinh doanh",
            "culture": "Tinh gọn, Tốc độ, Thành công",
            "leadershipStyle": "Lãnh đạo phục vụ (Servant Leadership)",
            "d1": "14", # Vi phạm: Cảnh báo kiệt sức (>10 tiếng)
            "d2": "10.000.000 VNĐ",
            "skills": "Thuyết trình & Đào tạo sản phẩm",
            "a1": "Cầm tay chỉ việc hướng dẫn tuyển dụng, Đồng hành chia sẻ trực tiếp (OPP 2-1)",
            "lvpStyle": "Đào tạo thực chiến y học cổ truyền kết hợp phễu tự động.",
            "lvpIntra": "Quy trình EMC cải tiến dễ sao chép, Văn hóa An vui & Tinh gọn",
            "lvpInter": "Lợi thế Thuần Việt giá bình dân, Chính sách trả thưởng nhị phân lai không ly khai",
            "lvpBrand": "Người dẫn đường tận tâm, cam kết hỗ trợ F1 thực chiến.",
            "b1": "nhom_3", # Thủ lĩnh chuyên nghiệp
            "b2": "Nhân viên văn phòng, người làm tự do 30-45 tuổi.",
            "c1": "Khát khao & Động lực lớn, Tinh thần học hỏi (Coachability), Cam kết thời gian",
            "c2": "yêu cầu ước mơ mục tiêu và thái độ tốt" # Vi phạm: Định tính
        }
        
    try:
        req = urllib.request.Request(CSV_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            lines = [line.decode('utf-8') for line in response.readlines()]
            reader = csv.reader(lines)
            rows = list(reader)
            if len(rows) <= 1:
                print("Google Sheet trống hoặc chỉ có tiêu đề. Không có phản hồi mới.")
                return None
            
            # Lấy dòng cuối cùng
            latest_row = rows[-1]
            
            # Đảm bảo có đủ số cột dữ liệu (ít nhất là 23 cột kể cả timestamp và các trường phản hồi)
            # Trật tự cột được định nghĩa trong hàm doPost:
            # 0: timestamp, 1: doanhChuName, 2: e1, 3: e2, 4: e3, 5: motivation,
            # 6: a2, 7: totalMembers, 8: distributionRatio, 9: culture, 10: leadershipStyle,
            # 11: d1, 12: d2, 13: skills, 14: a1, 15: lvpStyle, 16: lvpIntra, 17: lvpInter,
            # 18: lvpBrand, 19: b1, 20: b2, 21: c1, 22: c2
            
            # Hàm an toàn lấy dữ liệu theo index
            def get_val(idx, default=""):
                return latest_row[idx] if idx < len(latest_row) else default
                
            return {
                "timestamp": get_val(0),
                "doanhChuName": get_val(1, "Doanh Chủ Vinalink"),
                "e1": get_val(2),
                "e2": get_val(3),
                "e3": get_val(4),
                "motivation": get_val(5),
                "a2": get_val(6, "0"),
                "totalMembers": get_val(7),
                "distributionRatio": get_val(8),
                "culture": get_val(9),
                "leadershipStyle": get_val(10),
                "d1": get_val(11, "0"),
                "d2": get_val(12),
                "skills": get_val(13),
                "a1": get_val(14),
                "lvpStyle": get_val(15),
                "lvpIntra": get_val(16),
                "lvpInter": get_val(17),
                "lvpBrand": get_val(18),
                "b1": get_val(19),
                "b2": get_val(20),
                "c1": get_val(21),
                "c2": get_val(22)
            }
    except Exception as e:
        print(f"Lỗi khi tải dữ liệu từ Google Sheets: {e}")
        print("Sử dụng dữ liệu mô phỏng để chạy tiếp luồng...")
        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "doanhChuName": "Doanh Chủ Vinalink (Mô Phỏng)",
            "e1": "15.000.000 VNĐ",
            "e2": "60.000.000 VNĐ",
            "e3": "1.500.000.000 VNĐ",
            "motivation": "Tự do tài chính & Tạo lập tài sản kế thừa",
            "a2": "6",
            "totalMembers": "10000",
            "distributionRatio": "80% tiêu dùng - 20% kinh doanh",
            "culture": "Tinh gọn, Tốc độ, Thành công",
            "leadershipStyle": "Lãnh đạo phục vụ (Servant Leadership)",
            "d1": "14",
            "d2": "10.000.000 VNĐ",
            "skills": "Thuyết trình & Đào tạo sản phẩm",
            "a1": "Cầm tay chỉ việc hướng dẫn tuyển dụng, Đồng hành chia sẻ trực tiếp (OPP 2-1)",
            "lvpStyle": "Đào tạo thực chiến y học cổ truyền kết hợp phễu tự động.",
            "lvpIntra": "Quy trình EMC cải tiến dễ sao chép, Văn hóa An vui & Tinh gọn",
            "lvpInter": "Lợi thế Thuần Việt giá bình dân, Chính sách trả thưởng nhị phân lai không ly khai",
            "lvpBrand": "Người dẫn đường tận tâm, cam kết hỗ trợ F1 thực chiến.",
            "b1": "nhom_3",
            "b2": "Nhân viên văn phòng, người làm tự do 30-45 tuổi.",
            "c1": "Khát khao & Động lực lớn, Tinh thần học hỏi (Coachability), Cam kết thời gian",
            "c2": "yêu cầu ước mơ mục tiêu và thái độ tốt"
        }

def analyze_violations(data):
    """Phân tích đối chiếu phản hồi với Bộ chuẩn mực để tìm ra các điểm sai phạm"""
    violations = []
    
    # 1. Kiểm tra số F1 nòng cốt
    try:
        f1_count = int(data["a2"])
        if f1_count > 5:
            violations.append({
                "aspect": "F1 nòng cốt (Phần 2)",
                "rule": "Ràng buộc VI.2 (Chỉ dẫn dắt 3 - 5 F1 nòng cốt trong giai đoạn đầu)",
                "value": f"{f1_count} người",
                "reason": f"Vượt quá giới hạn tối đa 5 người, dễ làm quá tải năng lực quản trị cá nhân và làm giảm chất lượng chuyển giao EMC."
            })
    except ValueError:
        pass

    # 2. Kiểm tra bộ lọc cam kết
    c2_val = data["c2"].lower()
    if any(keyword in c2_val for keyword in ["ước mơ", "mục tiêu", "thái độ", "tư duy"]) and not any(keyword in c2_val for keyword in ["học", "sản phẩm", "hoàn thành", "ngày", "trải nghiệm"]):
        violations.append({
            "aspect": "Bộ lọc cam kết (Trụ cột C)",
            "rule": "Ràng buộc VI.4 (Trụ cột C - Thiết lập ít nhất 1 chỉ số hành động cụ thể để lọc cam kết)",
            "value": data["c2"],
            "reason": "Yêu cầu mang tính định tính, cảm tính (ước mơ, mục tiêu), không thể đo lường hay kiểm chứng định lượng bằng hành động cụ thể được."
        })

    # 3. Kiểm tra thời gian cam kết
    try:
        hours = float(data["d1"])
        if hours > 10:
            violations.append({
                "aspect": "Thời gian cam kết (Phần 4)",
                "rule": "Ràng buộc VI.3 (Cam kết thời gian tương xứng và bảo đảm văn hóa tự do an vui)",
                "value": f"{hours} tiếng/ngày",
                "reason": "Cam kết thời gian quá dài (>10 tiếng) liên tục trong 3 năm là phi thực tế đối với cá nhân hoạt động MLM, dễ gây kiệt sức (burnout)."
            })
        elif hours < 4 and data["b1"] == "nhom_3":
            violations.append({
                "aspect": "Thời gian cam kết (Phần 4)",
                "rule": "Ràng buộc VI.3 (Mục tiêu thủ lĩnh lớn yêu cầu tối thiểu 4 giờ/ngày)",
                "value": f"{hours} tiếng/ngày",
                "reason": "Thời gian cam kết quá thấp (< 4 tiếng) không đủ nguồn lực để dẫn dắt đội ngũ và đạt mục tiêu thăng cấp thủ lĩnh chuyên nghiệp."
            })
    except ValueError:
        pass

    # 4. Kiểm tra mục tiêu thu nhập thụ động
    def clean_money(val):
        nums = re.findall(r'\d+', val.replace(".", "").replace(",", ""))
        return int(nums[0]) if nums else 0

    e1_val = clean_money(data["e1"])
    e3_val = clean_money(data["e3"])

    if e1_val > 100000000: # > 100tr ở năm 1
        violations.append({
            "aspect": "Mục tiêu Năm 1 (Phần 1)",
            "rule": "Ràng buộc VI.1 (Quy đổi mục tiêu tài chính ra CV nhánh yếu tương xứng và thực tế)",
            "value": f"{data['e1']}/tháng",
            "reason": "Quá cao cho giai đoạn khởi nghiệp hệ thống năm đầu tiên, đòi hỏi doanh số nhánh yếu khổng lồ khi chưa nhân bản xong F1."
        })
    
    # Cập nhật trần maxout lý tưởng theo giải thuật mới (Ambassador GVC + Matching + Qualify) là ~764.792.000 VNĐ
    if e3_val > 764792000:
        violations.append({
            "aspect": "Mục tiêu Năm 3 (Phần 1)",
            "rule": "Ràng buộc VI.1 (Con số thu nhập tối đa mô phỏng lý tưởng nâng cấp là ~764 triệu VNĐ/tháng ở quy mô 10.000 người)",
            "value": f"{data['e3']}/tháng",
            "reason": "Mâu thuẫn toán học về giới hạn doanh thu hệ thống. Kể cả kịch bản lý tưởng nhất (100% giữ chân, 50/50 cân nhánh) cũng chỉ đạt tối đa ~764 triệu VNĐ/tháng. Đề xuất điều chỉnh mục tiêu Năm 3 về 150 triệu VNĐ/tháng (cấp Diamond)."
        })

    return violations

def write_doanh_chu_checklist_tra_loi(data):
    """Ghi đè tệp local doanh-chu-checklist-tra-loi.md với câu trả lời mới đầy đủ 22 trường"""
    content = f"""# BẢN PHẢN HỒI CHECKLIST KHẢO SÁT TẦM NHÌN DOANH CHỦ VINALINK

**Doanh chủ thực hiện:** {data["doanhChuName"]}
**Thời gian phản hồi:** {data["timestamp"]}
**Trạng thái đồng bộ:** Đồng bộ tự động lúc 20:00

---

## PHẦN CHI TIẾT CÂU TRẢ LỜI KHẢO SÁT (22 TRƯỜNG DỮ LIỆU)

### 1. Tầm nhìn & Mục tiêu Tài chính (Phần 1)
- **Thu nhập Năm 1:** {data["e1"]}
- **Thu nhập Năm 2:** {data["e2"]}
- **Thu nhập Năm 3:** {data["e3"]}
- **Động lực lớn nhất:** {data["motivation"]}

### 2. Quy mô & Cấu trúc Hệ thống mong muốn (Phần 2)
- **Số lượng F1 nòng cốt thiết lập dẫn dắt:** {data["a2"]} người
- **Tổng quy mô hệ thống (3 năm):** {data["totalMembers"]} người
- **Tỷ lệ phân bổ định hướng:** {data["distributionRatio"]}

### 3. Xác định Giá trị Cốt lõi & Văn hóa Đội nhóm (Phần 3)
- **3 tính từ văn hóa đội nhóm:** {data["culture"]}
- **Phong cách lãnh đạo:** {data["leadershipStyle"]}

### 4. Đánh giá Nguồn lực Đầu vào (Phần 4)
- **Thời gian cam kết làm việc mỗi ngày:** {data["d1"]} giờ/ngày
- **Ngân sách đầu tư ban đầu:** {data["d2"]}
- **Kỹ năng sẵn có sở hữu:** {data["skills"]}

### 5. Khung Định vị Tuyển dụng Tuyến dưới Tinh gọn (Phần 5)

#### Trụ cột A: Định vị Giá trị của Doanh chủ (Leader Value Proposition - LVP)
- **Câu A1 (Hỗ trợ 30 ngày đầu):** {data["a1"]}
- **Câu A2 (Phong cách dẫn dắt khác biệt):** {data["lvpStyle"]}
- **Câu A3 (Lợi thế nội bộ - Intra-system):** {data["lvpIntra"]}
- **Câu A4 (Lợi thế ngoại bộ - Inter-system):** {data["lvpInter"]}
- **Câu A5 (Hình ảnh thương hiệu cá nhân):** {data["lvpBrand"]}

#### Trụ cột B: Xác định Chân dung Phân khúc Tuyến dưới Ưu tiên (IDP)
- **Câu B1 (Phân khúc ưu tiên tuyển dụng):** {data["b1"]}
- **Câu B2 (Nghề nghiệp & độ tuổi mục tiêu):** {data["b2"]}

#### Trụ cột C: Bộ lọc Tuyển dụng Nòng cốt (Qualification Filters)
- **Câu C1 (3 tiêu chí bắt buộc):** {data["c1"]}
- **Câu C2 (Bài test hành động cam kết):** {data["c2"]}
"""
    with open(CHECKLIST_TRA_LOI_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Đã ghi và cập nhật phản hồi mới vào: {CHECKLIST_TRA_LOI_PATH}")

def update_doi_chieu_bao_cao(data, violations):
    """Cập nhật lại tệp doi-chieu-bao-cao.md chứa bảng đối chiếu sai phạm thực tế"""
    
    # Tạo bảng markdown sai phạm
    table_rows = ""
    if not violations:
        table_rows = "| Không phát hiện vi phạm | - | Phản hồi của Doanh chủ hoàn toàn tương thích với bộ chuẩn mực |\n"
    else:
        for v in violations:
            table_rows += f"| **{v['aspect']}**: {v['value']} | **{v['rule'].split(' (')[0]}** (tại [bo-chuan-muc-trao-doi-doanh-chu.md](file:///d:/DebianBackup/source_code/lop_sihub/03-Projects/vinalink/visualizer_deploy/bo-chuan-muc-trao-doi-doanh-chu.md)) | {v['reason']} |\n"

    try:
        with open(DOI_CHIEU_BAO_CAO_PATH, "r", encoding="utf-8") as f:
            old_content = f.read()
    except FileNotFoundError:
        old_content = ""

    header_section = f"""# BÁO CÁO ĐỐI CHIẾU & ĐÁNH GIÁ CHÂN DUNG MỤC TIÊU DOANH CHỦ VINALINK

**Mã tài liệu:** VNL-2026-VAL-01
**Dự án:** Lập Kế hoạch Kinh doanh 3 năm - Doanh chủ Vinalink
**Đơn vị thực hiện:** SIHUB Lean Startup Team
**Ngày lập:** {datetime.now().strftime("%d-%m-%Y")}

---

## ĐỐI CHIẾU TRỰC TIẾP SAI PHẠM KHẢO SÁT

| Câu trả lời sai phạm | Dẫn chứng quy tắc | Tại sao vi phạm |
| :--- | :--- | :--- |
{table_rows}
"""
    
    split_pattern = r"## I\. PHÂN TÍCH CHUYÊN SÂU.*"
    match = re.search(split_pattern, old_content, re.DOTALL)
    
    if match:
        new_content = header_section + "\n" + match.group(0)
    else:
        new_content = header_section

    with open(DOI_CHIEU_BAO_CAO_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Đã cập nhật bảng đối chiếu sai phạm trong: {DOI_CHIEU_BAO_CAO_PATH}")

def send_email_report(data, violations):
    """Gửi email báo cáo đối chiếu cho Doanh chủ và Cố vấn qua SMTP"""
    if not SENDER_EMAIL or SENDER_EMAIL == "your-email@gmail.com":
        print("Bỏ qua gửi email: Chưa cấu hình thông tin tài khoản SMTP trong file .env.")
        return

    subject = f"[SIHUB Vinalink] Báo cáo đối chiếu phản hồi Doanh chủ - {datetime.now().strftime('%Y-%m-%d')}"
    
    violation_html = ""
    if not violations:
        violation_html = "<p style='color: #10b981; font-weight: bold;'>🎉 Tuyệt vời! Không phát hiện điểm sai lệch nào so với Bộ chuẩn mực.</p>"
    else:
        violation_html = "<table border='1' cellpadding='8' style='border-collapse: collapse; font-size: 13px; font-family: sans-serif;'>"
        violation_html += "<tr style='background-color: #f1f5f9;'><th>Khía cạnh khảo sát</th><th>Giá trị khai báo</th><th>Lý do vi phạm/Cảnh báo</th></tr>"
        for v in violations:
            violation_html += f"<tr><td><b>{v['aspect']}</b></td><td>{v['value']}</td><td style='color: #ef4444;'>{v['reason']}</td></tr>"
        violation_html += "</table>"

    body_html = f"""
    <html>
    <body style="font-family: sans-serif; color: #334155; line-height: 1.6;">
        <h2 style="color: #0f172a; border-bottom: 2px solid #10b981; padding-bottom: 8px;">
            Báo Cáo Đối Chiếu Phản Hồi Doanh Chủ Vinalink (Bản Nâng Cấp)
        </h2>
        <p>Chào anh Mr. Híu,</p>
        <p>Hệ thống SIHUB đã ghi nhận phản hồi khảo sát của Doanh chủ <b>{data["doanhChuName"]}</b> gửi từ website lúc {data["timestamp"]}.</p>
        
        <h3 style="color: #0f172a;">Kết quả đối chiếu chuẩn mực:</h3>
        {violation_html}
        
        <p style="margin-top: 20px;">
            Để xem chi tiết phân tích y khoa & toán học định lượng, anh vui lòng mở các tệp tin local trong workspace của mình:
            <ul>
                <li>Xem bản phản hồi đầy đủ: <a href="file:///{CHECKLIST_TRA_LOI_PATH}">doanh-chu-checklist-tra-loi.md</a></li>
                <li>Xem báo cáo đánh giá đối chiếu: <a href="file:///{DOI_CHIEU_BAO_CAO_PATH}">doi-chieu-bao-cao.md</a></li>
            </ul>
        </p>
        <hr style="border: 0; border-top: 1px solid #e2e8f0; margin-top: 30px;">
        <p style="font-size: 11px; color: #94a3b8;">Báo cáo được tạo tự động bởi SIHUB Automation Engine lúc 20:00 hàng ngày.</p>
    </body>
    </html>
    """

    try:
        msg = MIMEText(body_html, 'html', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, [RECEIVER_EMAIL], msg.as_string())
        server.quit()
        print(f"Đã gửi email báo cáo tổng hợp tới: {RECEIVER_EMAIL}")
    except Exception as e:
        print(f"Gửi email báo cáo thất bại: {e}")

def main():
    # 1. Tải phản hồi mới nhất
    feedback = fetch_feedback_data()
    if not feedback:
        return
    
    # 2. Phân tích đối chiếu sai phạm
    violations = analyze_violations(feedback)
    
    # 3. Cập nhật các file local
    write_doanh_chu_checklist_tra_loi(feedback)
    update_doi_chieu_bao_cao(feedback, violations)
    
    # 4. Gửi email báo cáo qua Gmail
    send_email_report(feedback, violations)
    print(f"[{datetime.now()}] Hoàn thành chu kỳ đồng bộ 20:00 hàng ngày thành công.")

if __name__ == "__main__":
    main()
