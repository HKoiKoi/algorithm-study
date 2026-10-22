def solution(emergency):
    answer = []
    return answer


test_cases = [
    ([3, 76, 24], [3, 1, 2]),
    ([1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1]),
    ([30, 10, 23, 6, 100], [2, 4, 3, 5, 1])
]

for i, (emergency, expected) in enumerate(test_cases, 1):
    result = solution(emergency)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
