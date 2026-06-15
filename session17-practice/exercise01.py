students = [
    {
        "id": "SV001",
        "name": "Nguyen Van A",
        "math": 8.5,
        "physics": 7.0,
        "chemistry": 9.0,
        "average": 8.17,
        "rank": "Gioi"
    }
]


def display_menu():
    print("""
========== QUẢN LÝ SINH VIÊN ==========

1. Hiển thị danh sách sinh viên
2. Thêm sinh viên
3. Cập nhật điểm
4. Xóa sinh viên
5. Tìm kiếm sinh viên
6. Thống kê học lực
7. Phân loại lại học lực
8. Thoát
""")


# Hiển thị danh sách sinh viên
def display_student(student_list=None):
    if student_list is None:
        student_list = students

    if not student_list:
        print("DANH SÁCH TRỐNG!!!")
        return

    print("-" * 115)
    print(
        f"{'Mã SV':<10} | "
        f"{'Họ tên':<25} | "
        f"{'Toán':<8} | "
        f"{'Lý':<8} | "
        f"{'Hóa':<8} | "
        f"{'Điểm TB':<10} | "
        f"{'Xếp loại':<15}"
    )
    print("-" * 115)

    for student in student_list:
        print(
            f"{student['id']:<10} | "
            f"{student['name']:<25} | "
            f"{student['math']:<8.2f} | "
            f"{student['physics']:<8.2f} | "
            f"{student['chemistry']:<8.2f} | "
            f"{student['average']:<10.2f} | "
            f"{student['rank']:<15}"
        )

    print("-" * 115)


# Kiểm tra chuỗi rỗng
def is_empty(value):
    return value != ""


# Kiểm tra mã sinh viên trùng lặp
def check_duplication(student_id):
    for student in students:
        if student["id"] == student_id:
            return True
    return False


# Kiểm tra điểm hợp lệ
def validate_score(score):
    return 0 <= score <= 10


# Nhập điểm
def input_score(subject):
    while True:
        try:
            score = float(input(f"Nhập điểm {subject}: "))

            if validate_score(score):
                return score

            print("Điểm phải nằm trong khoảng từ 0 đến 10!")

        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")


# Tính điểm trung bình
def calculate_average(math, physics, chemistry):
    return round((math + physics + chemistry) / 3, 2)


# Xếp loại học lực
def classify_academic_rank(score):
    if score < 5:
        return "Yeu"
    elif score < 7:
        return "Trung binh"
    elif score < 8:
        return "Kha"
    return "Gioi"


# Tìm sinh viên theo mã
def find_student_by_id(student_id):
    for student in students:
        if student["id"] == student_id:
            return student

    return None


# Thêm sinh viên
def add_student():
    while True:
        student_id = input("Nhập mã sinh viên: ").strip().upper()

        if not is_empty(student_id):
            print("Mã sinh viên không được để trống!")
            continue

        if check_duplication(student_id):
            print("Mã sinh viên đã tồn tại!")
            continue

        break

    while True:
        student_name = input("Nhập họ tên sinh viên: ").strip()

        if not is_empty(student_name):
            print("Tên sinh viên không được để trống!")
            continue

        break

    math = input_score("Toán")
    physics = input_score("Lý")
    chemistry = input_score("Hóa")

    average = calculate_average(math, physics, chemistry)
    rank = classify_academic_rank(average)

    students.append(
        {
            "id": student_id,
            "name": student_name,
            "math": math,
            "physics": physics,
            "chemistry": chemistry,
            "average": average,
            "rank": rank
        }
    )

    print("Thêm sinh viên thành công!")


# Cập nhật điểm sinh viên
def update_student():
    student_id = input("Nhập mã sinh viên cần cập nhật: ").strip().upper()

    student = find_student_by_id(student_id)

    if student is None:
        print("Không tìm thấy sinh viên!")
        return

    print(f"Đang cập nhật điểm cho: {student['name']}")

    student["math"] = input_score("Toán")
    student["physics"] = input_score("Lý")
    student["chemistry"] = input_score("Hóa")

    student["average"] = calculate_average(
        student["math"],
        student["physics"],
        student["chemistry"]
    )

    student["rank"] = classify_academic_rank(student["average"])

    print("Cập nhật thành công!")


# Xóa sinh viên
def delete_student():
    student_id = input("Nhập mã sinh viên cần xóa: ").strip().upper()

    student = find_student_by_id(student_id)

    if student is None:
        print("Không tìm thấy sinh viên!")
        return

    confirm = input(
        f"Bạn có chắc muốn xóa {student['name']}? (Y/N): "
    ).strip().upper()

    if confirm == "Y":
        students.remove(student)
        print("Xóa thành công!")
    else:
        print("Đã hủy thao tác.")


# Tìm kiếm sinh viên
def search_student():
    print("""
1. Tìm theo mã sinh viên
2. Tìm theo tên
""")

    choice = input("Lựa chọn: ").strip()

    match choice:
        case "1":
            student_id = input(
                "Nhập mã sinh viên: "
            ).strip().upper()

            student = find_student_by_id(student_id)

            if student is None:
                print("Không tìm thấy sinh viên!")
            else:
                display_student([student])

        case "2":
            keyword = input(
                "Nhập tên cần tìm: "
            ).strip().lower()

            result = []

            for student in students:
                if keyword in student["name"].lower():
                    result.append(student)

            if not result:
                print("Không tìm thấy sinh viên!")
            else:
                display_student(result)

        case _:
            print("Lựa chọn không hợp lệ!")


# Thống kê học lực
def statistics():
    result = {
        "Gioi": 0,
        "Kha": 0,
        "Trung binh": 0,
        "Yeu": 0
    }

    for student in students:
        result[student["rank"]] += 1

    print("\n===== THỐNG KÊ HỌC LỰC =====")
    print(f"Giỏi: {result['Gioi']}")
    print(f"Khá: {result['Kha']}")
    print(f"Trung bình: {result['Trung binh']}")
    print(f"Yếu: {result['Yeu']}")


# Phân loại lại học lực
def recalculate_rank():
    if not students:
        print("Danh sách sinh viên trống!")
        return

    for student in students:
        student["average"] = calculate_average(
            student["math"],
            student["physics"],
            student["chemistry"]
        )

        student["rank"] = classify_academic_rank(
            student["average"]
        )

    print("Đã cập nhật lại học lực cho tất cả sinh viên!")


def main():
    while True:
        display_menu()

        choice = input("Lựa chọn của bạn: ").strip()

        match choice:
            case "1":
                display_student()

            case "2":
                add_student()

            case "3":
                update_student()

            case "4":
                delete_student()

            case "5":
                search_student()

            case "6":
                statistics()

            case "7":
                recalculate_rank()

            case "8":
                print("Thoát chương trình.")
                break

            case _:
                print("Vui lòng nhập lựa chọn từ 1 đến 8!")


main()