def add(num1, num2):
    result = num1 + num2

    return result


ret = add(9, 15)
print(ret)  # 24

# 람다를 이용한 간단한 함수 정의
add = lambda num1, num2: num1 + num2
print(add(4, 12))  # 16

numbers = [1, 2, 3, 4, 5, 6]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25, 36]
