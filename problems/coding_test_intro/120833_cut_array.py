def solution(numbers, num1, num2):
    answer = []
    return answer


test_cases = [
    ([1, 2, 3, 4, 5], 1, 3, [2, 3, 4]),
    ([1, 3, 5], 1, 2, [3, 5])
]

for i, (numbers, num1, num2, expected) in enumerate(test_cases, 1):
    result = solution(numbers, num1, num2)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
