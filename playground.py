import random
import time

def print_times_table(number: int):
    print(number, "*", 1, "=", number*1)
    print(number, "*", 2, "=", number*2)
    print(number, "*", 3, "=", number*3)
    print(number, "*", 4, "=", number*4)
    print(number, "*", 5, "=", number*5)
    print(number, "*", 6, "=", number*6)
    print(number, "*", 7, "=", number*7)
    print(number, "*", 8, "=", number*8)
    print(number, "*", 9, "=", number*9)

def example_function(input_arg: int) -> int:
    print("숫자 형태를 입력받아서 다른 숫자형태를 반환")
    return input_arg + 5

def updown():
    # random.randrange ( n, m )   n <= result < m
    print("WELCOME TO UP DOWN")
    result = random.randrange(1, 100)
    print("랜덤값이 생성되었습니다. (1이상 100미만)")
    is_success = False
    count = 5

    while count > 0:
        user_input = int(input("값을 입력하세요:"))
        count = count - 1
        if user_input > result:
            print("DOWN! 남은횟수 :", count)
        elif user_input < result:
            print("UP! 남은횟수 :", count)
        else:
            is_success = True
            break

    if is_success:
        print("정답입니다! 짝짝짝!")
    else:
        print("실패하셨습니다 ㅠㅠ 정답은 ", result)


def quiz():
    print("WELCOME TO QUIZ!")


def stop_watch():
    print("WELCOME TO UP STOPWATCH")
    seconds = random.randrange(1, 6)
    start = time.time()
    print("게임 시작! ", seconds, "초 후 c를 누르세요!")
    input("")
    end = time.time()
    if seconds - 0.3 <= end-start <= seconds + 0.3:
        print("성공! 소요시간:", end-start)
    else:
        print("실패! 소요시간:", end-start)


while True:
    print('''
    ================메뉴================
    A. Up & Down 게임
    B. 영어 낱말 맞추기
    C. Stop watch 게임
    Z. 프로그램 종료
    ====================================
    ''')
    user_input = input("값을 입력하세요 : ")

    if user_input.lower() == "a":
        updown()
    elif user_input.lower() == "b":
        quiz()
    elif user_input.lower() == "c":
        stop_watch()
    elif user_input.lower() == "z":
        break
