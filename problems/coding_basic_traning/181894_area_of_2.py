def solution(arr):
    if 2 not in arr:
        return [-1]

    return arr[arr.index(2):len(arr) - arr[::-1].index(2)]


arr_1 = [1, 2, 1, 4, 5, 2, 9]
arr_2 = [1, 2, 1]
arr_3 = [1, 1, 1]
arr_4 = [1, 2, 1, 2, 1, 10, 2, 1]

print(solution(arr_1))  # [2, 1, 4, 5, 2]
print(solution(arr_2))  # [2]
print(solution(arr_3))  # [-1]
print(solution(arr_4))  # [2, 1, 2, 1, 10, 2]
