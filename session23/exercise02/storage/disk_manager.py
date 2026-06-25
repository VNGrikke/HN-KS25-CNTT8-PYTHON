import math


def calculate_disk_blocks(
    size_bytes,
    block_size=4096
):
    """
    Tính số block bộ nhớ chiếm dụng.
    """

    return math.ceil(
        size_bytes / block_size
    )