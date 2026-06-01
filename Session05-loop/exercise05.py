print("=== HỆ THỐNG QUẢN LÝ THỐNG KÊ HỌC VIÊN ===")

while True:
    print("\n--- MENU ---")
    print("1. Nhập dữ liệu và xem báo cáo thống kê")
    print("2. Hiển thị hướng dẫn sử dụng")
    print("3. Thoát chương trình")
    
    choice = input("Vui lòng chọn chức năng (1-3): ").strip()
    
    if choice == '1':
        while True:
            num_branches_input = input("\nNhập số lượng chi nhánh: ").strip()
            if num_branches_input.isdigit() and int(num_branches_input) > 0:
                num_branches = int(num_branches_input)
                break
            print("Số lượng chi nhánh phải là số nguyên dương!")
            
        max_students = -1
        best_branch = 0
        low_classes_report = ""
        has_low_class = False
        
        print("\n--- NHẬP DỮ LIỆU ---")
        for branch in range(1, num_branches + 1):
            while True:
                num_classes_input = input(f"Nhập số lượng lớp học của Chi nhánh {branch}: ").strip()
                if num_classes_input.isdigit() and int(num_classes_input) > 0:
                    num_classes = int(num_classes_input)
                    break
                print("Số lượng lớp phải là số nguyên dương!")
                
            branch_total = 0
            
            for cls in range(1, num_classes + 1):
                while True:
                    students_input = input(f"Nhập số học viên của Lớp {cls} (Chi nhánh {branch}): ").strip()
                    if students_input.isdigit():
                        students = int(students_input)
                        break
                    print("Số học viên không hợp lệ (không được âm hoặc chứa chữ).")
                    
                branch_total += students
                
                if students < 10:
                    has_low_class = True
                    low_classes_report += f"Chi nhánh {branch}, Lớp {cls}: {students} học viên\n"
                    
            if branch_total > max_students:
                max_students = branch_total
                best_branch = branch
                
            print(f"=> Tổng số học viên của Chi nhánh {branch}: {branch_total}\n")
            
        print("=========================================")
        print("          BÁO CÁO THỐNG KÊ")
        print("=========================================")
        print(f"Chi nhánh có tổng số học viên cao nhất: Chi nhánh {best_branch} ({max_students} học viên)")
        
        print("\nDanh sách các lớp có sĩ số dưới 10 học viên:")
        if has_low_class:
            print(low_classes_report, end="")
        else:
            print("Không có lớp nào dưới 10 học viên.")
        print("=========================================\n")

    elif choice == '2':
        print("\n--- HƯỚNG DẪN SỬ DỤNG ---")
        print("- Chức năng 1: Lần lượt nhập số lượng chi nhánh, số lớp của từng chi nhánh và số học viên của từng lớp.")
        print("- Chức năng 2: Xem hướng dẫn sử dụng.")
        print("- Chức năng 3: Kết thúc và thoát hệ thống.")
        print("- Cảnh báo: Các dữ liệu nhập vào (số lượng, sĩ số) bắt buộc phải là số tự nhiên, không được nhập số âm hay chữ cái.")
        
    elif choice == '3':
        print("\nThoát chương trình. Tạm biệt!")
        break
        
    else:
        print("\nLựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 3!")