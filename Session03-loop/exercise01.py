print("--- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG ---")

total_budget = 0

for employee_number in range(1, 4):
    print("Đang xử lý nhân viên số", employee_number)
    salary_input = input(" Nhập mức lương (VNĐ): ").strip()
    
    if not salary_input.isdigit():
        print("Lỗi: Dữ liệu nhập vào không hợp lệ. Vui lòng nhập số nguyên!")
        break
        
    salary = int(salary_input)
    total_budget = total_budget + salary

else:
    print("=> KẾT QUẢ: TỔNG NGÂN SÁCH CẦN CHUẨN BỊ LÀ:", total_budget, "VNĐ")