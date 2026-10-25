def solution(dot):
    x, y = dot

    if x > 0:
        return 1 if y > 0 else 4
    else:
        return 2 if y > 0 else 3


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
