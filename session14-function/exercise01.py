"""
1. Giá trị 15000 và 0.1 được gán cho tham số nào?
calculate_final_price(100000, 15000, 0.1)
15000 → discount
0.1 → shipping_fee

2. Vì sao kết quả ra số âm?
Công thức:
100000 - (100000 * 15000) + 0.1
Do 15000 bị hiểu là tỷ lệ giảm giá nên: 100000 * 15000 = 1500000000
Kết quả: 100000 - 1500000000 + 0.1 = -1499999999.9

3. Vì sao final_payment = order_total + 5000 bị lỗi?
Vì order_total có giá trị None, không thể cộng với số nguyên.

4. order_total đang mang giá trị gì? Tại sao?
order_total = None
Vì hàm chỉ dùng print() mà không có return.

5. Khác nhau giữa print(total) và return total?
print(total): chỉ hiển thị kết quả.
return total: trả kết quả về cho nơi gọi hàm sử dụng tiếp.
"""

def calculate_final_price(price, discount, shipping_fee):
    total = price - (price * discount) + shipping_fee
    return total


price = 100000
discount = 0.1
shipping_fee = 15000

order_total = calculate_final_price(price, discount, shipping_fee)

final_payment = order_total + 5000

print("Đã tính xong tổng tiền:", order_total)
print("Khách hàng cần thanh toán:", final_payment)