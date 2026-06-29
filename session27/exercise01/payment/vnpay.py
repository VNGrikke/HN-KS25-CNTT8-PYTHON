class VNPayGateway:
    """
    Cổng thanh toán VNPay.
    """

    def execute_pay(self, account, amount):
        print(
            f"[Hệ thống VNPay]: Đang kết nối tới tài khoản "
            f"{account.account_number}..."
        )

        account.withdraw(amount)

        print("Xác thực thanh toán bằng Duck Typing thành công!")
        print(f"Tài khoản đã thanh toán hóa đơn: {amount:,.0f} VND")