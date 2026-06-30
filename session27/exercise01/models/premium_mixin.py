class DigitalPremiumMixin:
    """
    Mixin bổ sung tính năng hoàn tiền cho giao dịch lớn.
    Không kế thừa BaseAccount.
    """

    def cashback_reward(self, amount):
        """
        Hoàn tiền 1% nếu giao dịch > 5.000.000 VND
        """
        if amount > 5_000_000:
            cashback = amount * 0.01

            # cộng tiền hoàn vào tài khoản
            self._set_balance(self.balance + cashback)

            print(
                f"[Ưu đãi Premium]: Bạn được hoàn tiền "
                f"1% ({cashback:,.0f} VND) vào tài khoản!"      
            )

            return cashback

        return 0