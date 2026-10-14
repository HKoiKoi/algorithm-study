def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))


a_1 = 9
b_1 = 91
a_2 = 89
b_2 = 8

print(solution(a_1, b_1))  # 991
print(solution(a_2, b_2))  # 898
