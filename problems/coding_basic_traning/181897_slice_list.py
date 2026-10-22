def solution(n, slicer, num_list):
    a, b, c = slicer

    if n == 1:
        return num_list[:b + 1]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a:b + 1]
    else:
        return num_list[a:b + 1:c]


n_1 = 3
n_2 = 4
slicer = [1, 5, 2]
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(solution(n_1, slicer, num_list))  # [2, 3, 4, 5, 6]
print(solution(n_2, slicer, num_list))  # [2, 4, 6]
