import random
name = input("nhap ten benh nhan")
sex = input("nhap gioi tinh")
year_of_birth = int(input("nhap nam sinh"))
phone = input("nhap sdt ")
mail = input("nhap email ")
symptoms = input("nhap trieu chung ban dau")
cost = float(input("nhap tri phi"))

patient_code = random.randint(100, 999)



print("------the banh nhan------\n")
print("Ma BN: BN", year_of_birth + patient_code)
print("ten: ", name)
print("gioi tinh: ", sex)
print("dien thoai: ", phone)
print("email: ", mail)
print("trieu chung: ", symptoms)
print("tri phi: ", cost)
