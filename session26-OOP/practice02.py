# Một số loại kế thừa
"""
A->B: ke thừa đơn(Single)
A   B
|   |
----- : Đa kế thừa (Multiple)
  |
  C


A -> B -> C : Kế thừa đa cấp(Multilevel)

A->B, A->C : Kế thừa phân cấp(Hierachical)

"""


class Parent:
    def __init__(self):
        self.lastname = "Nguyen"
        self.home = "Nha cua bo"


class Children01(Parent):
    def __init__(self):
        super().__init__()
        self.sex = "Nam"
        
class Children02(Parent):
    def __init__(self):
        super().__init__()
        self.sex = "Nu"
    
