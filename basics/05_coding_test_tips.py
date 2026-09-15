# 조기 반환

def total_price(quantity, price):
    total = quantity * price

    if total > 100:
        # 실행 코드
        return total * 0.9

    return total


print(total_price(9, 15))  # 121.5


# 보호 구문

def calculate_average(numbers):
    if numbers is None:  # 값이 존재하지 않으면 None 반환 (예외)
        return None

    if not isinstance(numbers, list):  # numbers가 list가 아니면 None 반환 (예외)
        return None

    if len(numbers) == 0:  # numbers의 길이가 0이면 None 반환 (예외)
        return None

    total = sum(numbers)
    average = total / len(numbers)
    return average


# 합성 함수

def add_three(x):
    return x + 3


def square(x):
    return x * x


composed_function = lambda x: square(add_three(x))
print(composed_function(3))  # (3 + 3) * (3 + 3) = 36
