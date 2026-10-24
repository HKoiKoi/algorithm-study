def solution(numbers, n):
    answer = 0
    idx = 0

    while answer <= n:
        answer += numbers[idx]
        idx += 1

    return answer


test_cases = [
    ([34, 5, 71, 29, 100, 34], 123, 139),
    ([58, 44, 27, 10, 100], 139, 239)
]

for i, (numbers, n, expected) in enumerate(test_cases, 1):
    result = solution(numbers, n)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
