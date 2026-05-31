print("=== HỆ THỐNG KIOSK NHẬP LIỆU NHÂN SỰ SỐ ===")

for current_employee in range(1, 4):
    print(f"\n--- Đang xử lý nhân sự thứ {current_employee} ---")
    
    employee_id = input("Nhập mã nhân viên (Ví dụ: NV001): ").strip()
    employee_name = input("Nhập họ và tên: ").strip()
    employee_department = input("Nhập phòng ban công tác: ").strip()
    
    if employee_id == "" or employee_name == "":
        print("[!] CẢNH BÁO ĐỎ: Mã nhân viên và Họ tên không được phép bỏ trống hoặc chỉ chứa khoảng trắng!")
        print("-> Từ chối tạo hồ sơ. Chuyển sang nhân sự tiếp theo.")
        continue
        
    print("\n" + "="*45)
    print("           HỒ SƠ NHÂN SỰ ĐIỆN TỬ")
    print("="*45)
    print(f"Mã nhân viên : {employee_id.upper()}")
    print(f"Họ và tên    : {employee_name.title()}")
    print(f"Phòng ban    : {employee_department.title()}")
    print("="*45)

print("\n=> QUÁ TRÌNH ONBOARDING HÔM NAY ĐÃ KẾT THÚC!")