# -*- coding: utf-8 -*-
"""
Vinalink Network Marketing Compensation & Structure Simulator (Upgraded)
Created for: 2026 Lean Startup Program - Chuyên đề 2 & 3
Doanh chủ: Vinalink Group Compensation Model (Nâng cấp giải thuật danh hiệu & 7 Nguồn thu)
"""

import sys
import argparse
import math

# Định nghĩa các hằng số chính sách Vinalink
BRONZE_CV = 2000
SILVER_CV = 4000
GOLD_CV = 10000

RANKS = {
    "BRONZE": {"min_cv": BRONZE_CV, "name": "Đồng (Bronze)"},
    "SILVER": {"min_cv": SILVER_CV, "name": "Bạc (Silver)"},
    "GOLD": {"min_cv": GOLD_CV, "name": "Vàng/VIP (Gold)"}
}

# Điểm thưởng duy trì doanh số tích lũy cho các cấp bậc cá nhân (Bronze, Silver, Gold)
QUALIFY_BONUS_LOOKUP = {
    "BRONZE": {80000: 5000, 240000: 10000, 550000: 25000},
    "SILVER": {80000: 10000, 240000: 15000, 550000: 30000},
    "GOLD": {80000: 10000, 240000: 22000, 550000: 38000}
}

# Danh hiệu NPP và điều kiện doanh số tích lũy + yêu cầu danh hiệu F1 tối thiểu ở mỗi nhánh
TITLES = [
    {"id": "M", "min_group_cv": 80000, "name": "Manager", "req_f1_title": None},
    {"id": "SM", "min_group_cv": 240000, "name": "Senior Manager", "req_f1_title": None},
    {"id": "DIR", "min_group_cv": 550000, "name": "Director", "req_f1_title": None},
    {"id": "RUBY", "min_group_cv": 1100000, "name": "Ruby", "req_f1_title": None},
    {"id": "EME", "min_group_cv": 2200000, "name": "Emerald", "req_f1_title": None},
    {"id": "DIA", "min_group_cv": 4400000, "name": "Diamond", "req_f1_title": None},
    {"id": "BD", "min_group_cv": 6600000, "name": "Blue Diamond", "req_f1_title": "DIA"},
    {"id": "BKD", "min_group_cv": 10000000, "name": "Black Diamond", "req_f1_title": "BD"},
    {"id": "CD", "min_group_cv": 15000000, "name": "Crown Diamond", "req_f1_title": "BKD"},
    {"id": "AMB", "min_group_cv": 22000000, "name": "Ambassador", "req_f1_title": "CD"}
]

# Trần hoa hồng chu kỳ nhóm hàng tháng cho từng cấp bậc danh hiệu & cấp bậc cá nhân (Bronze, Silver, Gold)
MAX_BINARY_LIMITS = {
    "M": (5000000, 10000000, 20000000),
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

# Cấu hình điều kiện và tỷ lệ phần trăm Matching Bonus theo tầng (F1-F5)
MATCHING_RULES = {
    "DIR": {"min_weak_cv": 85000, "levels": {1: 0.10, 2: 0.10}},
    "RUBY": {"min_weak_cv": 85000, "levels": {1: 0.10, 2: 0.10}},
    "EME": {"min_weak_cv": 85000, "levels": {1: 0.10, 2: 0.10}},
    "DIA": {"min_weak_cv": 300000, "levels": {1: 0.10, 2: 0.10, 3: 0.05}},
    "BD": {"min_weak_cv": 300000, "levels": {1: 0.10, 2: 0.10, 3: 0.05}},
    "BKD": {"min_weak_cv": 300000, "levels": {1: 0.10, 2: 0.10, 3: 0.05}},
    "CD": {"min_weak_cv": 700000, "levels": {1: 0.10, 2: 0.10, 3: 0.05, 4: 0.05}},
    "AMB": {"min_weak_cv": 3000000, "levels": {1: 0.10, 2: 0.10, 3: 0.05, 4: 0.05, 5: 0.05}}
}

def get_title_by_cv_only(cv):
    """Tra cứu danh hiệu thô dựa duy nhất trên doanh số tích lũy (không xét F1)"""
    title_id = None
    title_name = "NPP Thường"
    for t in TITLES:
        if cv >= t["min_group_cv"]:
            title_id = t["id"]
            title_name = t["name"]
    return title_id, title_name

def determine_final_title(accumulated_group_cv, cv_weak_accumulated_f1, cv_strong_accumulated_f1):
    """Xác định danh hiệu cuối cùng có xét điều kiện doanh số tích lũy và danh hiệu F1 ở mỗi nhánh"""
    f1_weak_title_id, _ = get_title_by_cv_only(cv_weak_accumulated_f1)
    f1_strong_title_id, _ = get_title_by_cv_only(cv_strong_accumulated_f1)
    
    def is_f1_qualified(req_title_id, actual_title_id):
        if not req_title_id:
            return True
        if not actual_title_id:
            return False
        
        title_ids = [t["id"] for t in TITLES]
        try:
            req_idx = title_ids.index(req_title_id)
            actual_idx = title_ids.index(actual_title_id)
            return actual_idx >= req_idx
        except ValueError:
            return False

    final_title_id = None
    final_title_name = "NPP Thường"
    
    for t in TITLES:
        if accumulated_group_cv >= t["min_group_cv"]:
            req_f1 = t["req_f1_title"]
            if req_f1:
                ok_weak = is_f1_qualified(req_f1, f1_weak_title_id)
                ok_strong = is_f1_qualified(req_f1, f1_strong_title_id)
                if ok_weak and ok_strong:
                    final_title_id = t["id"]
                    final_title_name = t["name"]
                else:
                    break
            else:
                final_title_id = t["id"]
                final_title_name = t["name"]
        else:
            break
            
    return final_title_id, final_title_name, f1_weak_title_id, f1_strong_title_id

def simulate(n_total, p_consumer, p_distributor, r_retention, v_consumer_cv, v_distributor_cv, r_split_strong, personal_rank="GOLD", n_f1=3, dup_factor=2, f1_share=0.5):
    """Mô phỏng tĩnh tại điểm quy mô ổn định (lấy trung bình Qualify và các nguồn thu)"""
    # 1. Quy mô hoạt động
    n_consumer = int(n_total * p_consumer)
    n_distributor = int(n_total * p_distributor)
    n_active_distributor = int(n_distributor * r_retention)
    
    # 2. Doanh số phát sinh hàng tháng
    cv_consumer_monthly = n_consumer * v_consumer_cv
    cv_distributor_monthly = n_active_distributor * v_distributor_cv
    cv_total_monthly = cv_consumer_monthly + cv_distributor_monthly
    
    # Doanh số tích lũy ước tính trong 1 năm
    accumulated_group_cv = cv_total_monthly * 12
    
    # 3. Phân bổ nhánh
    r_split_weak = 1.0 - r_split_strong
    cv_weak_monthly = cv_total_monthly * r_split_weak
    cv_strong_monthly = cv_total_monthly * r_split_strong
    
    # Tích lũy F1 mạnh gánh
    cv_weak_accumulated_f1 = (cv_weak_monthly * f1_share) * 12
    cv_strong_accumulated_f1 = (cv_strong_monthly * f1_share) * 12
    
    # Thăng cấp danh hiệu
    title_id, group_title, f1_w_title, f1_s_title = determine_final_title(
        accumulated_group_cv, cv_weak_accumulated_f1, cv_strong_accumulated_f1
    )
    
    # --- 7 Nguồn thu nhập ---
    
    # Nguồn 1: Thu nhập Bán lẻ (Giả định NPP tự dùng & bán lẻ 200 CV cá nhân/tháng)
    retail_cv = 200
    retail_income = retail_cv * 1000  # 1 CV = 1.000 VNĐ
    
    # Nguồn 2: Hoa hồng Bảo trợ (Sponsor Bonus)
    # Giả định hàng tháng hệ thống tuyển mới thêm 5% số lượng NPP hoạt động
    new_npp = max(1, int(n_active_distributor * 0.05))
    sum_structural_npp = sum(n_f1 * (dup_factor**(i-1)) for i in range(1, 6))
    
    new_f1 = new_npp * (n_f1 / sum_structural_npp)
    new_f2 = new_npp * ((n_f1 * dup_factor) / sum_structural_npp)
    new_f3_f5 = new_npp * (sum(n_f1 * (dup_factor**(i-1)) for i in [3, 4, 5]) / sum_structural_npp)
    
    # Tầng F1-F2 nhận 10%, F3-F5 nhận 5% (gói tuyển dụng trung bình 2.000 CV)
    package_cv = 2000
    sponsor_income_raw = (new_f1 * 0.10 * package_cv * 1000) + (new_f2 * 0.10 * package_cv * 1000) + (new_f3_f5 * 0.05 * package_cv * 1000)
    # Cộng thưởng Gold Sponsor tuyển F1 Gold: Gold tuyển Gold nhận 2.000 CV thay vì 1.000 CV (chênh lệch 1.000 CV = 1.000.000 VNĐ)
    # Giả định 20% NPP mới chọn gói Vàng (10.000 CV)
    gold_sponsor_bonus = 0.0
    if personal_rank == "GOLD":
        gold_sponsor_bonus = (new_f1 * 0.20) * 1000000
    sponsor_income = sponsor_income_raw + gold_sponsor_bonus
    
    # Nguồn 3: Hoa hồng Doanh số Nhóm (GVC)
    title_ids = [t["id"] for t in TITLES]
    is_director_or_above = False
    if title_id:
        try:
            dir_idx = title_ids.index("DIR")
            curr_idx = title_ids.index(title_id)
            is_director_or_above = curr_idx >= dir_idx
        except ValueError:
            pass
            
    if is_director_or_above:
        cycle_size = 7000
        cycle_bonus = 560000
        extra_cycles = 8
        extra_bonus = 4480000
    else:
        cycle_size = 3000
        cycle_bonus = 300000
        extra_cycles = 20
        extra_bonus = 6000000
        
    num_cycles = int(cv_weak_monthly / cycle_size)
    binary_income_raw = num_cycles * cycle_bonus
    # Thêm thưởng chu kỳ đặc biệt (dưới Dir: 20 chu kỳ + 6M; trên Dir: 8 chu kỳ + 4.48M)
    if num_cycles >= extra_cycles:
        binary_income_raw += extra_bonus
        
    # Áp trần Maxout
    binary_limit = float('inf')
    rank_idx = 2  # Gold
    if personal_rank == "BRONZE":
        rank_idx = 0
    elif personal_rank == "SILVER":
        rank_idx = 1
        
    if title_id in MAX_BINARY_LIMITS:
        binary_limit = MAX_BINARY_LIMITS[title_id][rank_idx]
        binary_income = min(binary_income_raw, binary_limit)
    else:
        binary_income = binary_income_raw
        
    # Nguồn 4: Thưởng Duy trì Doanh số (Qualify Bonus) cộng dồn
    # Mô hình tĩnh: tính trực tiếp theo mốc đạt được trong tháng, không phân bổ (Amortization)
    qualify_income = 0.0
    if cv_weak_monthly >= 550000:
        qualify_income = QUALIFY_BONUS_LOOKUP[personal_rank][550000] * 1000
    elif cv_weak_monthly >= 240000:
        qualify_income = QUALIFY_BONUS_LOOKUP[personal_rank][240000] * 1000
    elif cv_weak_monthly >= 80000:
        qualify_income = QUALIFY_BONUS_LOOKUP[personal_rank][80000] * 1000
        
    # Nguồn 5: Hoa hồng Cộng hưởng (Matching Bonus) trực hệ cấu hình F1
    matching_income = 0.0
    matching_details = []
    
    if title_id in MATCHING_RULES:
        rule = MATCHING_RULES[title_id]
        if cv_weak_monthly >= rule["min_weak_cv"]:
            for level, rate in rule["levels"].items():
                npp_in_level = n_f1 * (dup_factor**(level - 1))
                # Số NPP hoạt động thực tế ở tầng này tỷ lệ theo r_retention
                npp_active_in_level = min(npp_in_level, max(1, int(npp_in_level * r_retention)))
                
                cv_weak_level = cv_weak_monthly / npp_in_level
                cv_accumulated_level = (cv_total_monthly / npp_in_level) * 12
                level_title_id, _ = get_title_by_cv_only(cv_accumulated_level)
                
                is_level_dir = False
                if level_title_id:
                    try:
                        dir_idx = title_ids.index("DIR")
                        l_idx = title_ids.index(level_title_id)
                        is_level_dir = l_idx >= dir_idx
                    except ValueError:
                        pass
                
                l_cycle_size = 7000 if is_level_dir else 3000
                l_cycle_bonus = 560000 if is_level_dir else 300000
                l_extra_cycles = 8 if is_level_dir else 20
                l_extra_bonus = 4480000 if is_level_dir else 6000000
                
                l_cycles = int(cv_weak_level / l_cycle_size)
                l_gvc_raw = l_cycles * l_cycle_bonus
                if l_cycles >= l_extra_cycles:
                    l_gvc_raw += l_extra_bonus
                
                l_limit = float('inf')
                if level_title_id in MAX_BINARY_LIMITS:
                    l_limit = MAX_BINARY_LIMITS[level_title_id][2] # Giả định Gold cap
                l_gvc = min(l_gvc_raw, l_limit)
                
                level_matching = npp_active_in_level * l_gvc * rate
                matching_income += level_matching
                matching_details.append({
                    "level": f"F{level}",
                    "active_npp": npp_active_in_level,
                    "avg_gvc": l_gvc,
                    "rate": rate,
                    "matching": level_matching
                })
        else:
            matching_details.append({"note": f"Nhánh yếu ({cv_weak_monthly:,.0f} CV) không đạt mốc tối thiểu của {group_title} ({rule['min_weak_cv']:,.0f} CV)"})
    else:
        matching_details.append({"note": "Danh hiệu dưới Director không được hưởng hoa hồng cộng hưởng"})
        
    # Nguồn 6: Hoa hồng Lãnh đạo (Leadership Commission)
    # Lấy doanh số nhánh yếu tháng này làm tham chiếu
    leadership_income = 0.0
    leadership_rate = 0.0
    if title_id:
        if title_id == "RUBY" and cv_weak_monthly >= 110000:
            leadership_rate = 0.010
        elif title_id == "EME" and cv_weak_monthly >= 220000:
            leadership_rate = 0.015
        elif title_id == "DIA" and cv_weak_monthly >= 440000:
            leadership_rate = 0.020
        elif title_id == "BD" and cv_weak_monthly >= 660000:
            leadership_rate = 0.025
        elif title_id == "BKD" and cv_weak_monthly >= 1000000:
            leadership_rate = 0.030
        elif title_id in ["CD", "AMB"] and cv_weak_monthly >= 1000000:
            leadership_rate = 0.035
            
        leadership_income = cv_weak_monthly * leadership_rate * 1000  # Quy đổi 1 CV = 1.000 VNĐ

    # Nguồn 7: Thưởng Vinh danh hiện vật cấp cao (Mô hình tĩnh ghi nhận 0, giải thích rõ)
    awards_income = 0.0
    
    total_income = retail_income + sponsor_income + binary_income + qualify_income + matching_income + leadership_income + awards_income
    
    return {
        "n_consumer": n_consumer,
        "n_active_distributor": n_active_distributor,
        "cv_total_monthly": cv_total_monthly,
        "accumulated_group_cv": accumulated_group_cv,
        "group_title": group_title,
        "title_id": title_id,
        "f1_w_title": f1_w_title,
        "f1_s_title": f1_s_title,
        "cv_weak_monthly": cv_weak_monthly,
        "num_cycles": num_cycles,
        "retail_income": retail_income,
        "sponsor_income": sponsor_income,
        "binary_income": binary_income,
        "binary_income_raw": binary_income_raw,
        "binary_limit": binary_limit,
        "qualify_income": qualify_income,
        "matching_income": matching_income,
        "matching_details": matching_details,
        "leadership_income": leadership_income,
        "leadership_rate": leadership_rate,
        "awards_income": awards_income,
        "total_income": total_income
    }

def simulate_dynamic_36months(n_total, p_consumer, p_distributor, r_retention, v_consumer_cv, v_distributor_cv, r_split_strong, personal_rank="GOLD", n_f1=3, dup_factor=2, f1_share=0.5, n_start=20, npp_start=6, khtt_start=15, f1_start=1, cv_start=20000, cv_weak_start=8000):
    """Mô phỏng động chuỗi thời gian 36 tháng, tăng trưởng S-curve từ hiện trạng Baseline, tích lũy Qualify và thuật toán quy hoạch tuyến KPIs"""
    results = []
    
    # Khởi tạo trạng thái tích lũy dựa trên Baseline
    accumulated_weak_cv = cv_weak_start
    accumulated_strong_cv = cv_start - cv_weak_start
    accumulated_qualify_cv = cv_weak_start
    
    # Trạng thái đạt mốc thưởng Qualify trong chu kỳ hiện tại
    qualify_milestones = {80000: False, 240000: False, 550000: False}
    
    # Theo dõi xem đã nhận thưởng vinh danh Crown Diamond / Ambassador chưa
    awards_achieved = {"CD": False, "AMB": False}
    
    # Cân nhánh yếu điểm dư carryover
    weak_cv_carryover = 0.0
    
    # Số NPP tháng trước đó để tính số tuyển mới
    n_distributor_prev = npp_start
    
    # Doanh số nhánh yếu tháng trước đó để tính hoa hồng lãnh đạo
    cv_weak_prev = cv_weak_start
    
    N_start = n_start
    t0 = 18.0
    growth_rate = 0.25
    
    title_ids = [t["id"] for t in TITLES]
    n_f1_current_float = float(f1_start)
    n_f1_current = f1_start
    
    for t in range(1, 37):
        # 1. Tính quy mô tích lũy theo S-curve ở tháng t
        n_t = N_start + (n_total - N_start) / (1.0 + math.exp(-growth_rate * (t - t0)))
        n_t = int(n_t)
        
        n_consumer = int(n_t * p_consumer)
        n_distributor = int(n_t * p_distributor)
        n_active_distributor = int(n_distributor * r_retention)
        
        # 2. Doanh số phát sinh trong tháng t
        cv_consumer_monthly = n_consumer * v_consumer_cv
        cv_distributor_monthly = n_active_distributor * v_distributor_cv
        cv_total_monthly = cv_consumer_monthly + cv_distributor_monthly
        
        # Phân bổ nhánh yếu / mạnh trong tháng t
        r_split_weak = 1.0 - r_split_strong
        cv_weak_monthly = cv_total_monthly * r_split_weak
        cv_strong_monthly = cv_total_monthly * r_split_strong
        
        # Cộng dồn lũy kế trọn đời
        accumulated_weak_cv += cv_weak_monthly
        accumulated_strong_cv += cv_strong_monthly
        accumulated_group_cv = accumulated_weak_cv + accumulated_strong_cv
        
        # Doanh số F1 mạnh gánh lũy kế
        cv_weak_accumulated_f1 = accumulated_weak_cv * f1_share
        cv_strong_accumulated_f1 = accumulated_strong_cv * f1_share
        
        # Thăng cấp danh hiệu của Doanh chủ ở tháng t
        title_id, group_title, f1_w_title, f1_s_title = determine_final_title(
            accumulated_group_cv, cv_weak_accumulated_f1, cv_strong_accumulated_f1
        )
        
        # --- Tính 7 nguồn thu nhập hàng tháng ---
        
        # 1. Thu nhập Bán lẻ (Giả định 200 CV cá nhân/tháng)
        retail_cv = 200
        retail_income = retail_cv * 1000
        
        # 2. Hoa hồng Bảo trợ (Sponsor Bonus) dựa trên NPP tuyển mới
        new_npp = max(0.0, n_active_distributor - n_distributor_prev)
        n_distributor_prev = n_active_distributor
        
        # Thuật toán Quy hoạch tuyến tính KPIs:
        active_npp_target = n_total * p_distributor * r_retention
        npp_gap = max(1.0, active_npp_target - npp_start)
        f1_gap = max(0.0, n_f1 - f1_start)
        
        n_f1_prev_int = int(round(n_f1_current_float))
        new_f1_this_month_float = 0.0
        if f1_gap > 0 and npp_gap > 0:
            new_f1_this_month_float = new_npp * (f1_gap / npp_gap)
        n_f1_current_float = min(float(n_f1), n_f1_current_float + new_f1_this_month_float)
        n_f1_current = int(round(n_f1_current_float))
        new_f1_this_month = n_f1_current - n_f1_prev_int
        
        # Optimal working hours/day
        optimal_hours = 4.0
        if n_active_distributor > 0:
            optimal_hours = 4.0 + 0.5 * new_f1_this_month + 0.1 * math.log2(n_active_distributor)
        if optimal_hours > 6.0:
            optimal_hours = 6.0
        elif optimal_hours < 4.0:
            optimal_hours = 4.0
            
        sum_structural_npp = sum(n_f1_current * (dup_factor**(i-1)) for i in range(1, 6))
        new_f1 = new_npp * (n_f1_current / sum_structural_npp)
        new_f2 = new_npp * ((n_f1_current * dup_factor) / sum_structural_npp)
        new_f3_f5 = new_npp * (sum(n_f1_current * (dup_factor**(i-1)) for i in [3, 4, 5]) / sum_structural_npp)
        
        package_cv = 2000
        sponsor_income_raw = (new_f1 * 0.10 * package_cv * 1000) + (new_f2 * 0.10 * package_cv * 1000) + (new_f3_f5 * 0.05 * package_cv * 1000)
        gold_sponsor_bonus = 0.0
        if personal_rank == "GOLD":
            gold_sponsor_bonus = (new_f1 * 0.20) * 1000000
        sponsor_income = sponsor_income_raw + gold_sponsor_bonus
        
        # 3. Hoa hồng Doanh số Nhóm (GVC) - Cân nhánh tích lũy
        is_director_or_above = False
        if title_id:
            try:
                dir_idx = title_ids.index("DIR")
                curr_idx = title_ids.index(title_id)
                is_director_or_above = curr_idx >= dir_idx
            except ValueError:
                pass
                
        if is_director_or_above:
            cycle_size = 7000
            cycle_bonus = 560000
            extra_cycles = 8
            extra_bonus = 4480000
        else:
            cycle_size = 3000
            cycle_bonus = 300000
            extra_cycles = 20
            extra_bonus = 6000000
            
        total_weak_cv = cv_weak_monthly + weak_cv_carryover
        num_cycles = int(total_weak_cv / cycle_size)
        binary_income_raw = num_cycles * cycle_bonus
        if num_cycles >= extra_cycles:
            binary_income_raw += extra_bonus
            
        weak_cv_carryover = total_weak_cv - (num_cycles * cycle_size)
        
        # Trần Maxout
        binary_limit = float('inf')
        rank_idx = 2  # Gold
        if personal_rank == "BRONZE":
            rank_idx = 0
        elif personal_rank == "SILVER":
            rank_idx = 1
            
        if title_id in MAX_BINARY_LIMITS:
            binary_limit = MAX_BINARY_LIMITS[title_id][rank_idx]
            binary_income = min(binary_income_raw, binary_limit)
        else:
            binary_income = binary_income_raw
            
        # 4. Thưởng Duy trì Doanh số (Qualify Bonus) cộng dồn liên tháng
        accumulated_qualify_cv += cv_weak_monthly
        qualify_income = 0.0
        rank_milestones = QUALIFY_BONUS_LOOKUP.get(personal_rank, {})
        
        # Kiểm tra thăng tiến mốc
        for milestone, bonus in sorted(rank_milestones.items()):
            if accumulated_qualify_cv >= milestone and not qualify_milestones[milestone]:
                qualify_income += bonus * 1000
                qualify_milestones[milestone] = True
                
        # Reset chu kỳ khi vượt mốc tối đa 550.000 CV
        if accumulated_qualify_cv >= 550000:
            accumulated_qualify_cv = 0.0
            qualify_milestones = {80000: False, 240000: False, 550000: False}
            
        # 5. Hoa hồng Cộng hưởng (Matching Bonus)
        matching_income = 0.0
        if title_id in MATCHING_RULES:
            rule = MATCHING_RULES[title_id]
            if cv_weak_monthly >= rule["min_weak_cv"]:
                for level, rate in rule["levels"].items():
                    npp_in_level = n_f1_current * (dup_factor**(level - 1))
                    npp_active_in_level = min(npp_in_level, max(1, int(npp_in_level * r_retention)))
                    
                    cv_weak_level = cv_weak_monthly / npp_in_level
                    cv_accumulated_level = (cv_total_monthly / npp_in_level) * 12
                    level_title_id, _ = get_title_by_cv_only(cv_accumulated_level)
                    
                    is_level_dir = False
                    if level_title_id:
                        try:
                            dir_idx = title_ids.index("DIR")
                            l_idx = title_ids.index(level_title_id)
                            is_level_dir = l_idx >= dir_idx
                        except ValueError:
                            pass
                    
                    l_cycle_size = 7000 if is_level_dir else 3000
                    l_cycle_bonus = 560000 if is_level_dir else 300000
                    l_extra_cycles = 8 if is_level_dir else 20
                    l_extra_bonus = 4480000 if is_level_dir else 6000000
                    
                    l_cycles = int(cv_weak_level / l_cycle_size)
                    l_gvc_raw = l_cycles * l_cycle_bonus
                    if l_cycles >= l_extra_cycles:
                        l_gvc_raw += l_extra_bonus
                    
                    l_limit = float('inf')
                    if level_title_id in MAX_BINARY_LIMITS:
                        l_limit = MAX_BINARY_LIMITS[level_title_id][2]
                    l_gvc = min(l_gvc_raw, l_limit)
                    
                    matching_income += npp_active_in_level * l_gvc * rate
                    
        # 6. Hoa hồng Lãnh đạo (Leadership Commission)
        # Sử dụng doanh số nhánh yếu của tháng trước đó
        leadership_income = 0.0
        leadership_rate = 0.0
        if title_id:
            if title_id == "RUBY" and cv_weak_prev >= 110000:
                leadership_rate = 0.010
            elif title_id == "EME" and cv_weak_prev >= 220000:
                leadership_rate = 0.015
            elif title_id == "DIA" and cv_weak_prev >= 440000:
                leadership_rate = 0.020
            elif title_id == "BD" and cv_weak_prev >= 660000:
                leadership_rate = 0.025
            elif title_id == "BKD" and cv_weak_prev >= 1000000:
                leadership_rate = 0.030
            elif title_id in ["CD", "AMB"] and cv_weak_prev >= 1000000:
                leadership_rate = 0.035
                
            leadership_income = cv_weak_monthly * leadership_rate * 1000
            
        cv_weak_prev = cv_weak_monthly
        
        # 7. Thưởng Vinh danh hiện vật cấp cao (Crown Diamond & Ambassador)
        awards_income = 0.0
        if title_id == "CD" and not awards_achieved["CD"]:
            awards_income = 1100000000.0  # Thưởng xe hơi CD ~ 1.1 tỷ
            awards_achieved["CD"] = True
        elif title_id == "AMB" and not awards_achieved["AMB"]:
            awards_income = 1900000000.0  # Thưởng xe hơi Ambassador ~ 1.9 tỷ
            awards_achieved["AMB"] = True
            
        total_income = retail_income + sponsor_income + binary_income + qualify_income + matching_income + leadership_income + awards_income
        
        results.append({
            "month": t,
            "n_total": n_t,
            "n_active_distributor": n_active_distributor,
            "cv_total_monthly": cv_total_monthly,
            "accumulated_group_cv": accumulated_group_cv,
            "group_title": group_title,
            "title_id": title_id,
            "cv_weak_monthly": cv_weak_monthly,
            "retail_income": retail_income,
            "sponsor_income": sponsor_income,
            "binary_income": binary_income,
            "qualify_income": qualify_income,
            "matching_income": matching_income,
            "leadership_income": leadership_income,
            "awards_income": awards_income,
            "total_income": total_income,
            "new_f1_this_month": new_f1_this_month,
            "optimal_hours": optimal_hours
        })
        
    return results

def main():
    parser = argparse.ArgumentParser(description="Vinalink Compensation Simulator CLI (Upgraded)")
    parser.add_argument("--size", type=int, default=10000, help="Tổng quy mô hệ thống sau 3 năm")
    parser.add_argument("--retention", type=float, default=0.3, help="Tỷ lệ giữ chân nhà phân phối (0.0 - 1.0)")
    parser.add_argument("--split", type=float, default=0.7, help="Tỷ lệ nhánh mạnh (ví dụ: 0.7 tương đương lệch 70/30)")
    parser.add_argument("--rank", type=str, default="GOLD", choices=["BRONZE", "SILVER", "GOLD"], help="Cấp bậc cá nhân của Doanh chủ")
    parser.add_argument("--f1", type=int, default=3, help="Số lượng F1 giả lập của Doanh chủ")
    parser.add_argument("--dup", type=int, default=2, help="Hệ số nhân bản chiều sâu")
    parser.add_argument("--f1-share", type=float, default=0.5, help="Tỷ lệ doanh số F1 mạnh gánh để tính danh hiệu (0.0 - 1.0)")
    parser.add_argument("--dynamic", action="store_true", help="Chạy mô phỏng động chuỗi thời gian 36 tháng")
    
    # Baseline args
    parser.add_argument("--n-start", type=int, default=20, help="Quy mô mạng lưới Baseline hiện trạng")
    parser.add_argument("--npp-start", type=int, default=6, help="Số NPP hoạt động Baseline")
    parser.add_argument("--khtt-start", type=int, default=15, help="Số KHTT hoạt động Baseline")
    parser.add_argument("--f1-start", type=int, default=1, help="Số F1 nòng cốt Baseline")
    parser.add_argument("--cv-start", type=int, default=20000, help="Doanh số nhóm hiện trạng Baseline")
    parser.add_argument("--cv-weak-start", type=int, default=8000, help="Doanh số nhánh yếu hiện trạng Baseline")
    
    args = parser.parse_args()
    
    if args.dynamic:
        res_list = simulate_dynamic_36months(
            n_total=args.size,
            p_consumer=0.8,
            p_distributor=0.2,
            r_retention=args.retention,
            v_consumer_cv=1000,
            v_distributor_cv=2000,
            r_split_strong=args.split,
            personal_rank=args.rank,
            n_f1=args.f1,
            dup_factor=args.dup,
            f1_share=args.f1_share,
            n_start=args.n_start,
            npp_start=args.npp_start,
            khtt_start=args.khtt_start,
            f1_start=args.f1_start,
            cv_start=args.cv_start,
            cv_weak_start=args.cv_weak_start
        )
        
        print("=" * 130)
        print("                 BÁO CÁO MÔ PHỎNG ĐỘNG DÒNG TIỀN 36 THÁNG HỆ THỐNG VINALINK (LOGISTIC S-CURVE)")
        print("=" * 130)
        print(f"Tổng quy mô tích lũy: {args.size} TV | F1 giả lập: {args.f1} | Hệ số nhân bản: {args.dup} | F1 Gánh: {args.f1_share*100:.0f}%")
        print(f"Giữ chân: {args.retention*100:.0f}% | Phân bổ nhánh: {args.split*100:.0f}/{ (1-args.split)*100:.0f} | Cấp bậc cá nhân: {args.rank}")
        print(f"Baseline: Quy mô {args.n_start} TV | NPP: {args.npp_start} | KHTT: {args.khtt_start} | F1: {args.f1_start} | DS: {args.cv_start} CV")
        print("-" * 130)
        print(f"{'Tháng':<5} | {'Quy mô':<7} | {'Doanh số':<12} | {'Danh hiệu':<14} | {'GVC (Nhóm)':<12} | {'Qualify':<10} | {'Matching':<10} | {'Lãnh đạo':<10} | {'F1 Mới':<8} | {'Giờ làm':<8} | {'TỔNG THU NHẬP':<15}")
        print("-" * 130)
        for r in res_list:
            if r["month"] in [1, 6, 12, 18, 24, 30, 36] or r["awards_income"] > 0 or r["qualify_income"] > 0:
                awards_tag = " (+Thưởng xe)" if r["awards_income"] > 0 else ""
                print(f"Tháng {r['month']:02d} | {r['n_total']:<7,d} | {r['cv_total_monthly']:<12,.0f} | {r['group_title']:<14} | {r['binary_income']:<12,.0f} | {r['qualify_income']:<10,.0f} | {r['matching_income']:<10,.0f} | {r['leadership_income']:<10,.0f} | {r['new_f1_this_month']:<8.1f} | {r['optimal_hours']:<8.1f} | {r['total_income']:<15,.0f}{awards_tag}")
        print("-" * 130)
        
        total_3y = sum(x["total_income"] for x in res_list)
        avg_3y = total_3y / 36
        print(f"Tổng thu nhập tích lũy 3 năm (36 tháng): {total_3y:,.0f} VNĐ")
        print(f"Thu nhập thụ động trung bình hàng tháng: {avg_3y:,.0f} VNĐ/tháng")
        print("=" * 110)
        
    else:
        res = simulate(
            n_total=args.size,
            p_consumer=0.8,
            p_distributor=0.2,
            r_retention=args.retention,
            v_consumer_cv=1000,
            v_distributor_cv=2000,
            r_split_strong=args.split,
            personal_rank=args.rank,
            n_f1=args.f1,
            dup_factor=args.dup,
            f1_share=args.f1_share
        )
        
        print("=" * 80)
        print("        BÁO CÁO MÔ PHỎNG TĨNH HỆ THỐNG VINALINK (7 NGUỒN THU)")
        print("=" * 80)
        print(f"Tổng quy mô hệ thống: {args.size} thành viên (80% Tiêu dùng - 20% Kinh doanh)")
        print(f"F1 giả lập: {args.f1} | Hệ số nhân bản: {args.dup} | Tỷ lệ F1 gánh nhánh: {args.f1_share*100:.0f}%")
        print(f"Tỷ lệ giữ chân NPP hoạt động thực tế: {args.retention * 100:.1f}%")
        print(f"Tỷ lệ phân bổ nhánh (Mạnh/Yếu): {args.split * 100:.0f}/{ (1 - args.split) * 100:.0f}")
        print(f"Cấp bậc cá nhân Doanh chủ: {args.rank}")
        print("-" * 80)
        print(f"Khách hàng thân thiết hoạt động: {res['n_consumer']:,} người")
        print(f"Nhà phân phối hoạt động thực tế: {res['n_active_distributor']:,} người")
        print(f"Doanh số phát sinh hàng tháng: {res['cv_total_monthly']:,} CV")
        print(f"Doanh số tích lũy nhóm ước tính (1 năm): {res['accumulated_group_cv']:,} CV")
        print(f"Danh hiệu thăng cấp của Doanh chủ: {res['group_title']} ({res['title_id']})")
        print(f"  * Danh hiệu F1 nhánh Yếu mạnh nhất: {res['f1_w_title']}")
        print(f"  * Danh hiệu F1 nhánh Mạnh mạnh nhất: {res['f1_s_title']}")
        print("-" * 80)
        print(f"1. Thu nhập Bán lẻ: {res['retail_income']:,} VNĐ/tháng")
        print(f"2. Hoa hồng Bảo trợ (Sponsor): {res['sponsor_income']:,} VNĐ/tháng")
        print(f"3. Hoa hồng Doanh số nhóm (GVC): {res['binary_income']:,} VNĐ/tháng")
        if res['binary_income_raw'] > res['binary_limit']:
            print(f"   ⚠️  BỊ CHẠM TRẦN MAXOUT HOA HỒNG CHU KỲ NHÓM: {res['binary_limit']:,} VNĐ")
        print(f"4. Thưởng duy trì doanh số (Qualify Bonus trung bình): {res['qualify_income']:,} VNĐ/tháng")
        
        print("5. Hoa hồng Cộng hưởng (Matching Bonus):")
        for detail in res["matching_details"]:
            if "note" in detail:
                print(f"   * {detail['note']}")
            else:
                print(f"   * Tầng {detail['level']}: Hưởng {detail['rate']*100:.0f}% trên {detail['active_npp']} NPP (Chu kỳ TB: {detail['avg_gvc']:,} VNĐ) = {detail['matching']:,} VNĐ")
        print(f"   Total Matching: {res['matching_income']:,} VNĐ/tháng")
        
        print(f"6. Hoa hồng Lãnh đạo (Quỹ Rub trở lên): {res['leadership_income']:,} VNĐ/tháng (Tỷ lệ: {res['leadership_rate']*100:.1f}%)")
        print(f"7. Thưởng Vinh danh & hiện vật cấp cao: {res['awards_income']:,} VNĐ (Mô phỏng tĩnh)")
        print("-" * 80)
        print(f"TỔNG THU NHẬP ƯỚC TÍNH HÀNG THÁNG: {res['total_income']:,} VNĐ/tháng")
        print("=" * 80)

if __name__ == "__main__":
    main()
