student_score_input = input("Nhập điểm trung bình: ").strip()
menu_choice = input("Nhập lựa chọn menu (1, 2, 3): ").strip()

is_valid_score = student_score_input.replace('.', '', 1).isdigit()

if not is_valid_score:
    print("Dữ liệu điểm không hợp lệ. Vui lòng kiểm tra lại.")
else:
    student_score = float(student_score_input)

    if student_score >= 8.5:
        grade = "Giỏi"
    elif student_score >= 6.5:
        grade = "Khá"
    elif student_score >= 5.0:
        grade = "Trung bình"
    else:
        grade = "Yếu"

    match menu_choice:
        case "1":
            drink_name = "Cà phê"
        case "2":
            drink_name = "Trà sữa"
        case "3":
            drink_name = "Nước ép"
        case _:
            drink_name = "Chọn sai menu"

    print(f"Điểm trung bình: {student_score}")
    print(f"Xếp loại học lực: {grade}\n")
    print(f"Lựa chọn menu: {menu_choice}")
    print(f"Món nước: {drink_name}")