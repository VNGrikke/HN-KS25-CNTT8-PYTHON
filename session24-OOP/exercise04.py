import re

class MenuItem:
    # Class Attribute: Phụ phí dịch vụ dùng chung cho toàn hệ thống
    service_charge = 0.0

    def __init__(self, item_id, item_name, base_price):
        self.item_id = item_id.upper()
        self.item_name = item_name.title()
        self.__base_price = base_price  # Private attribute (Name mangling)
        self.__is_available = True      # Private attribute: Mặc định là đang bán

    # Đóng gói: Getter cho is_available
    @property
    def is_available(self):
        return self.__is_available

    # Đóng gói: Getter cho base_price
    @property
    def base_price(self):
        return self.__base_price

    # Đóng gói: Setter cho base_price để kiểm duyệt dữ liệu đầu vào
    @base_price.setter
    def base_price(self, new_price):
        if new_price > 0:
            self.__base_price = new_price
            print("Cập nhật giá gốc thành công!")
        else:
            print("Giá đồ uống phải lớn hơn 0!\nGiá cũ được giữ nguyên.")

    # Instance Method: Đảo ngược trạng thái bán
    def toggle_availability(self):
        self.__is_available = not self.__is_available
        status = "ĐANG BÁN" if self.__is_available else "HẾT HÀNG"
        print(f">> Đã cập nhật {self.item_name} thành {status}!")

    # Getter giả lập để tính giá niêm yết tự động
    @property
    def listing_price(self):
        return int(self.__base_price + (self.__base_price * MenuItem.service_charge))

    # Static Method: Kiểm tra tính hợp lệ của mã món (Không phụ thuộc vào object)
    @staticmethod
    def is_valid_item_id(item_code):
        # Yêu cầu: 2 chữ cái in hoa theo sau là 2 chữ số (VD: CF01)
        pattern = r"^[A-Z]{2}\d{2}$"
        return bool(re.match(pattern, item_code))

    # Class Method: Cập nhật tỷ lệ phụ phí hệ thống
    @classmethod
    def update_service_charge(cls, new_rate):
        if new_rate >= 0:
            cls.service_charge = new_rate
            print("Cập nhật phụ phí dịch vụ thành công!")
        else:
            print("Phụ phí không hợp lệ!")


# ==========================================
# LUỒNG XỬ LÝ CHÍNH (MAIN FLOW)
# ==========================================

def get_item_by_id(menu_list, item_id):
    """Hàm hỗ trợ tìm kiếm đồ uống theo mã món"""
    for item in menu_list:
        if item.item_id == item_id.upper():
            return item
    return None

def main():
    # Mock data ban đầu
    menu_db = [
        MenuItem("CF01", "Cà Phê Đen", 30000),
        MenuItem("CF02", "Bạc Xỉu", 45000),
        MenuItem("TE01", "Trà Đào Cam Sả", 50000)
    ]

    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE =====")
        print("1. Xem thực đơn & Giá niêm yết")
        print("2. Thêm món mới vào menu")
        print("3. Cập nhật trạng thái (Hết hàng/Còn hàng)")
        print("4. Điều chỉnh giá gốc của món")
        print("5. Cập nhật phụ phí dịch vụ toàn hệ thống")
        print("6. Thoát chương trình")
        print("======================================================")
        
        choice = input("Chọn chức năng (1-6): ")

        if choice == '1':
            print("\n--- THỰC ĐƠN RIKKEI COFFEE ---")
            if not menu_db:
                print("Thực đơn đang trống.")
            else:
                for idx, item in enumerate(menu_db, 1):
                    status_text = "Đang bán" if item.is_available else "Hết hàng"
                    print(f"{idx}. Mã: {item.item_id} | Tên: {item.item_name:<15} | Trạng thái: {status_text:<9} | Giá niêm yết: {item.listing_price:,} VNĐ")

        elif choice == '2':
            print("\n--- THÊM MÓN MỚI VÀO MENU ---")
            item_id = input("Nhập mã món: ").strip()

            if not MenuItem.is_valid_item_id(item_id):
                print("\nMã món không hợp lệ!\nMã món phải gồm 2 chữ cái in hoa và 2 chữ số. Ví dụ: CF01.")
                continue

            if get_item_by_id(menu_db, item_id):
                print("\nMã món đã tồn tại trong thực đơn!")
                continue

            item_name = input("Nhập tên món: ").strip()
            try:
                base_price = int(input("Nhập giá gốc: "))
                if base_price <= 0:
                    print("Lỗi: Giá gốc phải lớn hơn 0.")
                    continue
                
                new_item = MenuItem(item_id, item_name, base_price)
                menu_db.append(new_item)
                print("\nThêm món mới thành công!")
            except ValueError:
                print("Lỗi: Giá tiền phải là một số nguyên.")

        elif choice == '3':
            print("\n--- CẬP NHẬT TRẠNG THÁI MÓN ---")
            item_id = input("Nhập mã món cần cập nhật: ").strip()
            item = get_item_by_id(menu_db, item_id)

            if item:
                item.toggle_availability()
            else:
                print("Lỗi: Không tìm thấy món đồ uống này!")

        elif choice == '4':
            print("\n--- ĐIỀU CHỈNH GIÁ GỐC CỦA MÓN ---")
            item_id = input("Nhập mã món cần đổi giá: ").strip()
            item = get_item_by_id(menu_db, item_id)

            if item:
                try:
                    new_price = int(input("Nhập giá tiền mới: "))
                    # Gọi tới setter để tự động check giá trị hợp lệ
                    item.base_price = new_price
                except ValueError:
                    print("Lỗi: Giá tiền phải là một số nguyên.")
            else:
                print("Lỗi: Không tìm thấy món đồ uống này!")

        elif choice == '5':
            print("\n--- CẬP NHẬT PHỤ PHÍ DỊCH VỤ TOÀN HỆ THỐNG ---")
            print(f"Phụ phí hiện tại: {int(MenuItem.service_charge * 100)}%")
            try:
                new_rate = float(input("Nhập phụ phí mới. Ví dụ 0.1 tương ứng 10%: "))
                MenuItem.update_service_charge(new_rate)
            except ValueError:
                print("Lỗi: Phụ phí phải là dạng số thực (VD: 0.1).")

        elif choice == '6':
            print("\nCảm ơn bạn đã sử dụng hệ thống Rikkei Coffee!")
            break

        else:
            print("\nLựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()