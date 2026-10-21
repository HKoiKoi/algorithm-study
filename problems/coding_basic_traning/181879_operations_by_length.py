import math


def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)

    answer = 1

    for num in num_list:
        answer *= num

    return answer


def solution_2(num_list):
    return sum(num_list) if len(num_list) >= 11 else math.prod(num_list)


num_list_1 = [3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]
num_list_2 = [2, 3, 4, 5]

print(solution(num_list_1))  # 51
print(solution_2(num_list_2))  # 120
