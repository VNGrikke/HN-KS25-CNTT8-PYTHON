class_count_input = input("Nhập vào số lượng lớp học: ").strip()

if class_count_input.isdigit() and class_count_input != "":
    class_count = int(class_count_input)
    
    if class_count > 0: 
        
        for classroom in range(1, class_count ):
            result = ""

            rows = int(input(f"Nhập vào số hàng của lớp thứ {classroom}: "))
            
            if rows <= 0 or rows > 10:

                print("Số lượng phòng học không hợp lệ")
                rows = 0
                continue
            
            else:
                seat_per_row = int(input(f"Nhập vào số ghế/hàng của lớp thứ {classroom}: "))

                for row in range(rows):
                    for seat in range(seat_per_row):
                        result += "*"
                    result += "\n"

                if seat_per_row <=0 or seat_per_row > 10:
                    print("Số lượng phòng học không hợp lệ")
                    continue
            print("\n", result)


    else: 
        print("Số lượng phòng học không hợp lệ")
else:
    print("Vui lòng nhập số nguyên dương hợp lệ")







                
                 
