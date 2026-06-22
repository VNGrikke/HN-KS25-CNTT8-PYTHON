import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)

def show_devices(devices_list):
    logger.debug(f"Hiển thị {len(devices_list)} thiết bị")

    if not devices_list:
        print("Hệ thống hiện chưa có thiết bị giám sát nào!")
        return

    print("\n" + "=" * 100)
    print(
        f"{'MÃ THIẾT BỊ':<15} |"
        f"{'VỊ TRÍ PHÂN XƯỞNG':<25} |"
        f"{'CHỈ SỐ CŨ':>15} |"
        f"{'CHỈ SỐ MỚI':>15} |"
        f"{'TRẠNG THÁI':>15}"
    )
    print("=" * 100)

    for device in devices_list:
        print(
            f"{device['id']:<15} |"
            f"{device['location']:<25} |"
            f"{device['old_index']:>15.2f} |"
            f"{device['new_index']:>15.2f} |"
            f"{device['status']:>15} |"
        )

def find_device_by_id(devices_list, device_id):
    for device in devices_list:
        if device["id"] == device_id:
            return device
    return None

def update_indices(devices_list):
    logger.debug("Bắt đầu cập nhật chỉ số điện")
    if not devices_list:
        print("Hệ thống hiện chưa có thiết bị giám sát nào!")
        return
    device_id = input("Nhập mã thiết bị cần cập nhật chỉ số: ").strip().upper()
    if not device_id:
        print("[Lỗi] (ERR-E01): Mã thiết bị này không tồn tại trong danh sách hệ thống!")
        return
    device = find_device_by_id(devices_list, device_id)
    if device is None:
        print("[Lỗi] (ERR-E01): Mã thiết bị này không tồn tại trong danh sách hệ thống!")
        return
    while True:
        try:
            old_index = float(input("Nhập chỉ số cũ: "))
            if old_index < 0:
                raise ValueError
            break
        except ValueError:
            logger.error("Sai định dạng chỉ số cũ")
            print("[Lỗi] (ERR-E03): Định dạng không hợp lệ! Chỉ số điện phải là số lớn hơn hoặc bằng 0!")
    while True:
        try:
            new_index = float(input("Nhập chỉ số mới: "))
            if new_index < 0:
                raise ValueError
            if new_index < old_index:
                print("[Lỗi] (ERR-E02): Số liệu lỗi! Chỉ số mới không được nhỏ hơn chỉ số cũ!")
                continue
            break
        except ValueError:
            logger.error("Sai định dạng chỉ số mới")
            print("[Lỗi] (ERR-E03): Định dạng không hợp lệ! Chỉ số điện phải là số lớn hơn hoặc bằng 0!")
    device["old_index"] = old_index
    device["new_index"] = new_index
    logger.info(f"[Thành công]: Đã check-in số liệu cho thiết bị {device_id}")
    print(f"[Thành công]: Đã cập nhật chỉ số cho thiết bị {device_id}")

def trigger_overload_alert(devices_list):
    logger.debug("Kiểm tra trạng thái quá tải")
    if not devices_list:
        print("Hệ thống hiện chưa có thiết bị giám sát nào!")
        return
    device_id = input("Nhập mã thiết bị cần kích hoạt cảnh báo: ").strip().upper()
    device = find_device_by_id(devices_list, device_id)
    if device is None:
        print("[Lỗi] (ERR-E01): Mã thiết bị này không tồn tại trong danh sách hệ thống!")
        return
    consumption = device["new_index"] - device["old_index"]
    if device["status"] == "Overload":
        print("[Lỗi] (ERR-E04): Thao tác bị hủy! Thiết bị này đã được kích hoạt trạng thái OVERLOAD từ trước!")
        return
    if consumption > 5000:
        device["status"] = "Overload"
        logger.warning(f"[Cảnh báo]: Thiết bị {device_id} đã vượt ngưỡng tiêu thụ an toàn!")
        print(f"[Thành công]: Thiết bị {device_id} đã được chuyển sang trạng thái OVERLOAD")
    else:
        print("Thiết bị chưa vượt ngưỡng tiêu thụ 5000 kWh.")

def calculate_energy_financials(devices_list):
    logger.debug(f"Đang tính toán chi phí năng lượng cho {len(devices_list)} thiết bị")
    if not devices_list:
        return (0.0, 0.0, 0.0)
    total_kwh = 0
    for device in devices_list:
        total_kwh += (device["new_index"] - device["old_index"])
    unit_price = 3000
    total_cost = total_kwh * unit_price
    discount_percent = 0.0
    if total_kwh >= 50000:
        discount_percent = 3.0
    final_cost = total_cost * (1 - discount_percent / 100)
    return (
        total_kwh,
        discount_percent,
        final_cost
    )

def main():
    devices_list = [
        {
            "id": "M01",
            "location": "Mechanical Shop A",
            "old_index": 10000,
            "new_index": 16000,
            "status": "Normal"
        },
        {
            "id": "M02",
            "location": "Assembly Shop",
            "old_index": 8000,
            "new_index": 12000,
            "status": "Normal"
        },
        {
            "id": "M03",
            "location": "Warehouse",
            "old_index": 5000,
            "new_index": 7000,
            "status": "Normal"
        }
    ]

    while True:
        print("\n===== SMART ENERGY MONITOR =====")
        print("1. Xem danh sách thiết bị")
        print("2. Cập nhật chỉ số điện")
        print("3. Kích hoạt cảnh báo quá tải")
        print("4. Tính tổng điện & chi phí")
        print("5. Thoát")

        try:
            choice = int(input("Nhập lựa chọn: "))

            if choice == 1:
                show_devices(devices_list)

            elif choice == 2:
                update_indices(devices_list)

            elif choice == 3:
                trigger_overload_alert(devices_list)

            elif choice == 4:
                total_kwh, discount, total_money = (
                    calculate_energy_financials(devices_list)
                )

                print("\n===== BÁO CÁO NĂNG LƯỢNG =====")
                print(f"Tổng điện tiêu thụ: {total_kwh:,.2f} kWh")
                print(f"Chiết khấu: {discount}%")
                print(f"Tổng tiền sau chiết khấu: {total_money:,.0f} VND")

            elif choice == 5:
                print("Kết thúc chương trình!")
                break

            else:
                print("[Lỗi] (ERR-E05): Lựa chọn sai! Vui lòng nhập đúng số thứ tự chức năng từ 1 đến 5!")

        except ValueError:
            logger.error("Lỗi nhập menu")
            print("[Lỗi] (ERR-E05): Lựa chọn sai! Vui lòng nhập đúng số thứ tự chức năng từ 1 đến 5!")

if __name__ == "__main__":
    main()