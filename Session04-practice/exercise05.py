total_revenue = 0
total_invoices = 0
large_invoices_count = 0

while True:
    invoice_input = input("\nNhập giá trị hóa đơn (hoặc gõ K/k để xuất báo cáo ngay): ").strip()
    
    if invoice_input.lower() == 'k':
        break
        
    if invoice_input.isdigit() and invoice_input != "":
        invoice_value = int(invoice_input)
        
        if invoice_value > 0:
            total_revenue += invoice_value
            total_invoices += 1
            
            if invoice_value >= 1000000:
                large_invoices_count += 1
                
            continue_choice = input("Đã ghi nhận! Tiếp tục nhập hóa đơn khác? (Gõ K/k để dừng, phím bất kỳ để tiếp tục): ").strip()
            if continue_choice.lower() == 'k':
                break
        else:
            print("Giá trị hóa đơn phải lớn hơn 0.")
    else:
        print("Dữ liệu không hợp lệ. Vui lòng nhập số nguyên dương!")

print("\nBÁO CÁO TỔNG KẾT CUỐI NGÀY")

if total_invoices == 0:
    print("Hôm nay chưa có hóa đơn nào được ghi nhận.")
else:
    large_invoice_percentage = (large_invoices_count / total_invoices) * 100
    
    print(f"Tổng số lượng hóa đơn  : {total_invoices}")
    print(f"Tổng doanh thu         : {total_revenue:,.0f} VND")
    print(f"Số lượng hóa đơn lớn   : {large_invoices_count} (>= 1.000.000 VND)")
    print(f"Tỷ lệ hóa đơn lớn      : {large_invoice_percentage:.2f}%")
