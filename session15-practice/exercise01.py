inventory_stock = 100
total_revenue = 0.0


def display_menu():
    print("""
========== TECHSTORE MANAGEMENT SYSTEM ==========
1. Nhập thêm hàng vào kho
2. Bán hàng (Tính toán hóa đơn)
3. Xem báo cáo tổng quan
4. Thoát chương trình
=================================================
""")


def add_stock(amount):
    global inventory_stock

    if amount <= 0:
        print("Dữ liệu nhập vào phải lớn hơn 0.")
        return

    inventory_stock += amount

    print(f"Đã nhập thành công {amount} sản phẩm.")
    print(f"Tồn kho hiện tại: {inventory_stock}")


def process_sale(quantity):
    if quantity <= 0:
        print("Dữ liệu nhập vào phải lớn hơn 0.")
        return False

    if quantity > inventory_stock:
        print(
            f"Lỗi: Không đủ hàng trong kho. "
            f"Tồn kho hiện tại chỉ còn {inventory_stock}."
        )
        return False

    return True


def calculate_final_price(quantity, price):
    subtotal = quantity * price

    discount = 0
    if subtotal >= 1000:
        discount = subtotal * 0.1

    after_discount = subtotal - discount
    vat = after_discount * 0.08
    final_total = after_discount + vat

    return subtotal, discount, vat, final_total


def complete_sale(quantity, final_total):
    global inventory_stock
    global total_revenue

    inventory_stock -= quantity
    total_revenue += final_total


def print_report():
    """
    Hiển thị báo cáo tồn kho và doanh thu hiện tại.
    """
    print("\n--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue:.2f}")

def main():
    while True:
        display_menu()

        choice = input("Chọn chức năng (1-4): ").strip()

        match choice:
            case "1":
                print("--- NHẬP HÀNG ---")

                amount = input("Nhập số lượng sản phẩm muốn thêm: ").strip()

                if not amount.isdigit():
                    print("Dữ liệu nhập vào phải là số.")
                    continue

                add_stock(int(amount))

            case "2":
                print("--- BÁN HÀNG ---")

                quantity = input("Nhập số lượng mua: ").strip()
                price = input("Nhập đơn giá ($): ").strip()

                if not quantity.isdigit() or not price.isdigit():
                    print("Dữ liệu nhập vào phải là số.")
                    continue

                quantity = int(quantity)
                price = float(price)

                if quantity <= 0 or price <= 0:
                    print("Dữ liệu nhập vào phải lớn hơn 0.")
                    continue

                if not process_sale(quantity):
                    continue

                subtotal, discount, vat, final_total = (
                    calculate_final_price(quantity, price)
                )

                complete_sale(quantity, final_total)

                print("-> Hóa đơn chi tiết:")
                print(f"Số lượng: {quantity} | Đơn giá: ${price}")
                print(f"Tạm tính: ${subtotal:.2f}")
                print(f"Giảm giá (10%): ${discount:.2f}")
                print(f"Thuế VAT (8%): ${vat:.2f}")
                print(f"Tổng thanh toán: ${final_total:.2f}")
                print("Đã bán thành công!")

            case "3":
                print_report()

            case "4":
                print("Đang lưu dữ liệu...")
                print("Thoát chương trình!")
                break

            case _:
                print("Lựa chọn không hợp lệ.")

main()