cart_items = [
         ["P001", "Dien thoai iPhone 15", 1, 25000000],
         ["P002", "Op lung Silicon", 2, 150000]
]


while True:
    print(
"""
=================================================
        shoppe cart management system
=================================================
1. Xem chi tiet gio hang & tinh tong tien
2. Them san pham moi/cong don so luong
3. Cap nhat so luong cua mmot san pham 
4. Xoa san pham ra khoi cua hang
5. Thoat chuong trinh
=================================================
""")
    choice = int(input("Moi ban chon tinh nang: "))

    match choice:
        case 1:
            print("--CHI TIET GIO HANG--")
            print(f"{'STT':<10} | {'MA SP':<10} | {'TEN SAN PHAM':<30} | {'SL':<5} | {'DON GIA':<15} | {'THANH TIEN':<15}") 
            for i in range(len(cart_items)):
                print(f"{i+1:<10} | {cart_items[i][0]:<10} | {cart_items[i][1]:<30} | {cart_items[i][2]:<5} | {cart_items[i][3]:<14,}d | {cart_items[i][3]:<14,}d") 

        case 2:
            flag = False
            id_product = input("Nhap vao ma cua san pham moi: ").strip().upper
            name_product = input("Nhap vao ten cua san pham moi: ").strip()
            amount = int(input("Nhap vao so luong san pham: "))
            price = float(input("Nhap vao gia tien cua san pham: "))
            
            if amount <= 0 or price < 0:
                print("Gia tien/so luong khong dc nho hon 0")
            else:
                new_product = [id_product, name_product, amount, price]
            
                for item in cart_items:
                    if new_product[0] == item[0]:
                        item[2] += new_product[2]
                        flag = True

                if flag == False:
                    cart_items.append(new_product)

        case 3:
            flag = False
            id_product = input("Nhap vao ma cua san pham: ").strip()
            
            for item in cart_items:
                if id_product == item[0]:
                    amount = int(input("Nhap vao so luong san pham: "))

                    if amount <= 0:
                        print("So luong khong dc nho hon 0")
                    else:
                        item[2] = amount
                    flag =True
            
            if flag == False:
                print(f"Khong tim thay san ma: {id_product}")

        case 4: 
            index = -1
            id_product = input("Nhap vao ma cua san pham: ").strip()
            
            for i in range(len(cart_items)):
                if id_product == item[0]:
                    index = i

            if index != -1:
                cart_items.pop(index)
            else:
                print(f"Khong tim thay san ma: {id_product}")

        case 5:
            print("Thoat chuong trinh")
            break

        case _:
            print("Lua chon khong hop le, vui long nhap lai!")