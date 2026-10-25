def solution(num_list, n):
    answer = [[]]
    return answer


test_cases = [
    ([1, 2, 3, 4, 5, 6, 7, 8], 2, [[1, 2], [3, 4], [5, 6], [7, 8]]),
    ([100, 95, 2, 4, 5, 6, 18, 33, 948], 3, [[100, 95, 2], [4, 5, 6], [18, 33, 948]])
]

for i, (num_list, n, expected) in enumerate(test_cases, 1):
    result = solution(num_list, n)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
