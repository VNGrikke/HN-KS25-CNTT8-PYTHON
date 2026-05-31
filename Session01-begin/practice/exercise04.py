student_name = input("Nhập họ tên sinh viên: ")
student_age = int(input("Nhập tuổi: "))
average_score = float(input("Nhập điểm trung bình: "))

bonus_score = average_score + 0.5

print(f"\nTên sinh viên: {student_name}")
print(f"Tuổi: {student_age}")
print(f"Điểm trung bình: {average_score}")
print(f"Điểm sau thưởng: {bonus_score}\n")

print(f"Kiểu dữ liệu của student_name: {type(student_name)}")
print(f"Kiểu dữ liệu của student_age: {type(student_age)}")
print(f"Kiểu dữ liệu của average_score: {type(average_score)}")
print(f"Kiểu dữ liệu của bonus_score: {type(bonus_score)}")