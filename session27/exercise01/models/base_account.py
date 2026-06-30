from abc import ABC, abstractmethod


class BaseAccount(ABC):
    """
    Lớp trừu tượng đại diện cho tài khoản ngân hàng.
    """

    bank_name = "Vietcombank"

    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.__balance = balance

    # Property: owner_name
    @property
    def owner_name(self):
        return self.__owner_name

    @owner_name.setter
    def owner_name(self, name):
        # Xóa khoảng trắng thừa và in hoa
        self.__owner_name = " ".join(name.strip().split()).upper()

    # Property: balance
    @property
    def balance(self):
        return self.__balance

    # Chỉ cho class con cập nhật
    def _set_balance(self, new_balance):
        self.__balance = new_balance

    # Abstract Methods
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    # Operator Overloading
    def __add__(self, other):

        if not isinstance(other, BaseAccount):
            return NotImplemented

        return self.balance + other.balance

    def __lt__(self, other):

        if not isinstance(other, BaseAccount):
            return NotImplemented

        return self.balance < other.balance

    # Static Method
    @staticmethod
    def validate_account_number(account_number):

        return (
            account_number.isdigit()
            and len(account_number) == 10
        )

    # Class Method
    @classmethod
    def update_bank_name(cls, new_name):

        cls.bank_name = new_name

    # Hiển thị
    def __str__(self):

        return (
            f"Ngân hàng      : {self.bank_name}\n"
            f"Số tài khoản   : {self.account_number}\n"
            f"Chủ tài khoản  : {self.owner_name}\n" 
            f"Số dư          : {self.balance:,.0f} VND"
        )