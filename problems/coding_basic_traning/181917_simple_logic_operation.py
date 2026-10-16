def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)


x1_1 = False
x2_1 = True
x3_1 = True
x4_1 = True
x1_2 = True
x2_2 = False
x3_2 = False
x4_2 = False

print(solution(x1_1, x2_1, x3_1, x4_1))
print(solution(x1_2, x2_2, x3_2, x4_2))
