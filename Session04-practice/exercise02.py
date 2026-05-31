wekly_revenue = []

for x in range (7) :
    revenue = input(f"nhap vao doanh thu cua ngay thu {x+1}: ")
    wekly_revenue.append(revenue)
total_revenue = sum(wekly_revenue)

print("tong doanh thu cua 1 tuan: ", total_revenue)