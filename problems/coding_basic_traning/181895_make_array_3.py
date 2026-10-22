def solution(arr, intervals):
    answer = []

    for start, end in intervals:
        answer += arr[start:end + 1]

    return answer


arr = [1, 2, 3, 4, 5]
intervals = [[1, 3], [0, 4]]

print(solution(arr, intervals))  # [2, 3, 4, 1, 2, 3, 4, 5]
