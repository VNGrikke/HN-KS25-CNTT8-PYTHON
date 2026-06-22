import logging

# 1. Sửa lỗi Logging: Thay đổi level thành logging.INFO để hiển thị luồng chạy bình thường
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)

def get_shipping_rate(method: str, distance: int) -> float:
    """Trả về chi phí vận chuyển cơ sở dựa trên phương thức và khoảng cách"""
    logger.info(f"Đang tính phí giao hàng cho phương thức {method} với khoảng cách {distance} km")
    
    # 2. Xử lý ngoại lệ chặt chẽ (Clean Code): Ném ra lỗi ValueError thay vì return 0.0
    if distance <= 0:
        logger.error("Khoảng cách vận chuyển không được nhỏ hơn hoặc bằng 0")
        raise ValueError("Distance must be positive")

    # Xác định phí cơ sở theo phương thức vận chuyển
    if method == "standard":
        base_rate = 15000
    elif method == "express":
        base_rate = 30000
    elif method == "next_day":
        base_rate = 50000
    else:
        base_rate = 20000
        
    # Phụ thu đường xa nếu khoảng cách từ 20km trở lên
    # 3. Sửa lỗi Logic: Sử dụng toán tử cộng dồn (+=) để thêm phí phụ thu
    if distance >= 20:
        base_rate += 10000
        
    return base_rate

def calculate_final_shipping(weight: float, distance: int, method: str) -> float:
    """Tính tổng chi phí vận chuyển cuối cùng dựa trên trọng lượng hàng hóa"""
    if weight < 0:
        raise ValueError("Trọng lượng hàng hóa không được âm")
        
    base_rate = get_shipping_rate(method, distance)
    
    # Giả sử phí tăng thêm 2,000đ cho mỗi kg hàng hóa
    total_cost = base_rate + (weight * 2000)
    
    logger.warning(f"Kết quả: Tổng phí vận chuyển = {total_cost}")
    return total_cost

if __name__ == "__main__":
    try:
        # Case kiểm tra lỗi logic biên (đường xa) -> Output kỳ vọng: 30000 + 10000 + (3.5 * 2000) = 47000
        calculate_final_shipping(3.5, 25, "express") 
        
        # Case kiểm tra lỗi dữ liệu đầu vào -> Sẽ văng ra ValueError và bị bắt bởi khối try-except
        calculate_final_shipping(2.0, -5, "standard") 
    except Exception as e:
        logger.error(f"Đã xảy ra lỗi: {e}")