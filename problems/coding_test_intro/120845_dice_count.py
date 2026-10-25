def solution(box, n):
    answer = 0
    return answer


test_cases = [
    ([1, 1, 1], 1, 1),
    ([10, 8, 6], 3, 12)
]

for i, (box, n, expected) in enumerate(test_cases, 1):
    result = solution(box, n)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
