branchs = int(input("Nhập số lượng chi nhánh: "))
for branch in range(branchs):
    print(f"Chi nhánh {branch}:")

    for i in range(2):
        students = int(input(f"Nhập số học sinh đi học của lớp {i+1}: "))

        while True:
            if students < 0: 
                students = int(input("Số học viên không hợp lệ. Vui lòng nhập lại. "))
            else:
                break
        if students == 0: 
            print("lớp vắng toàn bộ, bỏ qua đánh giá trạng thái")
            continue
        elif students < 20:
            print(f"chi nhánh {branch} - Lớp {i+1}: Lớp cần được nhắc nhở theo dõi")
        else:
            print(f"chi nhánh {branch} - Lớp {i+1}: Lớp ổn định")

