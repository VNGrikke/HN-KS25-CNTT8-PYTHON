def process_payment(payment_gateway, account, amount):
    """
    Duck Typing.

    Không quan tâm payment_gateway thuộc class nào.
    Chỉ cần có execute_pay().
    """

    try:
        payment_gateway.execute_pay(account, amount)

        print(f"Số dư mới: {account.balance:,.0f} VND")

    except AttributeError:
        print("Cổng thanh toán không hợp lệ hoặc chưa được tích hợp.")