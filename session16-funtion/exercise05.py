er_patients = [
    "ER01|Nguyen Van Quan|HR:115|TEMP:39.5",
    "ER02|Tran Thi Binh|HR:80|TEMP:37.0",
    "ER03|Le Van Cuong|HR:130|TEMP:38.2"
]


def find_patient_index(patients, er_id):
    er_id = er_id.strip().upper()

    for index, patient in enumerate(patients):
        if patient.startswith(er_id + "|"):
            return index

    return -1


def display_dashboard(patients):
    if len(patients) == 0:
        print("Khoa cấp cứu hiện đang trống.")
        return

    print("\n--- BẢNG THEO DÕI CA CẤP CỨU ------------------------------------")

    for index, patient in enumerate(patients, start=1):
        er_id, name, hr, temp = patient.split("|")

        print(
            f"{index}. [{er_id}] {name} | "
            f"Nhịp tim: {hr[3:]} bpm | "
            f"Nhiệt độ: {temp[5:]} °C"
        )

    print("-----------------------------------------------------------------")


def admit_patient(patients):
    print("\n--- TIẾP NHẬN CA CẤP CỨU MỚI ---")

    er_id = input("Nhập mã ER: ").strip().upper()

    if len(er_id) == 0:
        print("Mã ER không được để trống!")
        return

    if find_patient_index(patients, er_id) != -1:
        print("Mã ca cấp cứu đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip().title()

    if len(name) == 0:
        print("Tên bệnh nhân không được để trống!")
        return

    while True:
        hr = input("Nhập nhịp tim HR: ").strip()

        if hr.isdigit() and int(hr) > 0:
            break

        print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")

    while True:
        temp = input("Nhập nhiệt độ TEMP: ").strip()

        if temp.replace(".", "", 1).isdigit() and float(temp) >= 36.5:
            break

        print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")

    record = f"{er_id}|{name}|HR:{hr}|TEMP:{temp}"

    patients.append(record)

    print("\nTiếp nhận ca cấp cứu mới thành công!")
    print("Dữ liệu được lưu là:")
    print(record)


def update_vitals(patients):
    print("\n--- CẬP NHẬT LẠI SINH HIỆU ---")

    er_id = input("Nhập mã ER cần cập nhật: ").strip().upper()

    patient_index = find_patient_index(patients, er_id)

    if patient_index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return

    data = patients[patient_index].split("|")

    print(f"Tìm thấy bệnh nhân: {data[1]}")
    print(f"Sinh hiệu hiện tại: {data[2]} | {data[3]}")

    print("""
Bạn muốn cập nhật:
1. Nhịp tim HR
2. Nhiệt độ TEMP
""")

    choice = input("Chọn loại sinh hiệu: ").strip()

    if choice == "1":
        new_hr = input("Nhập nhịp tim mới: ").strip()

        if not (new_hr.isdigit() and int(new_hr) > 0):
            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn 0!")
            return

        data[2] = f"HR:{new_hr}"
        patients[patient_index] = "|".join(data)

        print("Cập nhật nhịp tim thành công!")

    elif choice == "2":
        new_temp = input("Nhập nhiệt độ mới: ").strip()

        if not (
            new_temp.replace(".", "", 1).isdigit()
            and float(new_temp) >= 36.5
        ):
            print("Sinh hiệu không hợp lệ, vui lòng nhập số lớn hơn hoặc bằng 36.5!")
            return

        data[3] = f"TEMP:{new_temp}"
        patients[patient_index] = "|".join(data)

        print("Cập nhật nhiệt độ thành công!")

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn 1 hoặc 2!")


def trigger_red_alert(patients):
    if len(patients) == 0:
        print("Khoa cấp cứu hiện đang trống.")
        return

    critical_patients = []

    for patient in patients:
        er_id, name, hr, temp = patient.split("|")

        hr_value = int(hr.split(":")[1])
        temp_value = float(temp.split(":")[1])

        if hr_value > 100 or temp_value >= 39.0:
            critical_patients.append(
                (er_id, name, hr_value, temp_value)
            )

    if len(critical_patients) == 0:
        print("--- KIỂM TRA BÁO ĐỘNG ĐỎ ---")
        print("Không có bệnh nhân nguy kịch tại thời điểm hiện tại.")
        return

    print("\n!!! BÁO ĐỘNG ĐỎ - DANH SÁCH BỆNH NHÂN NGUY KỊCH !!!")

    for index, patient in enumerate(critical_patients, start=1):
        print(
            f"{index}. [{patient[0]}] {patient[1]} | "
            f"HR: {patient[2]} bpm | "
            f"TEMP: {patient[3]} °C | "
            f"CẦN XỬ LÝ KHẨN CẤP"
        )

    print("-----------------------------------------------------")
    print(f"Tổng số ca nguy kịch: {len(critical_patients)}")


def discharge_patient(patients):
    print("\n--- XUẤT VIỆN / CHUYỂN KHOA ---")

    er_id = input("Nhập mã ER cần xóa khỏi hệ thống: ").strip().upper()

    if len(er_id) == 0:
        print("Mã ER không được để trống!")
        return

    patient_index = find_patient_index(patients, er_id)

    if patient_index == -1:
        print("Không tìm thấy bệnh nhân. Vui lòng kiểm tra lại mã ER!")
        return

    patient_name = patients[patient_index].split("|")[1]

    patients.pop(patient_index)

    print(f"Đã chuyển khoa thành công cho bệnh nhân {patient_name}!")


while True:
    print("""
===== HỆ THỐNG QUẢN LÝ CẤP CỨU RIKKEI ER =====
1. Bảng theo dõi bệnh nhân
2. Tiếp nhận ca cấp cứu mới
3. Cập nhật lại sinh hiệu
4. BÁO ĐỘNG ĐỎ - Lọc bệnh nhân nguy kịch
5. Xuất viện / Chuyển khoa
6. Thoát chương trình
=================================================
""")

    choice = input("Chọn chức năng (1-6): ").strip()

    match choice:
        case "1":
            display_dashboard(er_patients)

        case "2":
            admit_patient(er_patients)

        case "3":
            update_vitals(er_patients)

        case "4":
            trigger_red_alert(er_patients)

        case "5":
            discharge_patient(er_patients)

        case "6":
            print("Kết thúc ca trực. Tạm biệt!")
            break

        case _:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 6!")