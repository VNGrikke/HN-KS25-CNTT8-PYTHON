import logging

# =======================
# LOGGING CONFIG
# =======================
logging.basicConfig(
    filename="tournament_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)

logger = logging.getLogger()

# =======================
# DATA LAYER
# =======================
matches = [
    {
        "match_id": "M01",
        "team_a": "T1",
        "team_b": "GenG",
        "score_a": 2,
        "score_b": 1,
        "status": "Completed"
    },
    {
        "match_id": "M02",
        "team_a": "JDG",
        "team_b": "BLG",
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    }
]

# =======================
# VALIDATION LAYER
# =======================
def is_valid_score(value):
    try:
        score = int(value)
        if score < 0:
            logger.error(f"Negative score input detected: {value}")
            raise ValueError("Negative score")
        return score
    except ValueError as e:
        logger.error(f"Invalid score input. Error: {e}")
        raise


# =======================
# SERVICE LAYER
# =======================
def display_matches(match_list):
    print("\n--- LỊCH THI ĐẤU & KẾT QUẢ ---")

    if not match_list:
        print("Hiện chưa có trận đấu nào trong hệ thống.")
        return

    print(f"{'Mã trận':<10} | {'Đội A':<10} | {'Đội B':<10} | {'Tỷ số':<6} | {'Trạng thái'}")
    print("-" * 70)

    for m in match_list:
        try:
            print(
                f"{m.get('match_id','?'):<10} | "
                f"{m.get('team_a','?'):<10} | "
                f"{m.get('team_b','?'):<10} | "
                f"{m.get('score_a','?')}-{m.get('score_b','?'):<4} | "
                f"{m.get('status','Unknown')}"
            )
        except Exception as e:
            logger.error(f"Missing key error: {e}")

    logger.info("User viewed the match list.")


# =======================
# ADD MATCH
# =======================
def add_match(match_list):
    print("\n--- THÊM TRẬN ĐẤU MỚI ---")

    match_id = input("Nhập mã trận đấu: ").strip()
    team_a = input("Nhập tên Đội A: ").strip()
    team_b = input("Nhập tên Đội B: ").strip()

    if not match_id:
        print("Mã trận đấu không được để trống.")
        logger.warning("User tried to add a match with empty match ID.")
        return

    if not team_a or not team_b:
        print("Tên đội không được để trống.")
        logger.warning("User tried to add a match with empty team name.")
        return

    for m in match_list:
        if m["match_id"] == match_id:
            print(f"Lỗi: Mã trận đấu {match_id} đã tồn tại.")
            logger.warning(f"Match ID {match_id} already exists.")
            return

    match_list.append({
        "match_id": match_id,
        "team_a": team_a,
        "team_b": team_b,
        "score_a": 0,
        "score_b": 0,
        "status": "Pending"
    })

    print(f"Thành công: Đã thêm trận đấu {match_id}.")
    logger.info(f"Match {match_id} added successfully")


# =======================
# FIND MATCH
# =======================
def find_match(match_list, match_id):
    for m in match_list:
        if m["match_id"] == match_id:
            return m
    return None


# =======================
# UPDATE SCORE
# =======================
def update_score(match_list):
    print("\n--- CẬP NHẬT TỶ SỐ TRẬN ĐẤU ---")

    match_id = input("Nhập mã trận đấu cần cập nhật: ").strip()
    match = find_match(match_list, match_id)

    if not match:
        print(f"Không tìm thấy trận đấu {match_id}.")
        logger.warning(f"User tried to update non-existing match {match_id}")
        return

    print(f"Trận đấu: {match['team_a']} vs {match['team_b']} ({match['status']})")

    # nhập score A
    while True:
        try:
            score_a = is_valid_score(input("Nhập điểm Đội A: "))
            break
        except ValueError:
            print("Điểm phải là số nguyên >= 0. Nhập lại!")

    # nhập score B
    while True:
        try:
            score_b = is_valid_score(input("Nhập điểm Đội B: "))
            break
        except ValueError:
            print("Điểm phải là số nguyên >= 0. Nhập lại!")

    # edge case 0-0
    if score_a == 0 and score_b == 0:
        confirm = input("Tỷ số 0-0. Trận đã hoàn thành chưa? (y/n): ").strip().lower()
        match["status"] = "Completed" if confirm == "y" else "Pending"
    else:
        match["status"] = "Completed"

    match["score_a"] = score_a
    match["score_b"] = score_b

    print(f"Thành công: Đã cập nhật tỷ số trận đấu {match_id}.")
    logger.info(f"Match {match_id} score updated successfully")


# =======================
# REPORT
# =======================
def determine_winner(match):
    if match.get("status") != "Completed":
        return "Not Started"

    if match.get("score_a", 0) > match.get("score_b", 0):
        return match["team_a"]
    elif match.get("score_b", 0) > match.get("score_a", 0):
        return match["team_b"]
    else:
        return "Draw"


def generate_report(match_list):
    print("\n--- BÁO CÁO THỐNG KÊ GIẢI ĐẤU ---")

    completed = 0

    for m in match_list:
        if m.get("status") == "Completed":
            winner = determine_winner(m)
            print(f"{m['match_id']}: {m['team_a']} {m['score_a']}-{m['score_b']} {m['team_b']} | Kết quả: {winner}")
            completed += 1

    if completed == 0:
        print("Chưa có trận đấu nào hoàn thành.")

    print(f"Tổng số trận đã hoàn thành: {completed}")

    logger.info("User generated tournament report.")


# =======================
# EXIT
# =======================
def exit_system():
    print("Thoát hệ thống...")
    logger.info("System shutdown")


# =======================
# MENU CONTROLLER
# =======================
def menu():
    while True:
        print("""
===== RIKKEI ESPORTS =====
1. Hiển thị trận đấu
2. Thêm trận đấu
3. Cập nhật tỷ số
4. Báo cáo
5. Thoát
==========================
""")

        choice = input("Chọn (1-5): ").strip()

        if choice == "1":
            display_matches(matches)
        elif choice == "2":
            add_match(matches)
        elif choice == "3":
            update_score(matches)
        elif choice == "4":
            generate_report(matches)
        elif choice == "5":
            exit_system()
            break
        else:
            print("Lựa chọn không hợp lệ!")
            logger.warning("Invalid menu choice selected")


# =======================
# RUN PROGRAM
# =======================
if __name__ == "__main__":
    menu()