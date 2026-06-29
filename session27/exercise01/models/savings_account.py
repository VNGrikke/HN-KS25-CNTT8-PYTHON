from models.base_account import BaseAccount


class SavingsAccount(BaseAccount):
    """
    Tài khoản tiết kiệm.
    """

    def __init__(self,
                 account_number,
                 owner_name,
                 balance=0,
                 interest_rate=0.05):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    # ==========================
    # Nạp tiền
    # ==========================
    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền nạp phải lớn hơn 0.")
            return

        self._set_balance(self.balance + amount)

        print("Nạp tiền thành công!")
        print(f"Số dư hiện tại: {self.balance:,.0f} VND")

    # Rút tiền
    def withdraw(self, amount):

        if amount <= 0:
            print("Số tiền rút phải lớn hơn 0.")
            return

        fee = amount * 0.02
        total = amount + fee

        if total > self.balance:
            print("Không đủ số dư.")
            return

        self._set_balance(self.balance - total)

        print("Rút tiền thành công!")
        print(f"Số tiền rút: {amount:,.0f} VND")
        print(f"Phí rút trước hạn (2%): {fee:,.0f} VND")
        print(f"Số dư còn lại: {self.balance:,.0f} VND")

    # Tính lãi
    def apply_interest(self):

        interest = self.balance * self.interest_rate

        self._set_balance(self.balance + interest)

        print("Áp dụng lãi suất thành công!")
        print(f"Lãi nhận được: {interest:,.0f} VND")
        print(f"Số dư mới: {self.balance:,.0f} VND")