from datetime import datetime

patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]


def display_records(records):
    print("\n--- DANH SÁCH BỆNH NHÂN --------------------------------------------------")

    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    for index, record in enumerate(records, start=1):
        patient_id, name, birth_year, diagnosis = record.split("-")

        print(
            f"{index}. [{patient_id}] "
            f"{name:<20} | "
            f"Năm sinh: {birth_year} | "
            f"Chẩn đoán: {diagnosis}"
        )

    print("--------------------------------------------------------------------------")


def patient_exists(records, patient_id):
    for record in records:
        if record.startswith(patient_id + "-"):
            return True
    return False


def add_patient(records):
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if patient_exists(records, patient_id):
        print("\nMã bệnh nhân đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip()
    name = name.replace("-", " ").title()

    current_year = datetime.now().year

    while True:
        birth_year = input("Nhập năm sinh: ").strip()

        if (
            birth_year.isdigit()
            and 1900 <= int(birth_year) <= current_year
        ):
            break

        print("\nNăm sinh không hợp lệ, vui lòng nhập lại!")

    diagnosis = input("Nhập chẩn đoán: ").strip()
    diagnosis = diagnosis.replace("-", " ").capitalize()

    new_record = "-".join([
        patient_id,
        name,
        birth_year,
        diagnosis
    ])

    records.append(new_record)

    print("\nThêm hồ sơ bệnh nhân thành công!")
    print("Dữ liệu được lưu là:")
    print(new_record)


def update_diagnosis(records):
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")

    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()

    found_index = -1

    for index, record in enumerate(records):
        if record.startswith(patient_id + "-"):
            found_index = index
            break

    if found_index == -1:
        print(f"\nKhông tìm thấy bệnh nhân mang mã {patient_id}!")
        return

    data = records[found_index].split("-")

    print(f"\nTìm thấy bệnh nhân: {data[1]}")
    print(f"Chẩn đoán hiện tại: {data[3]}")

    new_diagnosis = input("Nhập chẩn đoán mới: ").strip()
    new_diagnosis = new_diagnosis.replace("-", " ").capitalize()

    data[3] = new_diagnosis

    records[found_index] = "-".join(data)

    print("\nCập nhật chẩn đoán thành công!")
    print("Dữ liệu mới được lưu:")
    print(records[found_index])


def generate_age_report(records):
    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")

    current_year = datetime.now().year

    children = 0
    adults = 0
    elderly = 0

    for record in records:
        data = record.split("-")
        birth_year = int(data[2])

        age = current_year - birth_year

        if age < 16:
            children += 1
        elif age <= 60:
            adults += 1
        else:
            elderly += 1

    print(f"Trẻ em: {children} bệnh nhân")
    print(f"Trưởng thành: {adults} bệnh nhân")
    print(f"Người cao tuổi: {elderly} bệnh nhân")
    print("--------------------------------------")


while True:
    print("""
===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====
1. Xem danh sách hồ sơ bệnh án
2. Thêm hồ sơ bệnh nhân mới
3. Cập nhật chẩn đoán theo Mã BN
4. Báo cáo phân loại theo độ tuổi
5. Thoát chương trình
==================================================
""")

    choice = input("Chọn chức năng (1-5): ").strip()

    match choice:
        case "1":
            display_records(patient_records)

        case "2":
            add_patient(patient_records)

        case "3":
            update_diagnosis(patient_records)

        case "4":
            generate_age_report(patient_records)

        case "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập từ 1-5!")