while True:
    print(
        "+==============================================+\n"
        "|         HE THONG QUAN LI NOI DUNG TIKTOK     |\n"
        "+==============================================+\n"
        "|  1. Nhap va phan tich thong tin video        |\n"
        "|  2. Chuan hoa ten tai khoan                  |\n"
        "|  3. Kiem tra tinh hop le cua hashtag         |\n"
        "|  4. Tim kiem va thay the tu khoa trong mo ta |\n"
        "|  5. Thoat chuong trinh                       |\n"
        "+==============================================+\n"
        )
    
    choice = input("Moi ban chon chuc nang (1-5):").strip()

    match choice:
        case "1":
            while True:
                account_name = input("Nhap vao ten tai khoan dang video: ").strip()
                if account_name == " " or account_name == "":
                    print("Ten tai khoan khong duoc trong. VUI LONG NHAP LAI!!!!!")
                else:
                    title_video = input("Nhap vao tieu de video: ").strip().title()
                    description = input("Nhap vao mo ta cua video: ").strip()
                    hashtag = input("Nhap vao danh sach hashtag (cach nhau boi dau phay): ").strip()

                    print(f"\n{account_name}")
                    print(title_video)
                    print(description)
                    print(f"Do dai mo ta {len(description)}")
                    print(f"Danh sach hashtag sau khi chuan hoa khoang trang: {hashtag}")
                    print(f"So luong hashtag: {len(hashtag)}")
                    print(f"Mo ta video (chu thuong): {description.lower()}")
                    print(f"Mo ta video (chu hoa): {description.upper()}")
                    break

        case "2":
            account_name = "@" + account_name.lower()
            print(f"{account_name}")
        case "3":
            check_hashtag = input("Nhap vao 1 hashtag de kiem tra: ").strip()
            

            
            print("cn2")

        case "4":
            print("cn2")
        case "5":
            break
        case _:
            print("Sai cu phap")

