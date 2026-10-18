def solution(num_list):
    for i, num in enumerate(num_list):
        if num < 0:
            return i

    return -1


num_list_1 = [12, 4, 15, 46, 38, -2, 15]
num_list_2 = [13, 22, 53, 24, 15, 6]

print(solution(num_list_1))  # 5
print(solution(num_list_2))  # -1
