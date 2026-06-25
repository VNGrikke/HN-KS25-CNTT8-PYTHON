from datetime import datetime


def parse_and_inspect_date(date_str):
    """
    Chuyển đổi chuỗi ngày tháng.
    Trả về None nếu dữ liệu không hợp lệ.
    """

    try:
        return datetime.strptime(
            date_str,
            "%Y-%m-%d"
        )

    except ValueError:
        print(
            f"[WARNING] Định dạng ngày upload "
            f"'{date_str}' không tồn tại"
        )
        return None