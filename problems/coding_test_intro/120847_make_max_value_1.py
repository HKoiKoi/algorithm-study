def solution(numbers):
    answer = 0
    return answer


test_cases = [
    ([1, 2, 3, 4, 5], 20),
    ([0, 31, 24, 10, 1, 9], 744)
]

for i, (numbers, expected) in enumerate(test_cases, 1):
    result = solution(numbers)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
