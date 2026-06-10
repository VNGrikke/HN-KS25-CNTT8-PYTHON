product_list = [
    {
        "product_id": "SP001",
        "product_name": "Ao polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quan kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Vay cong so nu",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    print("\n===== HE THONG QUAN LY SAN PHAM YODY =====")
    print("1. Hien thi danh sach san pham")
    print("2. Them san pham moi")
    print("3. Cap nhat thong tin san pham")
    print("4. Xoa san pham theo ma")
    print("5. Thoat chuong trinh")
    
    choice = input("Vui long nhap lua chon cua ban (1-5): ").strip()
    
    match choice:
        # CHUC NANG 1: Hien thi danh sach
        case '1':
            if len(product_list) == 0:
                print("Danh sach san pham hien dang trong.")
            else:
                print("Danh sach san pham hien tai:")
                for index, product in enumerate(product_list, start=1):
                    print(f"{index}. Ma SP: {product['product_id']} | Ten: {product['product_name']} | Gia: {product['price']} | So luong: {product['quantity']}")

        # CHUC NANG 2: Them san pham moi
        case '2':
            new_id = input("Nhap ma san pham: ").strip().upper()
            
            is_exist = any(p["product_id"] == new_id for p in product_list)
            if is_exist:
                print("Ma san pham bi trung!")
                continue
                
            new_name = input("Nhap ten san pham: ").strip()
            
            price_input = input("Nhap gia san pham: ").strip()
            quantity_input = input("Nhap so luong san pham: ").strip()
            
            if not price_input.isdigit() or int(price_input) <= 0:
                print("Gia/So luong khong hop le!")
                continue
                
            if not quantity_input.isdigit() or int(quantity_input) <= 0:
                print("Gia/So luong khong hop le!")
                continue
                
            new_price = int(price_input)
            new_quantity = int(quantity_input)
                
            new_product = {
                "product_id": new_id,
                "product_name": new_name,
                "price": new_price,
                "quantity": new_quantity
            }
            product_list.append(new_product)
            print("Them san pham thanh cong")

        # CHUC NANG 3: Cap nhat thong tin san pham
        case '3':
            update_id = input("Nhap ma san pham can cap nhat: ").strip().upper()
            
            product_found = None
            for product in product_list:
                if product["product_id"] == update_id:
                    product_found = product
                    break
                    
            if not product_found:
                print("Khong tim thay ma san pham can cap nhat!")
            else:
                new_name = input(f"Nhap ten san pham moi (Hien tai: {product_found['product_name']}): ").strip()
                
                price_input = input(f"Nhap gia san pham moi (Hien tai: {product_found['price']}): ").strip()
                quantity_input = input(f"Nhap so luong san pham moi (Hien tai: {product_found['quantity']}): ").strip()
                
                if not price_input.isdigit() or int(price_input) <= 0:
                    print("Gia/So luong khong hop le!")
                    continue
                    
                if not quantity_input.isdigit() or int(quantity_input) <= 0:
                    print("Gia/So luong khong hop le!")
                    continue
                    
                new_price = int(price_input)
                new_quantity = int(quantity_input)
                    
                product_found["product_name"] = new_name
                product_found["price"] = new_price
                product_found["quantity"] = new_quantity
                print("Cap nhat thong tin san pham thanh cong!")

        # CHUC NANG 4: Xoa san pham
        case '4':
            delete_id = input("Nhap ma san pham can xoa: ").strip().upper()
            
            index_to_delete = -1
            for i in range(len(product_list)):
                if product_list[i]["product_id"] == delete_id:
                    index_to_delete = i
                    break
                    
            if index_to_delete == -1:
                print("Khong tim thay ma san pham can xoa!")
            else:
                deleted_product = product_list.pop(index_to_delete)
                print(f"Da xoa thanh cong san pham: {deleted_product['product_name']}")

        # CHUC NANG 5: Thoat chuong trinh
        case '5':
            print("Thoat chuong trinh.")
            break
            
        case _:
            print("Lua chon khong hop le, vui long nhap lai!")