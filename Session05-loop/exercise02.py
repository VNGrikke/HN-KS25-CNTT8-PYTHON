branch_count = int(input("Nhập số lượng chi nhánh: "))
class_count = int(input("Nhập số lượng chi lớp mỗi chi nhánh: "))


result = ""

for branch in range(1, branch_count+1):

    total_student = 0

    student_count = input(f"Chi nhánh {branch} có {class_count} lớp: ")

    student_numbers = student_count.replace(',', ' ').split()

    for student in student_numbers:
        total_student += int(student)

    result += f"Chi nhánh {branch}: {total_student} học viên\n"

print(result)

