def solution(num_list, n):
    return num_list[n - 1:]


num_list_1 = [2, 1, 6]
n_1 = 3
num_list_2 = [5, 2, 1, 7, 5]
n_2 = 2

print(solution(num_list_1, n_1))  # [6]
print(solution(num_list_2, n_2))  # [2, 1, 7, 5]
