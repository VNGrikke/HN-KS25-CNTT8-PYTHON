products = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]


def display_products(products_list):
    print("\n--- DANH SÁCH SẢN PHẨM ---")

    if len(products_list) == 0:
        print("Cửa hàng hiện chưa có sản phẩm nào!")
        return

    print(f"{'ID':<10} | {'Tên sản phẩm':<30} | {'Giá bán':>15}")
    print("-" * 60)

    for product in products_list:
        print(f"{product['id']:<10} | {product['name']:<30} | {product['price']:>15,} VNĐ")

    print("-" * 60)


def is_not_empty(value):
    return value.strip() != ""


def check_duplication(value, key):
    for item in products:
        if item[key].upper() == value.upper():
            return True
    return False


def validate_price(price):
    return price > 0


def input_price():
    while True:
        try:
            price = int(input("Nhập giá bán: "))

            if validate_price(price):
                return price

            print("Giá sản phẩm phải lớn hơn 0!")

        except ValueError:
            print("Vui lòng nhập số nguyên hợp lệ!")


def add_product():
    while True:
        id_product = input("Nhập mã sản phẩm (ID): ").strip().upper()

        if not is_not_empty(id_product):
            print("Mã sản phẩm không được để trống!")
            continue

        if check_duplication(id_product, "id"):
            print("Mã sản phẩm đã tồn tại!")
            continue

        break

    while True:
        name_product = input("Nhập tên sản phẩm: ").strip()

        if not is_not_empty(name_product):
            print("Tên sản phẩm không được để trống!")
            continue

        break

    price = input_price()

    new_product = {
        "id": id_product,
        "name": name_product,
        "price": price
    }

    products.append(new_product)

    print("Thêm sản phẩm thành công!")


def update_price():
    id_product = input("Nhập mã sản phẩm cần cập nhật giá: ").strip().upper()

    for product in products:
        if product["id"] == id_product:
            print(f"Sản phẩm: {product['name']}")
            print(f"Giá hiện tại: {product['price']:,} VNĐ")

            new_price = input_price()

            product["price"] = new_price

            print("Cập nhật giá thành công!")
            return

    print(f"Không tìm thấy sản phẩm có mã {id_product}!")


def display_menu():
    print("""
=================================
      QUẢN LÝ CỬA HÀNG
=================================
1. Xem danh sách sản phẩm
2. Thêm mới sản phẩm
3. Cập nhật giá sản phẩm
4. Thoát chương trình
=================================
""")


def main():
    while True:
        display_menu()

        choice = input("Nhập vào lựa chọn của bạn: ").strip()

        match choice:
            case "1":
                display_products(products)

            case "2":
                add_product()

            case "3":
                update_price()

            case "4":
                print("Thoát chương trình.")
                break

            case _:
                print("Vui lòng nhập lựa chọn từ 1 đến 4!")


main()