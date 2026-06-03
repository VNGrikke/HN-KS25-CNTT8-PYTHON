raw_input = "   nGuyen vaN aN  ;  2004   "
data = raw_input.split(";")

while True:
    print(
        "===== HỆ THỐNG XỬ LÝ THÀNH VIÊN =====\n"
        "1. Hiển thị chuỗi dữ liệu gốc\n"
        "2. Chuẩn hóa Họ tên và tính Tuổi\n"
        "3. Tạo Mã ID và Email tự động\n"
        "4. Thoát chương trình\n"
        "=====================================\n"
    )

    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

    match choice:
        case "1":
            print(raw_input)

        case "2":
            print("[KẾT QUẢ CHUẨN HÓA DỮ LIỆU]")
            print(f"Họ và tên: {data[0].strip().title()}")
            print(f"Tuổi: {2026 - int(data[1].strip())}")

        case "3":
            member_name = data[0].strip().split()
            last_name = member_name[-1]

            id_member = last_name.upper() + data[1].strip()[2:]

            email = "".join(member_name[0][0:].lower() + member_name[1][0:].lower() + last_name.lower()) + "@company.com"

            print(f"Họ và tên: {data[0].strip().title()}")
            print(f"ID: {id_member}")
            print(f"Email: {email}")

        case "4":
            break

        case _:
            print("Lựa chọn sai...")