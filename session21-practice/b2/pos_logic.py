import logging

# --- CUSTOM EXCEPTIONS ---
class ItemNotFoundError(Exception):
    """Lỗi ném ra khi mã đồ uống không tồn tại trong thực đơn."""
    pass

class InvalidQuantityError(Exception):
    """Lỗi ném ra khi số lượng nhập vào nhỏ hơn hoặc bằng 0."""
    pass


# --- GLOBAL DATA ---
DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000}
}

current_order = []


# --- LOGIC FUNCTIONS ---
def process_add_to_order(drink_code: str, quantity: int):
    """Xử lý dữ liệu và kiểm tra ngoại lệ trước khi thêm vào giỏ hàng."""
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


def calculate_total(order: list) -> int:
    """Tính tổng tiền của một giỏ hàng bất kỳ."""
    total = sum(item["price"] * item["quantity"] for item in order)
    return total


def get_current_order() -> list:
    """Trả về trạng thái hiện tại của giỏ hàng."""
    return current_order


def clear_order():
    """Làm rỗng giỏ hàng."""
    current_order.clear()