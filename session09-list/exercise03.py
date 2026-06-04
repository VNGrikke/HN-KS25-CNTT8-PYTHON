order_list = ["GE001", "GE002", "GE003"]


while True:
    print(""" 
    ===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
    1. Hiển thị danh sách đơn hàng
    2. Thêm đơn hàng mới
    3. Xóa đơn hàng theo mã
    4. Thoát chương trình
    """)

    choice = input("Nhap vao lua chon cua ban: ")

    match choice:
        case "1":
            if order_list == []:
                print("Danh sach rong")
            else:     
                for i in range(len(order_list)):
                    print(f"{i+1}. {order_list[i]}")
        case "2":
            new_order = input("Nhap vao ma don hang moi: ").strip().upper()
            order_list.append(new_order)
        case "3":
            del_order = input("Nhap vao ma don hang: ").strip().upper()
            if del_order in order_list:
                order_list.remove(del_order)
                print("Xoa thanh cong")
            else:
                print("Khong tim thay don hang can xoa")
            
        case "4":
            print("Thoat chuong trinh")
            break
        case _:
            print("Sai cu phap. Nhap lai!!!")