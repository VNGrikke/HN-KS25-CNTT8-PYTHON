raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 "
    
while True:
    print("\n===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====")
    print("1. Hiển thị chuỗi mã vạch gốc")
    print("2. Giải mã, làm sạch và in báo cáo kiểm kê")
    print("3. Tra cứu nhanh theo đuôi Serial")
    print("4. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    
    if choice == '1':
        print("\n*** Chuỗi mã vạch gốc:")
        print(raw_batch)
        
    elif choice == '2':
        products = raw_batch.split(';')
        total_products = len(products)
        valid_count = 0
        
        print("\n*** BÁO CÁO KIỂM KÊ:")
        print(f"{'MÃ SP':<10} | {'XUẤT XỨ':<10} | {'NĂM SX':<8} | {'SERIAL':<10} | {'TRẠNG THÁI'}")
        print("-" * 65)
        
        for prod in products:
            prod_clean = prod.strip().upper()
            
            if not prod_clean:
                continue
            
            parts = prod_clean.split('-')
            if len(parts) == 4:
                prod_type, country, year, serial = parts
                full_year = f"20{year}"
                
                if serial.isdigit():
                    status = "Pass"
                    valid_count += 1
                else:
                    status = "Lỗi Serial - Reject"
                    
                print(f"{prod_type:<10} | {country:<10} | {full_year:<8} | {serial:<10} | {status}")
        
        # In tổng kết
        print("-" * 65)
        print(f"Đã giải mã thành công {valid_count} sản phẩm hợp lệ / Tổng số {total_products} sản phẩm.")
        
    elif choice == '3':
        search_term = input("Nhập 2 số cuối của Serial cần tìm: ").strip()
        found = False
        
        products = raw_batch.split(';')
        print("\n*** Kết quả tra cứu:")
        for prod in products:
            prod_clean = prod.strip().upper()
            if not prod_clean:
                continue
                
            parts = prod_clean.split('-')
            if len(parts) == 4:
                serial = parts[3]
                if serial[-2:] == search_term:
                    print(f"- Tìm thấy: {prod_clean} (Năm sản xuất: 20{parts[2]})")
                    found = True
        
        if not found:
            print("Không tìm thấy sản phẩm phù hợp")
            
    elif choice == '4':
        print("\nĐóng ca kiểm kho. Chào tạo biệt!")
        break
        
    else:
        print("\nChức năng không tồn tại, vui lòng nhập số từ 1-4!")