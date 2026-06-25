# Hệ thống quản lý hóa đơn Rikkei Coffee
class CoffeeOrder:
    # Thuộc tính của lớp (Class Attribute)
    vat_rate = 0.10  # Mặc định thuế VAT là 10%

    def __init__(self, table_number):
        self.table_number = table_number
        self.total_amount = 0  

    # Phương thức thêm tiền món ăn vào hóa đơn
    def add_item(self, price):
        if price > 0:
            self.total_amount += price

    # Tính tổng tiền khách phải trả (đã cộng VAT)
    def calculate_final_bill(self):
        return self.total_amount + (self.total_amount * self.vat_rate)

    # Lỗ hổng 2: Dùng Instance Method để thay đổi Class Attribute
    def update_vat_rate(self, new_rate):
        self.vat_rate = new_rate

# --- KỊCH BẢN TẤN CÔNG & LỖI HỆ THỐNG ---

# Khách vào quán, hệ thống mở hóa đơn cho 2 bàn
order_table1 = CoffeeOrder("Bàn 1")
order_table2 = CoffeeOrder("Bàn 2")

# Khách gọi món
order_table1.add_item(50000) # Bàn 1 gọi Cà phê sữa
order_table2.add_item(30000) # Bàn 2 gọi Trà đào

# 1. Nhân viên gian lận tự gán đè tổng tiền của Bàn 1 về 0 để ăn trộm tiền
order_table1.total_amount = 0

# 2. Quản lý chi nhánh cập nhật thuế VAT xuống 8% (0.08) cho hệ thống
order_table1.update_vat_rate(0.08)

print(f"Tổng tiền Bàn 1 (sau VAT): {order_table1.calculate_final_bill()} VNĐ")
print(f"Thuế VAT đang áp dụng cho Bàn 1: {order_table1.vat_rate}")
print(f"Thuế VAT đang áp dụng cho Bàn 2: {order_table2.vat_rate}")