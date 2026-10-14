def solution(info, edges):
    answer = 0
    return answer


info_1 = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
info_2 = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges_1 = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
edges_2 = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]

print(solution(info_1, edges_1))  # 5
print(solution(info_2, edges_2))  # 5
