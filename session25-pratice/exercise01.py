class BankAccount:
    # 1. Class Attributes: Thuộc tính dùng chung cho toàn hệ thống
    bank_name = "Vietcombank"
    transaction_fee = 2000

    # 2. Initialization: Khởi tạo với các thuộc tính private
    def __init__(self, account_number, account_name):
        self.__account_number = account_number
        self.__balance = 0
        self.__account_name = ""  # Khởi tạo rỗng trước để tránh lỗi AttributeError
        self.account_name = account_name  # Gọi thông qua setter để chuẩn hóa dữ liệu

    # 3. Tính Đóng Gói (Encapsulation)
    @property
    def balance(self):
        # Read-only property: Chỉ cho phép xem số dư, không có setter
        return self.__balance

    @property
    def account_name(self):
        return self.__account_name

    @account_name.setter
    def account_name(self, value):
        # Loại bỏ khoảng trắng thừa ở hai đầu
        cleaned_name = value.strip()
        
        # Bẫy 3: Tên tài khoản rỗng
        if not cleaned_name:
            print("Tên tài khoản không được để trống")
        else:
            self.__account_name = cleaned_name.upper()

    # 4. Class Method & Static Method
    @staticmethod
    def validate_account_number(account_number):
        # Kiểm tra chuỗi toàn số và có đúng 10 ký tự
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_transaction_fee(cls, new_fee):
        if new_fee < 0:
            print("Phí giao dịch không được âm")
            print(f"Phí giao dịch hiện tại vẫn là  {cls.transaction_fee:,} VND")
        else:
            cls.transaction_fee = new_fee
            print(f"Đã cập nhật phí giao dịch toàn hệ thống thành {cls.transaction_fee:,} VND")

    # 5. Instance Methods
    def deposit(self, amount):
        # Bẫy 1: Số tiền giao dịch không hợp lệ
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return

        self.__balance += amount
        print(f"Nạp tiền thành công: +{amount:,} VND")
        print(f"Số dư mới: {self.balance:,} VND")

    def withdraw(self, amount):
        # Bẫy 1: Số tiền giao dịch không hợp lệ
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return

        total_deduction = amount + self.transaction_fee

        # Bẫy 2: Số dư không đủ
        if self.__balance < total_deduction:
            print("Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch")
            print(f"Số dư mới: {self.balance:,} VND")
        else:
            self.__balance -= total_deduction
            print(f"Rút tiền thành công: -{amount:,} VND")
            print(f"Phí giao dịch: {self.transaction_fee:,} VND")
            print(f"Số dư mới: {self.balance:,} VND")

    def display_info(self):
        print("--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Ngân hàng: {self.bank_name}")
        print(f"Số tài khoản: {self.__account_number}")
        print(f"Tên chủ tài khoản: {self.__account_name}")
        print(f"Số dư hiện tại: {self.balance:,} VND")
        print(f"Phí giao dịch: {self.transaction_fee:,} VND")


# ==========================================
# HỆ THỐNG MENU CLI (NGHIỆP VỤ)
# ==========================================
def main():
    current_account = None

    while True:
        print("\n===== VIETCOMBANK DIGIBANK SIMULATOR =====")
        print("1. Mở tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Giao dịch Nạp / Rút tiền")
        print("4. Cập nhật Tên chủ tài khoản")
        print("5. Đổi phí giao dịch hệ thống")
        print("6. Thoát chương trình")
        print("==========================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == '1':
            print("\n--- MỞ TÀI KHOẢN MỚI ---")
            
            while True:
                acc_number = input("Nhập số tài khoản 10 chữ số: ").strip()
                if BankAccount.validate_account_number(acc_number):
                    break
                print("Số tài khoản không hợp lệ!")
                print("Số tài khoản phải gồm đúng 10 chữ số.")

            acc_name = input("Nhập tên chủ tài khoản: ")
            current_account = BankAccount(acc_number, acc_name)
            
            # Đảm bảo người dùng nhập tên hợp lệ trước khi đi tiếp
            while not current_account.account_name:
                acc_name = input("Vui lòng nhập lại tên chủ tài khoản: ")
                current_account.account_name = acc_name

            print("Mở tài khoản thành công!")
            print(f"Số tài khoản: {acc_number}")
            print(f"Tên chủ tài khoản: {current_account.account_name}")

        elif choice in ['2', '3', '4']:
            # Bẫy 4: Thao tác khi chưa có đối tượng
            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản")
                print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
                continue

            if choice == '2':
                print()
                current_account.display_info()

            elif choice == '3':
                print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")
                print("1. Nạp tiền")
                print("2. Rút tiền")
                trans_choice = input("Chọn loại giao dịch (1-2): ").strip()

                if trans_choice in ['1', '2']:
                    try:
                        amount = int(input("Nhập số tiền giao dịch: "))
                        if trans_choice == '1':
                            current_account.deposit(amount)
                        else:
                            current_account.withdraw(amount)
                    except ValueError:
                        print("Lỗi: Số tiền phải là một số nguyên.")
                else:
                    print("Lựa chọn giao dịch không hợp lệ.")

            elif choice == '4':
                print("\n--- CẬP NHẬT TÊN CHỦ TÀI KHOẢN ---")
                new_name = input("Nhập tên mới: ")
                current_account.account_name = new_name
                
                # Nếu tên mới hợp lệ thì biến account_name sẽ được cập nhật
                if new_name.strip():
                    print(f"Cập nhật thành công. Tên mới: {current_account.account_name}")

        elif choice == '5':
            print("\n--- ĐỔI PHÍ GIAO DỊCH HỆ THỐNG ---")
            print(f"Phí giao dịch hiện tại: {BankAccount.transaction_fee:,} VND")
            try:
                new_fee = int(input("Nhập phí giao dịch mới: "))
                BankAccount.update_transaction_fee(new_fee)
            except ValueError:
                print("Lỗi: Phí giao dịch phải là một số nguyên.")

        elif choice == '6':
            print("Cảm ơn bạn đã sử dụng Vietcombank Digibank!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 6.")

# Kích hoạt chương trình
if __name__ == "__main__":
    main()