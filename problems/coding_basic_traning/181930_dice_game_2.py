def solution(a, b, c):
    answer = a + b + c

    if a == b or a == c or b == c:
        answer *= a ** 2 + b ** 2 + c ** 2

    if a == b == c:
        answer *= a ** 3 + b ** 3 + c ** 3

    return answer


a_1 = 2
b_1 = 6
c_1 = 1
a_2 = 5
b_2 = 3
c_2 = 3
a_3 = 4
b_3 = 4
c_3 = 4

print(solution(a_1, b_1, c_1))  # 9
print(solution(a_2, b_2, c_2))  # 473
print(solution(a_3, b_3, c_3))  # 110592
