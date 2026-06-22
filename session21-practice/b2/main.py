import logging
from pos_logic import (
    DRINK_MENU,
    ItemNotFoundError,
    InvalidQuantityError,
    process_add_to_order,
    calculate_total,
    get_current_order,
    clear_order
)

# Cấu hình logging cơ bản xuất ra Terminal
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def display_menu():
    """Hiển thị thực đơn đồ uống cho người dùng."""
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, details in DRINK_MENU.items():
        price_str = f"{details['price']:,}".replace(',', ',')
        print(f"[{code}] - {details['name']} - {price_str} VNĐ")

def handle_add_to_order():
    """Giao diện nhận đầu vào từ người dùng và xử lý các lỗi (Edge Cases)."""
    print("\n--- THÊM MÓN VÀO GIỎ ---")
    raw_code = input("Nhập mã đồ uống: ")
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

def view_order():
    """In chi tiết các món trong giỏ hàng và tổng tiền."""
    order = get_current_order()
    if not order:
        print("\nGiỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return False

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")
    print(f"{'Mã SP':<5} | {'Tên đồ uống':<20} | {'Đơn giá':<8} | {'Số lượng':<8} | {'Thành tiền'}")
    print("-" * 64)
    
    for item in order:
        line_total = item['price'] * item['quantity']
        price_str = f"{item['price']:,}"
        line_total_str = f"{line_total:,} VNĐ"
        print(f"{item['code']:<5} | {item['name']:<20} | {price_str:<8} | {item['quantity']:<8} | {line_total_str}")
        
    print("-" * 64)
    total = calculate_total(order)
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")
    return True

def checkout():
    """Xử lý thanh toán và dọn dẹp giỏ hàng."""
    order = get_current_order()
    if not order:
        print("\nGiỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    print("\n--- THANH TOÁN ---")
    total = calculate_total(order)
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")
    
    confirm = input(f"Xác nhận thanh toán {total:,} VNĐ? (y/n): ").strip().lower()

    if confirm == 'y':
        print("Thanh toán thành công.")
        logging.info("Checkout successful")
        clear_order()
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