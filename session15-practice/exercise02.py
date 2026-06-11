atm_vault_balance = 50000000
user_account_balance = 10000000


def display_menu():
    print("""
============= SMART ATM =============
1. Xem số dư
2. Nạp tiền
3. Rút tiền
4. Kết thúc giao dịch
=====================================
""")


def display_balances():
    print(f"""
--- SỐ DƯ TÀI KHOẢN ---
Tài khoản của bạn: {user_account_balance:,} VND
(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND
""")


def deposit_money(amount):
    global user_account_balance
    global atm_vault_balance

    if amount <= 0:
        print("Số tiền không hợp lệ")
        return False

    user_account_balance += amount
    atm_vault_balance += amount

    return True


def check_withdrawal_rules(amount):
    fee = 1100

    if amount <= 0:
        return "INVALID_AMOUNT"

    if amount % 50000 != 0:
        return "INVALID_MULTIPLE"

    if amount + fee > user_account_balance:
        return "INSUFFICIENT_FUNDS"

    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"

    return "OK"


def execute_withdrawal(total_deduction, amount_to_dispense):
    global user_account_balance
    global atm_vault_balance

    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense


def main():
    while True:
        display_menu()

        choice = input(
            "Vui lòng chọn giao dịch (1-4): "
        ).strip()

        match choice:

            case "1":
                display_balances()

            case "2":
                print("--- NẠP TIỀN ---")

                amount_str = input(
                    "Nhập số tiền muốn nạp: "
                ).strip()

                if not amount_str.isdigit():
                    print("Số tiền không hợp lệ")
                    continue

                amount = int(amount_str)

                if deposit_money(amount):
                    print(
                        f"Giao dịch thành công! "
                        f"Số dư tài khoản hiện tại: "
                        f"{user_account_balance:,} VND."
                    )

            case "3":
                print("--- RÚT TIỀN ---")

                amount_str = input(
                    "Nhập số tiền cần rút: "
                ).strip()

                if not amount_str.isdigit():
                    print("Số tiền không hợp lệ")
                    continue

                amount = int(amount_str)

                result = check_withdrawal_rules(amount)

                if result == "INVALID_AMOUNT":
                    print("Số tiền không hợp lệ")

                elif result == "INVALID_MULTIPLE":
                    print(
                        "Số tiền rút phải là bội số của 50,000"
                    )

                elif result == "INSUFFICIENT_FUNDS":
                    print(
                        "Giao dịch thất bại: "
                        "Tài khoản không đủ số dư."
                    )

                elif result == "ATM_OUT_OF_CASH":
                    print(
                        "Giao dịch thất bại: "
                        "Máy ATM không đủ tiền mặt để phục vụ."
                    )

                elif result == "OK":
                    fee = 1100
                    total_deduction = amount + fee

                    print("Giao dịch đang xử lý...")

                    execute_withdrawal(
                        total_deduction,
                        amount
                    )

                    print(
                        f"Phí giao dịch: {fee:,} VND"
                    )
                    print(
                        f"Bạn đã rút thành công "
                        f"{amount:,} VND."
                    )
                    print(
                        f"Số dư tài khoản còn lại: "
                        f"{user_account_balance:,} VND."
                    )

            case "4":
                print(
                    "Cảm ơn quý khách đã sử dụng dịch vụ!"
                )
                break

            case _:
                print("Lựa chọn không hợp lệ!")


main()