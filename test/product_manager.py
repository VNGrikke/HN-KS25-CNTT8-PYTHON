from product import Product
from utils import get_valid_float,get_valid_int,get_valid_string

class ProductManager:
    def __init__(self):
        self.products = []

    def find_product_by_id(self, id):
        for p in self.products:
            if p.id == id:
                return p
        return None
        
        

    def show_all(self):
        if not self.products:
            print("\nDanh sach san pham dang trong")
            return
        
        print("\n" + "="*115)
        print(f'{"Ma SP":<10} | {"Ten san pham":<25} | {"Gia ban":<15} | {"SL ban":<8} | {"Giam gia":<15} | {"Tong doanh thu":<15} | {"Loai DT":<10}')
        for p in self.products:
            print(f"{p.id:<10} | {p.name:<25} | {p.price:<15} | {p.quantity_sold:<8} | {p.discount:<15} | {p.total_revenue:<15} | {p.revenue_type:<10}")
        print("+"*115)

    def add_product(self):
        print("Them san pham moi")

        while True:
            id_product = get_valid_string("Nhap vao ma san pham moi: ").strip().upper()
            if self.find_product_by_id(id_product):
                print("San pham da ton tai. Vui long nhap ma khac")
            else:
                break

        name = get_valid_string("Nhap ten san pham: ")
        price = get_valid_float("Nhap gia ban cua san pham: ")
        quantity_sold = get_valid_int("Nhap vao so luong da ban cua san pham: ")
        discount = get_valid_float("Nhap giam gia: ")

        new_product = Product(id_product, name, price, quantity_sold, discount)
        self.products.append(new_product)

        print("Them san pham thanh cong!")

    def update_product(self):
        print("Cap nhat san Pham")
        id_product = get_valid_string("Nhap vao ma san pham ").strip().upper()
        product = self.find_product_by_id(id_product)

        if not product:
            print("Khong tim thay san pham can cap nhat")
            return

        print("Dang cap nhat san pham: " + product.name)

        product.price = get_valid_float("Nhap gia moi cua san pham: ")
        product.quantity_sold = get_valid_int("Nhap so luong da ban moi cua san pham: ")
        product.discount = get_valid_float("Nhap giam gia moi: ")
        product.calculate_revenue()

        print("Cap nhat thanh cong")

    def delete_product(self):
        print("Xoa san pham")
        id_product = get_valid_string("Nhap vao ma san pham ").strip().upper()
        product = self.find_product_by_id(id_product)

        if not product:
            print("Khong tim thay san pham can cap nhat")
            return
        
        confirm = input(f"Ban co chac muon xoa san pham {product.name}? (y/n):").strip().lower()

        if confirm == "y":
            self.products.remove(product)
            print("Xoa thanh cong!")
        elif confirm == "n":
            print("Da huy thao tac xoa")
        else:
            print("Cu phap khong hop le. Da huy thao tac xoa")

    def search_product(self):
        print("Tim kiem san pham")
        keyword = get_valid_string("Nhap vao tu khoa tim kiem: ").strip().lower()

        found_product = [ p for p in self.products if keyword in p.name.lower()]

        if not found_product:
            print("Khong tim thay san pham")
            return
        
        print("\n" + "="*115)
        print(f'{"Ma SP":<10} | {"Ten san pham":<25} | {"Gia ban":<15} | {"SL ban":<8} | {"Giam gia":<15} | {"Tong doanh thu":<15} | {"Loai DT":<10}')
        print("-"*115)
        for p in found_product:
            print(f"{p.id:<10} | {p.name:<25} | {p.price:<15} | {p.quantity_sold:<8} | {p.discount:<15} | {p.total_revenue:<15} | {p.revenue_type:<10}")
        print("+"*115)