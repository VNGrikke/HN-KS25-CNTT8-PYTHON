student_records = [
    {
        "student_id": "RA01",
        "name": "Nguyen Van Code",
        "current_points": 1500,
        "spent_points": 500,
        "refunded_points": 0,
        "multiplier": 1.0
    },
    {
        "student_id": "RA02",
        "name": "Tran Thi Bug",
        "current_points": 800,
        "spent_points": 1200,
        "refunded_points": 100,
        "multiplier": 1.5
    },
    {
        "student_id": "RA03",
        "name": "Le Van Fix",
        "current_points": 300,
        "spent_points": 0,
        "refunded_points": 0,
        "multiplier": 2.0
    }
]


def is_positive_integer(value):
    return value.isdigit() and int(value) > 0


def find_student(records, student_id):
    student_id = student_id.strip().upper()

    for student in records:
        if student["student_id"] == student_id:
            return student

    return None


def get_status(points):
    if points < 500:
        return "Can tich luy them"
    elif points <= 1500:
        return "Thanh vien tiem nang"
    else:
        return "Thanh vien uu tu"


def display_statements(records):
    print("\n--- SAO KE DIEM SO ---")

    for index, student in enumerate(records, start=1):
        print(
            f"{index}. Ma: {student['student_id']} | "
            f"Ten: {student['name']} | "
            f"Hien co: {student['current_points']} | "
            f"Da tieu: {student['spent_points']} | "
            f"Hoan tra: {student['refunded_points']} | "
            f"He so: x{student['multiplier']} | "
            f"Trang thai: {get_status(student['current_points'])}"
        )

    print("----------------------")


def redeem_rewards(records):
    student_id = input("Nhap ma hoc vien doi qua: ")
    student = find_student(records, student_id)

    if not student:
        print("Khong tim thay ho so hoc vien!")
        return

    points = input("Nhap so diem can tieu: ").strip()

    if not is_positive_integer(points):
        print("Vui long nhap so nguyen duong!")
        return

    points = int(points)

    if points > student["current_points"]:
        print("So du diem khong du de thuc hien giao dich!")
        return

    student["current_points"] -= points
    student["spent_points"] += points

    print(
        f"Giao dich thanh cong! "
        f"'{student['name']}' da tieu {points} diem. "
        f"So du con lai: {student['current_points']} diem."
    )


def appeal_score(records):
    student_id = input("Nhap ma hoc vien can phuc khao: ")
    student = find_student(records, student_id)

    if not student:
        print("Khong tim thay ho so hoc vien!")
        return

    points = input("Nhap so diem hoan lai: ").strip()

    if not is_positive_integer(points):
        print("Vui long nhap so nguyen duong!")
        return

    points = int(points)

    if points > student["spent_points"]:
        print("Khong the hoan so diem lon hon tong diem da tieu!")
        return

    student["spent_points"] -= points
    student["current_points"] += points
    student["refunded_points"] += points

    print(
        f"Hoan diem thanh cong! "
        f"'{student['name']}' duoc cong lai {points} diem."
    )


def activate_multiplier(records):
    student_id = input("Nhap ma hoc vien nhan he so: ")
    student = find_student(records, student_id)

    if not student:
        print("Khong tim thay ho so hoc vien!")
        return

    multiplier = input(
        "Nhap he so nhan moi (1.0 - 3.0): "
    ).strip()

    if multiplier.count(".") > 1:
        print(
            "He so nhan khong hop le. "
            "Chi chap nhan so tu 1.0 den 3.0"
        )
        return

    if not multiplier.replace(".", "").isdigit():
        print(
            "He so nhan khong hop le. "
            "Chi chap nhan so tu 1.0 den 3.0"
        )
        return

    multiplier = float(multiplier)

    if multiplier < 1.0 or multiplier > 3.0:
        print(
            "He so nhan khong hop le. "
            "Chi chap nhan so tu 1.0 den 3.0"
        )
        return

    student["multiplier"] = multiplier

    print(
        f"Da kich hoat he so x{multiplier} "
        f"cho hoc vien '{student['name']}'."
    )


def grade_assignment(records):
    student_id = input("Nhap ma hoc vien vua nop bai: ")
    student = find_student(records, student_id)

    if not student:
        print("Khong tim thay ho so hoc vien!")
        return

    base_points = input(
        "Nhap so diem goc dat duoc: "
    ).strip()

    if not is_positive_integer(base_points):
        print("Vui long nhap so nguyen duong!")
        return

    base_points = int(base_points)

    earned_points = int(
        base_points * student["multiplier"]
    )

    print(
        f"He so hien tai cua "
        f"'{student['name']}' la x{student['multiplier']}."
    )

    print(f"Diem thuc nhan: {earned_points}")

    student["current_points"] += earned_points

    print(
        f"Da cong {earned_points} diem vao tai khoan!"
    )


while True:
    print("""
===== HE THONG NGAN HANG DIEM SO RIKKEI ACADEMY =====
1. Hien thi sao ke diem so
2. Doi diem lay phan thuong
3. Phuc khao bai thi (Hoan diem)
4. Kich hoat he so nhan diem
5. Cham bai (Them diem)
6. Thoat chuong trinh
=====================================================
""")

    choice = input("Chon chuc nang (1-6): ").strip()

    match choice:
        case "1":
            display_statements(student_records)

        case "2":
            redeem_rewards(student_records)

        case "3":
            appeal_score(student_records)

        case "4":
            activate_multiplier(student_records)

        case "5":
            grade_assignment(student_records)

        case "6":
            print("Cam on ban da su dung he thong!")
            break

        case _:
            print("Lua chon khong hop le!")