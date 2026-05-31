print("=== HỆ THỐNG SÀNG LỌC TIỀN PHẪU THUẬT ===")

age_input = input("Nhập tuổi bệnh nhân: ").strip()
blood_pressure_input = input("Nhập huyết áp tâm thu (mmHg): ").strip()
blood_sugar_input = input("Nhập đường huyết (mg/dL): ").strip()

is_age_valid = age_input.lstrip('-').isdigit()
is_bp_valid = blood_pressure_input.lstrip('-').isdigit()
is_bs_valid = blood_sugar_input.lstrip('-').isdigit()

if not (is_age_valid and is_bp_valid and is_bs_valid):
    print("\n[CẢNH BÁO] LỖI HỆ THỐNG: Các chỉ số phải được nhập bằng chữ số nguyên. Không được nhập chữ!")
else:
    age = int(age_input)
    blood_pressure = int(blood_pressure_input)
    blood_sugar = int(blood_sugar_input)

    if age < 0 or blood_pressure < 0 or blood_sugar < 0:
        print("\n[CẢNH BÁO] LỖI: Dữ liệu nhập vào không hợp lệ (Tồn tại chỉ số âm).")
        print("Vui lòng kiểm tra lại thao tác nhập liệu của điều dưỡng!")
    
    else:
        print("\n--- KẾT QUẢ SÀNG LỌC ---")
        
        if age < 75:
            
            if 90 <= blood_pressure <= 140:
                
                if blood_sugar < 150:
                    print("KẾT LUẬN: ĐỦ ĐIỀU KIỆN PHẪU THUẬT.")
                    print("Bệnh nhân đã sẵn sàng chuyển lên phòng mổ.")
                else:
                    print("KẾT LUẬN: TỪ CHỐI PHẪU THUẬT.")
                    print(f"Lý do: Đường huyết ({blood_sugar} mg/dL) vượt mức an toàn (<150 mg/dL).")
            
            else:
                print("KẾT LUẬN: TỪ CHỐI PHẪU THUẬT.")
                print(f"Lý do: Huyết áp ({blood_pressure} mmHg) nằm ngoài giới hạn an toàn (90 - 140 mmHg).")
                
        else:
            print("KẾT LUẬN: TỪ CHỐI PHẪU THUẬT.")
            print(f"Lý do: Tuổi của bệnh nhân ({age} tuổi) vượt quá giới hạn cho phép (<75 tuổi).")