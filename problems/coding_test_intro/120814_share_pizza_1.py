import math


def solution(n):
    return math.ceil(n / 7)


def solution_2(n):
    return (n - 1) // 7 + 1


def solution_3(n):
    return n // 7 + (1 if n % 7 != 0 else 0)


n_1 = 7
n_2 = 1
n_3 = 15

print(solution(n_1))  # 1
print(solution_2(n_2))  # 1
print(solution_3(n_3))  # 3
