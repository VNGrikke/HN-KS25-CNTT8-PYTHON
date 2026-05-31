print("--- HỆ THỐNG KHAI BÁO NHÂN SỰ MỚI ---")

while True:
    qty_input = input("Vui lòng nhập số lượng nhân sự mới trong tháng này: ").strip()
    
    if qty_input.lstrip('-').isdigit() and qty_input != "":
        qty = int(qty_input)
        
        if qty <= 0:
            print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.\n")
        else:
            print(f"[THÀNH CÔNG] Đã ghi nhận yêu cầu cấp phát tài sản cho {qty} nhân sự mới!")
            print("--- CHƯƠNG TRÌNH KẾT THÚC ---")
            break
    else:
        print("[LỖI] Số lượng không hợp lệ! Vui lòng nhập một con số lớn hơn 0.\n")