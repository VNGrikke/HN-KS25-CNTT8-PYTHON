total_bill_input = input("Nhập tổng số tiền hóa đơn: ").strip()
people_input = input("Nhập số người tham gia: ").strip()

if not total_bill_input.isdigit() or not people_input.isdigit():
    print("Dữ liệu không hợp lệ. Vui lòng nhập số nguyên.")
else:
    total_bill = int(total_bill_input)
    people = int(people_input)

    if people == 0:
        print("Số người phải lớn hơn 0.")
    else:
        money_per_person = total_bill / people
        remaining_money = total_bill % people
        
        service_fee = total_bill * 10 / 100
        total_after_fee = total_bill + service_fee

        print(f"Tổng hóa đơn: {total_bill}")
        print(f"Số người: {people}")
        print(f"Tiền mỗi người: {money_per_person}")
        print(f"Tiền dư: {remaining_money}")
        print(f"Tổng sau phí phục vụ: {total_after_fee}")