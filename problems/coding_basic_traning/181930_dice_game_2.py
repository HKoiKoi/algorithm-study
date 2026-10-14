def solution(a, b, c):
    answer = a + b + c

    if a == b or a == c or b == c:
        answer *= a ** 2 + b ** 2 + c ** 2

    if a == b == c:
        answer *= a ** 3 + b ** 3 + c ** 3

    return answer


test_a_1 = 2
test_b_1 = 6
test_c_1 = 1
test_a_2 = 5
test_b_2 = 3
test_c_2 = 3
test_a_3 = 4
test_b_3 = 4
test_c_3 = 4

print(solution(test_a_1, test_b_1, test_c_1))  # 9
print(solution(test_a_2, test_b_2, test_c_2))  # 473
print(solution(test_a_3, test_b_3, test_c_3))  # 110592
