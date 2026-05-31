student_score_input = input("Nhập điểm trung bình: ").strip()
is_member = input("Khách hàng thành viên (yes/no): ").strip().lower()
customer_rank = input("Nhập hạng thẻ: ").strip().lower()

is_valid_score = student_score_input.replace('.', '', 1).isdigit()

if not is_valid_score:
    print("Dữ liệu không hợp lệ. Vui lòng kiểm tra lại.")
else:
    student_score = float(student_score_input)

    if student_score >= 5.0:
        if student_score >= 8.0:
            grade = "Giỏi"
        elif student_score >= 6.5:
            grade = "Khá"
        else:
            grade = "Trung bình"
    else:
        grade = "Yếu"

    result = "Đậu" if student_score >= 5.0 else "Rớt"

    if is_member == "yes":
        if customer_rank == "vàng":
            discount = "20%"
        elif customer_rank == "bạc":
            discount = "10%"
        else:
            discount = "5%"
    else:
        discount = "0%"

    print(f"Điểm trung bình: {student_score}")
    print(f"Xếp loại học lực: {grade}")
    print(f"Kết quả môn học: {result}\n")
    print(f"Khách hàng thành viên: {is_member}")
    print(f"Hạng thẻ: {customer_rank}")
    print(f"Giảm giá: {discount}")