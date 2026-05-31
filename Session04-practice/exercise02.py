print("=== HỆ THỐNG BÁO CÁO DOANH THU TUẦN ===")

total_revenue = 0
high_revenue_days = 0

for day in range(1, 8):
    while True:
        daily_revenue_input = input(f"Nhập doanh thu Ngày {day} (VND): ").strip()
        
        if daily_revenue_input.isdigit() and daily_revenue_input != "":
            daily_revenue = int(daily_revenue_input)
            
            total_revenue += daily_revenue
            
            if daily_revenue >= 5000000:
                high_revenue_days += 1
                
            break
        else:
            print("Doanh thu không hợp lệ. Vui lòng nhập số nguyên dương!")

average_revenue = total_revenue / 7

print("\nTỔNG KẾT DOANH THU 7 NGÀY")
print(f"Tổng doanh thu tuần  : {total_revenue:,.0f} VND")
print(f"Doanh thu trung bình : {average_revenue:,.0f} VND/ngày")
print(f"Số ngày đạt mục tiêu : {high_revenue_days} ngày (>= 5.000.000 VND)")