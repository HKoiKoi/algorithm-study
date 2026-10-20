from collections import Counter


def solution(array):
    count = Counter(array)
    sorted_count = count.most_common()

    if len(sorted_count) == 1:
        return sorted_count[0][0]
    elif sorted_count[0][1] == sorted_count[1][1]:
        return -1

    return sorted_count[0][0]


array_1 = [1, 2, 3, 3, 3, 4]
array_2 = [1, 1, 2, 2]
array_3 = [1]

print(solution(array_1))  # 3
print(solution(array_2))  # -1
print(solution(array_3))  # 1
