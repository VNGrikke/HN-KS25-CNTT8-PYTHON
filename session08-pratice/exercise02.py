shop_name = ""
product_name = ""
description = ""
category = ""
keyword_list = []

while True:
    print("\n+=====================================================================+")
    print("| HE THONG QUAN LY VA CHUAN HOA THONG TIN SAN PHAM THUONG MAI DIEN TU |")
    print("+=====================================================================+")
    print("| 1. Nhap du lieu san pham va xem bao cao thong ke                    |")
    print("| 2. Chuan hoa ten Shop                                               |")
    print("| 3. Kiem tra ma giam gia hop le                                      |")
    print("| 4. Tim kiem va thay the tu khoa trong mo ta san pham                |")
    print("| 5. Thoat chuong trinh                                               |")
    print("+=====================================================================+")
    
    choice = input("Moi ban chon chuc nang (1-5): ").strip()
    
    match choice:
        case "1":
            while True:
                shop_name = input("Nhap ten shop: ").strip()
                if shop_name == "":
                    print("Ten shop khong duoc bo trong")
                else:
                    break
            
            product_name = input("Nhap ten san pham: ").strip().title()
            
            while True:
                description = input("Nhap mo ta san pham: ").strip()
                if description == "":
                    print("Mo ta san pham khong duoc rong")
                else:
                    break
            
            category = input("Nhap danh muc san pham: ").strip().lower()
            
            raw_keywords = input("Nhap danh sach tu khoa (cach nhau boi dau phay): ").strip()
            if raw_keywords != "":
                keyword_list = [k.strip() for k in raw_keywords.split(",")]
            else:
                keyword_list = []
                
            print(f"\n--- BAO CAO THONG KE ---")
            print(f"Ten shop: {shop_name}")
            print(f"Ten san pham: {product_name}")
            print(f"Mo ta san pham: {description}")
            print(f"Do dai mo ta san pham: {len(description)}")
            print(f"Danh muc san pham: {category}")
            print(f"Danh sach tu khoa: {', '.join(keyword_list)}")
            print(f"So luong tu khoa: {len(keyword_list)}")
            print(f"Mo ta (chu thuong): {description.lower()}")
            print(f"Mo ta (chu hoa): {description.upper()}")
            
        case "2":
            if shop_name != "":
                print(f"\nTen shop ban dau: {shop_name}")
                
                words = shop_name.lower().split()
                norm_shop = "-".join(words)
                
                if not norm_shop.startswith("shop-"):
                    norm_shop = "shop-" + norm_shop
                    
                print(f"Ten shop sau khi chuan hoa: {norm_shop}")
            else:
                print("\nVui long nhap thong tin san pham tai chuc nang 1 truoc!")
                
        case "3":
            discount_code = input("Nhap ma giam gia can kiem tra: ")
            
            if discount_code == "":
                print("Ma giam gia khong duoc rong")
            elif " " in discount_code:
                print("Ma giam gia khong duoc chua khoang trang")
            elif not (6 <= len(discount_code) <= 12):
                print("Ma giam gia phai co do dai tu 6 den 12 ky tu")
            elif not discount_code.isupper():
                print("Ma giam gia phai duoc viet hoa toan bo")
            elif not discount_code.isalnum():
                print("Ma giam gia chi duoc chua chu cai va chu so")
            elif not discount_code.startswith("SALE"):
                print("Ma giam gia phai bat dau bang chuoi SALE")
            else:
                print("Ma giam gia hop le")
                
        case "4":
            if description == "":
                print("\nVui long nhap thong tin san pham tai chuc nang 1 truoc!")
            else:
                search_kw = input("Tu khoa can tim: ").strip()
                replace_kw = input("Tu khoa thay the: ").strip()
                
                count = description.count(search_kw)
                if count > 0:
                    description = description.replace(search_kw, replace_kw)
                    print(f"\nSo lan xuat hien cua tu khoa: {count}")
                    print("Mo ta sau khi thay the:")
                    print(description)
                else:
                    print("\nKhong tim thay tu khoa trong mo ta san pham")
                    
        case "5":
            print("Thoat chuong trinh")
            break
            
        case _:
            print("Lua chon khong hop le, vui long nhap lai!")