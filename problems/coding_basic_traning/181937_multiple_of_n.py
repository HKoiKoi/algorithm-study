def solution(num, n):
    return int(not (num % n))


num_1 = 98
n_1 = 2
num_2 = 34
n_2 = 3

print(solution(num_1, n_1))  # 1
print(solution(num_2, n_2))  # 0
