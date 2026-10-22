def solution(hp):
    answer = 0
    return answer


test_cases = [
    (23, 5),
    (24, 6),
    (999, 201)
]

for i, (hp, expected) in enumerate(test_cases, 1):
    result = solution(hp)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
