def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i

    return -1


arr_1 = [0, 0, 0, 1]
idx_1 = 1
arr_2 = [1, 0, 0, 1, 0, 0]
idx_2 = 4
arr_3 = [1, 1, 1, 1, 0]
idx_3 = 3

print(solution(arr_1, idx_1))  # 3
print(solution(arr_2, idx_2))  # -1
print(solution(arr_3, idx_3))  # 3
