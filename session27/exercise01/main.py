
# main.py
from models.base_account import BaseAccount
from models.savings_account import SavingsAccount
from models.credit_account import CreditAccount
from models.hybrid_account import HybridAccount

from payment.vnpay import VNPayGateway
from payment.viettel_money import ViettelMoneyGateway
from payment.process_payment import process_payment

accounts = []
current_account = None


def choose_account():
    global current_account
    if not accounts:
        print("Hệ thống chưa có thông tin tài khoản.")
        return None
    for i, acc in enumerate(accounts, 1):
        print(f"{i}. {acc.account_number} - {acc.owner_name}")
    try:
        idx = int(input("Chọn tài khoản: ")) - 1
        current_account = accounts[idx]
        return current_account
    except Exception:
        print("Lựa chọn không hợp lệ.")
        return None


def menu():
    while True:
        print("""
===== VIETCOMBANK DIGIBANK PRO SIMULATOR =====
1. Mở tài khoản mới
2. Xem thông tin & MRO
3. Giao dịch
4. Áp dụng lãi suất
5. Overloading
6. Thanh toán hóa đơn
7. Thoát
==============================================
""")
        ch = input("Chọn chức năng (1-7): ")

        match ch:

            case "1":
                t = input("1.Savings 2.Credit 3.Hybrid: ")
                acc_no = input("Số TK: ")

                if not BaseAccount.validate_account_number(acc_no):
                    print("Số tài khoản không hợp lệ!")
                    continue

                name = input("Tên: ")

                match t:
                    case "1":
                        ir = float(input("Lãi suất: "))
                        acc = SavingsAccount(acc_no, name, 0, ir)

                    case "2":
                        limit = float(input("Hạn mức tín dụng: "))
                        acc = CreditAccount(acc_no, name, 0, limit)

                    case "3":
                        ir = float(input("Lãi suất: "))
                        acc = HybridAccount(acc_no, name, 0, ir)

                    case _:
                        print("Loại tài khoản không hợp lệ!")
                        continue

                accounts.append(acc)
                current_account = acc
                print("Mở tài khoản thành công!")

            case "2":
                acc = current_account or choose_account()

                if acc:
                    print(acc)
                    print("\nMRO:")
                    for cls in acc.__class__.__mro__:
                        print("-", cls.__name__)

            case "3":
                acc = current_account or choose_account()

                if not acc:
                    continue

                op = input("1.Nạp 2.Rút: ")
                amount = float(input("Số tiền: "))

                match op:
                    case "1":
                        acc.deposit(amount)

                    case "2":
                        acc.withdraw(amount)

                    case _:
                        print("Lựa chọn không hợp lệ!")

            case "4":
                acc = current_account or choose_account()

                if isinstance(acc, (SavingsAccount, HybridAccount)):
                    acc.apply_interest()
                else:
                    print("Tính năng không hỗ trợ.")

            case "5":
                acc = current_account or choose_account()

                if not acc or len(accounts) < 2:
                    print("Cần ít nhất 2 tài khoản.")
                    continue

                other = accounts[0] if accounts[0] != acc else accounts[1]

                print(f"Tổng số dư: {acc + other:,.0f} VND")
                print("A < B:", acc < other)

            case "6":
                acc = current_account or choose_account()

                if not acc:
                    continue

                gateway_choice = input("1.VNPay 2.Viettel Money: ")

                match gateway_choice:
                    case "1":
                        gateway = VNPayGateway()

                    case "2":
                        gateway = ViettelMoneyGateway()

                    case _:
                        print("Cổng thanh toán không hợp lệ!")
                        continue

                amount = float(input("Hóa đơn: "))
                process_payment(gateway, acc, amount)

            case "7":
                print("Cảm ơn đã sử dụng chương trình!")
                break

            case _:
                print("Vui lòng nhập từ 1 đến 7.")


if __name__ == "__main__":
    menu()
