parking_lot = []
current_id = 1

MOTORBIKE_RATE = 5000
CAR_RATE = 10000

while True:
    print("""
=================================================
            HE THONG QUAN LY BAI XE
=================================================
1. Check-in xe vao bai
2. Check-out xe ra bai
3. Hien thi danh sach xe dang do
4. Tim kiem bien so
5. Thoat chuong trinh
=================================================
""")

    choice = input("Nhap lua chon cua ban (1-5): ").strip()

    if not choice.isdigit() or int(choice) not in range(1, 6):
        print("[Loi]: Lua chon khong hop le. Vui long nhap tu 1-5!")
        continue

    match int(choice):

        case 1:
            print("\n===== DANG KY XE VAO BAI =====")

            while True:
                plate = input("Nhap bien so: ").strip().upper()

                if plate == "":
                    print("[Loi]: Bien so khong duoc de trong!")
                    continue

                duplicate = False

                for vehicle in parking_lot:
                    if vehicle["plate"] == plate:
                        duplicate = True
                        break

                if duplicate:
                    print("[Loi]: Xe voi bien so nay da ton tai trong bai!")
                else:
                    break

            while True:
                vehicle_type = input(
                    "Nhap loai xe (1-Xe may, 2-O to): "
                ).strip()

                if not vehicle_type.isdigit():
                    print(
                        "[Loi]: Loai xe khong hop le (1: Xe may, 2: O to)!"
                    )
                    continue

                vehicle_type = int(vehicle_type)

                if vehicle_type in [1, 2]:
                    break

                print(
                    "[Loi]: Loai xe khong hop le (1: Xe may, 2: O to)!"
                )

            while True:
                entry_time = input(
                    "Nhap gio vao (0-24): "
                ).strip()

                if not entry_time.isdigit():
                    print("[Loi]: Vui long nhap gio hop le!")
                    continue

                entry_time = int(entry_time)

                if 0 <= entry_time <= 24:
                    break

                print("[Loi]: Gio vao phai trong khoang 0-24!")

            vehicle = {
                "id": current_id,
                "plate": plate,
                "type": vehicle_type,
                "entry_time": entry_time,
                "status": "parked"
            }

            parking_lot.append(vehicle)

            print(
                f"[Thanh cong]: Xe {plate} da duoc dang ky vao bai."
            )

            current_id += 1

        case 2:
            print("\n===== XE RA BAI =====")

            if len(parking_lot) == 0:
                print("[Thong bao]: Bai xe dang trong!")
                continue

            plate = input(
                "Nhap bien so can check-out: "
            ).strip().upper()

            found_vehicle = None

            for vehicle in parking_lot:
                if vehicle["plate"] == plate:
                    found_vehicle = vehicle
                    break

            if found_vehicle is None:
                print(
                    f"[Loi]: Khong tim thay bien so {plate} trong he thong!"
                )
                continue

            while True:
                exit_time = input(
                    "Nhap gio ra (0-24): "
                ).strip()

                if not exit_time.isdigit():
                    print("[Loi]: Vui long nhap gio hop le!")
                    continue

                exit_time = int(exit_time)

                if not (0 <= exit_time <= 24):
                    print("[Loi]: Gio ra phai trong khoang 0-24!")
                    continue

                if exit_time < found_vehicle["entry_time"]:
                    print(
                        "[Loi]: Gio ra phai sau hoac bang gio vao!"
                    )
                    continue

                break

            duration = exit_time - found_vehicle["entry_time"]

            if found_vehicle["type"] == 1:
                fee = duration * MOTORBIKE_RATE
                vehicle_name = "Xe may"
            else:
                fee = duration * CAR_RATE
                vehicle_name = "O to"

            print("\n========== HOA DON ==========")
            print(f"Bien so    : {plate}")
            print(f"Loai xe    : {vehicle_name}")
            print(f"Gio vao    : {found_vehicle['entry_time']}")
            print(f"Gio ra     : {exit_time}")
            print(f"So gio gui : {duration}")
            print(f"Thanh tien : {fee:,} VND")

            parking_lot.remove(found_vehicle)

            print(
                f"[Thanh cong]: Xe {plate} da roi khoi bai xe."
            )

        case 3:
            print("\n===== DANH SACH XE DANG DO =====")

            if len(parking_lot) == 0:
                print("[Thong bao]: Khong co xe nao trong bai.")
                continue

            print(
                f"{'ID':<5}{'BIEN SO':<15}{'LOAI XE':<12}{'GIO VAO':<10}"
            )
            print("-" * 42)

            for vehicle in parking_lot:

                if vehicle["type"] == 1:
                    vehicle_name = "Xe may"
                else:
                    vehicle_name = "O to"

                print(
                    f"{vehicle['id']:<5}"
                    f"{vehicle['plate']:<15}"
                    f"{vehicle_name:<12}"
                    f"{vehicle['entry_time']:<10}"
                )

        case 4:
            print("\n===== TIM KIEM XE =====")

            if len(parking_lot) == 0:
                print("[Thong bao]: Bai xe dang trong!")
                continue

            plate = input(
                "Nhap bien so can tim: "
            ).strip().upper()

            found = False

            for vehicle in parking_lot:

                if vehicle["plate"] == plate:

                    if vehicle["type"] == 1:
                        vehicle_name = "Xe may"
                    else:
                        vehicle_name = "O to"

                    print("\n===== THONG TIN XE =====")
                    print(f"ID        : {vehicle['id']}")
                    print(f"Bien so   : {vehicle['plate']}")
                    print(f"Loai xe   : {vehicle_name}")
                    print(f"Gio vao   : {vehicle['entry_time']}")
                    print(f"Trang thai: {vehicle['status']}")

                    found = True
                    break

            if not found:
                print(
                    f"[Loi]: Khong tim thay bien so {plate} trong he thong!"
                )

        case 5:
            print("Cam on da su dung he thong!")
            break