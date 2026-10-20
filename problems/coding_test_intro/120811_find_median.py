import statistics


def solution(array):
    array.sort()
    return array[len(array) // 2]


def solution_2(array):
    return statistics.median(array)


array_1 = [1, 2, 7, 10, 11]
array_2 = [9, -1, 0]

print(solution_2(array_1))  # 7
print(solution(array_2))  # 0
