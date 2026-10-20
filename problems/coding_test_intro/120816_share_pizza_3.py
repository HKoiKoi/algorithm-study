def solution(slice, n):
    return (n - 1) // slice + 1


slice_1 = 7
n_1 = 10
slice_2 = 4
n_2 = 12

print(solution(slice_1, n_1))  # 2
print(solution(slice_2, n_2))  # 3
