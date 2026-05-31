print("=== HỆ THỐNG KHỞI TẠO & PHÂN LUỒNG BỆNH ÁN SỐ ===")

patient_name = input("Nhập họ và tên bệnh nhân: ").strip()
patient_age_input = input("Nhập tuổi bệnh nhân: ").strip()

if not patient_age_input.lstrip('-').isdigit() or patient_age_input == "":
    print("\n[!] LỖI HỆ THỐNG: Tuổi bắt buộc phải là một số nguyên. Không được nhập chữ!")
else:
    patient_age = int(patient_age_input)
    
    # Kiểm tra các bẫy dữ liệu logic
    if patient_name == "" or patient_age < 0 or patient_age > 150:
        print("\n[!] LỖI: Tên không hợp lệ hoặc Tuổi nằm ngoài phạm vi con người (0-150)!")
        print("Hệ thống từ chối cấp phiếu khám. Vui lòng nhập lại.")
        
    else:
        if patient_age < 6:
            triage_result = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
        elif patient_age >= 80:
            triage_result = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
        else:
            triage_result = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."
            
        print("\n" + "="*35)
        print("     PHIẾU KHÁM BỆNH ĐIỆN TỬ     ")
        print("="*35)
        print(f"Họ và tên  : {patient_name.upper()}") 
        print(f"Tuổi       : {patient_age}")
        print(f"Phân luồng : {triage_result}")
        print("="*35)