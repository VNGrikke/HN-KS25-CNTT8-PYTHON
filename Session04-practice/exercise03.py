
while True:
    num_bills_input = input("Nhập tổng số lượng hóa đơn trong ca: ").strip()
    if num_bills_input.isdigit() and num_bills_input != "":
        num_bills = int(num_bills_input)
        if num_bills > 0:
            break
        else:
            print("Số lượng hóa đơn phải lớn hơn 0!")
    else:
        print("Vui lòng nhập số nguyên dương hợp lệ!")

max_bill = 0
min_bill = float('inf')

for i in range(1, num_bills + 1):
    while True:
        bill_value_input = input(f"Nhập giá trị hóa đơn thứ {i} (VND): ").strip()
        
        if bill_value_input.isdigit() and bill_value_input != "":
            bill_value = int(bill_value_input)
            
            if bill_value > max_bill:
                max_bill = bill_value
            
            if bill_value < min_bill:
                min_bill = bill_value
                
            break
        else:
            print("Giá trị hóa đơn không hợp lệ. Vui lòng nhập số nguyên dương!")

print("\nKẾT QUẢ THỐNG KÊ CA LÀM")
print(f"Tổng số lượng hóa đơn : {num_bills}")
print(f"Hóa đơn có giá trị lớn nhất : {max_bill:,.0f} VND")
print(f"Hóa đơn có giá trị nhỏ nhất : {min_bill:,.0f} VND")