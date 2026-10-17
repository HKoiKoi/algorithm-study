def solution(num1, num2):
    return 1 if num1 == num2 else -1


num1_1 = 2
num2_1 = 3
num1_2 = 11
num2_2 = 11
num1_3 = 7
num2_3 = 99

print(solution(num1_1, num2_1))  # -1
print(solution(num1_2, num2_2))  # 1
print(solution(num1_3, num2_3))  # -1
