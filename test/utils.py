def get_valid_string(promt, error_message = "Khong duoc de trong"):
    while True:
        value = input(promt).strip()
        if value:
            return value
        print(f"Loi: {error_message}")


def get_valid_float(promt):
    while True:
        try:
            value = float(input(promt).strip())
            if value >= 0:
                return value
            print("Loi: Gia tri phai lon hon hoac bang khong")
        except ValueError:
            print("Loi: Vui long nhap 1 so hop le")

def get_valid_int(promt, min_val = 0, max_val = 10_000):
    while True:
        try:
            value = int(input(promt).strip())
            if min_val <= value <= max_val :
                return value
            print(f"Loi: Vui long nhap so nguyen trong khoang {min_val} - {max_val}")
        except ValueError:
            print("Loi: Vui long nhap 1 so nguyen hop le")
            
            

