def solution(n):
    return sum([i for i in range(2, n + 1, 2)])


n_1 = 10
n_2 = 4

print(solution(n_1))  # 30
print(solution(n_2))  # 6
