from data.students import (
    student_records
)

import utils.string_utils as string_utils

from utils.random_utils import (
    generate_assignment_code
)

from reports.report_generator import (
    display_student_scores,
    export_learning_report
)


def main():

    while True:

        print(
            "\n===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY ====="
            "1. Xem danh sách sinh viên và điểm trung bình"
            "2. Chuẩn hóa tên sinh viên"
            "3. Sinh mã bài tập ngẫu nhiên"
            "4. Xuất báo cáo học tập"
            "5. Thoát chương trình"
            "=" * 52
        )

        try:

            choice = int(
                input(
                    "Chọn chức năng (1-5): "
                )
            )

            if choice == 1:

                display_student_scores(
                    student_records
                )

            elif choice == 2:

                string_utils.normalize_student_names(
                    student_records
                )

            elif choice == 3:

                print(
                    "--- SINH MÃ BÀI TẬP ---"
                )

                print(
                    "Mã bài tập của bạn là:",
                    generate_assignment_code()
                )

            elif choice == 4:

                export_learning_report(
                    student_records
                )

            elif choice == 5:

                print(
                    "Cảm ơn bạn đã sử dụng hệ thống!"
                )
                break

            else:

                print(
                    "Chức năng không hợp lệ. "
                    "Vui lòng chọn từ 1 đến 5."
                )

        except ValueError:

            print(
                "Chức năng không hợp lệ. "
                "Vui lòng chọn từ 1 đến 5."
            )


if __name__ == "__main__":
    main()