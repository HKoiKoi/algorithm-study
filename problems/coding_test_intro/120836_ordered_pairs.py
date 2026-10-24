def solution(n):
    answer = 0

    for i in range(1, n + 1):
        if n % i != 0:
            continue

        answer += 1

    return answer


test_cases = [
    (20, 6),
    (100, 9)
]

for i, (n, expected) in enumerate(test_cases, 1):
    result = solution(n)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
