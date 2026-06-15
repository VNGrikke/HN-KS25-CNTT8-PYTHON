students = [{
    "id": "SV001",
    "name": "Nguyen Van A",
    "math": 8.5,
    "physics": 7.0,
    "chemistry": 9.0,
    "average": 8.17,
    "rank": "Gioi"
}]

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

# Hien thi danh sach sinh vien
def display_student():
    
    print(f"{'Mã sinh viên':<20} | {'Họ tên':<20}  | {'Điểm Toán':<10} | {'Điểm Lý':<10} | {'Điểm Hóa':<10} | {'Điểm trung bình':<20} | {'Xếp loại':<15}")
    
    if len(students) == 0:
        print(f"{'DANH SACH TRONG!!!'}")
    else:     
        for student in students:
            print(f"{student['id']:<20} | {student['name']:<20}  | {student['math']:<10.2f} | {student['physics']:<10.2f} | {student['chemistry']:<10.2f} | {student['average']:<20.2f} | {student['rank']:<15.2f}")

# Kiem tra rong
def is_empty(value):
    if value == "":
        return False
    return True

# Kiem tra trung lap
def check_dupplication(value, value_to_check):
    
    for student in students:
        if value == student[value_to_check]:
            print("Da ton tai!!!")
            return False
    return True

# Kiem tra diem so
def validate_score(score):
    if score < 0 or score > 10:
        return False
    return True

# Nhap diem so
def input_score(subject):
    while True:
        try:
            score = float(input(f"Nhap diem {subject}: "))

            if validate_score(score):
                return score

            print("Diem phai tu 0 den 10")

        except ValueError:
            print("Vui long nhap so")

def classify_academic_rank(score):
    if score < 5.0 :
        return "Yeu"
    if score < 7.0 :
        return "Trung binh"
    if score < 8.0 :
        return "Kha"
    if score <= 10.0 :
        return "Gioi"
    
# Them sinh vien
def add_student():
    
    while True:
        id_student = input("Nhap ma sinh vien moi: ").strip().upper()

        if is_empty(id_student) == False:
            print("Ma sinnh vien khong duoc de trong")
            continue

        if check_dupplication(id_student, "id"):
            break

    while True:
        name_student = input("Nhap ten sinh vien: ").strip()

        if not is_empty(name_student):
            print("Ten sinh vien khong duoc de trong")
            continue

        break

    score_math = input_score("Toan")
    score_physics = input_score("Ly")
    score_chemistry = input_score("Hoa")

    average = (score_chemistry + score_math + score_physics)/3

    rank = classify_academic_rank(average)


    students.append({id_student, name_student, score_math, score_chemistry, score_physics, average, rank})

def main():
    while True:
        display_menu()

        choice = input("Lựa chọn của bạn: ").strip()

        match choice:
            case "1":
                display_student()

            case "2": 
                add_student()

            case "8":
                print("Thoát chương trình.")
                break
            case _:
                print("Vui long nhap lai!!!")


main()