import random

upgrade_rates = [{"up": 70, "keep": 30, "down": 0, "break": 0},
                 {"up": 60, "keep": 85, "down": 95, "break": 100},
                 {"up": 50, "keep": 30, "down": 15, "break": 5},
                 {"up": 45, "keep": 30, "down": 20, "break": 5},
                 {"up": 40, "keep": 30, "down": 20, "break": 10},
                 {"up": 35, "keep": 30, "down": 25, "break": 10},
                 {"up": 30, "keep": 30, "down": 30, "break": 10},
                 {"up": 25, "keep": 30, "down": 30, "break": 15},
                 {"up": 20, "keep": 30, "down": 30, "break": 20},
                 ]

def upgrade_weapon(current_lv):
    ran_num = random.randint(0, 100)
    rate = upgrade_rates[current_lv]

    if current_lv == 10:
        print("더 이상 업그레이드가 불가합니다")
        return current_lv

    if 0 < ran_num <= rate['up']:
        print("up")
        return current_lv + 1

    if ran_num <= rate['up'] + rate['keep']:
        print("keep")
        return current_lv

    if ran_num <= rate['up'] + rate['keep'] + rate['down']:
        print("down")
        return current_lv - 1

    print('break')
    return 0

print("게임에 오신 것을 환영합니다!")

choice = 1

while True:
    weapon_level = 0

    print("1. 무기 강화")
    print("0. 종료하기")

    choice = input("숫자를 입력하세요 (0을 입력하면 종료): ")

    if int(choice) == 0:
        break
    if int(choice) == 1:
        weapon_level = upgrade_weapon(weapon_level)


if choice == 0:
    print("게임을 종료합니다")