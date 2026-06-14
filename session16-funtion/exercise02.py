"""
1. Tại sao append("Oresol") làm thay đổi cả yesterday_prescription?
Vì:
new_prescription = old_prescription
không tạo list mới mà chỉ tạo thêm một biến cùng trỏ đến một vùng nhớ. Do đó thay đổi new_prescription cũng làm thay đổi old_prescription.

2. Cách tạo bản sao độc lập của List
Ít nhất 2 cách:
new_prescription = old_prescription.copy()
new_prescription = old_prescription[:]
Ngoài ra:
new_prescription = list(old_prescription)

3. Tại sao replace() không có tác dụng?
Vì String là immutable, replace() tạo ra chuỗi mới nhưng không tự cập nhật giá trị trong list nếu không gán lại.

4. Sửa như thế nào để cập nhật tên thuốc?
Phải gán kết quả trở lại vị trí index 0:
new_prescription[0] = new_prescription[0].replace(
    "Panadol",
    "Paracetamol"
)
Hoặc ngắn gọn:
new_prescription[0] = "Paracetamol"
"""

yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

def update_prescription(old_prescription):
    new_prescription = old_prescription.copy()

    new_prescription[0] = new_prescription[0].replace(
        "Panadol",
        "Paracetamol"
    )

    new_prescription.append("Oresol")

    return new_prescription

today_prescription = update_prescription(yesterday_prescription)

print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)