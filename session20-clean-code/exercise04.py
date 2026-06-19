import logging

# =========================
# LOGGING CONFIG
# =========================
logging.basicConfig(
    filename="roster_app.log",
    level=logging.INFO,
    format="[%(asctime)s] - [%(levelname)s] - %(message)s"
)

logger = logging.getLogger()

# =========================
# DATA LAYER
# =========================
roster = [
    {
        "player_id": "P01",
        "name": "Faker",
        "role": "Mid Lane",
        "salary": 5000.0,
        "status": "Active"
    },
    {
        "player_id": "P02",
        "name": "Oner",
        "role": "Jungle",
        "salary": 3500.0,
        "status": "Active"
    },
    {
        "player_id": "P03",
        "name": "Ruler",
        "role": "ADC",
        "salary": 6000.0,
        "status": "Benched"
    }
]

# =========================
# UTILS
# =========================
def normalize_id(player_id: str) -> str:
    return player_id.strip().upper()


def find_player(roster_list, player_id):
    player_id = normalize_id(player_id)
    for p in roster_list:
        if p.get("player_id", "").upper() == player_id:
            return p
    return None


def safe_float(value):
    try:
        val = float(value)
        if val <= 0:
            raise ValueError("Salary must be positive")
        return val
    except ValueError as e:
        logger.error(f"Failed to sign player - Invalid salary input: {e}")
        raise


# =========================
# FUNCTION 1 - DISPLAY
# =========================
def display_roster(roster_list):
    print("\n--- ĐỘI HÌNH RIKKEI ESPORTS ---")

    if not roster_list:
        print("Đội hình hiện đang trống.")
        return

    print(f"{'ID':<8} | {'Tên tuyển thủ':<20} | {'Vị trí':<15} | {'Lương':<10} | {'Trạng thái'}")
    print("-" * 80)

    for p in roster_list:
        try:
            name = p.get("name", "?")
            if p.get("status") == "Benched":
                name += " [DỰ BỊ]"

            print(
                f"{p.get('player_id','?'):<8} | "
                f"{name:<20} | "
                f"{p.get('role','?'):<15} | "
                f"{p.get('salary','?'):<10} | "
                f"{p.get('status','Unknown')}"
            )
        except KeyError:
            logger.error("Missing key in roster data")

    logger.info("Coach viewed the team roster.")


# =========================
# FUNCTION 2 - SIGN PLAYER
# =========================
def sign_player(roster_list):
    print("\n--- CHIÊU MỘ TUYỂN THỦ MỚI ---")

    player_id = normalize_id(input("Nhập mã tuyển thủ: "))

    if find_player(roster_list, player_id):
        print(f"Lỗi: Mã tuyển thủ {player_id} đã tồn tại.")
        logger.warning(f"Failed to sign player - Duplicate player ID {player_id}")
        return

    name = input("Nhập tên tuyển thủ: ").strip()
    role = input("Nhập vị trí thi đấu: ").strip()

    if not name or not role:
        print("Tên hoặc vị trí không được để trống.")
        return

    while True:
        try:
            salary = safe_float(input("Nhập mức lương hàng tháng: "))
            break
        except ValueError:
            print("Lương phải là số dương. Vui lòng nhập lại.")

    roster_list.append({
        "player_id": player_id,
        "name": name,
        "role": role,
        "salary": salary,
        "status": "Active"
    })

    print(f"Thành công: Đã chiêu mộ tuyển thủ {name}.")
    logger.info(f"Signed new player {name} with salary {salary}")


# =========================
# FUNCTION 3 - UPDATE PLAYER
# =========================
def update_player_status(roster_list):
    print("\n--- CẬP NHẬT LƯƠNG & TRẠNG THÁI ---")

    player_id = normalize_id(input("Nhập mã tuyển thủ: "))
    player = find_player(roster_list, player_id)

    if not player:
        print("Không tìm thấy tuyển thủ.")
        logger.warning(f"Failed to update player - Player ID {player_id} not found")
        return

    print(f"\nTuyển thủ: {player['name']}")
    print(f"Vị trí: {player['role']}")
    print(f"Lương hiện tại: {player['salary']}")
    print(f"Trạng thái: {player['status']}")

    print("\n1. Cập nhật lương")
    print("2. Cập nhật trạng thái")

    choice = input("Chọn: ").strip()

    # ---- UPDATE SALARY ----
    if choice == "1":
        old_salary = player["salary"]

        while True:
            try:
                new_salary = safe_float(input("Nhập lương mới: "))
                break
            except ValueError:
                print("Lương phải là số dương.")

        player["salary"] = new_salary

        print("Cập nhật lương thành công.")
        logger.info(f"Updated player {player_id} salary from {old_salary} to {new_salary}")

    # ---- UPDATE STATUS ----
    elif choice == "2":
        print("\n1. Active")
        print("2. Benched")

        status_choice = input("Chọn trạng thái: ").strip()

        new_status = "Active" if status_choice == "1" else "Benched"

        old_status = player["status"]
        player["status"] = new_status

        print("Cập nhật trạng thái thành công.")
        logger.info(f"Updated player {player_id} status from {old_status} to {new_status}")

    else:
        print("Lựa chọn không hợp lệ.")


# =========================
# FUNCTION 4 - PAYROLL
# =========================
def generate_payroll_report(roster_list):
    print("\n--- BÁO CÁO QUỸ LƯƠNG ---")

    if not roster_list:
        print("Đội hình trống. Tổng quỹ lương: 0.0")
        return

    total = 0

    print(f"{'ID':<8} | {'Tên':<15} | {'Status':<10} | {'Salary':<10} | {'Thực nhận'}")
    print("-" * 80)

    for p in roster_list:
        try:
            salary = p["salary"]
            status = p.get("status", "Unknown")

            actual_salary = salary if status == "Active" else salary * 0.5

            total += actual_salary

            print(
                f"{p['player_id']:<8} | "
                f"{p['name']:<15} | "
                f"{status:<10} | "
                f"{salary:<10} | "
                f"{actual_salary}"
            )

        except KeyError as e:
            logger.error(f"Missing key while generating payroll report: {e}")
            print("Lỗi: Một tuyển thủ đang bị thiếu dữ liệu.")
            return

    print("-" * 80)
    print(f"Tổng quỹ lương hàng tháng: {total}")

    logger.info(f"Generated monthly payroll report. Total: {total}")


# =========================
# FUNCTION 5 - EXIT
# =========================
def exit_system():
    print("Thoát hệ thống...")
    logger.info("System shutdown")


# =========================
# MENU CONTROLLER
# =========================
def menu():
    while True:
        print("""
===== RIKKEI ESPORTS TEAM MANAGEMENT =====
1. Xem đội hình
2. Chiêu mộ tuyển thủ
3. Cập nhật lương & trạng thái
4. Báo cáo quỹ lương
5. Thoát
==========================================
""")

        choice = input("Chọn (1-5): ").strip()

        if choice == "1":
            display_roster(roster)

        elif choice == "2":
            sign_player(roster)

        elif choice == "3":
            update_player_status(roster)

        elif choice == "4":
            generate_payroll_report(roster)

        elif choice == "5":
            exit_system()
            break

        else:
            print("Lựa chọn không hợp lệ!")
            logger.warning("Invalid menu choice selected")


# =========================
# RUN
# =========================
if __name__ == "__main__":
    menu()