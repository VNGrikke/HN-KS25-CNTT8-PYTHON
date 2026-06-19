def display_orders(order_list):
    """Hàm xử lý hiển thị danh sách đơn hàng dạng bảng."""
    print("\n--- DANH SÁCH ĐƠN HÀNG ---")
    if not order_list:
        print("Thông báo: Danh sách đơn hàng hiện đang trống!")
        return

    # Căn lề: Trái (<), Phải (>) với số lượng ký tự cố định
    print(f"{'Mã ĐH':<10} | {'Tên Đại Lý':<25} | {'Giá Trị (VND)':>15} | {'Trạng Thái':<10}")
    print("-" * 68)
    
    for order in order_list:
        # Sử dụng f-string định dạng số tiền có dấu phẩy ngăn cách hàng nghìn
        print(f"{order['id']:<10} | {order['name']:<25} | {order['price']:>15,} | {order['status']:<10}")


def add_order(order_list):
    """Hàm xử lý thêm mới đơn hàng, validate dữ liệu và bắt lỗi trùng lặp."""
    print("\n--- TẠO MỚI ĐƠN HÀNG ---")
    
    # 1. Thu thập và Validate Mã đơn hàng
    while True:
        order_id = input("Nhập Mã đơn hàng: ").strip()
        if not order_id:
            print("Lỗi: Mã đơn hàng không được để trống. Vui lòng nhập lại!")
            continue
            
        # Kiểm tra trùng mã
        is_exist = False
        for order in order_list:
            if order['id'] == order_id:
                is_exist = True
                break
                
        if is_exist:
            print("ERR-01: Mã đơn hàng đã tồn tại. Hủy thao tác tạo mới!")
            return  # Dừng hàm, quay lại menu chính
        break

    # 2. Thu thập và Validate Tên đại lý
    while True:
        name = input("Nhập Tên đại lý: ").strip()
        if not name:
            print("Lỗi: Tên đại lý không được để trống. Vui lòng nhập lại!")
            continue
        break

    # 3. Thu thập và Validate Giá trị đơn hàng (Xử lý ngoại lệ)
    while True:
        price_str = input("Nhập Giá trị đơn hàng (VND): ").strip()
        try:
            price = int(price_str)
            if price <= 0:
                print("Lỗi: Giá trị đơn hàng phải lớn hơn 0. Vui lòng nhập lại!")
                continue
            break
        except ValueError:
            print("Lỗi: Sai định dạng. Giá trị đơn hàng phải là số nguyên!")

    new_order = {
        'id': order_id, 
        'name': name, 
        'price': price, 
        'status': 'Unpaid'
    }
    order_list.append(new_order)
    print("Thông báo: Tạo mới đơn hàng thành công!")


def update_order_status(order_list):
    """Hàm tìm kiếm đơn hàng theo mã và cập nhật trạng thái thanh toán."""
    print("\n--- CẬP NHẬT TRẠNG THÁI THANH TOÁN ---")
    order_id = input("Nhập Mã đơn hàng cần cập nhật: ").strip()
    
    if not order_id:
        print("Lỗi: Mã đơn hàng không được để trống!")
        return

    # Tìm kiếm tuyến tính
    for order in order_list:
        if order['id'] == order_id:
            if order['status'] == 'Paid':
                print("ERR-04: Đơn hàng đã được thanh toán từ trước.")
            else:
                order['status'] = 'Paid'
                print("Thông báo: Cập nhật trạng thái thành công!")
            return
            
    # Nếu chạy hết vòng lặp mà không return -> Không tìm thấy
    print("ERR-03: Không tìm thấy mã đơn hàng trong hệ thống.")


def calculate_revenue(order_list):
    """
    Hàm tính toán tổng doanh thu của các đơn 'Paid' và mức chiết khấu.
    Chỉ tính toán và trả về Tuple (tổng doanh thu, % chiết khấu, tiền chiết khấu).
    """
    total_revenue = 0
    for order in order_list:
        if order['status'] == 'Paid':
            total_revenue += order['price']
            
    # Áp dụng quy tắc chiết khấu
    if total_revenue >= 100000000:
        discount_percent = 5
    else:
        discount_percent = 0
        
    discount_amount = int(total_revenue * (discount_percent / 100))
    
    return (total_revenue, discount_percent, discount_amount)


def main():
    """Hàm điều phối chính, chứa dữ liệu gốc và vòng lặp Menu."""
    # Khởi tạo dữ liệu gốc theo yêu cầu
    orders = [
        {'id': 'HD01', 'name': 'Dai ly Hoang Long', 'price': 45000000, 'status': 'Paid'},
        {'id': 'HD02', 'name': 'Tap hoa Minh Thu', 'price': 15000000, 'status': 'Unpaid'}
    ]

    while True:
        print("\n==========================================")
        print("  HỆ THỐNG QUẢN LÝ ĐƠN HÀNG ĐẠI LÝ")
        print("==========================================")
        print("1. Xem danh sách đơn hàng hiện có")
        print("2. Tạo mới đơn hàng đại lý")
        print("3. Cập nhật trạng thái thanh toán")
        print("4. Tính tổng doanh thu & Chiết khấu")
        print("5. Thoát chương trình")
        print("==========================================")
        
        # Bẫy lỗi người dùng nhập sai kiểu dữ liệu ở Menu
        try:
            choice = int(input("Vui lòng chọn chức năng (1-5): "))
        except ValueError:
            print("Lỗi: Vui lòng chỉ nhập số từ 1 đến 5!")
            continue

        if choice == 1:
            display_orders(orders)
            
        elif choice == 2:
            add_order(orders)
            
        elif choice == 3:
            update_order_status(orders)
            
        elif choice == 4:
            revenue, percent, discount = calculate_revenue(orders)
            print("\n--- BÁO CÁO DOANH THU ---")
            print(f"Tổng doanh thu thực tế: {revenue:,} VND")
            print(f"Phần trăm chiết khấu áp dụng: {percent}%")
            print(f"Số tiền chiết khấu: {discount:,} VND")
            print(f"Doanh thu thuần (sau chiết khấu): {revenue - discount:,} VND")
            
        elif choice == 5:
            print("\nCảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")
            break
            
        else:
            print("Lỗi: Chức năng không tồn tại. Vui lòng chọn từ 1 đến 5!")

main()