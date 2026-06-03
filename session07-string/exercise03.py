raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "
employees = raw_data.split("|")
count = 0

while True:
    print("===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    choice = input("NHap vao lua chon chua ban: ").strip()

    match choice:

        case "1":
            print(raw_data)

        case "2":

            print(f"{'ID':<10}{'HỌ TÊN':<20}{'SĐT':<20}{'PHÒNG BAN'}")
            print("-" * 60)

            for employee in employees:
                data = employee.split(";")

                employee_id = data[0]
                employee_name = data[1]

                phone = data[2].strip().replace("-", "")

                if phone.isdigit():
                    phone = "******" + phone[6:]
                else:
                    phone = "Invalid Format"

                department = data[3]

                print(f"{employee_id.strip().upper():<10}{employee_name.strip().title():<20}{phone:<20}{department.strip().upper()}")   
                


        case "3":
            find_id = input("Nhap vao id can tim: ").strip()

            for employee in employees:
                data = employee.split(";")

                if find_id.upper().strip() == data[0].upper().strip() : 
                    count  += 1
                    employee_id = data[0]
                    employee_name = data[1]

                    phone = data[2].strip().replace("-","")

                    if phone.isdigit():
                        phone = "******" + phone[6:]
                    else:
                        phone = "Invalid Format"

                    department = data[3]
                    print(f"{employee_id.strip().upper():<10}{employee_name.strip().title():<20}{phone:<20}{department.strip().upper()}")  

            if count == 0:
                print("Khong tim thay....")

        case "4":
            break
        
        case _:
            print("lua chon sai, nhap lai")