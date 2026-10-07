def solution(arr1, arr2):
    arr3_row_size = len(arr1)
    arr3_col_size = len(arr2[0])
    common_size = len(arr1[0])

    answer = [[0] * arr3_col_size for _ in range(arr3_row_size)]

    for i in range(arr3_row_size):
        for j in range(arr3_col_size):
            for k in range(common_size):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer


test_arr1_1 = [[1, 4], [3, 2], [4, 1]]
test_arr2_1 = [[3, 3], [3, 3]]
test_arr1_2 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
test_arr2_2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

print(solution(test_arr1_1, test_arr2_1))
print(solution(test_arr1_2, test_arr2_2))
