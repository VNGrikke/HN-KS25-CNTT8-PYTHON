print("--- HỆ THỐNG GỬI EMAIL THƯỞNG TẾT ---")

for employee_number in range(1, 4):
    print(f"--- Đang xử lý nhân viên số {employee_number} ---")
    
    working_days_input = input("Nhập số ngày công trong tháng: ").strip()
    
    if not working_days_input.isdigit():
        print("Dữ liệu không hợp lệ. Vui lòng nhập số nguyên dương hoặc 0.")
        print("-" * 40 + "\n")
        continue
        
    working_days = int(working_days_input)
    
    if working_days == 0:
        print("CẢNH BÁO: Nhân viên nghỉ cả tháng. Không xét duyệt thưởng.")
        print("-" * 40 + "\n")
        continue
        
    bonus_amount = working_days * 200000
    print(f"-> Đã gửi Email: Chúc mừng nhận được {bonus_amount} VNĐ tiền thưởng!")
    print("-" * 40 + "\n")

print("Đã hoàn tất quá trình duyệt thưởng cho 3 nhân viên!")