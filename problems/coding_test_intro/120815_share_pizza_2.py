import math


def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def solution(n):
    return math.lcm(n, 6) // 6


def solution_2(n):
    return lcm(n, 6) // 6


n_1 = 6
n_2 = 10
n_3 = 4

print(solution_2(n_1))  # 1
print(solution_2(n_2))  # 5
print(solution_2(n_3))  # 2
