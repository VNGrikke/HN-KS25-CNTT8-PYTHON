product_list = [
    {
        "product_id": "SP001",
        "product_name": "Ao polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5,
        "returned": 1,
        "discount": 0
    },
    {
        "product_id": "SP002",
        "product_name": "Quan kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3,
        "returned": 0,
        "discount": 10
    },
    {
        "product_id": "SP003",
        "product_name": "Vay cong so nu",
        "price": 459000,
        "quantity": 3,
        "sold": 7,
        "returned": 1,
        "discount": 15
    }
]

while True:
    print("\n===== HE THONG QUAN LY GIAO DICH CUA HANG YODY =====")
    print("1. Hien thi danh sach san pham")
    print("2. Ban san pham cho khach hang")
    print("3. Xu ly doi tra san pham")
    print("4. Ap dung giam gia cho san pham")
    print("5. Nhap them hang vao kho cua hang")
    print("6. Thoat chuong trinh")
    
    user_choice = input("Vui long nhap lua chon cua ban (1-6): ").strip()
    
    match user_choice:
        # CHUC NANG 1: Hien thi danh sach san pham
        case '1':
            if len(product_list) == 0:
                print("Danh sach san pham hien dang trong.")
            else:
                print("Danh sach san pham hien tai:")
                for index, product in enumerate(product_list, start=1):
                    current_qty = product['quantity']
                    if current_qty == 0:
                        stock_status = "Het hang"
                    elif current_qty <= 5:
                        stock_status = "Sap het hang"
                    else:
                        stock_status = "Con hang"
                        
                    print(f"{index}. Ma SP: {product['product_id']} | Ten: {product['product_name']} | "
                          f"Gia: {product['price']} | Ton kho: {current_qty} | Da ban: {product['sold']} | "
                          f"Doi tra: {product['returned']} | Giam gia: {product['discount']}% | Trang thai: {stock_status}")

        # CHUC NANG 2: Ban san pham cho khach
        case '2':
            sell_id = input("Nhap ma san pham khach muon mua: ").strip().upper()
            
            target_product = None
            for p in product_list:
                if p['product_id'] == sell_id:
                    target_product = p
                    break
                    
            if not target_product:
                print("Khong tim thay san pham can ban!")
                continue
                
            qty_input = input("Nhap so luong khach mua: ").strip()
            
            if not qty_input.isdigit() or int(qty_input) <= 0:
                print("So luong mua khong hop le!")
                continue
                
            sell_qty = int(qty_input)
            
            if sell_qty > target_product['quantity']:
                print("So luong trong kho khong du de ban!")
                continue
                
            target_product['quantity'] -= sell_qty
            target_product['sold'] += sell_qty
            
            discounted_price = int(target_product['price'] * (100 - target_product['discount']) / 100)
            total_payment = discounted_price * sell_qty
            
            print(f"Ban hang thanh cong! Tong tien khach can thanh toan: {total_payment} VND")

        # CHUC NANG 3: Xu ly doi tra san pham
        case '3':
            return_id = input("Nhap ma san pham khach muon doi/tra: ").strip().upper()
            
            target_product = None
            for p in product_list:
                if p['product_id'] == return_id:
                    target_product = p
                    break
                    
            if not target_product:
                print("Khong tim thay san pham can doi tra!")
                continue
                
            qty_input = input("Nhap so luong doi/tra: ").strip()
            
            if not qty_input.isdigit() or int(qty_input) <= 0:
                print("So luong doi/tra khong hop le!")
                continue
                
            return_qty = int(qty_input)
            
            if return_qty > target_product['sold']:
                print("So luong doi/tra khong duoc vuot qua so luong da ban!")
                continue
                
            target_product['sold'] -= return_qty
            target_product['quantity'] += return_qty
            target_product['returned'] += return_qty
            
            discounted_price = int(target_product['price'] * (100 - target_product['discount']) / 100)
            refund_amount = discounted_price * return_qty
            
            print(f"Xu ly doi tra thanh cong! So tien can hoan lai cho khach: {refund_amount} VND")

        # CHUC NANG 4: Ap dung giam gia
        case '4':
            discount_id = input("Nhap ma san pham can ap dung giam gia: ").strip().upper()
            
            target_product = None
            for p in product_list:
                if p['product_id'] == discount_id:
                    target_product = p
                    break
                    
            if not target_product:
                print("Khong tim thay ma san pham can ap dung!")
                continue
                
            discount_input = input("Nhap phan tram giam gia: ").strip()
            
            if not discount_input.isdigit() or int(discount_input) < 0 or int(discount_input) > 70:
                print("Phan tram giam gia khong hop le!")
                continue
                
            target_product['discount'] = int(discount_input)
            print(f"Da cap nhat muc giam gia {target_product['discount']}% cho san pham {target_product['product_name']}.")

        # CHUC NANG 5: Nhap them hang vao kho
        case '5':
            restock_id = input("Nhap ma san pham can nhap them: ").strip().upper()
            
            target_product = None
            for p in product_list:
                if p['product_id'] == restock_id:
                    target_product = p
                    break
                    
            if not target_product:
                print("Khong tim thay san pham can nhap them!")
                continue
                
            qty_input = input("Nhap so luong nhap them: ").strip()
            
            if not qty_input.isdigit() or int(qty_input) <= 0:
                print("So luong nhap them khong hop le!")
                continue
                
            restock_qty = int(qty_input)
            target_product['quantity'] += restock_qty
            
            print(f"Da nhap kho thanh cong! Ton kho hien tai cua {target_product['product_name']} la {target_product['quantity']}.")

        # CHUC NANG 6: Thoat chuong trinh
        case '6':
            print("Thoat chuong trinh. Hen gap lai!")
            break
            
        case _:
            print("Lua chon khong hop le, vui long nhap lai!")