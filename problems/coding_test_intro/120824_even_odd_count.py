def solution(num_list):
    answer = [0, 0]

    for num in num_list:
        answer[num % 2] += 1

    return answer


num_list_1 = [1, 2, 3, 4, 5]
num_list_2 = [1, 3, 5, 7]

print(solution(num_list_1))  # [2, 3]
print(solution(num_list_2))  # [0, 4]
