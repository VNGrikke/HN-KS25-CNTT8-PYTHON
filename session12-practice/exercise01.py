cart_items = [
         {
         	"id": "P001", 
         	"name": "Dien thoai iPhone 15",
         	"number": 1,
         	"price": 25000000
         },
         {
         	"id": "P002",
         	"name": "Op lung Silicon", 
         	"number": 2, 
         	"price": 150000
         }
]


while True:
    print("""
============================================
        SHOPPE CART MANAGERMENT SYSTEM
============================================
1. Xem chi tiet gio hang & tinh tong tien
2. Them/Cong don so luong san pham
3. Cap nhat so luong cua 1 san pham
4. Xoa san pham khoi gio hang
5. Thoat chuong trinh
============================================
""")
    your_choice = int(input("Moi ban chon chuc nang(1-5): "))

    match your_choice:
        case 1:
            print("--CHI TIET GIO HANG--")
            print(f"{'STT':<10} | {'MA SP':<10} | {'TEN SAN PHAM':<30} | {'SL':<5} | {'DON GIA':<15} | {'THANH TIEN':<15}") 

            total_item = 0
            total_price = 0
            
            for i in range(len(cart_items)):
                print(f"{i+1:<10} | {cart_items[i]["id"]:<10} | {cart_items[i]["name"]:<30} | {cart_items[i]["number"]:<5} | {cart_items[i]["price"]:<14,}d | {cart_items[i]["price"]*cart_items[i]["number"]:<14,}d") 
                total_item += cart_items[i]["number"]
                total_price += cart_items[i]["number"]*cart_items[i]["price"]
            
            print(f"=> Tong so luong san pham: {total_item}")
            print(f"=> Tong tien thanh toan: {total_price:,}d")
        
        case 2:
            flag = False

            id_product = input("Nhap ma san pham: ").strip().upper()
            name_product = input("Nhap ten san pham: ").strip()
            number = int(input("Nhap so luong: "))
            price = float(input("Nhap gia tien: "))

            if number <= 0 or price <= 0:
                print("So luong va gia tien phai lon hon 0")
            else:
                for item in cart_items:
                    if item["id"] == id_product:
                        item["number"] += number
                        flag = True
                        print("Da cong don so luong san pham.")
                        break

                if not flag:
                    new_product = {
                        "id": id_product,
                        "name": name_product,
                        "number": number,
                        "price": price
                    }

                    cart_items.append(new_product)
                    print("Them san pham thanh cong.")
        case 3:
            id_product = input("Nhap ma san pham can cap nhat: ").strip().upper()

            found = False

            for item in cart_items:
                if item["id"] == id_product:
                    new_number = int(input("Nhap so luong moi: "))

                    if new_number <= 0:
                        print("So luong phai lon hon 0")
                    else:
                        item["number"] = new_number
                        print("Cap nhat thanh cong")

                    found = True
                    break

            if not found:
                print("Khong tim thay san pham")

        case 4:
            found = False
            id_product = input("Nhap ma san pham can xoa: ").strip().upper()

            for item in cart_items:
                if item["id"] == id_product:
                    cart_items.remove(item)
                    found = True
                    print("Da xoa san pham")
                    break

            if not found:
                print("Khong tim thay san pham")

        case 5:
            print("Thoat chong trinh!!!")
            break

        case _:
            print("Vui long nhap tu 1-5!!!")