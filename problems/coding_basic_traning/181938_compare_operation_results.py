def solution(a, b):
    return max(int(f"{a}{b}"), 2 * a * b)


test_a1 = 2
test_b1 = 91
test_a2 = 91
test_b2 = 2

print(solution(test_a1, test_b1))  # 364
print(solution(test_a2, test_b2))  # 912
