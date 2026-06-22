from typing import List, Tuple, Optional, Union


PlayerRaw = Tuple


def safe_int(value: Union[str, int]) -> Optional[int]:
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def calculate_bonus(matches: int, mmr: int) -> float:
    return (matches * 10) + (mmr * 0.5)


def parse_player(record: Tuple) -> Optional[tuple]:
    """
    Chuẩn hóa dữ liệu input:
    (name, matches, mmr)
    """
    if len(record) < 3:
        print(f"[WARN] Thiếu dữ liệu: {record}")
        return None

    name, matches, mmr = record

    matches = safe_int(matches)
    mmr = safe_int(mmr)

    if matches is None or mmr is None:
        print(f"[WARN] Sai định dạng dữ liệu: {record}")
        return None

    return name, matches, mmr


def process(data: List[Tuple]) -> None:
    print("--- BẢNG TÍNH THƯỞNG RP ---")

    results = []

    for record in data:
        parsed = parse_player(record)
        if not parsed:
            continue

        name, matches, mmr = parsed
        bonus = calculate_bonus(matches, mmr)
        results.append((name, bonus))

    for name, bonus in results:
        print(f"Tuyển thủ {name} nhận được {bonus:.0f} RP")