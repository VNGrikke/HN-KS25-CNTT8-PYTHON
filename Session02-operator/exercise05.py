print("=== KIOSK PHÂN LUỒNG TỰ PHỤC VỤ ===")

patient_name = input("Họ và tên bệnh nhân (Ví dụ: Nguyen Van A): ").strip()
patient_age_input = input("Tuổi của bệnh nhân (Ví dụ: 35): ").strip()
spo2_level_input = input("Nồng độ oxy trong máu SpO2 (%) (Ví dụ: 98): ").strip()
heart_rate_input = input("Nhịp tim (nhịp/phút) (Ví dụ: 80): ").strip()
insurance_input = input("Bạn có thẻ Bảo hiểm Y tế không? (Vui lòng chỉ gõ 'yes' hoặc 'no'): ").strip().lower()

if not (patient_age_input.isdigit() and spo2_level_input.isdigit() and heart_rate_input.isdigit()):
    print("\n[!] LỖI HỆ THỐNG: Tuổi, SpO2 và Nhịp tim bắt buộc phải là số nguyên. Vui lòng thao tác lại!")
else:
    patient_age = int(patient_age_input)
    spo2_level = int(spo2_level_input)
    heart_rate = int(heart_rate_input)
    
    has_insurance = insurance_input == 'yes'
    
    if spo2_level < 90 or heart_rate > 120:
        triage_status = "BÁO ĐỘNG ĐỎ - Cấp cứu khẩn"
    elif (90 <= spo2_level <= 95) or (100 <= heart_rate <= 120):
        triage_status = "BÁO ĐỘNG VÀNG - Theo dõi sát"
    else:
        triage_status = "XANH - Khám thường"
        
    if patient_age < 6 or patient_age >= 80:
        medical_fee = 0
    elif has_insurance:
        medical_fee = 250000
    else:
        medical_fee = 500000
        
    print("\n" + "="*50)
    print("             PHIẾU KHÁM BỆNH ĐIỆN TỬ             ")
    print("="*50)
    print(f"Họ và tên             : {patient_name.upper()}")
    print(f"Tuổi                  : {patient_age}")
    print(f"SpO2                  : {spo2_level}%")
    print(f"Nhịp tim              : {heart_rate} bpm")
    print(f"Thẻ Bảo hiểm Y tế     : {'Có' if has_insurance else 'Không'}")
    print("-" * 50)
    print(f"PHÂN LUỒNG Y KHOA     : {triage_status}")
    print(f"TẠM ỨNG VIỆN PHÍ      : {medical_fee:,} VNĐ")
    print("="*50)
    
    print("\n--- SYSTEM LOGS ---")
    print(f"patient_name  : {type(patient_name)}")
    print(f"patient_age   : {type(patient_age)}")
    print(f"spo2_level    : {type(spo2_level)}")
    print(f"heart_rate    : {type(heart_rate)}")
    print(f"has_insurance : {type(has_insurance)}")