n_str = input("Nhập số lượng phiếu đăng ký: ")

if not (n_str.isdigit() or (n_str.startswith('-') and n_str[1:].isdigit())):
    print("Số lượng phiếu đăng ký không hợp lệ")

n = int(n_str)

if n <= 0:
    print("Số lượng phiếu đăng ký không hợp lệ")

for i in range(n):
    raw_data = input(f"\nNhập chuỗi đăng ký thứ {i+1}: ")
    
    parts = raw_data.split('|')
    
    if len(parts) != 4:
        print("Dữ liệu đăng ký không hợp lệ. Bỏ qua phiếu này")
        continue
        
    raw_name = parts[0].strip()
    raw_course = parts[1].strip()
    raw_id = parts[2].strip()
    raw_email = parts[3].strip()
    
    email = raw_email.lower()
    if '@' not in email:
        print("Email không hợp lệ. Bỏ qua phiếu này")
        continue
        
    student_id = raw_id.upper()
    if len(student_id) < 5:
        print("Mã học viên không hợp lệ. Bỏ qua phiếu này")
        continue
        
    name = " ".join(word.capitalize() for word in raw_name.split())
    
    course = " ".join(word.capitalize() for word in raw_course.split())
    
    course_code_part = "-".join(word.upper() for word in raw_course.split())
    confirm_code = f"{student_id}_{course_code_part}"
    
    print("===== PHIẾU ĐĂNG KÝ ĐÃ CHUẨN HÓA =====")
    print(f"Học viên: {name}")
    print(f"Khóa học: {course}")
    print(f"Mã học viên: {student_id}")
    print(f"Email: {email}")
    print(f"Mã xác nhận: {confirm_code}")