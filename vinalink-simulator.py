# -*- coding: utf-8 -*-
"""
Vinalink Network Marketing Compensation & Structure Simulator
Created for: SIHUB 2026 Lean Startup Program - Chuyên đề 2 & 3
Doanh chủ: Vinalink Group Compensation Model
"""

import sys
import argparse

# Định nghĩa các hằng số chính sách Vinalink
BRONZE_CV = 2000
SILVER_CV = 4000
GOLD_CV = 10000

RANKS = {
    "BRONZE": {"min_cv": BRONZE_CV, "name": "Đồng (Bronze)", "sponsor_cap_gold_f1": 1000},
    "SILVER": {"min_cv": SILVER_CV, "name": "Bạc (Silver)", "sponsor_cap_gold_f1": 1000},
    "GOLD": {"min_cv": GOLD_CV, "name": "Vàng/VIP (Gold)", "sponsor_cap_gold_f1": 2000}
}

# Điểm thưởng duy trì doanh số tích lũy cho các cấp bậc cá nhân (Bronze, Silver, Gold)
# Mỗi mốc 80.000 CV, 240.000 CV, 550.000 CV sẽ mang lại lượng điểm thưởng tích lũy tương ứng
QUALIFY_BONUS_LOOKUP = {
    "BRONZE": {80000: 5000, 240000: 10000, 550000: 25000},
    "SILVER": {80000: 10000, 240000: 15000, 550000: 30000},
    "GOLD": {80000: 10000, 240000: 22000, 550000: 38000}
}

# Tính tổng điểm thưởng của mỗi cấp bậc cho một chu kỳ tích lũy 550.000 CV
TOTAL_QUALIFY_BONUS = {
    rank: sum(milestones.values()) for rank, milestones in QUALIFY_BONUS_LOOKUP.items()
}


TITLES = [
    {"id": "SM", "min_group_cv": 240000, "name": "Senior Manager"},
    {"id": "DIR", "min_group_cv": 550000, "name": "Director"},
    {"id": "RUBY", "min_group_cv": 1100000, "name": "Ruby"},
    {"id": "EME", "min_group_cv": 2200000, "name": "Emerald"},
    {"id": "DIA", "min_group_cv": 4400000, "name": "Diamond"},
    {"id": "BD", "min_group_cv": 6600000, "name": "Blue Diamond"},
    {"id": "BKD", "min_group_cv": 10000000, "name": "Black Diamond"},
    {"id": "CD", "min_group_cv": 15000000, "name": "Crown Diamond"},
    {"id": "AMB", "min_group_cv": 22000000, "name": "Ambassador"}
]

# Trần hoa hồng chu kỳ nhóm hàng tháng cho từng cấp bậc danh hiệu & cấp bậc cá nhân (Đồng, Bạc, Vàng)
MAX_BINARY_LIMITS = {
    "SM": (10000000, 20000000, 40000000), 
    "DIR": (50000000, 100000000, 200000000),
    "RUBY": (150000000, 300000000, 600000000),
    "EME": (300000000, 600000000, 1200000000),
    "DIA": (500000000, 1000000000, 2000000000),
    "BD": (800000000, 1600000000, 3000000000),
    "BKD": (1000000000, 2000000000, 4000000000),
    "CD": (1200000000, 2400000000, 5000000000),
    "AMB": (1500000000, 3000000000, 6000000000)
}

def get_group_title(accumulated_group_cv):
    title = "Manager"
    title_id = "M"
    for item in TITLES:
        if accumulated_group_cv >= item["min_group_cv"]:
            title = item["name"]
            title_id = item["id"]
    return title, title_id

def simulate(n_total, p_consumer, p_distributor, r_retention, v_consumer_cv, v_distributor_cv, r_split_strong, personal_rank="GOLD"):
    # 1. Số lượng thành viên hoạt động
    n_consumer = int(n_total * p_consumer)
    n_distributor = int(n_total * p_distributor)
    n_active_distributor = int(n_distributor * r_retention)
    
    # 2. Tính doanh số phát sinh hàng tháng
    cv_consumer_monthly = n_consumer * v_consumer_cv
    cv_distributor_monthly = n_active_distributor * v_distributor_cv
    cv_total_monthly = cv_consumer_monthly + cv_distributor_monthly
    
    # Giả định doanh số nhóm tích lũy lũy kế (lấy tương đương doanh số phát sinh trong 1 năm để thăng chức danh)
    accumulated_group_cv = cv_total_monthly * 12
    group_title, title_id = get_group_title(accumulated_group_cv)
    
    # 3. Phân bổ nhánh mạnh / nhánh yếu
    r_split_weak = 1.0 - r_split_strong
    cv_weak_monthly = cv_total_monthly * r_split_weak
    cv_strong_monthly = cv_total_monthly * r_split_strong
    
    # 4. Tính hoa hồng chu kỳ nhóm (Group Volume Commission)
    # Director trở lên (chu kỳ 7.000 CV nhận 560.000 VNĐ), dưới Director (chu kỳ 3.000 CV nhận 300.000 VNĐ)
    is_director_or_above = accumulated_group_cv >= 550000
    if is_director_or_above:
        cycle_size = 7000
        cycle_bonus = 560000
    else:
        cycle_size = 3000
        cycle_bonus = 300000
        
    num_cycles = int(cv_weak_monthly / cycle_size)
    binary_income_raw = num_cycles * cycle_bonus
    
    # Áp dụng trần hoa hồng chu kỳ nhóm (Maxout Limit)
    binary_limit = float('inf')
    rank_idx = 2  # Mặc định Gold
    if personal_rank == "BRONZE":
        rank_idx = 0
    elif personal_rank == "SILVER":
        rank_idx = 1
        
    if title_id in MAX_BINARY_LIMITS:
        binary_limit = MAX_BINARY_LIMITS[title_id][rank_idx]
        binary_income = min(binary_income_raw, binary_limit)
    else:
        # Danh hiệu Manager không áp trần hoặc trần rất cao
        binary_income = binary_income_raw
        
    # 5. Tính toán thưởng duy trì doanh số (Qualify Volume Bonus)
    # Thưởng được chi trả dựa trên doanh số phát sinh độc lập của nhánh yếu trong tháng đó.
    # NPP nhận được tổng điểm thưởng của tất cả các mốc đạt được trong tháng (tối đa 1 chu kỳ reset).
    qualify_bonus_monthly_cv = 0.0
    rank_milestones = QUALIFY_BONUS_LOOKUP.get(personal_rank, {})
    for milestone, bonus in rank_milestones.items():
        if cv_weak_monthly >= milestone:
            qualify_bonus_monthly_cv += bonus
    qualify_income = qualify_bonus_monthly_cv * 1000  # Quy đổi hoa hồng thưởng: 1 CV = 1.000 VNĐ
    
    # 6. Ước tính các hoa hồng khác (Bảo trợ trực tiếp, Matching Bonus F1-F5, Lãnh đạo toàn quốc)
    # Dựa trên thực tế hệ thống, các khoản này chiếm khoảng 30% trên hoa hồng chu kỳ nhóm
    other_bonuses = binary_income * 0.30
    total_income = binary_income + other_bonuses + qualify_income
    
    return {
        "n_consumer": n_consumer,
        "n_active_distributor": n_active_distributor,
        "cv_total_monthly": cv_total_monthly,
        "accumulated_group_cv": accumulated_group_cv,
        "group_title": group_title,
        "cv_weak_monthly": cv_weak_monthly,
        "num_cycles": num_cycles,
        "binary_income_raw": binary_income_raw,
        "binary_income": binary_income,
        "binary_limit": binary_limit,
        "qualify_income": qualify_income,
        "other_bonuses": other_bonuses,
        "total_income": total_income
    }

def main():
    parser = argparse.ArgumentParser(description="Vinalink Compensation Simulator CLI")
    parser.add_argument("--size", type=int, default=10000, help="Tổng quy mô hệ thống sau 3 năm")
    parser.add_argument("--retention", type=float, default=0.3, help="Tỷ lệ giữ chân nhà phân phối (0.0 - 1.0)")
    parser.add_argument("--split", type=float, default=0.7, help="Tỷ lệ nhánh mạnh (ví dụ: 0.7 tương đương lệch 70/30)")
    parser.add_argument("--rank", type=str, default="GOLD", choices=["BRONZE", "SILVER", "GOLD"], help="Cấp bậc cá nhân của Doanh chủ")
    
    args = parser.parse_args()
    
    # Chạy mô phỏng
    res = simulate(
        n_total=args.size,
        p_consumer=0.8,
        p_distributor=0.2,
        r_retention=args.retention,
        v_consumer_cv=1000,
        v_distributor_cv=2000,
        r_split_strong=args.split,
        personal_rank=args.rank
    )
    
    # In báo cáo kết quả trên terminal
    print("=" * 60)
    print("      BÁO CÁO MÔ PHỎNG ĐỊNH LƯỢNG HỆ THỐNG VINALINK")
    print("=" * 60)
    print(f"Tổng quy mô hệ thống: {args.size} thành viên (80% Tiêu dùng - 20% Kinh doanh)")
    print(f"Tỷ lệ giữ chân NPP hoạt động thực tế: {args.retention * 100:.1f}%")
    print(f"Tỷ lệ phân bổ nhánh (Mạnh/Yếu): {args.split * 100:.0f}/{ (1 - args.split) * 100:.0f}")
    print(f"Cấp bậc cá nhân Doanh chủ: {args.rank}")
    print("-" * 60)
    print(f"Khách hàng thân thiết hoạt động: {res['n_consumer']:,} người")
    print(f"Nhà phân phối hoạt động thực tế: {res['n_active_distributor']:,} người")
    print(f"Doanh số phát sinh hàng tháng: {res['cv_total_monthly']:,} CV")
    print(f"Doanh số tích lũy nhóm ước tính: {res['accumulated_group_cv']:,} CV")
    print(f"Danh hiệu thăng cấp dự kiến: {res['group_title']}")
    print("-" * 60)
    print(f"Doanh số nhánh Yếu hàng tháng: {res['cv_weak_monthly']:,} CV")
    print(f"Số chu kỳ cân nhánh yếu: {res['num_cycles']} chu kỳ")
    print(f"Hoa hồng Chu kỳ nhóm (Thực tế): {res['binary_income_raw']:,} VNĐ")
    if res['binary_income_raw'] > res['binary_limit']:
        print(f"⚠️  BỊ CHẠM TRẦN MAXOUT HOA HỒNG CHU KỲ NHÓM: {res['binary_limit']:,} VNĐ")
    print(f"Hoa hồng Chu kỳ nhóm nhận được: {res['binary_income']:,} VNĐ")
    print(f"Thưởng duy trì doanh số (Qualify Bonus): {res['qualify_income']:,} VNĐ/tháng")
    print(f"Ước tính các hoa hồng khác (30%): {res['other_bonuses']:,} VNĐ")
    print(f"TỔNG THU NHẬP ƯỚC TÍNH HÀNG THÁNG: {res['total_income']:,} VNĐ/tháng")
    print("=" * 60)

if __name__ == "__main__":
    main()
