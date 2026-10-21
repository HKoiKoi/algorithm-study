def solution(arr, k):
    if k % 2 == 0:
        return [i + k for i in arr]
    else:
        return [i * k for i in arr]


arr_1 = [1, 2, 3, 100, 99, 98]
k_1 = 3
arr_2 = [1, 2, 3, 100, 99, 98]
k_2 = 2

print(solution(arr_1, k_1))  # [3, 6, 9, 300, 297, 294]
print(solution(arr_2, k_2))  # [3, 4, 5, 102, 101, 100]
