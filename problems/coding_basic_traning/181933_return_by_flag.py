def solution(a, b, flag):
    return a + b if flag else a - b


a = -4
b = 7
flag_1 = True
flag_2 = False

print(solution(a, b, flag_1))  # 3
print(solution(a, b, flag_2))  # -11
