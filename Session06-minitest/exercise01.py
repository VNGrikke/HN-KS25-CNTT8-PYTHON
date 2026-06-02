laptop = 0
phone = 0
tablet = 0
while True:
    print("----- HỆ THỐNG QUẢN LÝ KHO -----")
    print("1.Xem báo cáo tồn kho")
    print("2.Nhập kho")
    print("3.Xuất kho")
    print("4.Cảnh báo hàng tồn kho thấp")
    print("5.Thoát chương trình")
    choice = int(input("Nhập lựa chọn của bạn: "))
    if(choice == 1):
        print("----- BÁO CÁO TỒN KHO -----")
        print(f"Laptop: {laptop}")
        print(f"Điện thoại: {phone}")
        print(f"Máy tính bảng : {tablet}")
        print("Laptop: " , end="")
        for i in range(laptop):
            print("*", end="")
        print()
        print("Điện thoại:", end="")
        for i in range(phone):
            print("*", end="")
        print()
        print("Máy tính bảng: ", end="")
        for i in range(tablet):
            print("*", end="")
        print()
    elif(choice == 2):
        print("----- NHẬP KHO -----")
        print("1.Laptop")
        print("2.Điện thoại")
        print("3.Máy tính bảng")
        number = int(input("Mời bạn chọn mặt hàng cần nhập kho: "))
        while True:
            quantity = int(input("Nhập số lượng hàng cần nhập kho: "))
            if(quantity < 0):
                print("Số lượng hàng nhập kho không hợp lệ, vui lòng nhập lại:")
            else:
                break
        if(number == 1):
            laptop += quantity
            print("Nhập kho thành công!")
        elif(number == 2):
            phone += quantity
            print("Nhập kho thành công!")
        elif(number == 3):
            tablet += quantity
            print("Nhập kho thành công!")
        else:
            print("mặt hàng không hợp lệ!")
    elif(choice == 3):
        print("----- XUẤT KHO -----")
        print("1.Laptop")
        print("2.Điện thoại")
        print("3.Máy tính bảng")
        number = int(input("Mời bạn chọn mặt hàng cần xuất kho: "))
        while True:
            quantity = int(input("Nhập số lượng hàng cần xuất kho: "))
            if(quantity < 0):
                print("Số lượng hàng xuất kho không hợp lệ, vui lòng nhập lại:")
            else:
                break
        if(number == 1):
            if(quantity > laptop):
                print("Không đủ hàng.Hủy giao dịch!")
            else:
                laptop -= quantity
                print("Xuất kho thành công!")
        if(number == 2):
            if(quantity > phone):
                print("Không đủ hàng.Hủy giao dịch!")
            else:
                phone -= quantity
                print("Xuất kho thành công!")
        if(number == 3):
            if(quantity > tablet):
                print("Không đủ hàng.Hủy giao dịch!")
            else:
                tablet -= quantity
                print("Xuất kho thành công!")
        else:
            print("mặt hàng không hợp lệ!")
    elif(choice == 4):
        check = 1
        if(laptop < 10):
            print(f"CẢNH BÁO! Mặt hàng laptop sắp hết(chỉ còn {laptop} sản phẩm)")
            check = 0
        if(phone < 10):
            print(f"CẢNH BÁO! Mặt hàng điện thoại sắp hết(chỉ còn {phone} sản phẩm)")
            check = 0
        if(tablet < 10):
            print(f"CẢNH BÁO! Mặt hàng máy tính bảng sắp hết(chỉ còn {tablet} sản phẩm)")
            check = 0
        if(check == 1):
            print("Tất cả mặt hàng đều còn")
    elif(choice == 5):
        print("Chào tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ! VUi lòng nhập lại")