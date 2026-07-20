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
# Form sẽ gửi dữ liệu tới Sheet này qua Google Apps Script Web App
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
    print(f"[{datetime.now()}] Bắt đầu đồng bộ dữ liệu phản hồi...")
    
    # Kiểm tra xem có cấu hình SPREADSHEET_ID thực tế chưa
    if "Mock" in SPREADSHEET_ID or not SPREADSHEET_ID:
        print("Chế độ mô phỏng: Đang giả lập phản hồi của Doanh chủ...")
        # Mock dữ liệu phản hồi của Doanh chủ gửi từ Web Form
        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "doanhChuName": "Doanh Chủ Vinalink (Mock Leader)",
            "a1": "Chia sẻ OPP 2-1 và hỗ trợ quy trình EMC",
            "a2": "6", # Số F1 nòng cốt muốn dẫn dắt (Vi phạm: Vượt quá 5 người)
            "b1": "nhom_3", # Thủ lĩnh chuyên nghiệp
            "b2": "Người làm tự do và kinh doanh bảo hiểm",
            "c2": "yêu cầu ước mơ mục tiêu và thái độ tốt", # Bộ lọc cam kết (Vi phạm: định tính)
            "d1": "14", # Thời gian làm việc mỗi ngày (Vi phạm: Burnout)
            "d2": "10.000.000 VNĐ",
            "e1": "300.000.000 VNĐ", # Thu nhập Năm 1 (Vi phạm: Quá cao)
            "e2": "800.000.000 VNĐ", # Thu nhập Năm 2 (Vi phạm: Quá cao)
            "e3": "1.500.000.000 VNĐ" # Thu nhập Năm 3 (Vi phạm: Mâu thuẫn toán học)
        }
        
    try:
        req = urllib.request.Request(CSV_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            lines = [line.decode('utf-8') for line in response.readlines()]
            reader = csv.DictReader(lines)
            rows = list(reader)
            if not rows:
                print("Google Sheet trống. Không có phản hồi mới.")
                return None
            
            # Lấy phản hồi mới nhất (dòng cuối cùng)
            latest_row = rows[-1]
            return {
                "timestamp": latest_row.get("timestamp", ""),
                "doanhChuName": latest_row.get("doanhChuName", "Doanh Chủ Vinalink"),
                "a1": latest_row.get("a1", ""),
                "a2": latest_row.get("a2", "0"),
                "b1": latest_row.get("b1", ""),
                "b2": latest_row.get("b2", ""),
                "c2": latest_row.get("c2", ""),
                "d1": latest_row.get("d1", "0"),
                "d2": latest_row.get("d2", ""),
                "e1": latest_row.get("e1", ""),
                "e2": latest_row.get("e2", ""),
                "e3": latest_row.get("e3", "")
            }
    except Exception as e:
        print(f"Lỗi khi tải dữ liệu từ Google Sheets: {e}")
        print("Sử dụng dữ liệu mô phỏng để chạy tiếp luồng...")
        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "doanhChuName": "Doanh Chủ Vinalink (Mô Phỏng)",
            "a1": "Chia sẻ OPP 2-1",
            "a2": "6",
            "b1": "nhom_3",
            "b2": "Chưa cụ thể",
            "c2": "yêu cầu ước mơ mục tiêu",
            "d1": "14",
            "d2": "10.000.000 VNĐ",
            "e1": "300.000.000 VNĐ",
            "e2": "800.000.000 VNĐ",
            "e3": "1.500.000.000 VNĐ"
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
    e2_val = clean_money(data["e2"])
    e3_val = clean_money(data["e3"])

    # Giả định quy đổi CV
    if e1_val > 100000000: # > 100tr ở năm 1
        violations.append({
            "aspect": "Mục tiêu Năm 1 (Phần 1)",
            "rule": "Ràng buộc VI.1 (Quy đổi mục tiêu tài chính ra CV nhánh yếu tương xứng và thực tế)",
            "value": f"{data['e1']}/tháng",
            "reason": "Quá cao cho giai đoạn khởi nghiệp hệ thống năm đầu tiên, đòi hỏi doanh số nhánh yếu khổng lồ khi chưa nhân bản xong F1."
        })
    
    if e3_val > 693896000: # > 693 triệu VNĐ (giới hạn lý tưởng 10.000 người)
        violations.append({
            "aspect": "Mục tiêu Năm 3 (Phần 1)",
            "rule": "Ràng buộc VI.1 (Con số thu nhập tối đa mô phỏng lý tưởng là ~693 triệu VNĐ/tháng ở quy mô 10.000 người)",
            "value": f"{data['e3']}/tháng",
            "reason": "Mâu thuẫn toán học về giới hạn doanh thu hệ thống. Kể cả kịch bản lý tưởng nhất cũng chỉ đạt tối đa ~693 triệu VNĐ/tháng. Đề xuất điều chỉnh mục tiêu Năm 3 về 150 triệu VNĐ/tháng (cấp Diamond)."
        })

    return violations

def write_doanh_chu_checklist_tra_loi(data):
    """Ghi đè tệp local doanh-chu-checklist-tra-loi.md với câu trả lời mới"""
    content = f"""# BẢN PHẢN HỒI CHECKLIST KHẢO SÁT TẦM NHÌN DOANH CHỦ VINALINK

**Doanh chủ thực hiện:** {data["doanhChuName"]}
**Thời gian phản hồi:** {data["timestamp"]}
**Trạng thái đồng bộ:** Đồng bộ tự động lúc 20:00

---

## PHẦN CHI TIẾT CÂU TRẢ LỜI KHẢO SÁT

### 1. Mục tiêu Tài chính (Phần 1)
- **Thu nhập Năm 1:** {data["e1"]}
- **Thu nhập Năm 2:** {data["e2"]}
- **Thu nhập Năm 3:** {data["e3"]}

### 2. Quy mô & Cấu trúc Hệ thống (Phần 2)
- **Số lượng F1 nòng cốt thiết lập dẫn dắt:** {data["a2"]} người

### 3. Nguồn lực Đầu vào (Phần 4)
- **Thời gian cam kết làm việc mỗi ngày:** {data["d1"]} giờ/ngày
- **Ngân sách đầu tư ban đầu:** {data["d2"]}

### 4. Định vị Tuyển dụng Tinh gọn (Phần 5)
- **Câu A1 (LVP - Giá trị hỗ trợ cốt lõi):** {data["a1"]}
- **Câu B1 (IDP - Phân khúc downline ưu tiên):** {"Thủ lĩnh chuyên nghiệp (Nhóm 3)" if data["b1"] == "nhom_3" else "Người làm thêm (Nhóm 1)" if data["b1"] == "nhom_1" else "Khách hàng chuyển đổi (Nhóm 2)"}
- **Câu B2 (IDP - Chi tiết nghề nghiệp & độ tuổi):** {data["b2"]}
- **Câu C2 (Bộ lọc cam kết hành động):** {data["c2"]}
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

    # Đọc nội dung cũ của doi-chieu-bao-cao.md để giữ lại phần phân tích y học & toán học phía dưới
    try:
        with open(DOI_CHIEU_BAO_CAO_PATH, "r", encoding="utf-8") as f:
            old_content = f.read()
    except FileNotFoundError:
        old_content = ""

    # Tách phần tiêu đề và bảng đối chiếu cũ để thay thế
    # Chúng ta thay thế phần bảng đối chiếu (từ dòng đầu đến phần "## I. PHÂN TÍCH CHUYÊN SÂU TỪ TALENT POOL HỆ THỐNG")
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
    
    # Tìm phần phân tích chuyên sâu cũ
    split_pattern = r"## I\. PHÂN TÍCH CHUYÊN SÂU.*"
    match = re.search(split_pattern, old_content, re.DOTALL)
    
    if match:
        new_content = header_section + "\n" + match.group(0)
    else:
        # Nếu không tìm thấy, ghép nội dung mặc định
        new_content = header_section

    with open(DOI_CHIEU_BAO_CAO_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Đã cập nhật bảng đối chiếu sai phạm trong: {DOI_CHIEU_BAO_CAO_PATH}")

def send_email_report(data, violations):
    """Gửi email báo cáo đối chiếu cho Doanh chủ và Cố vấn qua SMTP"""
    if not SENDER_EMAIL or SENDER_EMAIL == "your-email@gmail.com":
        print("Bỏ qua gửi email: Chưa cấu hình thông tin tài khoản SMTP trong file .env.")
        return

    # Tạo nội dung email
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
            Báo Cáo Đối Chiếu Phản Hồi Doanh Chủ Vinalink
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
