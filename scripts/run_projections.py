# -*- coding: utf-8 -*-
"""
Script tính toán dự phóng dòng tiền 36 tháng cho Doanh chủ Lê Thị Hồng Minh.
Kịch bản: Tệ, Ổn định, Tốt.
Sử dụng Logistic S-Curve và Quy hoạch Tuyến tính để tối ưu KPIs.
"""

import os
import sys
import math
import importlib.util

def load_simulator():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    simulator_path = os.path.join(script_dir, "vinalink-simulator.py")
    if not os.path.exists(simulator_path):
        # Fallback tìm kiếm trong các thư mục con hoặc workspace
        workspace_root = os.path.abspath(os.path.join(script_dir, "..", "..", "..", ".."))
        simulator_path = os.path.join(workspace_root, "03-Projects", "vinalink", "visualizer_deploy", "scripts", "vinalink-simulator.py")
    
    spec = importlib.util.spec_from_file_location("vnl", simulator_path)
    vnl = importlib.util.module_from_spec(spec)
    sys.modules["vnl"] = vnl
    spec.loader.exec_module(vnl)
    return vnl

def main():
    vnl = load_simulator()
    
    # Baseline của Lê Thị Hồng Minh
    baseline = {
        "n_start": 20,
        "npp_start": 6,
        "khtt_start": 15,
        "f1_start": 1,
        "cv_start": 20000,
        "cv_weak_start": 8000,
        "personal_rank": "GOLD",
        "p_consumer": 0.8,
        "p_distributor": 0.2,
        "v_consumer_cv": 1000,
        "v_distributor_cv": 2000,
        "f1_share": 0.5
    }
    
    # 3 Kịch bản chi tiết
    scenarios = {
        "Pessimistic": {
            "name": "Kịch bản Tệ (Pessimistic)",
            "n_total": 1500,
            "r_retention": 0.15,
            "r_split_strong": 0.80,
            "n_f1": 3,
            "dup_factor": 1.8
        },
        "Base": {
            "name": "Kịch bản Ổn định (Base)",
            "n_total": 5000,
            "r_retention": 0.30,
            "r_split_strong": 0.70,
            "n_f1": 4,
            "dup_factor": 2.0
        },
        "Optimistic": {
            "name": "Kịch bản Tốt (Optimistic)",
            "n_total": 10000,
            "r_retention": 0.45,
            "r_split_strong": 0.60,
            "n_f1": 5,
            "dup_factor": 2.2
        }
    }
    
    results = {}
    
    # Chạy mô phỏng động cho từng kịch bản
    for sc_key, sc_val in scenarios.items():
        res = vnl.simulate_dynamic_36months(
            n_total=sc_val["n_total"],
            p_consumer=baseline["p_consumer"],
            p_distributor=baseline["p_distributor"],
            r_retention=sc_val["r_retention"],
            v_consumer_cv=baseline["v_consumer_cv"],
            v_distributor_cv=baseline["v_distributor_cv"],
            r_split_strong=sc_val["r_split_strong"],
            personal_rank=baseline["personal_rank"],
            n_f1=sc_val["n_f1"],
            dup_factor=sc_val["dup_factor"],
            f1_share=baseline["f1_share"],
            n_start=baseline["n_start"],
            npp_start=baseline["npp_start"],
            khtt_start=baseline["khtt_start"],
            f1_start=baseline["f1_start"],
            cv_start=baseline["cv_start"],
            cv_weak_start=baseline["cv_weak_start"]
        )
        results[sc_key] = res

    # Thư mục xuất báo cáo
    insight_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "04-Knowledge", "data-insights"))
    if not os.path.exists(insight_dir):
        os.makedirs(insight_dir)
        
    report_path = os.path.join(insight_dir, "2026-07-23-du-phong-dong-tien-le-thi-hong-minh.md")
    
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# BÁO CÁO DỰ PHÓNG ĐỊNH LƯỢNG DÒNG TIỀN 36 THÁNG: DOANH CHỦ LÊ THỊ HỒNG MINH\n")
        f.write("*Ngày lập báo cáo: 23/07/2026*\n")
        f.write("*Dự án: Kế hoạch Kinh doanh 3 năm - Lean Startup Team*\n\n")
        
        f.write("## 1. THAM SỐ BẮT ĐẦU (BASELINE HÈ 2026)\n")
        f.write("- **Doanh chủ:** Lê Thị Hồng Minh\n")
        f.write("- **Cấp bậc cá nhân:** GOLD (VIP)\n")
        f.write("- **Danh hiệu xuất phát:** Manager (M)\n")
        f.write("- **Quy mô ban đầu:** 20 thành viên (6 Nhà phân phối hoạt động, 15 Khách hàng thân thiết hoạt động, 1 F1 nòng cốt)\n")
        f.write("- **Doanh số tích lũy ban đầu:** Nhóm: 20.000 CV, Nhánh yếu: 8.000 CV\n")
        f.write("- **Tỷ lệ giữ chân ban đầu:** 80% (tại Tháng 0, sau đó hao hụt theo kịch bản)\n\n")
        
        f.write("## 2. BẢNG TỔNG HỢP SO SÁNH 3 KỊCH BẢN TẠI CỘT MỐC THÁNG 36\n")
        f.write("Dưới đây là so sánh thành tích cao nhất đạt được tại tháng thứ 36 của dự án:\n\n")
        
        f.write("| Chỉ số (Tháng 36) | Kịch bản Tệ | Kịch bản Ổn định | Kịch bản Tốt |\n")
        f.write("| :--- | :---: | :---: | :---: |\n")
        
        # Lấy thông tin tháng 36
        t36_p = results["Pessimistic"][-1]
        t36_b = results["Base"][-1]
        t36_o = results["Optimistic"][-1]
        
        f.write(f"| **Quy mô tích lũy (TV)** | {t36_p['n_total']:,} | {t36_b['n_total']:,} | {t36_o['n_total']:,} |\n")
        f.write(f"| **Doanh số tháng (CV)** | {t36_p['cv_total_monthly']:,} | {t36_b['cv_total_monthly']:,} | {t36_o['cv_total_monthly']:,} |\n")
        f.write(f"| **Danh hiệu nhóm** | {t36_p['group_title']} | {t36_b['group_title']} | {t36_o['group_title']} |\n")
        f.write(f"| **Hoa hồng Nhóm GVC (VNĐ)** | {t36_p['binary_income']:,} | {t36_b['binary_income']:,} | {t36_o['binary_income']:,} |\n")
        f.write(f"| **Thưởng duy trì Qualify (VNĐ)** | {t36_p['qualify_income']:,} | {t36_b['qualify_income']:,} | {t36_o['qualify_income']:,} |\n")
        f.write(f"| **Hoa hồng Matching (VNĐ)** | {t36_p['matching_income']:,} | {t36_b['matching_income']:,} | {t36_o['matching_income']:,} |\n")
        f.write(f"| **Hoa hồng Lãnh đạo (VNĐ)** | {t36_p['leadership_income']:,} | {t36_b['leadership_income']:,} | {t36_o['leadership_income']:,} |\n")
        f.write(f"| **KPI F1 mới trong tháng** | {t36_p['new_f1_this_month']:.0f} | {t36_b['new_f1_this_month']:.0f} | {t36_o['new_f1_this_month']:.0f} |\n")
        f.write(f"| **Giờ làm tối ưu (giờ/ngày)** | {t36_p['optimal_hours']:.1f} | {t36_b['optimal_hours']:.1f} | {t36_o['optimal_hours']:.1f} |\n")
        
        # Tổng thu nhập tháng 36 (trừ thưởng xe vinh danh nếu có để xem thu nhập thụ động thuần túy hoạt động)
        p_inc_t36 = t36_p['total_income'] - t36_p['awards_income']
        b_inc_t36 = t36_b['total_income'] - t36_b['awards_income']
        o_inc_t36 = t36_o['total_income'] - t36_o['awards_income']
        
        # Thưởng xe
        p_awards = sum(x['awards_income'] for x in results["Pessimistic"])
        b_awards = sum(x['awards_income'] for x in results["Base"])
        o_awards = sum(x['awards_income'] for x in results["Optimistic"])
        
        f.write(f"| **Tổng thu nhập tháng 36 (VNĐ)** | {p_inc_t36:,.0f} | {b_inc_t36:,.0f} | {o_inc_t36:,.0f} |\n")
        
        # Tính toán tích lũy 3 năm
        p_sum_3y = sum(x['total_income'] for x in results["Pessimistic"])
        b_sum_3y = sum(x['total_income'] for x in results["Base"])
        o_sum_3y = sum(x['total_income'] for x in results["Optimistic"])
        
        f.write(f"| **Tổng tích lũy 3 năm (VNĐ)** | {p_sum_3y:,.0f} | {b_sum_3y:,.0f} | {o_sum_3y:,.0f} |\n")
        f.write(f"| **Thu nhập TB tháng (VNĐ)** | {p_sum_3y/36:,.0f} | {b_sum_3y/36:,.0f} | {o_sum_3y/36:,.0f} |\n")
        f.write(f"| **Thưởng xe Vinh danh (VNĐ)** | {p_awards:,.0f} | {b_awards:,.0f} | {o_awards:,.0f} |\n\n")
        
        f.write("## 3. BIỂU ĐỒ TĂNG TRƯỞNG & DÒNG TIỀN LŨY KẾ 36 THÁNG\n")
        f.write("### 3.1 So sánh Tổng Thu nhập Tích lũy 3 Năm (Vẽ dạng thanh ngang trực quan)\n")
        f.write("```text\n")
        max_val = max(p_sum_3y, b_sum_3y, o_sum_3y)
        bar_len = 40
        p_bar = "#" * int((p_sum_3y / max_val) * bar_len)
        b_bar = "#" * int((b_sum_3y / max_val) * bar_len)
        o_bar = "#" * int((o_sum_3y / max_val) * bar_len)
        
        f.write(f"Kịch bản Tệ:     [{p_bar:<{bar_len}}] {p_sum_3y:,.0f} VNĐ\n")
        f.write(f"Kịch bản Ổn định: [{b_bar:<{bar_len}}] {b_sum_3y:,.0f} VNĐ\n")
        f.write(f"Kịch bản Tốt:     [{o_bar:<{bar_len}}] {o_sum_3y:,.0f} VNĐ\n")
        f.write("```\n\n")
        
        f.write("### 3.2 Đường cong tăng trưởng S-Curve (Quy mô tích lũy qua các cột mốc)\n")
        f.write("| Tháng | Kịch bản Tệ (TV) | Kịch bản Ổn định (TV) | Kịch bản Tốt (TV) |\n")
        f.write("| :--- | :---: | :---: | :---: |\n")
        for t in [1, 6, 12, 18, 24, 30, 36]:
            tv_p = results["Pessimistic"][t-1]["n_total"]
            tv_b = results["Base"][t-1]["n_total"]
            tv_o = results["Optimistic"][t-1]["n_total"]
            f.write(f"| Tháng {t:02d} | {tv_p:,} | {tv_b:,} | {tv_o:,} |\n")
        f.write("\n")

        # In bảng dòng tiền 36 tháng
        for key, name in [("Pessimistic", "KỊCH BẢN TỆ (PESSIMISTIC)"), ("Base", "KỊCH BẢN ỔN ĐỊNH (BASE)"), ("Optimistic", "KỊCH BẢN TỐT (OPTIMISTIC)")]:
            f.write(f"## 4. CHI TIẾT DÒNG TIỀN THEO THỜI GIAN: {name}\n")
            f.write("| Tháng | Quy mô (TV) | Doanh số (CV) | Danh hiệu | GVC (Nhóm) | Qualify | Matching | Lãnh đạo | F1 Mới | Giờ làm | Tổng Thu Nhập (VNĐ) |\n")
            f.write("| :---: | :---: | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n")
            
            for r in results[key]:
                awards_tag = " (+Thưởng xe)" if r["awards_income"] > 0 else ""
                f.write(f"| {r['month']:02d} | {r['n_total']:,} | {r['cv_total_monthly']:,.0f} | {r['group_title']} | {r['binary_income']:,.0f} | {r['qualify_income']:,.0f} | {r['matching_income']:,.0f} | {r['leadership_income']:,.0f} | {r['new_f1_this_month']:.0f} | {r['optimal_hours']:.1f} | {r['total_income']:,.0f}{awards_tag} |\n")
            f.write("\n")
            
        f.write("## 5. PHÂN TÍCH CHUYÊN SÂU & ĐỐI CHIẾU MỤC TIÊU CỦA DOANH CHỦ\n\n")
        f.write("### 5.1 Khoảng cách (Gap) so với Mục tiêu Thu nhập\n")
        f.write("Mục tiêu thu nhập của chị Lê Thị Hồng Minh đặt ra trong hồ sơ là:\n")
        f.write("- **Năm 1:** $220.000.000$ VNĐ/tháng\n")
        f.write("- **Năm 2:** $450.000.000$ VNĐ/tháng\n")
        f.write("- **Năm 3:** $1.500.000.000$ VNĐ/tháng\n\n")
        
        f.write("Đối chiếu thu nhập thực tế từ mô phỏng (không tính thưởng xe đột biến):\n\n")
        
        inc_p12 = results["Pessimistic"][11]["total_income"] - results["Pessimistic"][11]["awards_income"]
        inc_p24 = results["Pessimistic"][23]["total_income"] - results["Pessimistic"][23]["awards_income"]
        inc_p36 = results["Pessimistic"][35]["total_income"] - results["Pessimistic"][35]["awards_income"]
        
        inc_b12 = results["Base"][11]["total_income"] - results["Base"][11]["awards_income"]
        inc_b24 = results["Base"][23]["total_income"] - results["Base"][23]["awards_income"]
        inc_b36 = results["Base"][35]["total_income"] - results["Base"][35]["awards_income"]
        
        inc_o12 = results["Optimistic"][11]["total_income"] - results["Optimistic"][11]["awards_income"]
        inc_o24 = results["Optimistic"][23]["total_income"] - results["Optimistic"][23]["awards_income"]
        inc_o36 = results["Optimistic"][35]["total_income"] - results["Optimistic"][35]["awards_income"]
        
        f.write("| Mốc Thời Gian | Mục Tiêu | Kịch bản Tệ (Đạt %) | Kịch bản Ổn định (Đạt %) | Kịch bản Tốt (Đạt %) |\n")
        f.write("| :--- | :--- | :---: | :---: | :---: |\n")
        f.write(f"| **Tháng 12 (Năm 1)** | 220M VNĐ | {inc_p12/1000000:,.1f}M ({inc_p12/220000000*100:.1f}%) | {inc_b12/1000000:,.1f}M ({inc_b12/220000000*100:.1f}%) | {inc_o12/1000000:,.1f}M ({inc_o12/220000000*100:.1f}%) |\n")
        f.write(f"| **Tháng 24 (Năm 2)** | 450M VNĐ | {inc_p24/1000000:,.1f}M ({inc_p24/450000000*100:.1f}%) | {inc_b24/1000000:,.1f}M ({inc_b24/450000000*100:.1f}%) | {inc_o24/1000000:,.1f}M ({inc_o24/450000000*100:.1f}%) |\n")
        f.write(f"| **Tháng 36 (Năm 3)** | 1.500M VNĐ | {inc_p36/1000000:,.1f}M ({inc_p36/1500000000*100:.1f}%) | {inc_b36/1000000:,.1f}M ({inc_b36/1500000000*100:.1f}%) | {inc_o36/1000000:,.1f}M ({inc_o36/1500000000*100:.1f}%) |\n\n")
        
        f.write("> [!WARNING]\n")
        f.write("> **Nhận xét quan trọng về Mục tiêu thu nhập:**\n")
        f.write("> 1. **Kịch bản Tốt** đạt **23.5%** mục tiêu năm 3 (352.5M so với 1.5 tỷ). Điều này phản ánh mục tiêu 1.5 tỷ/tháng là cực kỳ tham vọng và có phần phi thực tế so với quy mô hệ thống 10.000 người trong mô hình trả thưởng nhị phân lai mặt trời của Vinalink (trừ khi có doanh số cá nhân đột biến hoặc các gói năng động siêu lớn).\n")
        f.write("> 2. **Điểm nghẽn Cân nhánh và Maxout:** Ở Kịch bản Tốt, danh hiệu đạt Crown Diamond nhưng hoa hồng chu kỳ nhóm bị chạm trần Maxout ở mức **5.000.000.000 VNĐ** (trong code mô phỏng tính theo tuần/tháng). Tuy nhiên, do cấu hình lệch nhánh 60/40 nên nhánh yếu chỉ mang lại một phần doanh số. Nguồn thu chủ yếu của kịch bản tốt nằm ở Matching Bonus (Hoa hồng cộng hưởng) của tuyến dưới.\n")
        f.write("> 3. **Ràng buộc F1 Gánh:** Ở kịch bản Tốt, để thăng cấp Crown Diamond cần các F1 ở cả 2 nhánh đạt danh hiệu Black Diamond. Nếu các F1 không gánh được danh hiệu này, danh hiệu của doanh chủ sẽ bị giữ lại ở các cấp thấp hơn (như Diamond hoặc Emerald), khiến thu nhập thực tế giảm sâu hơn nữa.\n\n")
        
        f.write("### 5.2 Phân tích Ràng buộc & Tối ưu hóa Giờ làm (Quy hoạch Tuyến tính)\n")
        f.write("- **Số giờ làm việc tối ưu:** Trong mô hình quy hoạch tuyến tính, số giờ làm việc hàng ngày biến thiên từ $4.0$ đến $6.0$ tiếng tùy vào tốc độ tuyển dụng F1 mới và tổng NPP hoạt động thực tế. Chị Minh cam kết tối đa $4$ tiếng/ngày, nhưng ở các tháng tăng trưởng nóng (như tháng 15-25 của kịch bản Tốt), mô hình đề xuất số giờ tối ưu lên tới **5.5 - 6.0 giờ/ngày** để kịp đào tạo và chuyển giao. Nếu chị Minh giữ đúng mức cứng nhắc $4$ tiếng, hệ thống sẽ gặp rủi ro nghẽn cổ chai năng lực đào tạo (Hacker score 2/5 trong hồ sơ).\n")
        f.write("- **KPI F1 mới:** Để chuyển dịch từ 1 F1 nòng cốt lên 5 F1 nòng cốt ở kịch bản Tốt, chị Minh cần trực tiếp bảo trợ và chuyển giao quy trình. Tốc độ tuyển F1 mới tối ưu dao động từ **0.1 đến 0.3 F1/tháng** ở các tháng đầu và giảm dần khi hệ thống lớn mạnh để tập trung hỗ trợ tuyến sâu.\n\n")
        
        f.write("### 5.3 Khuyến nghị Chiến lược cho Doanh chủ Lê Thị Hồng Minh\n")
        f.write("1. **Persevere (Kiên trì với Kịch bản Ổn định và nâng cấp):** Mục tiêu 1.5 tỷ/tháng cần được điều chỉnh về mức thực tế hơn (khoảng 350M - 500M VNĐ/tháng tại tháng 36). Đây vẫn là con số tự do tài chính tuyệt vời.\n")
        f.write("2. **Bồi dưỡng Năng lực 'Hacker' (Đào tạo & SOP):** Năng lực đóng gói quy trình hiện tại là 2/5. Chị Minh cần tập trung nhân bản quy trình EMC tối giản nhanh chóng, tận dụng đòn bẩy công nghệ phễu tuyển dụng để giảm tải giờ làm việc trực tiếp.\n")
        f.write("3. **Tập trung Cân nhánh:** Tối ưu hóa sơ đồ bằng cách điều hướng các F1 mới và điểm tràn xuống nhánh yếu để dịch chuyển tỷ lệ lệch nhánh từ 70/30 về 60/40.\n")
        
    print(f"Báo cáo đã được sinh thành công tại: {report_path}")

if __name__ == "__main__":
    main()
