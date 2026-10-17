def solution(num1, num2):
    return int(num1 / num2 * 1000)


num1_1 = 3
num2_1 = 2
num1_2 = 7
num2_2 = 3
num1_3 = 1
num2_3 = 16

print(solution(num1_1, num2_1))  # 1500
print(solution(num1_2, num2_2))  # 2333
print(solution(num1_3, num2_3))  # 62
