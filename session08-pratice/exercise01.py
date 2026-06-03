account_name = ""
title_video = ""
description = ""
hashtag_list = []

while True:
    print("\n+==============================================+")
    print("|        HE THONG QUAN LI NOI DUNG TIKTOK      |")
    print("+==============================================+")
    print("|  1. Nhap va phan tich thong tin video        |")
    print("|  2. Chuan hoa ten tai khoan                  |")
    print("|  3. Kiem tra tinh hop le cua hashtag         |")
    print("|  4. Tim kiem va thay the tu khoa trong mo ta |")
    print("|  5. Thoat chuong trinh                       |")
    print("+==============================================+")
    
    choice = input("Moi ban chon chuc nang (1-5): ").strip()
    
    match choice:
        case "1":
            while True:
                account_name = input("Nhap ten tai khoan dang video: ").strip()
                if account_name == "":
                    print("Ten tai khoan khong duoc rong")
                else:
                    break
            
            title_video = input("Nhap tieu de video: ").strip().title()
            
            while True:
                description = input("Nhap mo ta video: ").strip()
                if description == "":
                    print("Mo ta video khong duoc rong")
                else:
                    break
            
            raw_hashtags = input("Nhap danh sach hashtag (cach nhau boi dau phay): ").strip()
            if raw_hashtags != "":
                hashtag_list = [h.strip() for h in raw_hashtags.split(",")]
            else:
                hashtag_list = []
            
            print(f"\nTen tai khoan: {account_name}")
            print(f"Tieu de video: {title_video}")
            print(f"Mo ta video: {description}")
            print(f"Do dai mo ta: {len(description)}")
            print(f"So luong tu trong mo ta: {len(description.split())}")
            print(f"Danh sach hashtag sau khi chuan hoa: {', '.join(hashtag_list)}")
            print(f"So luong hashtag: {len(hashtag_list)}")
            print(f"Mo ta video (chu thuong): {description.lower()}")
            print(f"Mo ta video (chu hoa): {description.upper()}")
            
        case "2":
            if account_name != "":
                print(f"\nTen tai khoan ban dau: {account_name}")
                std_account = "@" + account_name.lower()
                print(f"Ten tai khoan chuan hoa: {std_account}")
            else:
                print("\nVui long nhap thong tin tai chuc nang 1 truoc")
                
        case "3":
            ht = input("Nhap 1 hashtag de kiem tra: ").strip()
            if ht == "":
                print("Hashtag khong duoc rong")
            elif not ht.startswith("#"):
                print("Hashtag phai bat dau bang ky tu #")
            elif " " in ht:
                print("Hashtag khong duoc chua khoang trang")
            elif len(ht) < 2:
                print("Hashtag phai co it nhat 2 ky tu")
            else:
                is_valid = True
                for c in ht[1:]:
                    if not (c.isalnum() or c == "_"):
                        is_valid = False
                        break
                
                if is_valid:
                    print("Hashtag hop le")
                    hashtag_list.append(ht)
                else:
                    print("Hashtag chi nen su dung chu cai, chu so hoac dau gach duoi")
                    
        case "4":
            if description == "":
                print("\nVui long nhap thong tin tai chuc nang 1 truoc")
            else:
                search_kw = input("Nhap tu khoa can tim: ").strip()
                replace_kw = input("Nhap tu khoa thay the: ").strip()
                
                count = description.count(search_kw)
                if count > 0:
                    description = description.replace(search_kw, replace_kw)
                    print(f"\nMo ta sau khi thay the: {description}")
                    print(f"So lan tu khoa xuat hien: {count}")
                else:
                    print("\nKhong tim thay tu khoa trong mo ta")
                    
        case "5":
            print("Thoat chuong trinh")
            break
            
        case _:
            print("Lua chon khong hop le, vui long nhap lai so tu 1 den 5!")