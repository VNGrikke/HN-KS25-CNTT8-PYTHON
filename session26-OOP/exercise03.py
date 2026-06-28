from abc import ABC, abstractmethod


class Champion(ABC):
    def __init__(self, champion_id, name, base_hp, base_atk):
        self.champion_id = champion_id
        self.name = name

        # Edge Case: HP hoặc ATK <= 0 thì mặc định =100
        self.base_hp = base_hp if base_hp > 0 else 100
        self.base_atk = base_atk if base_atk > 0 else 100

    @abstractmethod
    def calculate_skill_damage(self):
        pass

    def get_combat_power(self):
        return self.base_hp + self.calculate_skill_damage() * 1.5

    # Nạp chồng toán tử +
    def __add__(self, other):
        if isinstance(other, Champion):
            return self.get_combat_power() + other.get_combat_power()

        elif isinstance(other, (int, float)):
            return self.get_combat_power() + other

        return NotImplemented

    # hỗ trợ sum()
    def __radd__(self, other):
        if other == 0:
            return self.get_combat_power()
        return other + self.get_combat_power()

    # Nạp chồng >
    def __gt__(self, other):
        return self.get_combat_power() > other.get_combat_power()

    def __str__(self):
        return (
            f"{self.champion_id} | {self.name} | "
            f"{self.get_combat_power():.0f}"
        )


class Warrior(Champion):

    def __init__(self,
                 champion_id,
                 name,
                 base_hp,
                 base_atk,
                 shield_bonus):

        super().__init__(
            champion_id,
            name,
            base_hp,
            base_atk
        )

        self.shield_bonus = shield_bonus

    def calculate_skill_damage(self):
        return self.base_atk * 2 + self.shield_bonus


class Mage(Champion):

    def __init__(self,
                 champion_id,
                 name,
                 base_hp,
                 base_atk,
                 ability_power):

        super().__init__(
            champion_id,
            name,
            base_hp,
            base_atk
        )

        self.ability_power = ability_power

    def calculate_skill_damage(self):
        return self.base_atk * self.ability_power
    
champion_pool = [

    Warrior(
        "WAR01",
        "Rikkei Knight",
        1200,
        300,
        150
    ),

    Warrior(
        "WAR02",
        "Steel Guardian",
        1500,
        250,
        200
    ),

    Mage(
        "MAG01",
        "Rikkei Wizard",
        800,
        500,
        2.0
    )

]

def find_champion(champion_id):

    for champion in champion_pool:
        if champion.champion_id == champion_id:
            return champion

    return None


def is_duplicate_id(champion_id):

    return find_champion(champion_id) is not None

# CHỨC NĂNG 1

def display_champions():

    print("\n--- DANH SÁCH QUÂN CỜ TRONG BỂ TƯỚNG ---")
    print(
        f"{'Mã':<8}"
        f"{'Tên tướng':<22}"
        f"{'Hệ':<12}"
        f"{'HP':<8}"
        f"{'ATK':<8}"
        f"{'Chỉ số riêng':<22}"
        f"{'Chiến lực'}"
    )

    print("-" * 95)
    for champion in champion_pool:

        if isinstance(champion, Warrior):
            champion_type = "Warrior"
            special = f"Armor: {champion.shield_bonus}"

        elif isinstance(champion, Mage):
            champion_type = "Mage"
            special = f"AP: {champion.ability_power}"

        else:
            champion_type = "Unknown"
            special = ""

        print(
            f"{champion.champion_id:<8}"
            f"{champion.name:<22}"
            f"{champion_type:<12}"
            f"{champion.base_hp:<8}"
            f"{champion.base_atk:<8}"
            f"{special:<22}"
            f"{champion.get_combat_power():.0f}"
        )
    print("-" * 95)


# CHỨC NĂNG 2

def add_champion():

    print("\n===== THÊM QUÂN CỜ =====")
    print("1. Warrior")
    print("2. Mage")
    choice = input("Chọn hệ: ")

    if choice not in ["1", "2"]:
        print("Lựa chọn không hợp lệ!")
        return
    
    champion_id = input("Nhập mã tướng: ").strip()

    if is_duplicate_id(champion_id):
        print("Lỗi: Mã tướng đã tồn tại!")
        return
    
    name = input("Nhập tên tướng: ")
    hp = int(input("Nhập HP: "))
    atk = int(input("Nhập ATK: "))

    if choice == "1":
        armor = int(input("Nhập Armor: "))
        champion = Warrior(
            champion_id,
            name,
            hp,
            atk,
            armor
        )

        champion_pool.append(champion)
        print("\nThêm Warrior thành công!")

    else:
        ap = float(input("Nhập Ability Power: "))
        champion = Mage(
            champion_id,
            name,
            hp,
            atk,
            ap
        )

        champion_pool.append(champion)
        print("\nThêm Mage thành công!")

    print(
        f"Mã: {champion.champion_id}"
        f" | Tên: {champion.name}"
        f" | Chiến lực: {champion.get_combat_power():.0f}"
    )


# CHỨC NĂNG 3
def compare_champions():
    print("\n===== SO SÁNH SỨC MẠNH =====")
    id1 = input("Nhập mã tướng thứ nhất: ").strip().upper()
    id2 = input("Nhập mã tướng thứ hai: ").strip().upper()
    champion1 = find_champion(id1)
    champion2 = find_champion(id2)

    if champion1 is None:
        print(f"Mã tướng {id1} không hợp lệ!")
        return

    if champion2 is None:
        print(f"Mã tướng {id2} không hợp lệ!")
        return

    print("\nThông tin:")

    print(
        f"{champion1.champion_id} - {champion1.name}"
        f" | Chiến lực: {champion1.get_combat_power():.0f}"
    )

    print(
        f"{champion2.champion_id} - {champion2.name}"
        f" | Chiến lực: {champion2.get_combat_power():.0f}"
    )

    print()
    if champion1 > champion2:
        print(f"Kết quả: {champion1.name} mạnh hơn {champion2.name}")

    elif champion2 > champion1:
        print(f"Kết quả: {champion2.name} mạnh hơn {champion1.name}")

    else:
        print("Hai quân cờ có sức mạnh ngang nhau.")


# CHỨC NĂNG 4
def calculate_team_power():
    print("\n===== TÍNH TỔNG CHIẾN LỰC =====")
    ids = input(
        "Nhập danh sách mã tướng (cách nhau bởi dấu phẩy): "
    )
    ids = ids.split(",")
    team = []
    for champion_id in ids:
        champion_id = champion_id.strip().upper()
        champion = find_champion(champion_id)

        if champion is None:
            print(f"Mã tướng [{champion_id}] không hợp lệ, bỏ qua!")
            continue
        team.append(champion)

    if len(team) == 0:
        print("Không có quân cờ hợp lệ.")
        return

    print("\n===== ĐỘI HÌNH =====")

    for index, champion in enumerate(team, start=1):
        print(
            f"{index}. "
            f"{champion.champion_id}"
            f" - "
            f"{champion.name}"
            f" | Chiến lực: "
            f"{champion.get_combat_power():.0f}"
        )

    total_power = sum(team)
    print("-" * 40)
    print(f"Tổng chiến lực đội hình: {total_power:.0f}")


# ==========================
# MENU
# ==========================

def menu():
    while True:
        print("\n")
        print("=" * 50)
        print("      RIKKEI RPG - AUTO BATTLER MANAGER")
        print("=" * 50)
        print("1. Hiển thị bể tướng")
        print("2. Thêm quân cờ mới")
        print("3. So sánh 2 quân cờ")
        print("4. Tính tổng chiến lực đội hình")
        print("5. Thoát")
        print("=" * 50)

        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            display_champions()

        elif choice == "2":
            try:
                add_champion()
            except ValueError:
                print("Dữ liệu nhập không hợp lệ!")

        elif choice == "3":
            compare_champions()

        elif choice == "4":
            calculate_team_power()

        elif choice == "5":

            print("\nCảm ơn bạn đã sử dụng")
            print("RIKKEI RPG - AUTO BATTLER MANAGER!")
            break

        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":

    menu()