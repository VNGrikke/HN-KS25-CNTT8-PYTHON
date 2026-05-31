import random
secret_number = random.randint(1, 100)
max_attempts = 5

for attempt in range(1, max_attempts + 1):
    while True:
        guess_input = input(f"Lượt {attempt}/{max_attempts} - Nhập con số dự đoán của bạn: ").strip()
        
        if guess_input.isdigit() and guess_input != "":
            guess = int(guess_input)
            break
        else:
            print("Vui lòng nhập một số nguyên dương hợp lệ!")

    if guess == secret_number:
        print("\nBạn đã đoán chính xác mã số may mắn là", secret_number)
        break
    elif guess < secret_number:
        print("Mã số may mắn LỚN HƠN số bạn vừa nhập\n")
    else:
        print("Mã số may mắn NHỎ HƠN số bạn vừa nhập\n")
else:
    print("Rất tiếc, bạn đã sử dụng hết cả 5 lượt đoán.")
    print(f"Mã số may mắn của chương trình hôm nay là: {secret_number}")