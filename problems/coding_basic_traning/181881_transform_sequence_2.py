def solution(arr):
    answer = 0
    return answer


test_cases = [
    ([1, 2, 3, 100, 99, 98], 5)
]

for i, (arr, expected) in enumerate(test_cases, 1):
    result = solution(arr)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
