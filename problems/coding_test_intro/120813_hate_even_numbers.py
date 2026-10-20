def solution(n):
    return [n for n in range(1, n + 1) if n % 2 != 0]


n_1 = 10
n_2 = 15

print(solution(n_1))  # [1, 3, 5, 7, 9]
print(solution(n_2))  # [1, 3, 5, 7, 9, 11, 13, 15]
