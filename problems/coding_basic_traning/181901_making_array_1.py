def solution(n, k):
    return [i for i in range(k, n + 1, k)]


n_1 = 10
k_1 = 3
n_2 = 15
k_2 = 5

print(solution(n_1, k_1))  # [3, 6, 9]
print(solution(n_2, k_2))  # [5, 10, 15]
