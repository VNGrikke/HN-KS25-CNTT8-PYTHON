user_age_input = input("Nhập tuổi người dùng: ").strip()
average_score_input = input("Nhập điểm trung bình: ").strip()

is_valid_age = user_age_input.isdigit()
is_valid_score = average_score_input.replace('.', '', 1).isdigit()

if not is_valid_age or not is_valid_score:
    print("Dữ liệu không hợp lệ. Vui lòng kiểm tra lại.")
else:
    user_age = int(user_age_input)
    average_score = float(average_score_input)

    is_eligible = (user_age >= 18) and (average_score >= 5.0)
    is_excellent = (average_score >= 8.0) or (average_score == 10.0)
    is_failed = not (average_score >= 5.0)

    print(f"Tuổi người dùng: {user_age}")
    print(f"Điểm trung bình: {average_score}")
    print(f"Đủ điều kiện tham gia: {is_eligible}")
    print(f"Học sinh giỏi: {is_excellent}")
    print(f"Rớt môn: {is_failed}")