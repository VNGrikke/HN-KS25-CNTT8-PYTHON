order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

while True:
    print("""
===== HE THONG QUAN LY DON HANG GRAB EXPRESS =====
1. Hien thi danh sach don hang
2. Cap nhat danh sach don hang
3. Thong ke don hang theo trang thai
4. Thoat chuong trinh
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
            while True:
                print("""
----- CAP NHAT DANH SACH DON HANG -----
1. Them don hang moi
2. Sua don hang theo vi tri
3. Xoa don hang theo vi tri
4. Quay lai menu chinh
""")

                choice2 = input("Nhap vao lua chon cua ban: ").strip()

                match choice2:
                    case "1":
                        id_order = input("Nhap ma don hang: ").strip().upper()
                        status_order = input("Nhap trang thai don hang: ").strip().upper()

                        new_order = id_order + " - " + status_order
                        order_list.append(new_order)

                        print("Them don hang thanh cong!")

                    case "2":
                        position = input("Nhap vi tri can sua: ").strip()

                        if not position.isdigit():
                            print("Vi tri khong hop le!")
                        else:
                            index = int(position) - 1

                            if index < 0 or index >= len(order_list):
                                print("Khong ton tai don hang o vi tri nay!")
                            else:
                                id_order = input("Nhap ma don hang moi: ").strip().upper()
                                status_order = input("Nhap trang thai moi: ").strip().upper()

                                order_list[index] = id_order + " - " + status_order

                                print("Cap nhat thanh cong!")

                    case "3":
                        position = input("Nhap vi tri can xoa: ").strip()

                        if not position.isdigit():
                            print("Vi tri khong hop le!")
                        else:
                            index = int(position) - 1

                            if index < 0 or index >= len(order_list):
                                print("Khong ton tai don hang o vi tri nay!")
                            else:
                                deleted_order = order_list.pop(index)
                                print("Da xoa:", deleted_order)

                    case "4":
                        break

                    case _:
                        print("Lua chon khong hop le, vui long nhap lai!")

        case "3":
            pending = 0
            delivering = 0
            completed = 0
            cancelled = 0

            for order in order_list:
                status = order.split(" - ")[1]

                if status == "PENDING":
                    pending += 1
                elif status == "DELIVERING":
                    delivering += 1
                elif status == "COMPLETED":
                    completed += 1
                elif status == "CANCELLED":
                    cancelled += 1

            print("===== THONG KE DON HANG =====")
            print("PENDING:", pending)
            print("DELIVERING:", delivering)
            print("COMPLETED:", completed)
            print("CANCELLED:", cancelled)
            print("Tong so don hang:", len(order_list))

        case "4":
            print("Thoat chuong trinh")
            break

        case _:
            print("Lua chon khong hop le, vui long nhap lai!")