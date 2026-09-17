# 두 개 뽑아서 더하기

def solution(numbers):
    answer = []
    length = len(numbers)

    for i in range(length - 1):
        for j in range(i + 1, length):
            answer.append(numbers[i] + numbers[j])

    return sorted(set(answer))


test_array1 = [2, 1, 3, 4, 1]
test_array2 = [5, 0, 2, 7]

print(solution(test_array1))
print(solution(test_array2))


# 리스트 컴프리헨션 사용 풀이
def solution_2(numbers):
    answer = [numbers[i] + numbers[j] for i in range(len(numbers) - 1) for j in range(i + 1, len(numbers))]

    return sorted(set(answer))


print(solution_2(test_array1))
print(solution_2(test_array2))

# combinations 사용 풀이
from itertools import combinations


def solution_3(numbers):
    answer = [sum(comb) for comb in combinations(numbers, 2)]

    return sorted(set(answer))


print(solution_3(test_array1))
print(solution_3(test_array2))
