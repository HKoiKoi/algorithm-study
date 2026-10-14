def solution(arr, queries):
    for query in queries:
        arr[query[0]], arr[query[1]] = arr[query[1]], arr[query[0]]

    return arr


test_arr = [0, 1, 2, 3, 4]
test_queries = [[0, 3], [1, 2], [1, 4]]

print(solution(test_arr, test_queries))  # [3, 4, 1, 0, 2]
