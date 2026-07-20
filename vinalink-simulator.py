# -*- coding: utf-8 -*-
"""
Vinalink Network Marketing Compensation & Structure Simulator
Created for: SIHUB 2026 Lean Startup Program - Chuyên đề 2 & 3
Doanh chủ: Vinalink Group Compensation Model (Nâng cấp giải thuật danh hiệu & Matching Bonus)
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
    # 1. Xác định danh hiệu tối đa của F1 mạnh nhất ở nhánh yếu và nhánh mạnh (tra cứu bằng doanh số tích lũy của F1)
    f1_weak_title_id, _ = get_title_by_cv_only(cv_weak_accumulated_f1)
    f1_strong_title_id, _ = get_title_by_cv_only(cv_strong_accumulated_f1)
    
    # Hàm kiểm tra xem danh hiệu F1 có đạt yêu cầu tối thiểu không
    def is_f1_qualified(req_title_id, actual_title_id):
        if not req_title_id:
            return True
        if not actual_title_id:
            return False
        
        # Lấy chỉ mục danh hiệu để so sánh thứ bậc
        title_ids = [t["id"] for t in TITLES]
        try:
            req_idx = title_ids.index(req_title_id)
            actual_idx = title_ids.index(actual_title_id)
            return actual_idx >= req_idx
        except ValueError:
            return False

    # 2. Duyệt qua danh sách danh hiệu từ thấp đến cao để kiểm tra điều kiện của Doanh chủ
    final_title_id = None
    final_title_name = "NPP Thường"
    
    for t in TITLES:
        if accumulated_group_cv >= t["min_group_cv"]:
            req_f1 = t["req_f1_title"]
            # Kiểm tra ràng buộc danh hiệu F1 ở cả 2 nhánh (yếu và mạnh)
            if req_f1:
                ok_weak = is_f1_qualified(req_f1, f1_weak_title_id)
                ok_strong = is_f1_qualified(req_f1, f1_strong_title_id)
                if ok_weak and ok_strong:
                    final_title_id = t["id"]
                    final_title_name = t["name"]
                else:
                    # Bị nghẽn danh hiệu do F1 không đạt chuẩn nâng đỡ
                    break
            else:
                final_title_id = t["id"]
                final_title_name = t["name"]
        else:
            break
            
    return final_title_id, final_title_name, f1_weak_title_id, f1_strong_title_id

def simulate(n_total, p_consumer, p_distributor, r_retention, v_consumer_cv, v_distributor_cv, r_split_strong, personal_rank="GOLD"):
    # 1. Số lượng thành viên hoạt động
    n_consumer = int(n_total * p_consumer)
    n_distributor = int(n_total * p_distributor)
    n_active_distributor = int(n_distributor * r_retention)
    
    # 2. Tính doanh số phát sinh hàng tháng
    cv_consumer_monthly = n_consumer * v_consumer_cv
    cv_distributor_monthly = n_active_distributor * v_distributor_cv
    cv_total_monthly = cv_consumer_monthly + cv_distributor_monthly
    
    # Giả định doanh số nhóm tích lũy lũy kế trong 1 năm
    accumulated_group_cv = cv_total_monthly * 12
    
    # 3. Phân bổ nhánh mạnh / nhánh yếu
    r_split_weak = 1.0 - r_split_strong
    cv_weak_monthly = cv_total_monthly * r_split_weak
    cv_strong_monthly = cv_total_monthly * r_split_strong
    
    # Giả định doanh số tích lũy lũy kế của F1 mạnh nhất ở mỗi nhánh (nhánh yếu và nhánh mạnh)
    # Giả định F1 mạnh nhất gánh 50% doanh số tích lũy của nhánh đó
    cv_weak_accumulated_f1 = (cv_weak_monthly * 0.5) * 12
    cv_strong_accumulated_f1 = (cv_strong_monthly * 0.5) * 12
    
    # Xác định danh hiệu cuối cùng của Doanh chủ có xét điều kiện F1
    title_id, group_title, f1_w_title, f1_s_title = determine_final_title(
        accumulated_group_cv, cv_weak_accumulated_f1, cv_strong_accumulated_f1
    )
    
    # 4. Tính hoa hồng chu kỳ nhóm (Group Volume Commission)
    # Director trở lên (chu kỳ 7.000 CV nhận 560.000 VNĐ), dưới Director (chu kỳ 3.000 CV nhận 300.000 VNĐ)
    is_director_or_above = False
    if title_id:
        title_ids = [t["id"] for t in TITLES]
        try:
            dir_idx = title_ids.index("DIR")
            curr_idx = title_ids.index(title_id)
            is_director_or_above = curr_idx >= dir_idx
        except ValueError:
            pass
            
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
        binary_income = binary_income_raw
        
    # 5. Tính toán thưởng duy trì doanh số (Qualify Volume Bonus)
    qualify_bonus_monthly_cv = 0.0
    rank_milestones = QUALIFY_BONUS_LOOKUP.get(personal_rank, {})
    for milestone, bonus in rank_milestones.items():
        if cv_weak_monthly >= milestone:
            qualify_bonus_monthly_cv += bonus
    qualify_income = qualify_bonus_monthly_cv * 1000  # Quy đổi hoa hồng thưởng: 1 CV = 1.000 VNĐ
    
    # 6. Tính Hoa hồng Cộng hưởng (Matching Bonus) chi tiết từ F1 - F5
    matching_income = 0.0
    matching_details = []
    
    # Định nghĩa cấu hình điều kiện doanh số và phân bổ tầng theo danh hiệu
    matching_rules = {
        "DIR": {"min_weak_cv": 85000, "levels": {1: 0.10, 2: 0.10}},
        "RUBY": {"min_weak_cv": 85000, "levels": {1: 0.10, 2: 0.10}},
        "EME": {"min_weak_cv": 85000, "levels": {1: 0.10, 2: 0.10}},
        "DIA": {"min_weak_cv": 300000, "levels": {1: 0.10, 2: 0.10, 3: 0.05}},
        "BD": {"min_weak_cv": 300000, "levels": {1: 0.10, 2: 0.10, 3: 0.05}},
        "BKD": {"min_weak_cv": 300000, "levels": {1: 0.10, 2: 0.10, 3: 0.05}},
        "CD": {"min_weak_cv": 700000, "levels": {1: 0.10, 2: 0.10, 3: 0.05, 4: 0.05}},
        "AMB": {"min_weak_cv": 3000000, "levels": {1: 0.10, 2: 0.10, 3: 0.05, 4: 0.05, 5: 0.05}}
    }
    
    if title_id in matching_rules:
        rule = matching_rules[title_id]
        # Kiểm tra điều kiện doanh số nhóm phát sinh mới trong tháng tính trên Nhóm yếu của tháng trước
        if cv_weak_monthly >= rule["min_weak_cv"]:
            # Tính toán Matching Bonus cho từng tầng được hưởng
            for level, rate in rule["levels"].items():
                # Số lượng nhà phân phối hoạt động ở tầng này (theo phân rã nhị phân trực hệ lũy thừa)
                npp_in_level = 2**level
                # Giới hạn số lượng NPP hoạt động thực tế ở tầng này không vượt quá tổng NPP hoạt động của hệ thống
                npp_active_in_level = min(npp_in_level, max(1, int(n_active_distributor / 2**level)))
                
                # Ước lượng doanh số nhánh yếu trung bình của một NPP ở tầng này
                cv_weak_level = cv_weak_monthly / (2**level)
                
                # Ước lượng doanh số tích lũy 1 năm của NPP ở tầng này để xác định danh hiệu của họ
                cv_accumulated_level = (cv_total_monthly / (2**level)) * 12
                level_title_id, _ = get_title_by_cv_only(cv_accumulated_level)
                
                # Xác định kích thước chu kỳ và hoa hồng của NPP ở tầng này
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
                
                l_cycles = int(cv_weak_level / l_cycle_size)
                l_gvc_raw = l_cycles * l_cycle_bonus
                
                # Áp trần Maxout cho NPP ở tầng này (giả định cấp bậc Gold)
                l_limit = float('inf')
                if level_title_id in MAX_BINARY_LIMITS:
                    l_limit = MAX_BINARY_LIMITS[level_title_id][2] # Gold cap
                l_gvc = min(l_gvc_raw, l_limit)
                
                # Tính tổng Matching Bonus nhận được từ tầng này
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
            # Doanh số nhóm yếu tháng trước không đạt mốc tối thiểu của danh hiệu
            matching_details.append({"note": f"Nhánh yếu ({cv_weak_monthly:,.0f} CV) không đạt mốc tối thiểu của {group_title} ({rule['min_weak_cv']:,.0f} CV)"})
    else:
        matching_details.append({"note": "Danh hiệu dưới Director không được hưởng hoa hồng cộng hưởng"})

    # 7. Ước tính các hoa hồng khác (Bảo trợ trực tiếp Sponsor Bonus, Quỹ Lãnh đạo toàn quốc)
    # Các khoản này ước tính chiếm khoảng 10% trên hoa hồng chu kỳ nhóm
    other_bonuses = binary_income * 0.10
    total_income = binary_income + other_bonuses + qualify_income + matching_income
    
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
        "binary_income_raw": binary_income_raw,
        "binary_income": binary_income,
        "binary_limit": binary_limit,
        "qualify_income": qualify_income,
        "matching_income": matching_income,
        "matching_details": matching_details,
        "other_bonuses": other_bonuses,
        "total_income": total_income
    }

def main():
    parser = argparse.ArgumentParser(description="Vinalink Compensation Simulator CLI (Upgraded Model)")
    parser.add_argument("--size", type=int, default=10000, help="Tổng quy mô hệ thống sau 3 năm")
    parser.add_argument("--retention", type=float, default=0.3, help="Tỷ lệ giữ chân nhà phân phối (0.0 - 1.0)")
    parser.add_argument("--split", type=float, default=0.7, help="Tỷ lệ nhánh mạnh (ví dụ: 0.7 tương đương lệch 70/30)")
    parser.add_argument("--rank", type=str, default="GOLD", choices=["BRONZE", "SILVER", "GOLD"], help="Cấp bậc cá nhân của Doanh chủ")
    
    args = parser.parse_args()
    
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
    
    print("=" * 70)
    print("      BÁO CÁO MÔ PHỎNG ĐỊNH LƯỢNG HỆ THỐNG VINALINK (NÂNG CẤP)")
    print("=" * 70)
    print(f"Tổng quy mô hệ thống: {args.size} thành viên (80% Tiêu dùng - 20% Kinh doanh)")
    print(f"Tỷ lệ giữ chân NPP hoạt động thực tế: {args.retention * 100:.1f}%")
    print(f"Tỷ lệ phân bổ nhánh (Mạnh/Yếu): {args.split * 100:.0f}/{ (1 - args.split) * 100:.0f}")
    print(f"Cấp bậc cá nhân Doanh chủ: {args.rank}")
    print("-" * 70)
    print(f"Khách hàng thân thiết hoạt động: {res['n_consumer']:,} người")
    print(f"Nhà phân phối hoạt động thực tế: {res['n_active_distributor']:,} người")
    print(f"Doanh số phát sinh hàng tháng: {res['cv_total_monthly']:,} CV")
    print(f"Doanh số tích lũy nhóm ước tính (1 năm): {res['accumulated_group_cv']:,} CV")
    print(f"Danh hiệu thăng cấp của Doanh chủ: {res['group_title']} ({res['title_id']})")
    print(f"  * Danh hiệu F1 nhánh Yếu mạnh nhất: {res['f1_w_title']}")
    print(f"  * Danh hiệu F1 nhánh Mạnh mạnh nhất: {res['f1_s_title']}")
    print("-" * 70)
    print(f"Doanh số nhánh Yếu hàng tháng: {res['cv_weak_monthly']:,} CV")
    print(f"Số chu kỳ cân nhánh yếu: {res['num_cycles']} chu kỳ")
    print(f"Hoa hồng Chu kỳ nhóm (Thực tế): {res['binary_income_raw']:,} VNĐ")
    if res['binary_income_raw'] > res['binary_limit']:
        print(f"⚠️  BỊ CHẠM TRẦN MAXOUT HOA HỒNG CHU KỲ NHÓM: {res['binary_limit']:,} VNĐ")
    print(f"Hoa hồng Chu kỳ nhóm nhận được: {res['binary_income']:,} VNĐ")
    print(f"Thưởng duy trì doanh số (Qualify Bonus): {res['qualify_income']:,} VNĐ/tháng")
    
    print("-" * 70)
    print("HOA HỒNG CỘNG HƯỞNG MATCHING BONUS:")
    for detail in res["matching_details"]:
        if "note" in detail:
            print(f"  * {detail['note']}")
        else:
            print(f"  * Tầng {detail['level']}: Hưởng {detail['rate']*100:.0f}% trên {detail['active_npp']} NPP (Thu nhập chu kỳ bình quân: {detail['avg_gvc']:,} VNĐ) = {detail['matching']:,} VNĐ")
    print(f"Tổng hoa hồng Cộng hưởng nhận được: {res['matching_income']:,} VNĐ/tháng")
    
    print("-" * 70)
    print(f"Ước tính các hoa hồng khác (10%): {res['other_bonuses']:,} VNĐ")
    print(f"TỔNG THU NHẬP ƯỚC TÍNH HÀNG THÁNG: {res['total_income']:,} VNĐ/tháng")
    print("=" * 70)

if __name__ == "__main__":
    main()
