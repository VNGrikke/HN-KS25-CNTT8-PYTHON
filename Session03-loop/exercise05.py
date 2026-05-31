print("============================================================")
print("       KIOSK HR: CẬP NHẬT HỒ SƠ & ĐÁNH GIÁ KPI")
print("============================================================")

while True:
    print("\n[Nhập thông tin nhân viên]")
    
    while True:
        employee_id = input("1. Enter Employee ID: ").strip()
        if employee_id != "":
            break
        print("   [!] LỖI: Mã nhân viên không được để trống!")

    while True:
        employee_name = input("2. Enter Full Name: ").strip()
        if employee_name != "":
            break
        print("   [!] LỖI: Họ và tên không được để trống!")

    while True:
        salary_input = input("3. Enter current Salary in VND (Number > 0): ").strip()
        if salary_input.lstrip('-').isdigit():
            current_salary = int(salary_input)
            if current_salary > 0:
                break
            else:
                print("   [!] LỖI: Lương không thể là số âm hoặc bằng 0. Vui lòng nhập lại!")
        else:
            print("   [!] LỖI: Vui lòng nhập một số nguyên hợp lệ!")

    while True:
        kpi_input = input("4. Enter Performance Score (1.0 to 5.0): ").strip()
        if kpi_input.replace('.', '', 1).isdigit() and kpi_input != "":
            performance_score = float(kpi_input)
            if 1.0 <= performance_score <= 5.0:
                break
            else:
                print("   [!] LỖI: Điểm KPI phải nằm trong khoảng từ 1.0 đến 5.0!")
        else:
            print("   [!] LỖI: Điểm KPI phải là một số!")

    while True:
        exp_input = input("5. Enter Year of Experience (Integer >= 0): ").strip()
        if exp_input.isdigit():
            experience_years = int(exp_input)
            break
        else:
            print("   [!] LỖI: Số năm kinh nghiệm phải là số nguyên lớn hơn hoặc bằng 0!")

    print("\n============================================================")
    print("                  E-PROFILE CẬP NHẬT")
    print("============================================================")
    print(f"- ID: {employee_id.upper()}")
    print(f"- Name: {employee_name.title()}")
    print(f"- Salary: {current_salary} VND")
    print(f"- KPI Score: {performance_score} / 5.0")
    print(f"- Experience: {experience_years} years")
    
    print("============================================================")
    print("                    IT SYSTEM LOG")
    print("============================================================")
    print(f"{'employee_id':<18} | {str(type(employee_id))}")
    print(f"{'employee_name':<18} | {str(type(employee_name))}")
    print(f"{'current_salary':<18} | {str(type(current_salary))}")
    print(f"{'performance_score':<18} | {str(type(performance_score))}")
    print(f"{'experience_years':<18} | {str(type(experience_years))}")
    print("------------------------------------------------------------")

    continue_choice = input("\nDo you want to enter another employee? (y/n): ").strip().lower()
    if continue_choice != 'y':
        print("\nĐang tắt Kiosk... Tạm biệt!")
        break