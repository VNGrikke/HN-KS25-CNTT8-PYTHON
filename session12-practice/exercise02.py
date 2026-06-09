saving_accounts = [
    {
        "account_id": "STK001",
        "customer_name": "Nguyễn Văn An",
        "balance": 50000000,
        "term_months": 6,
        "interest_rate": 6.5,
        "status": "active"
    },
    {
        "account_id": "STK002",
        "customer_name": "Trần Thị Bình",
        "balance": 120000000,
        "term_months": 12,
        "interest_rate": 7.2,
        "status": "active"
    }
]

while True:
    print("""
===== HỆ THỐNG QUẢN LÝ TÀI KHOẢN TIẾT KIỆM TECHBANK =====
1. Xem danh sách sổ tiết kiệm
2. Mở sổ tiết kiệm mới
3. Cập nhật thông tin sổ tiết kiệm
4. Tất toán hoặc xóa sổ tiết kiệm
5. Tính lãi dự kiến khi đến hạn
6. Kiểm tra điều kiện rút trước hạn
7. Thoát chương trình
""")

    choice = input("Nhập lựa chọn: ").strip()

    match choice:

        case "1":
            if len(saving_accounts) == 0:
                print("Danh sách sổ tiết kiệm hiện đang trống")
            else:
                print("Danh sách sổ tiết kiệm:")
                for i, account in enumerate(saving_accounts, start=1):
                    print(
                        f"{i}. Mã sổ: {account['account_id']} | "
                        f"Khách hàng: {account['customer_name']} | "
                        f"Số tiền gửi: {account['balance']} | "
                        f"Kỳ hạn: {account['term_months']} tháng | "
                        f"Lãi suất: {account['interest_rate']}%/năm | "
                        f"Trạng thái: {account['status']}"
                    )

        case "2":
            account_id = input(
                "Nhập mã sổ tiết kiệm: "
            ).strip().upper()

            customer_name = input(
                "Nhập tên khách hàng: "
            ).strip()

            if customer_name == "":
                print("Tên khách hàng không được để trống")
                continue

            duplicate = False

            for account in saving_accounts:
                if account["account_id"] == account_id:
                    duplicate = True
                    break

            if duplicate:
                print("Mã sổ tiết kiệm đã tồn tại!")
                continue

            try:
                balance = int(input("Nhập số tiền gửi: "))
                term_months = int(
                    input("Nhập kỳ hạn gửi theo tháng: ")
                )

                if balance <= 0 or term_months <= 0:
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                    continue

            except:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            try:
                interest_rate = float(
                    input("Nhập lãi suất năm: ")
                )

                if interest_rate <= 0:
                    print("Lãi suất không hợp lệ!")
                    continue

            except:
                print("Lãi suất không hợp lệ!")
                continue

            saving_accounts.append(
                {
                    "account_id": account_id,
                    "customer_name": customer_name,
                    "balance": balance,
                    "term_months": term_months,
                    "interest_rate": interest_rate,
                    "status": "active"
                }
            )

            print("Mở sổ tiết kiệm thành công!")

        case "3":
            account_id = input(
                "Nhập mã sổ tiết kiệm cần cập nhật: "
            ).strip().upper()

            found = None

            for account in saving_accounts:
                if account["account_id"] == account_id:
                    found = account
                    break

            if found is None:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue

            if found["status"] == "closed":
                print(
                    "Không thể cập nhật sổ tiết kiệm đã tất toán!"
                )
                continue

            customer_name = input(
                "Nhập tên khách hàng mới: "
            ).strip()

            if customer_name == "":
                print("Tên khách hàng không được để trống")
                continue

            try:
                balance = int(
                    input("Nhập số tiền gửi mới: ")
                )

                term_months = int(
                    input("Nhập kỳ hạn mới theo tháng: ")
                )

                if balance <= 0 or term_months <= 0:
                    print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                    continue

            except:
                print("Số tiền gửi hoặc kỳ hạn không hợp lệ")
                continue

            try:
                interest_rate = float(
                    input("Nhập lãi suất năm mới: ")
                )

                if interest_rate <= 0:
                    print("Lãi suất không hợp lệ!")
                    continue

            except:
                print("Lãi suất không hợp lệ!")
                continue

            found["customer_name"] = customer_name
            found["balance"] = balance
            found["term_months"] = term_months
            found["interest_rate"] = interest_rate

            print("Cập nhật thành công!")

        case "4":
            account_id = input(
                "Nhập mã sổ tiết kiệm cần tất toán/xóa: "
            ).strip().upper()

            found = None

            for account in saving_accounts:
                if account["account_id"] == account_id:
                    found = account
                    break

            if found is None:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue

            if found["status"] == "closed":
                print("Sổ tiết kiệm đã được tất toán trước đó")
                continue

            found["status"] = "closed"

            print("Tất toán sổ tiết kiệm thành công!")

        case "5":
            account_id = input(
                "Nhập mã sổ tiết kiệm cần tính lãi: "
            ).strip().upper()

            found = None

            for account in saving_accounts:
                if account["account_id"] == account_id:
                    found = account
                    break

            if found is None:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue

            if found["status"] == "closed":
                print(
                    "Không thể thao tác với sổ tiết kiệm đã tất toán"
                )
                continue

            interest = (
                found["balance"]
                * found["interest_rate"]
                / 100
                * found["term_months"]
                / 12
            )

            total = found["balance"] + interest

            print(f"Tiền lãi dự kiến: {interest:,.0f} VNĐ")
            print(f"Tổng tiền nhận: {total:,.0f} VNĐ")

        case "6":
            account_id = input(
                "Nhập mã sổ tiết kiệm cần kiểm tra: "
            ).strip().upper()

            found = None

            for account in saving_accounts:
                if account["account_id"] == account_id:
                    found = account
                    break

            if found is None:
                print("Không tìm thấy mã sổ tiết kiệm")
                continue

            if found["status"] == "closed":
                print(
                    "Không thể thao tác với sổ tiết kiệm đã tất toán"
                )
                continue

            try:
                actual_months = int(
                    input("Nhập số tháng thực gửi: ")
                )

                if actual_months <= 0:
                    print(
                        "Số tháng thực gửi không hợp lệ!"
                    )
                    continue

            except:
                print(
                    "Số tháng thực gửi không hợp lệ!"
                )
                continue

            if actual_months < found["term_months"]:
                applied_rate = 0.5
                print("Khách hàng rút trước hạn")
            else:
                applied_rate = found["interest_rate"]
                print(
                    "Khách hàng đủ điều kiện hưởng lãi đúng hạn"
                )

            interest = (
                found["balance"]
                * applied_rate
                / 100
                * actual_months
                / 12
            )

            total = found["balance"] + interest

            print(f"Lãi suất áp dụng: {applied_rate}%/năm")
            print(f"Tiền lãi thực nhận: {interest:,.0f} VNĐ")
            print(f"Tổng tiền thực nhận: {total:,.0f} VNĐ")

        case "7":
            print("Thoát chương trình!")
            break

        case _:
            print(
                "Lựa chọn không hợp lệ, vui lòng nhập lại"
            )