student_records = [
    {
        "student_id": "SV001",
        "name": "Nguyen Van A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0
    },
    {
        "student_id": "SV002",
        "name": "Tran Thi B",
        "math": 4.0,
        "physics": 5.5,
        "chemistry": 5.0
    },
    {
        "student_id": "SV003",
        "name": "Le Van C",
        "math": 9.5,
        "physics": 9.0,
        "chemistry": 8.5
    }
]


def calculate_average(student):
    return (student["math"] + student["physics"] + student["chemistry"]) / 3


def get_rank(avg):
    if avg >= 8:
        return "Gioi"
    elif avg >= 6.5:
        return "Kha"
    elif avg >= 5:
        return "Trung binh"
    return "Yeu"


def find_student(records, student_id):
    for student in records:
        if student["student_id"] == student_id:
            return student
    return None


def display_grades(records):
    if not records:
        print("He thong chua co du lieu sinh vien.")
        return

    print("\n--- BANG DIEM SINH VIEN ---")

    for index, student in enumerate(records, start=1):
        avg = calculate_average(student)
        rank = get_rank(avg)

        print(
            f"{index}. [{student['student_id']}] {student['name']} | "
            f"Toan: {student['math']} | "
            f"Ly: {student['physics']} | "
            f"Hoa: {student['chemistry']} | "
            f"DTB: {avg:.2f} - {rank}"
        )

    print("---------------------------")


def update_student_score(records):
    student_id = input(
        "Nhap ma sinh vien can cap nhat: "
    ).strip().upper()

    student = find_student(records, student_id)

    if student is None:
        print(
            f"Khong tim thay sinh vien mang ma {student_id} trong he thong!"
        )
        return

    subject = input(
        "Chon mon hoc (1-Toan, 2-Ly, 3-Hoa): "
    ).strip()

    subject_map = {
        "1": "math",
        "2": "physics",
        "3": "chemistry"
    }

    if subject not in subject_map:
        print("Lua chon mon hoc khong hop le!")
        return

    while True:
        try:
            score = float(input("Nhap diem moi: "))

            if 0 <= score <= 10:
                break

            print(
                "Diem so khong hop le. Vui long nhap tu 0 den 10!"
            )

        except ValueError:
            print("Vui long nhap dung dinh dang so!")

    student[subject_map[subject]] = score

    print(
        f"Da cap nhat diem cua sinh vien "
        f"'{student['name']}' thanh {score}."
    )


def generate_report(records):
    if not records:
        print("He thong chua co du lieu sinh vien.")
        return

    total = len(records)
    passed = 0
    failed = 0

    for student in records:
        avg = calculate_average(student)

        if avg >= 5:
            passed += 1
        else:
            failed += 1

    print("\n--- BAO CAO HOC VU ---")
    print(f"Tong so sinh vien: {total}")
    print(
        f"So luong qua mon: {passed} sinh vien "
        f"({passed / total * 100:.2f}%)"
    )
    print(
        f"So luong truot: {failed} sinh vien "
        f"({failed / total * 100:.2f}%)"
    )
    print("----------------------")


def find_valedictorian(records):
    if not records:
        print("He thong chua co du lieu sinh vien.")
        return

    top_student = max(
        records,
        key=calculate_average
    )

    avg = calculate_average(top_student)

    print("\n--- VINH DANH THU KHOA ---")
    print(
        f"Sinh vien: {top_student['name']} "
        f"(Ma: {top_student['student_id']})"
    )
    print(f"Diem Trung Binh: {avg:.2f}")
    print(
        "Chuc mung sinh vien da dat thanh tich "
        "xuat sac nhat khoa!"
    )
    print("--------------------------")


while True:
    print("""
===== HE THONG QUAN LY DIEM THI RIKKEI UNIVERSITY =====
1. Xem bang diem va hoc luc
2. Cap nhat diem thi sinh vien
3. Bao cao thong ke (Do/Truot)
4. Tim sinh vien Thu khoa
5. Thoat chuong trinh
======================================================
""")

    choice = input(
        "Chon chuc nang (1-5): "
    ).strip()

    match choice:
        case "1":
            display_grades(student_records)

        case "2":
            update_student_score(student_records)

        case "3":
            generate_report(student_records)

        case "4":
            find_valedictorian(student_records)

        case "5":
            print(
                "Cam on ban da su dung he thong!"
            )
            break

        case _:
            print(
                "Lua chon khong hop le!"
            )
