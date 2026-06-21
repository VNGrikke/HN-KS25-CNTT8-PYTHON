import logging

# Cấu hình logging cơ bản xuất ra Terminal
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ItemNotFoundError(Exception):
    """Lỗi ném ra khi mã đồ uống không tồn tại trong thực đơn."""
    pass

class InvalidQuantityError(Exception):
    """Lỗi ném ra khi số lượng nhập vào nhỏ hơn hoặc bằng 0."""
    pass


DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}

current_order = []


# --- FUNCTIONS ---
def display_menu():
    """Hiển thị thực đơn đồ uống cho người dùng."""
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, details in DRINK_MENU.items():
        # Sử dụng format {,} và replace để biến dấu phẩy thành chuẩn hiển thị tiền tệ
        price_str = f"{details['price']:,}".replace(',', ',')
        print(f"[{code}] - {details['name']} - {price_str} VNĐ")


def process_add_to_order(drink_code: str, quantity: int):
    """Luồng xử lý dữ liệu và kiểm tra ngoại lệ trước khi thêm vào giỏ hàng."""
    if drink_code not in DRINK_MENU:
        raise ItemNotFoundError(drink_code)
    
    if quantity <= 0:
        raise InvalidQuantityError(quantity)

    current_order.append({
        "code": drink_code,
        "name": DRINK_MENU[drink_code]["name"],
        "price": DRINK_MENU[drink_code]["price"],
        "quantity": quantity
    })
    logging.info(f"Added {quantity} of {drink_code} to order")


def handle_add_to_order():
    """Giao diện nhận đầu vào từ người dùng và xử lý các lỗi (Edge Cases)."""
    print("\n--- THÊM MÓN VÀO GIỎ ---")
    raw_code = input("Nhập mã đồ uống: ")
    # Chuẩn hóa mã đồ uống: cắt khoảng trắng 2 đầu và in hoa (Vd: ' f1 ' -> 'F1')
    drink_code = raw_code.strip().upper()

    try:
        raw_quantity = input("Nhập số lượng: ")
        quantity = int(raw_quantity)
        
        process_add_to_order(drink_code, quantity)
        print(f"Đã thêm {quantity} x {DRINK_MENU[drink_code]['name']} vào giỏ hàng.")
        
    except ValueError:
        print("Vui lòng nhập số lượng là một số nguyên!")
        logging.error("ValueError - Invalid quantity input")
    except ItemNotFoundError as e:
        print("Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!")
        logging.warning(f"ItemNotFoundError - Code: {e}")
    except InvalidQuantityError as e:
        print("Số lượng phải lớn hơn 0!")
        logging.warning(f"InvalidQuantityError - Quantity: {e}")


def calculate_total(order: list) -> int:
    """Tính tổng tiền của giỏ hàng."""
    total = sum(item["price"] * item["quantity"] for item in order)
    return total


def view_order():
    """In chi tiết các món trong giỏ hàng và tổng tiền."""
    if not current_order:
        print("\nGiỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return False

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")
    print(f"{'Mã SP':<5} | {'Tên đồ uống':<20} | {'Đơn giá':<8} | {'Số lượng':<8} | {'Thành tiền'}")
    print("-" * 64)
    
    for item in current_order:
        line_total = item['price'] * item['quantity']
        price_str = f"{item['price']:,}"
        line_total_str = f"{line_total:,} VNĐ"
        print(f"{item['code']:<5} | {item['name']:<20} | {price_str:<8} | {item['quantity']:<8} | {line_total_str}")
        
    print("-" * 64)
    total = calculate_total(current_order)
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")
    return True


def checkout():
    """Xử lý thanh toán và dọn dẹp giỏ hàng."""
    global current_order
    
    if not current_order:
        print("\nGiỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    print("\n--- THANH TOÁN ---")
    total = calculate_total(current_order)
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")
    
    confirm = input(f"Xác nhận thanh toán {total:,} VNĐ? (y/n): ").strip().lower()

    if confirm == 'y':
        print("Thanh toán thành công.")
        logging.info("Checkout successful")
        current_order.clear()  # Làm rỗng giỏ hàng
        print("Giỏ hàng đã được làm trống.")
    elif confirm == 'n':
        print("Đã hủy thao tác thanh toán. Quay lại menu chính.")
    else:
        print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")


def main():
    """Vòng lặp chính của chương trình POS."""
    while True:
        print("\n========== HIGHLANDS MINI POS ==========")
        print("1. Xem thực đơn")
        print("2. Thêm món vào giỏ")
        print("3. Xem giỏ hàng & Tính tổng tiền")
        print("4. Thanh toán & Xóa giỏ hàng")
        print("5. Thoát ca làm việc")
        print("========================================")
        
        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == '1':
            display_menu()
        elif choice == '2':
            handle_add_to_order()
        elif choice == '3':
            view_order()
        elif choice == '4':
            checkout()
        elif choice == '5':
            logging.info("Cashier logged out. System shutdown.")
            print("Đã thoát ca làm việc. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn từ 1-5.")

if __name__ == "__main__":
    main()