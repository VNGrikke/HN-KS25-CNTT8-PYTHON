student_age_input = input("Nhập tuổi của học sinh: ").strip()
average_score_input = input("Nhập điểm trung bình: ").strip()

is_valid_age = student_age_input.isdigit()
is_valid_score = average_score_input.replace('.', '', 1).isdigit()

if not is_valid_age or not is_valid_score:
    print("Dữ liệu không hợp lệ. Vui lòng kiểm tra lại.")
else:
    student_age = int(student_age_input)
    average_score = float(average_score_input)

    required_age = 18
    passing_score = 5.0
    standard_score = 7.0

    is_eligible = student_age >= required_age
    is_passed = average_score >= passing_score
    is_above_standard = average_score > standard_score

    print(f"Tuổi học sinh: {student_age}")
    print(f"Điểm trung bình: {average_score}")
    print(f"Đủ tuổi đi thi: {is_eligible}")
    print(f"Qua môn: {is_passed}")
    print(f"Điểm lớn hơn điểm chuẩn: {is_above_standard}")