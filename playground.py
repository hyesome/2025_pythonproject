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


while True:
    user_input = input("값을 입력하세요 : ")

    if user_input.lower() == "z":
        break

    # test

    print_times_table(int(user_input))