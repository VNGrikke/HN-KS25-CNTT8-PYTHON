from models.savings_account import SavingsAccount
from models.premium_mixin import DigitalPremiumMixin


class HybridAccount(SavingsAccount, DigitalPremiumMixin):
    """
    Tài khoản đa năng.

    Kế thừa:
        SavingsAccount
        DigitalPremiumMixin

    Có:
        - Nạp/Rút tiền như SavingsAccount
        - Tính lãi
        - Cashback Premium
    """

    def __init__(self, account_number, owner_name, balance=0, interest_rate=0.05):

        super().__init__(account_number, owner_name, balance, interest_rate)

    # Override Deposit
    def deposit(self, amount):

        if amount <= 0:
            print("Số tiền nạp phải lớn hơn 0.")
            return

        # Gọi deposit của SavingsAccount
        super().deposit(amount)

        # Áp dụng hoàn tiền Premium
        self.cashback_reward(amount)

        print(f"Số dư mới: {self.balance:,.0f} VND")