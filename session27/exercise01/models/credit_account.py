from models.base_account import BaseAccount


class CreditAccount(BaseAccount):
    """
    Tài khoản tín dụng.
    Cho phép số dư âm nhưng không vượt quá hạn mức tín dụng.
    """

    def __init__(self, account_number, owner_name, balance=0, credit_limit=20000000):
        super().__init__(account_number, owner_name, balance)
        self.credit_limit = credit_limit

    # Nạp tiền (trả nợ)
    def deposit(self, amount):

        if amount <= 0:
            print("Số tiền nạp phải lớn hơn 0.")
            return

        self._set_balance(self.balance + amount)

        print("Nạp tiền thành công!")

        if self.balance >= 0:
            print("Bạn đã thanh toán hết khoản nợ.")
        else:
            print("Khoản nợ còn lại: {:,.0f} VND".format(abs(self.balance)))

        print("Số dư hiện tại: {:,.0f} VND".format(self.balance))

    # Rút tiền
    def withdraw(self, amount):

        if amount <= 0:
            print("Số tiền rút phải lớn hơn 0.")
            return

        new_balance = self.balance - amount

        if new_balance < -self.credit_limit:
            print("Vượt quá hạn mức thấu chi cho phép.")
            return

        self._set_balance(new_balance)

        print("Rút tiền thành công! (Sử dụng hạn mức thấu chi)")
        print(f"Số tiền rút: {amount:,.0f} VND")
        print(f"Số dư hiện tại: {self.balance:,.0f} VND")