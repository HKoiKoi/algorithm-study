import statistics


def solution(numbers):
    return statistics.mean(numbers)


numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

print(solution(numbers_1))  # 5.5
print(solution(numbers_2))  # 94.0
