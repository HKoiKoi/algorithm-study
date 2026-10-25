def solution(numbers, k):
    answer = 0
    return answer


test_cases = [
    ([1, 2, 3, 4], 2, 3),
    ([1, 2, 3, 4, 5, 6], 5, 3),
    ([1, 2, 3], 3, 2)
]

for i, (numbers, k, expected) in enumerate(test_cases, 1):
    result = solution(numbers, k)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
