def solution(arr, queries):
    for query in queries:
        arr[query[0]], arr[query[1]] = arr[query[1]], arr[query[0]]

    return arr


arr = [0, 1, 2, 3, 4]
queries = [[0, 3], [1, 2], [1, 4]]

print(solution(arr, queries))  # [3, 4, 1, 0, 2]
