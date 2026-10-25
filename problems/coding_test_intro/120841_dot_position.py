def solution(dot):
    answer = 0
    return answer


test_cases = [
    ([2, 4], 1),
    ([-7, 9], 2)
]

for i, (dot, expected) in enumerate(test_cases, 1):
    result = solution(dot)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
