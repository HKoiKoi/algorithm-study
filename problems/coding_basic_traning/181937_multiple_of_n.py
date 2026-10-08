def solution(num, n):
    return int(not (num % n))


test_num1 = 98
test_n1 = 2
test_num2 = 34
test_n2 = 3

print(solution(test_num1, test_n1))  # 1
print(solution(test_num2, test_n2))  # 0
