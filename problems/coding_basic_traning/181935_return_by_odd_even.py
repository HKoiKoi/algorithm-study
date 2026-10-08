def solution(n):
    if n % 2 != 0:
        return sum([x for x in range(n + 1) if x % 2 != 0])

    return sum([x * x for x in range(n + 1) if x % 2 == 0])


test_n1 = 7
test_n2 = 10

print(solution(test_n1))  # 16
print(solution(test_n2))  # 220
