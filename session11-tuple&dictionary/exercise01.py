"""
1. total_points là biến Global hay Local? Vì sao?
total_points là biến toàn cục (Global Variable) vì được khai báo bên ngoài hàm.
2. Giải thích lỗi UnboundLocalError
Python thấy dòng:
total_points = total_points + points_earned
nên tự coi total_points trong hàm là biến cục bộ (local). Nhưng biến này chưa được gán giá trị trước khi sử dụng nên phát sinh lỗi:
UnboundLocalError: local variable 'total_points' referenced before assignment
3. Nếu chỉ đọc (print) total_points trong hàm thì có lỗi không?
Không.
Ví dụ:
def show_points():
    print(total_points)
Hàm chỉ đọc nên Python sẽ sử dụng biến global.
4. Cách sửa 1
Dùng từ khóa:
global total_points
để sử dụng và thay đổi biến toàn cục trong hàm.
5. Cách sửa 2 (Khuyến nghị)
Dùng lệnh:
return
để trả về tổng điểm mới.
Ví dụ:
def add_reward_points(current_points, points_earned):
    return current_points + points_earned
"""


total_points = 100

def add_reward_points(current_points, points_earned):
    print(f"Da cong them {points_earned} diem.")
    return current_points + points_earned

total_points = add_reward_points(total_points, 50)

print(f"Tong diem hien tai cua khach hang: {total_points}")