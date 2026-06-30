from product_manager import ProductManager

def display_menu():
    print("""
======================Menu======================
1. HIen thi danh sach san pham
2. Them san pham moi
3. Cap nhat san pham
4. Xoa san pham
5.Tim kiem san pham
6.Thoat
================================================
""")


def main():
    manager = ProductManager()

    while True:
        display_menu()

        choice = input("NHap lua chon chua ban: ").strip()

        match choice:

            case "1":
                manager.show_all()
            case "2":
                manager.add_product()
            case "3":
                manager.update_product()
            case "4":
                manager.delete_product()
            case "5":
                manager.search_product()
            case "6":
                break

            case _:
                print("Cu phap khong hop le! Nhap lai")

if __name__ == "__main__":
    main()