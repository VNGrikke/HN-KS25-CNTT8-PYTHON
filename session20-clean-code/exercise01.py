from typing import List, Tuple, Optional


PlayerRaw = Tuple[str, str, str, str]


def safe_int(value: str) -> Optional[int]:
    """
    Chuyển string → int an toàn.
    Trả về None nếu dữ liệu không hợp lệ.
    """
    try:
        return int(value)
    except ValueError:
        return None


def calculate_kda(kills: int, deaths: int, assists: int) -> float:
    """
    Tính KDA an toàn.
    Xử lý deaths = 0 bằng quy ước game:
    - nếu deaths = 0 → coi như 1 để tránh crash
    """
    safe_deaths = deaths if deaths != 0 else 1
    return (kills + assists) / safe_deaths


def process_player(player: PlayerRaw) -> Optional[tuple]:
    """
    Xử lý 1 player:
    - Validate input
    - Trả về (name, kda) hoặc None nếu lỗi
    """
    name, k, d, a = player

    kills = safe_int(k)
    deaths = safe_int(d)
    assists = safe_int(a)

    if kills is None or deaths is None or assists is None:
        print(f"[WARN] Dữ liệu lỗi của {name}: {player}")
        return None

    kda = calculate_kda(kills, deaths, assists)
    return name, kda


def tinh_toan(data: List[PlayerRaw]) -> None:
    print("--- BẢNG XẾP HẠNG KDA ---")

    results = []

    for player in data:
        result = process_player(player)
        if result:
            results.append(result)

    for name, kda in results:
        print(f"Tuyển thủ {name} có chỉ số KDA là: {kda:.2f}")