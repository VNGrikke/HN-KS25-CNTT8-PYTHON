from datetime import (
    datetime,
    timedelta
)


def calculate_eta(flight_list):

    print(
        "----- TÍNH TOÁN THỜI GIAN "
        "HẠ CÁNH (ETA) -----"
    )

    flight_id = input(
        "Nhập mã chuyến bay cần tính: "
    ).strip().upper()

    for flight in flight_list:

        if flight["flight_id"] == flight_id:

            departure_time = (
                datetime.strptime(
                    flight["depart_time"],
                    "%Y-%m-%d %H:%M:%S"
                )
            )

            eta = (
                departure_time
                + timedelta(
                    minutes=flight[
                        "duration_min"
                    ]
                )
            )

            print(
                f"-> Chuyến bay "
                f"{flight_id} "
                f"cất cánh lúc: "
                f"{flight['depart_time']}"
            )

            print(
                f"-> Thời gian hạ cánh "
                f"dự kiến (ETA): "
                f"{eta.strftime('%Y-%m-%d %H:%M:%S')}"
            )

            return

    print(
        "Không tìm thấy chuyến bay!"
    )