from core.logistics import (
    display_flights_and_logistics
)

from core.manager import (
    add_new_flight
)

from utils.time_helper import (
    calculate_eta
)

from utils.file_helper import (
    create_log_folder
)


flights = [
    {
        "flight_id": "RA001",
        "passengers": 154,
        "depart_time":
        "2026-06-15 08:00:00",
        "duration_min": 120
    },
    {
        "flight_id": "RA002",
        "passengers": 85,
        "depart_time":
        "2026-06-15 13:30:00",
        "duration_min": 45
    }
]


def display_menu():

    print()
    print(
        "===== HỆ THỐNG ĐIỀU HÀNH "
        "BAY RIKKEI AVIATION ====="
    )

    print(
        "1. Hiển thị lịch trình "
        "và Thống kê hậu cần"
    )

    print(
        "2. Tiếp nhận chuyến bay mới"
    )

    print(
        "3. Tính thời gian "
        "hạ cánh dự kiến (ETA)"
    )

    print(
        "4. Khởi tạo thư mục "
        "lưu trữ log hệ thống"
    )

    print(
        "5. Thoát chương trình"
    )

    print(
        "======================================="
    )


while True:

    display_menu()

    try:

        choice = int(
            input(
                "Nhập lựa chọn của bạn: "
            )
        )

        if choice == 1:

            display_flights_and_logistics(
                flights
            )

        elif choice == 2:

            add_new_flight(
                flights
            )

        elif choice == 3:

            calculate_eta(
                flights
            )

        elif choice == 4:

            create_log_folder()

        elif choice == 5:

            print(
                "Cảm ơn kỹ sư đã sử dụng hệ thống!"
            )
            break

        else:

            print(
                "Vui lòng nhập từ 1-5."
            )

    except ValueError:

        print(
            "Lỗi! Vui lòng nhập số từ 1-5."
        )