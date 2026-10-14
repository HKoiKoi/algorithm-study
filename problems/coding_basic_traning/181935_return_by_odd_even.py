def solution(n):
    if n % 2 != 0:
        return sum([x for x in range(n + 1) if x % 2 != 0])

    return sum([x * x for x in range(n + 1) if x % 2 == 0])


n_1 = 7
n_2 = 10

print(solution(n_1))  # 16
print(solution(n_2))  # 220
