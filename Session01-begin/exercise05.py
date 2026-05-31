print("="*50)
print(" CHÀO MỪNG BẠN ĐẾN VỚI BỆNH VIỆN SỨC KHỎE VÀNG ")
print(" KIOSK KHAI BÁO THÔNG TIN Y TẾ TỰ PHỤC VỤ ")
print("="*50)
print("Vui lòng làm theo hướng dẫn bên dưới. Đọc kỹ ví dụ để nhập đúng thông tin.\n")

raw_name = input("1. Họ và tên của bạn là gì?\n   [Ví dụ: Nguyen Van A] -> Trả lời: ")
raw_age = input("2. Bạn năm nay bao nhiêu tuổi? (Chỉ nhập số)\n   [Ví dụ: 25] -> Trả lời: ")
raw_temperature = input("3. Nhiệt độ cơ thể của bạn hiện tại là bao nhiêu độ C? (Dùng dấu chấm cho số thập phân)\n   [Ví dụ: 37.5] -> Trả lời: ")
raw_heart_rate = input("4. Nhịp tim hiện tại của bạn là bao nhiêu? (Nhịp/phút, chỉ nhập số)\n   [Ví dụ: 80] -> Trả lời: ")
raw_first_visit = input("5. Đây có phải lần đầu bạn đến khám không? (Nhập 1 nếu CÓ, nhập 0 nếu KHÔNG)\n   [Ví dụ: 1] -> Trả lời: ")

patient_name = str(raw_name).strip().upper() 
patient_age = int(raw_age)                  
body_temperature = float(raw_temperature)    
heart_rate = int(raw_heart_rate)              
is_first_visit = bool(int(raw_first_visit))   


print("\n" + "="*50)
print(" PHIẾU KHÁM BỆNH ĐIỆN TỬ ")
print("="*50)
print(f"Họ và tên bệnh nhân : {patient_name}")
print(f"Tuổi                : {patient_age} tuổi")
print(f"Nhiệt độ cơ thể     : {body_temperature} °C")
print(f"Nhịp tim            : {heart_rate} bpm")

if is_first_visit:
    print("Trạng thái          : Khám lần đầu (Cần lập hồ sơ mới)")
else:
    print("Trạng thái          : Bệnh nhân cũ (Đã có hồ sơ)")

print("="*50)
print(" Vui lòng cầm phiếu này và di chuyển đến Phòng khám số 1.")
print("="*50)

print("\n[SYSTEM LOG] - KIỂM TRA KIỂU DỮ LIỆU ĐÃ CHUẨN HÓA:")
print("-" * 50)
print(f"Biến patient_name     : Giá trị = {patient_name:<15} | Kiểu = {type(patient_name)}")
print(f"Biến patient_age      : Giá trị = {patient_age:<15} | Kiểu = {type(patient_age)}")
print(f"Biến body_temperature : Giá trị = {body_temperature:<15} | Kiểu = {type(body_temperature)}")
print(f"Biến heart_rate       : Giá trị = {heart_rate:<15} | Kiểu = {type(heart_rate)}")
print(f"Biến is_first_visit   : Giá trị = {str(is_first_visit):<15} | Kiểu = {type(is_first_visit)}")
print("-" * 50)