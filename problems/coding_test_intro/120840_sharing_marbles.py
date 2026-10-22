def solution(balls, share):
    answer = 0
    return answer


test_cases = [
    (3, 2, 3),
    (5, 3, 10)
]

for i, (balls, share, expected) in enumerate(test_cases, 1):
    result = solution(balls, share)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
