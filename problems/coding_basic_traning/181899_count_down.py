def solution(start_num, end_num):
    return list(range(start_num, end_num - 1, -1))


start_num = 10
end_num = 3

print(solution(start_num, end_num))  # [10, 9, 8, 7, 6, 5, 4, 3]
