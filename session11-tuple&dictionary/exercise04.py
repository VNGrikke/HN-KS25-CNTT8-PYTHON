# Khoi tao danh sach san pham ban dau
product_list = [
    {
        "product_id": "SP001",
        "product_name": "Ao polo nam",
        "price": 299000,
        "quantity": 20,
        "sold": 5
    },
    {
        "product_id": "SP002",
        "product_name": "Quan kaki nam",
        "price": 399000,
        "quantity": 8,
        "sold": 3
    },
    {
        "product_id": "SP003",
        "product_name": "Vay cong so nu",
        "price": 459000,
        "quantity": 3,
        "sold": 7
    }
]

# Main program loop
while True:
    # Hien thi menu
    print("\n===== HE THONG VAN HANH CUA HANG YODY =====")
    print("1. Hien thi danh sach san pham va canh bao ton kho")
    print("2. Ban san pham cho khach hang")
    print("3. Nhap them hang vao kho")
    print("4. Xem bao cao doanh thu")
    print("5. Thoat chuong trinh")
    
    choice = input("Vui long nhap lua chon cua ban (1-5): ").strip()
    
    match choice:
        # CHUC NANG 1: Hien thi danh sach san pham va canh bao ton kho
        case '1':
            if len(product_list) == 0:
                print("Danh sach san pham hien dang trong.")
            else:
                print("Danh sach san pham hien tai:")
                for index, product in enumerate(product_list, start=1):
                    # Xu ly logic trang thai ton kho
                    current_quantity = product['quantity']
                    if current_quantity == 0:
                        status = "Het hang"
                    elif current_quantity <= 5:
                        status = "Sap het hang"
                    else:
                        status = "Con hang"
                        
                    print(f"{index}. Ma SP: {product['product_id']} | Ten: {product['product_name']} | Gia: {product['price']} | Ton kho: {current_quantity} | Da ban: {product['sold']} | Trang thai: {status}")

        # CHUC NANG 2: Ban san pham
        case '2':
            sell_id = input("Nhap ma san pham khach muon mua: ").strip().upper()
            
            found_product = None
            for product in product_list:
                if product['product_id'] == sell_id:
                    found_product = product
                    break
            
            if not found_product:
                print("Khong tim thay san pham can ban!")
                continue
                
            qty_input = input("Nhap so luong khach mua: ").strip()
            
            if not qty_input.isdigit() or int(qty_input) <= 0:
                print("So luong mua khong hop le!")
                continue
                
            sell_quantity = int(qty_input)
            
            if sell_quantity > found_product['quantity']:
                print("So luong trong kho khong du de ban!")
                continue
                
            # Cap nhat so luong va tinh tien
            found_product['quantity'] -= sell_quantity
            found_product['sold'] += sell_quantity
            total_payment = sell_quantity * found_product['price']
            
            print(f"Ban thanh cong! Tong tien khach can thanh toan: {total_payment}")

        # CHUC NANG 3: Nhap them hang vao kho
        case '3':
            restock_id = input("Nhap ma san pham can nhap them: ").strip().upper()
            
            found_product = None
            for product in product_list:
                if product['product_id'] == restock_id:
                    found_product = product
                    break
            
            if not found_product:
                print("Khong tim thay san pham can Nhap kho!")
                continue
                
            qty_input = input("Nhap so luong nhap them: ").strip()
            
            if not qty_input.isdigit() or int(qty_input) <= 0:
                print("So luong Nhap kho khong hop le!")
                continue
                
            restock_quantity = int(qty_input)
            
            found_product['quantity'] += restock_quantity
            print("Nhap kho thanh cong!")

        # CHUC NANG 4: Xem bao cao doanh thu
        case '4':
            total_sold_all = sum(p['sold'] for p in product_list)
            
            if total_sold_all == 0:
                print("Chua co doanh thu phat sinh.")
            else:
                print("\n===== BAO CAO DOANH THU CUA HANG YODY =====")
                total_revenue = 0
                max_sold = -1
                best_seller = ""
                
                for index, product in enumerate(product_list, start=1):
                    revenue = product['price'] * product['sold']
                    total_revenue += revenue
                    print(f"{index}. {product['product_name']} | Da ban: {product['sold']} | Doanh thu: {revenue}")
                    
                    if product['sold'] > max_sold:
                        max_sold = product['sold']
                        best_seller = product['product_name']
                
                print(f"\nTong doanh thu: {total_revenue}")
                print(f"San pham ban chay nhat: {best_seller}")

        # CHUC NANG 5: Thoat chuong trinh
        case '5':
            print("Thoat chuong trinh.")
            break
            
        case _:
            print("Lua chon khong hop le, vui long nhap lai!")