def solution(numbers):
    return [num * 2 for num in numbers]


numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [1, 2, 100, -99, 1, 2, 3]

print(solution(numbers_1))  # [2, 4, 6, 8, 10]
print(solution(numbers_2))  # [2, 4, 200, -198, 2, 4, 6]
