def solution(arr, queries):
    answer = []

    for s, e, k in queries:
        numbers = [num for num in arr[s:e + 1] if num > k]
        answer.append(min(numbers) if numbers else -1)

    return answer


arr = [0, 1, 2, 3, 4]
queries = [[0, 4, 2], [0, 3, 2], [0, 2, 2]]

print(solution(arr, queries))  # [3, 4, -1]
