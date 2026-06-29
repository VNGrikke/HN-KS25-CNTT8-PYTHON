class ViettelMoneyGateway:
    """
    Cổng thanh toán Viettel Money.
    """

    def execute_pay(self, account, amount):
        print(
            f"[Hệ thống Viettel Money]: Đang kết nối tới tài khoản "
            f"{account.account_number}..."
        )

        account.withdraw(amount)

        print("Thanh toán thành công qua Viettel Money!")
        print(f"Tài khoản đã thanh toán hóa đơn: {amount:,.0f} VND")