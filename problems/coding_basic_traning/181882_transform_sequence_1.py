def solution(arr):
    for idx, val in enumerate(arr):
        if val >= 50 and val % 2 == 0:
            arr[idx] = val // 2
        elif val < 50 and val % 2 != 0:
            arr[idx] = val * 2

    return arr


test_cases = [
    ([1, 2, 3, 100, 99, 98], [2, 2, 6, 50, 99, 49])
]

for i, (arr, expected) in enumerate(test_cases, 1):
    result = solution(arr)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
