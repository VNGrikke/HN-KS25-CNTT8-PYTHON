from base_vehicle import BaseVehicle
from robo_bus import RoboBus

current_vehicle = None

while True:

    print("\n===== HE THONG QUAN LY PHUONG TIEN =====")
    print("1. Khoi tao xe")
    print("2. Gia lap chay")
    print("3. Thoat")

    choice = input("Nhap lua chon: ")

    if choice == "1":

        while True:
            plate = input("Nhap bien so: ")

            if BaseVehicle.validate_license_plate(plate):

                current_vehicle = RoboBus(plate)
                print("Tao xe thanh cong!")
                print("\nDanh sach MRO:")

                for cls in RoboBus.__mro__:
                    print(cls.__name__)
                break

            print("Bien so khong hop le!")

    elif choice == "2":

        if current_vehicle is None:
            print("Chua co xe!")
            continue

        try:
            distance = float(input("Nhap so km vua di: "))
            current_vehicle.drive(distance)

            print("Tong so km:", current_vehicle.odometer)
            print("Hieu suat:", current_vehicle.calculate_efficiency(), 2)

        except ValueError as e:
            print("Loi:", e)

    elif choice == "3":
        print("Tam biet!")
        break

    else:
        print("Lua chon khong hop le!")