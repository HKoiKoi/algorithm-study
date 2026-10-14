def solution(a, b):
    return max(int(f"{a}{b}"), 2 * a * b)


a_1 = 2
b_1 = 91
a_2 = 91
b_2 = 2

print(solution(a_1, b_1))  # 364
print(solution(a_2, b_2))  # 912
