order_list = [
    "GE001 - PENDING",
    "GE002 - ASSIGNED",
    "GE003 - DELIVERING"
]

while True:
    print("""
===== HE THONG DIEU PHOI GRAB EXPRESS =====
1. Hien thi danh sach don hang
2. Gan tai xe cho don hang
3. Cap nhat trang thai giao hang
4. Huy don hang
5. Thoat chuong trinh
""")

    choice = input("Nhap vao lua chon cua ban: ").strip()

    match choice:
        case "1":
            if len(order_list) == 0:
                print("Danh sach don hang hien dang trong.")
            else:
                print("Danh sach don hang hien tai:")
                for i in range(len(order_list)):
                    print(f"{i + 1}. {order_list[i]}")

        case "2":
            order_id = input("Nhap ma don hang can gan tai xe: ").strip().upper()

            found = False

            for i in range(len(order_list)):
                code, status = order_list[i].split(" - ")

                if code == order_id:
                    found = True

                    if status == "PENDING":
                        order_list[i] = code + " - ASSIGNED"
                        print("Gan tai xe thanh cong.")
                    else:
                        print("Chi co the gan tai xe cho don hang dang cho xu ly.")

                    break

            if not found:
                print("Khong tim thay ma don hang.")

        case "3":
            order_id = input("Nhap ma don hang can cap nhat: ").strip().upper()

            found = False

            for i in range(len(order_list)):
                code, status = order_list[i].split(" - ")

                if code == order_id:
                    found = True

                    if status == "ASSIGNED":
                        order_list[i] = code + " - DELIVERING"
                        print("Cap nhat thanh DELIVERING thanh cong.")

                    elif status == "DELIVERING":
                        order_list[i] = code + " - COMPLETED"
                        print("Cap nhat thanh COMPLETED thanh cong.")

                    elif status == "PENDING":
                        print("Don hang chua duoc gan tai xe, khong the chuyen sang trang thai giao hang.")

                    elif status == "COMPLETED":
                        print("Don hang da hoan tat, khong the cap nhat tiep.")

                    elif status == "CANCELLED":
                        print("Don hang da bi huy, khong the cap nhat.")

                    break

            if not found:
                print("Khong tim thay ma don hang.")

        case "4":
            order_id = input("Nhap ma don hang can huy: ").strip().upper()

            found = False

            for i in range(len(order_list)):
                code, status = order_list[i].split(" - ")

                if code == order_id:
                    found = True

                    if status == "PENDING" or status == "ASSIGNED":
                        order_list[i] = code + " - CANCELLED"
                        print("Huy don hang thanh cong.")

                    elif status == "DELIVERING":
                        print("Don hang dang duoc giao, khong the huy.")

                    elif status == "COMPLETED":
                        print("Don hang da hoan tat, khong the huy.")

                    elif status == "CANCELLED":
                        print("Don hang da duoc huy truoc do.")

                    break

            if not found:
                print("Khong tim thay ma don hang.")

        case "5":
            print("Thoat chuong trinh")
            break

        case _:
            print("Lua chon khong hop le, vui long nhap lai!")