class Parent:
    def __init__(self):
        self.home = "Parent home"
        self.room = "Phong cua gia dinh"

class Children(Parent):
    def __init__(self):
        super().__init__()
        self.pool = "be boi"

    
child = Children()
print(child.pool)