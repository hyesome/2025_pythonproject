x = "안녕"       # x 에 문자열 "안녕" 값을 대입
print(x)
print(type(x))

x = 3           # x 에 정수형 3을 대입
print(x)
print(type(x))

x = 3.5         # x 에 실수형 3.5 을 대입
print(x)
print(type(x))

x = 3 + 5       # x 에 3 + 5 의 연산결과 8 을 대입
print(x)
print(type(x))

x = 3 == 5      # 3 == 5 는 거짓이므로 Boolean 값 False를 x에 대입
print(x)
print(type(x))

x = True        # x에 boolean 값 True 대입
print(x)
print(type(x))

x = [1, 2, 3, 4, 5] # list
print(x)
print(x[0])  #index : 몇번째 있는가
print(x[3])
print(type(x))

x = {'a':100, 'b':200}  #dictionary   key:value
print(x)
print(x['a'])
print(type(x))

# 정오표
example = {
    'python': [True, False, True, True, True, True, True, False, False, True],
    'java': [True, False, False, True, True, True, False, False, False, True],
    'git': [False, False, True, True, False, True, True, True, True, True],
}

print(example)
print(example['python'])
print(example['python'][1])

# 문제 답안
python_description = [
    {
        'answer': 1,
        'description': 'python에 대한 설명은 1번이 맞습니다.'
    },
    {
        'answer': "list",
        'description': 'python의 열거형 데이터 타입은 list입니다.'
    },
    {
        'answer': True,
        'description': 'python의 LIST 안에 Dictionary를 사용할 수 있습니다.'
    },
]

print(python_description[0])

list_example = [1, "+", 2, "=", 1+2]

print(list_example)
print(list_example[1])

# 변할 수 있는 데이터는 key값으로 사용 불가능
dict_example = {
    1: 'value 1',
    'a': 'value a',
    # x: 'asdf'         # 변수는 사용 불가능
    # [1,2] : 'asdf'    # 리스트도 사용 불가능
}

print(dict_example)