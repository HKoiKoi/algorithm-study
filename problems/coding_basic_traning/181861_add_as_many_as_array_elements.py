def solution(arr):
    answer = []

    for a in arr:
        for _ in range(a):
            answer.append(a)

    return answer


arr_1 = [5, 1, 4]
arr_2 = [6, 6]
arr_3 = [1]

print(solution(arr_1))  # [5, 5, 5, 5, 5, 1, 4, 4, 4, 4]
print(solution(arr_2))  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
print(solution(arr_3))  # [1]
