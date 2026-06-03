transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "

transaction = transaction.split("|")

student_name = transaction[0].strip().title()

subject_code = transaction[1].strip()

cost = int(transaction[2].strip())

status = transaction[3].strip().upper()

print(f"Tên học viên: {student_name}")
print(f"Mã khóa học: {subject_code}")
print(f"so tien: {cost:,} VND")
print(f"Trang thai {status}")