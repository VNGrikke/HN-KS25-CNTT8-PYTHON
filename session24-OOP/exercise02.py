# Hệ thống Thẻ thành viên Rikkei Coffee - Đã được Refactor
class MemberCard:
    def __init__(self, customer_name, points=0):
        self.customer_name = customer_name
        self.__points = 0      # Khởi tạo giá trị mặc định an toàn
        self.points = points   # Gọi đến setter để kiểm duyệt giá trị khởi tạo ban đầu

    # Đóng gói (Encapsulation): Getter cho thuộc tính points
    @property
    def points(self):
        return self.__points

    # Đóng gói (Encapsulation): Setter kiểm duyệt dữ liệu đầu vào
    @points.setter
    def points(self, value):
        # Kiểm tra kiểu dữ liệu là số nguyên (int) và không được nhỏ hơn 0
        if isinstance(value, int) and value >= 0:
            self.__points = value
        else:
            print("Lỗi: Dữ liệu điểm không hợp lệ! Vui lòng nhập số nguyên dương.")

    def add_points(self, amount):
        # Việc += sẽ tự động gọi đến cả getter và setter của thuộc tính 'points'
        # Nên logic kiểm tra vẫn được đảm bảo
        self.points += amount

    # Chuyển thành Static Method vì không phụ thuộc vào trạng thái của object (self)
    @staticmethod
    def is_eligible_for_voucher(bill_amount):
        return bill_amount >= 200000


# --- KỊCH BẢN THAO TÁC CỦA THU NGÂN (TESTING) ---

print("--- 1. Tạo thẻ và kiểm tra dữ liệu hợp lệ ---")
card1 = MemberCard("Le Van C", 100)
print(f"Khách hàng: {card1.customer_name} | Điểm ban đầu: {card1.points}\n")

print("--- 2. Thu ngân gõ nhầm điểm (Âm hoặc Chuỗi) ---")
# Thử gán điểm âm
card1.points = -50  
# Thử gán chuỗi
card1.points = "một trăm" 
print(f"Điểm sau khi gán sai vẫn được bảo toàn: {card1.points}\n")

print("--- 3. Khách hàng tích thêm điểm hợp lệ ---")
card1.add_points(50)
print(f"Điểm sau khi được cộng thêm 50: {card1.points}\n")

print("--- 4. Kiểm tra Voucher cho khách vãng lai (Gọi trực tiếp từ Class) ---")
# Không cần khởi tạo object, gọi thẳng từ Class MemberCard
bill_amount = 250000
result = MemberCard.is_eligible_for_voucher(bill_amount)

print(f"Hóa đơn {bill_amount:,} VNĐ có được tặng Voucher không? {result}")