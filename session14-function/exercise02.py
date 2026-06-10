"""
1. total_points là biến Global hay Local?
total_points là biến toàn cục vì được khai báo bên ngoài hàm.

2. Vì sao xảy ra lỗi UnboundLocalError?
Trong hàm:
total_points = total_points + points_earned
Python thấy có phép gán nên coi total_points là biến cục bộ (Local). Nhưng biến này chưa có giá trị nên báo lỗi:
UnboundLocalError: local variable 'total_points' referenced before assignment

3. Nếu chỉ print(total_points) trong hàm thì có lỗi không?
Không.
Vì chỉ đọc giá trị nên Python sẽ sử dụng biến global bên ngoài.

4. Cách sửa 1
Dùng từ khóa:
global total_points
để sử dụng và thay đổi biến toàn cục trong hàm.

5. Cách sửa 2 
Dùng lệnh:
return
để trả về tổng điểm mới.
Ví dụ:

def add_reward_points(current_points, points_earned):
    return current_points + points_earned
"""


# Tong diem hien tai cua khach hang
total_points = 100

# Ham cong diem thuong
def add_reward_points(current_points, points_earned):
    print("Da cong them", points_earned, "diem.")
    return current_points + points_earned

# Khach mua hang duoc thuong 50 diem
total_points = add_reward_points(total_points, 50)

# In ket qua
print("Tong diem hien tai cua khach hang:", total_points)