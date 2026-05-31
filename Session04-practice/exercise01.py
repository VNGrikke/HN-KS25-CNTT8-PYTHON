total_amount_input = input("Nhập tổng số tiền hóa đơn (VND): ").strip()

if not total_amount_input.isdigit() or total_amount_input == "":
    print("\nDữ liệu nhập vào không hợp lệ. Vui lòng nhập số nguyên dương!")
else:
    total_amount = int(total_amount_input)
    
    if total_amount >= 500000:
        discount_amount = total_amount * 10 / 100
    else:
        discount_amount = 0
        
    final_amount = total_amount - discount_amount
    
    print(f"Tổng tiền ban đầu      : {total_amount:,.0f} VND")
    print(f"Mức chiết khấu áp dụng : {'10%' if total_amount >= 500000 else '0%'}")
    print(f"Số tiền giảm giá       : {discount_amount:,.0f} VND")
    print(f"Số tiền khách phải trả : {final_amount:,.0f} VND")