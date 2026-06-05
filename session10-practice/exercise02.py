list_music = ["shape of you", "perfect"]

while True:
    print("""
============== MENU QUAN LY DANH SACH PHAT ==============
1. Them bai hat vao danh sach phat
2. Xem danh sach phat
3. Xoa bai hat khoi danh sach
4. Sap xep va trich xuat danh sach
5. Thoat chuong trinh
=========================================================
""")

    choice = input("Nhap lua chon cua ban: ").strip()

    if not choice.isdigit():
        print("Lua chon khong hop le, vui long nhap so nguyen")
        continue

    choice = int(choice)

    match choice:

        case 1:
            print("""
----- THEM BAI HAT -----
1. Them vao cuoi danh sach
2. Chen vao vi tri cu the
""")

            choice2 = input("Nhap lua chon cua ban: ").strip()

            if not choice2.isdigit():
                print("Lua chon khong hop le, vui long nhap so nguyen")
                continue

            choice2 = int(choice2)

            match choice2:

                case 1:
                    song = input("Nhap ten bai hat: ").strip()

                    list_music.append(song)

                    print("Them bai hat thanh cong!")
                    print(f"So luong bai hat hien tai: {len(list_music)}")

                case 2:
                    song = input("Nhap ten bai hat: ").strip()

                    pos = input("Nhap vi tri muon chen: ").strip()

                    if not pos.isdigit():
                        print("Vi tri khong hop le.")
                        continue

                    pos = int(pos)
                    index = pos - 1

                    if index < 0 or index > len(list_music):
                        print("Vi tri khong hop le.")
                    else:
                        list_music.insert(index, song)

                        print("Them bai hat thanh cong!")
                        print(f"So luong bai hat hien tai: {len(list_music)}")

                case _:
                    print("Lua chon khong hop le.")

        case 2:

            if len(list_music) == 0:
                print("Danh sach phat hien dang trong!")
                continue

            print("\n===== DANH SACH PHAT =====")

            for i in range(len(list_music)):
                print(f"{i + 1}. {list_music[i]}")

        case 3:

            if len(list_music) == 0:
                print("Danh sach phat hien dang trong!")
                continue

            print("""
----- XOA BAI HAT -----
1. Xoa theo vi tri
2. Xoa theo ten
""")

            choice2 = input("Nhap lua chon cua ban: ").strip()

            if not choice2.isdigit():
                print("Lua chon khong hop le, vui long nhap so nguyen")
                continue

            choice2 = int(choice2)

            match choice2:

                case 1:
                    pos = input("Nhap vi tri muon xoa: ").strip()

                    if not pos.isdigit():
                        print("Vi tri khong hop le.")
                        continue

                    pos = int(pos)
                    index = pos - 1

                    if index < 0 or index >= len(list_music):
                        print("Vi tri khong hop le.")
                    else:
                        removed_song = list_music.pop(index)
                        print(f"Da xoa bai hat '{removed_song}' khoi danh sach.")

                case 2:
                    song = input("Nhap ten bai hat can xoa: ").strip()

                    if song in list_music:
                        list_music.remove(song)
                        print(f"Da xoa bai hat '{song}' khoi danh sach.")
                    else:
                        print("Khong tim thay bai hat trong danh sach phat.")

                case _:
                    print("Lua chon khong hop le.")

        case 4:

            if len(list_music) == 0:
                print("Danh sach phat hien dang trong!")
                continue

            print("""
----- SAP XEP VA TRICH XUAT -----
1. Sap xep theo bang chu cai (A-Z)
2. Hien thi 3 bai hat dau tien
""")

            choice2 = input("Nhap lua chon cua ban: ").strip()

            if not choice2.isdigit():
                print("Lua chon khong hop le, vui long nhap so nguyen")
                continue

            choice2 = int(choice2)

            match choice2:

                case 1:
                    list_music.sort()

                    print("Danh sach sau khi sap xep:")

                    for i in range(len(list_music)):
                        print(f"{i + 1}. {list_music[i]}")

                case 2:
                    print("3 bai hat dau tien:")

                    for i in range(min(3, len(list_music))):
                        print(f"{i + 1}. {list_music[i]}")

                case _:
                    print("Lua chon khong hop le.")

        case 5:
            print("Cam on ban da su dung dich vu. Tam biet!")
            break

        case _:
            print("Lua chon khong hop le.")