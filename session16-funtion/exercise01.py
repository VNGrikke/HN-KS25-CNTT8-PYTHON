"""
1. Tại sao strip() và title() không làm thay đổi raw_diagnosis?
Vì String trong Python là immutable (bất biến). Các phương thức strip() và title() tạo ra một chuỗi mới chứ không sửa trực tiếp chuỗi gốc.

2. Cần sửa cú pháp như thế nào?
Phải gán lại kết quả cho biến:
raw_diagnosis = raw_diagnosis.strip()
raw_diagnosis = raw_diagnosis.title()
Hoặc:
raw_diagnosis = raw_diagnosis.strip().title()

3. extend() hoạt động như thế nào với String?
extend() sẽ duyệt qua từng phần tử của đối tượng được truyền vào. Với String, mỗi ký tự là một phần tử nên nó thêm từng ký tự riêng lẻ vào list.
Ví dụ:
my_list.extend("ABC")
Kết quả:
['A', 'B', 'C']
Do đó xuất hiện các ký tự 'v', 'i', 'E', 'm' rời rạc trong danh sách.

4. Thay extend() bằng gì?
Dùng append() để thêm nguyên vẹn chuỗi vào list:
current_list.append(raw_diagnosis)
Kết quả:
['Sốt Xuất Huyết', 'Viem Phe Quan']
"""


patient_diagnoses = ["Sốt Xuất Huyết"]

def add_diagnosis(raw_diagnosis, current_list):
    normalized_diagnosis = raw_diagnosis.strip().title()

    current_list.append(normalized_diagnosis)

    return current_list


new_diagnosis = "  viEm phE QUan  "

updated_diagnoses = add_diagnosis(
    new_diagnosis,
    patient_diagnoses
)

print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)