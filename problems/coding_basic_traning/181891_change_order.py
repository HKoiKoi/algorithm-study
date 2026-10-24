def solution(num_list, n):
    return num_list[n:] + num_list[:n]


test_cases = [
    ([2, 1, 6], 1, [1, 6, 2]),
    ([5, 2, 1, 7, 5], 3, [7, 5, 5, 2, 1])
]

for i, (num_list, n, expected) in enumerate(test_cases, 1):
    result = solution(num_list, n)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
