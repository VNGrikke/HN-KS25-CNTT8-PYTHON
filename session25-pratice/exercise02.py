class NetflixAccount:
    # 1. Class Attributes (Chính sách chung của toàn hệ thống)
    platform_name = "Netflix"
    max_profiles = 5

    # 2. Instance Attributes & Initialization
    def __init__(self, email):
        self.email = email
        self.__password = None  # Khởi tạo rỗng, sẽ gán qua setter để kiểm duyệt
        self.__plan = "Basic"
        self.profiles = []

    # 3. Tính Đóng Gói (Encapsulation)
    
    # Getter cho password: Che giấu mật khẩu thật
    @property
    def password(self):
        return "********"

    # Setter cho password: Bẫy 2 - Kiểm tra độ dài mật khẩu
    @password.setter
    def password(self, value):
        if len(value) < 6:
            raise ValueError("Password is too short")
        self.__password = value

    # Getter cho plan: Read-only, ngăn chặn sửa gói cước bên ngoài method hợp lệ
    @property
    def plan(self):
        return self.__plan

    # 4. Class Method & Static Method
    
    @staticmethod
    def validate_email(email):
        # Bẫy 1: Yêu cầu chứa '@' và '.'
        return "@" in email and "." in email

    @classmethod
    def update_max_profiles(cls, new_limit):
        if new_limit > 0:
            cls.max_profiles = new_limit
            print(f"Đã cập nhật giới hạn Profile toàn hệ thống thành {cls.max_profiles}")
        else:
            print("Lỗi: Giới hạn Profile phải lớn hơn 0.")

    # 5. Instance Methods
    
    def add_profile(self, profile_name):
        # Bẫy 3: Kiểm tra vượt quá giới hạn Profile
        if len(self.profiles) >= self.max_profiles:
            print("Đã đạt giới hạn số lượng Profile trên tài khoản này.")
        else:
            self.profiles.append(profile_name.strip())
            print(f"Đã thêm Profile: '{profile_name}' thành công!")

    def upgrade_plan(self, new_plan):
        valid_plans = ["Basic", "Standard", "Premium"]
        if new_plan in valid_plans:
            self.__plan = new_plan
            print(f"Nâng cấp thành công! Gói cước hiện tại: {self.__plan}")
        else:
            print(f"Gói cước không hợp lệ. Vui lòng chọn: {', '.join(valid_plans)}")

    def display_info(self):
        print(f"\n--- THÔNG TIN TÀI KHOẢN {self.platform_name.upper()} ---")
        print(f"Email: {self.email}")
        print(f"Mật khẩu: {self.password}")  # Gọi getter sẽ in ra ********
        print(f"Gói cước hiện tại: {self.plan}")
        profiles_str = ", ".join(self.profiles) if self.profiles else "Chưa có"
        print(f"Danh sách Profiles ({len(self.profiles)}/{self.max_profiles}): {profiles_str}")


# ==========================================
# HỆ THỐNG MENU CLI (NGHIỆP VỤ)
# ==========================================

def main():
    current_account = None

    while True:
        print("\n===== NETFLIX ACCOUNT MANAGER =====")
        print("1. Đăng ký tài khoản mới")
        print("2. Xem thông tin tài khoản")
        print("3. Thêm người xem")
        print("4. Nâng cấp gói cước")
        print("5. Cập nhật chính sách Netflix (Admin Only)")
        print("6. Thoát chương trình")
        print("===================================")
        
        choice = input("Chọn chức năng (1-6): ").strip()

        if choice == '1':
            print("\n--- ĐĂNG KÝ TÀI KHOẢN MỚI ---")
            email = input("Nhập Email: ").strip()
            
            # Bẫy 1: Validate email
            if not NetflixAccount.validate_email(email):
                print("Email không hợp lệ, vui lòng chứa ký tự '@' và '.'")
                continue

            temp_account = NetflixAccount(email)
            
            # Bẫy 2: Cài đặt mật khẩu với try...except
            password = input("Nhập mật khẩu (>= 6 ký tự): ")
            try:
                temp_account.password = password
                current_account = temp_account
                print("Đăng ký tài khoản thành công!")
            except ValueError as e:
                print(f"Lỗi: {e}. Đăng ký thất bại!")

        elif choice in ['2', '3', '4']:
            # Bẫy 4: Thao tác khi chưa có tài khoản
            if current_account is None:
                print("Vui lòng đăng ký tài khoản trước (Chức năng 1).")
                continue

            if choice == '2':
                current_account.display_info()

            elif choice == '3':
                print("\n--- THÊM NGƯỜI XEM (PROFILE) ---")
                profile_name = input("Nhập tên Profile mới: ").strip()
                if profile_name:
                    current_account.add_profile(profile_name)
                else:
                    print("Tên Profile không được để trống.")

            elif choice == '4':
                print("\n--- NÂNG CẤP GÓI CƯỚC ---")
                print("Các gói khả dụng: Basic, Standard, Premium")
                new_plan = input("Nhập tên gói cước muốn nâng cấp: ").strip().capitalize()
                current_account.upgrade_plan(new_plan)

        elif choice == '5':
            print("\n--- CẬP NHẬT CHÍNH SÁCH NETFLIX ---")
            try:
                new_limit = int(input("Nhập giới hạn số lượng Profile tối đa mới: "))
                NetflixAccount.update_max_profiles(new_limit)
            except ValueError:
                print("Lỗi: Vui lòng nhập một số nguyên hợp lệ.")

        elif choice == '6':
            print("Cảm ơn bạn đã sử dụng hệ thống Netflix!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 6.")

# Kích hoạt chương trình
if __name__ == "__main__":
    main()