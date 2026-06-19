import logging

logging.basicConfig(
    filename="momo_transations.log",
    level= logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
    )

wallet_state = {"balance": 0 }



def process_deposit(state: dict, amount: int) -> None:
    if amount <= 0:
        # Ném ra lỗi mặc định của Python, kẹp tên Custom Error vào chuỗi
        raise Exception(f"InvalidAmountError: Attempted to process {amount} VND.")

    state["balance"] += amount
    logging.info(f"Deposit successful: +{amount} VND. Current Balance: {state['balance']}")


def handle_deposit(state: dict) -> None:
    print("\n--- NẠP TIỀN VÀO VÍ ---")
    
    try:
        amount_str = input("Nhập số tiền cần nạp: ")
        amount = int(amount_str)  # Sẽ raise ValueError nếu nhập chữ
        
        process_deposit(state, amount)
        
        print(f"\nNạp tiền thành công: +{amount:,.0f} VND")
        print(f"Số dư hiện tại: {state['balance']:,.0f} VND")

    except ValueError:
        logging.error("ValueError: Invalid numeric input for deposit.")
        print("\nLỗi: Vui lòng nhập số tiền hợp lệ.")
        
    except Exception as e:
        # Bắt mọi lỗi Exception khác và bóc tách thông báo
        error_message = str(e)
        
        if "InvalidAmountError" in error_message:
            logging.error(f"[ERROR] - {error_message}")
            print("\nLỗi: Số tiền giao dịch phải lớn hơn 0.")
        else:
            # Nếu là lỗi khác không lường trước
            logging.error(f"Unexpected Error: {error_message}")
            print("\nLỗi hệ thống không xác định.")


def process_transfer(state: dict, phone: str, amount: int) -> None:
    """Xử lý logic trừ tiền và ghi log cho giao dịch chuyển tiền."""
    
    # Bẫy 1: Số tiền âm hoặc bằng 0
    if amount <= 0:
        raise Exception(f"InvalidAmountError: Attempted to process {amount} VND.")

    # Bẫy 2: Số dư không đủ
    if amount > state["balance"]:
        raise Exception(
            f"InsufficientBalanceError: Attempted to transfer {amount} VND "
            f"with balance {state['balance']} VND."
        )

    # Thực hiện trừ tiền
    state["balance"] -= amount

    # Yêu cầu Logging: Giao dịch giá trị cao
    if amount >= 10000000:
        logging.warning(f"High value transaction detected: {amount} VND to {phone}")

    # Ghi log thành công (Ghi sau log Warning nếu có)
    logging.info(
        f"Transfer successful: -{amount} VND to {phone}. "
        f"Current Balance: {state['balance']}"
    )


def handle_transfer(state: dict) -> None:
    """Xử lý giao diện CLI cho nghiệp vụ chuyển tiền."""
    print("\n--- CHUYỂN TIỀN ---")
    
    # Kiểm tra định dạng số điện thoại (10 chữ số)
    phone = input("Nhập số điện thoại người nhận: ").strip()
    if len(phone) != 10 or not phone.isdigit():
        print("\nLỗi: Số điện thoại không hợp lệ (phải gồm đúng 10 chữ số).")
        return  # Dừng hàm, quay lại menu chính

    try:
        amount_str = input("Nhập số tiền cần chuyển: ")
        amount = int(amount_str)  # Sẽ raise ValueError nếu nhập chữ
        
        # Gọi logic xử lý
        process_transfer(state, phone, amount)
        
        # Output thành công
        print(f"\nChuyển tiền thành công tới số điện thoại {phone}.")
        print(f"Số tiền đã chuyển: {amount:,.0f} VND")
        print(f"Số dư còn lại: {state['balance']:,.0f} VND")

    except ValueError:
        logging.error("ValueError: Invalid numeric input for transfer.")
        print("\nLỗi: Vui lòng nhập số tiền hợp lệ.")
        
    except Exception as e:
        error_message = str(e)
        
        # Bóc tách lỗi theo từ khóa như đã làm ở Chức năng 1
        if "InvalidAmountError" in error_message:
            logging.error(f"[ERROR] - {error_message}")
            print("\nLỗi: Số tiền giao dịch phải lớn hơn 0.")
            
        elif "InsufficientBalanceError" in error_message:
            logging.error(f"[ERROR] - {error_message}")
            print("\nGiao dịch thất bại: Số dư của bạn không đủ.")
            
        else:
            logging.error(f"Unexpected Error: {error_message}")
            print("\nLỗi hệ thống không xác định.")


def handle_check_balance(state: dict) -> None:
    """Xử lý hiển thị số dư hiện tại và ghi log."""
    balance = state["balance"]
    
    # In ra giao diện người dùng
    print("\n--- SỐ DƯ VÍ MOMO ---")
    print(f"Số dư hiện tại: {balance:,.0f} VND")
    
    # Ghi log theo đúng chuẩn yêu cầu
    logging.info(f"Balance checked. Current Balance: {balance}")



def menu():
    print("""
========== VÍ MOMO GIẢ LẬP ==========

1. Nạp tiền vào ví

2. Chuyển tiền

3.  Xem số dư hiện tại

4. Thoát chương trình 

=====================================
""")
    

def main():
    while True:
        menu()

        choice = input("Chon chuc nang (1-4): ").strip()

        match choice:
            case "1":
                handle_deposit(wallet_state)

            case "2":
                handle_transfer(wallet_state)
            
            case "3":
                handle_check_balance(wallet_state)

            case "4": 
                print("Thoat chuong trinh.")
                break
            
            case _:
                print("Chuc nang khong ton tai.")


main()