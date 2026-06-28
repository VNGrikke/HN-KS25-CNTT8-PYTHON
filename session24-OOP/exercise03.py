import re

class MemberCard:
    # Class Attribute: Tỷ giá quy đổi chung của hệ thống
    point_value_vnd = 1000

    def __init__(self, card_id, name, points=0):
        self.card_id = card_id
        self.name = name.title()  # Tự động viết hoa chữ cái đầu
        self.__points = points
        # Cập nhật hạng thẻ lúc khởi tạo dựa vào số điểm truyền vào (nếu có)
        self.__tier = "VIP" if self.__points >= 100 else "Standard"

    # Encapsulation: Getter cho points (Không có setter)
    @property
    def points(self):
        return self.__points

    # Encapsulation: Getter cho tier (Không có setter)
    @property
    def tier(self):
        return self.__tier

    # Static Method: Kiểm tra định dạng mã thẻ trước khi khởi tạo
    @staticmethod
    def is_valid_card_id(card_id):
        # Regex: Bắt đầu bằng RC (chữ hoa), theo sau là chính xác 2 chữ số (00-99)
        pattern = r"^RC\d{2}$"
        return bool(re.match(pattern, card_id))

    # Class Method: Cập nhật tỷ giá hệ thống
    @classmethod
    def update_point_value(cls, new_value):
        if new_value > 0:
            cls.point_value_vnd = new_value
            print("\nCập nhật tỷ giá thành công!")
            print(f"Tỷ giá mới: 1 điểm = {cls.point_value_vnd:,} VNĐ")
        else:
            print("\nLỗi: Tỷ giá phải lớn hơn 0.")

    # Instance Method: Khách mua hàng tích điểm
    def earn_points(self, bill_amount):
        if bill_amount < 0:
            print("Lỗi: Tổng tiền hóa đơn không hợp lệ.")
            return

        points_earned = int(bill_amount // 10000)
        self.__points += points_earned

        print(f"\nKhách hàng: {self.name}")
        print(f"Hóa đơn: {bill_amount:,} VNĐ")
        print(f"Số điểm được tích: {points_earned}")
        print(f"Tổng điểm hiện tại: {self.__points}")

        # Tự động thăng hạng
        if self.__points >= 100 and self.__tier != "VIP":
            self.__tier = "VIP"
            print("Chúc mừng! Khách hàng đã được nâng hạng lên VIP.")
        
        print(f"Hạng thẻ hiện tại: {self.__tier}")

    # Instance Method: Khách dùng điểm đổi ưu đãi
    def redeem_points(self, points_to_use):
        if points_to_use <= 0:
            print("\nLỗi: Số điểm muốn sử dụng phải lớn hơn 0.")
            return

        if points_to_use > self.__points:
            print("\nKhông thể đổi điểm!")
            print("Số điểm muốn sử dụng vượt quá số điểm hiện có.")
            print(f"Điểm hiện tại của khách: {self.__points}")
            print("Điểm cũ được giữ nguyên:")
            print(f"Số điểm sau giao dịch: {self.__points}")
        else:
            self.__points -= points_to_use
            discount = points_to_use * MemberCard.point_value_vnd
            print(f"\nĐã trừ {points_to_use} điểm.")
            print(f"Khách hàng được giảm giá {discount:,} VNĐ vào hóa đơn!")
            print(f"Số điểm còn lại: {self.__points}")
            print(f"Hạng thẻ hiện tại: {self.__tier}")



def get_card_by_id(cards_list, card_id):
    """Hàm tiện ích giúp tìm thẻ trong Database"""
    for card in cards_list:
        if card.card_id == card_id:
            return card
    return None

def main():
    cards_database = []

    # Dữ liệu giả lập ban đầu để test
    cards_database.append(MemberCard("RC01", "Nguyen Van A", 150))
    cards_database.append(MemberCard("RC02", "Tran Thi B", 20))

    while True:
        print("\n===== HỆ THỐNG THẺ THÀNH VIÊN RIKKEI COFFEE =====")
        print("1. Xem danh sách thẻ thành viên")
        print("2. Đăng ký thẻ mới")
        print("3. Khách mua hàng (Tích điểm)")
        print("4. Khách dùng điểm (Đổi ưu đãi)")
        print("5. Cập nhật tỷ giá quy đổi điểm (Hệ thống)")
        print("6. Thoát chương trình")
        print("======================================================")
        
        choice = input("Chọn chức năng (1-6): ")

        if choice == '1':
            print("\n--- DANH SÁCH THẺ THÀNH VIÊN ---")
            if not cards_database:
                print("Hệ thống chưa có thẻ thành viên nào.")
            else:
                for card in cards_database:
                    print(f"Mã: {card.card_id} | Tên: {card.name:<15} | Điểm: {card.points:<3} | Hạng: {card.tier}")

        elif choice == '2':
            print("\n--- ĐĂNG KÝ THẺ THÀNH VIÊN MỚI ---")
            card_id = input("Nhập mã thẻ: ").strip()

            if not MemberCard.is_valid_card_id(card_id):
                print("Lỗi: Mã thẻ không hợp lệ! Vui lòng bắt đầu bằng 'RC' và 2 chữ số (VD: RC01, RC99).")
                continue

            if get_card_by_id(cards_database, card_id):
                print("Mã thẻ đã tồn tại trong hệ thống!\nVui lòng kiểm tra lại.")
                continue

            name = input("Nhập tên khách hàng: ").strip()
            new_card = MemberCard(card_id, name)
            cards_database.append(new_card)

            print("\nĐăng ký thẻ thành viên thành công!")
            print(f"Mã thẻ: {new_card.card_id}")
            print(f"Tên khách hàng: {new_card.name}")
            print(f"Điểm ban đầu: {new_card.points}")
            print(f"Hạng thẻ: {new_card.tier}")

        elif choice == '3':
            print("\n--- KHÁCH MUA HÀNG - TÍCH ĐIỂM ---")
            card_id = input("Nhập mã thẻ: ").strip()
            card = get_card_by_id(cards_database, card_id)

            if not card:
                print("Lỗi: Không tìm thấy mã thẻ trong hệ thống.")
                continue

            try:
                bill_amount = int(input("Nhập tổng tiền hóa đơn: "))
                card.earn_points(bill_amount)
            except ValueError:
                print("Lỗi: Số tiền hóa đơn phải là số nguyên.")

        elif choice == '4':
            print("\n--- KHÁCH DÙNG ĐIỂM - ĐỔI ƯU ĐÃI ---")
            print(f"(Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ)")
            card_id = input("Nhập mã thẻ: ").strip()
            card = get_card_by_id(cards_database, card_id)

            if not card:
                print("Lỗi: Không tìm thấy mã thẻ trong hệ thống.")
                continue

            try:
                points_to_use = int(input("Nhập số điểm muốn sử dụng: "))
                card.redeem_points(points_to_use)
            except ValueError:
                print("Lỗi: Số điểm phải là số nguyên.")

        elif choice == '5':
            print("\n--- CẬP NHẬT TỶ GIÁ QUY ĐỔI ĐIỂM ---")
            print(f"Tỷ giá hiện tại: 1 điểm = {MemberCard.point_value_vnd:,} VNĐ")
            try:
                new_value = int(input("Nhập tỷ giá mới cho 1 điểm: "))
                MemberCard.update_point_value(new_value)
            except ValueError:
                print("Lỗi: Tỷ giá phải là số nguyên.")

        elif choice == '6':
            print("\nCảm ơn bạn đã sử dụng hệ thống thẻ thành viên Rikkei Coffee!")
            break

        else:
            print("\nLựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 6.")

# Chạy chương trình
if __name__ == "__main__":
    main()