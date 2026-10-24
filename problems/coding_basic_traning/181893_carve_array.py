def solution(arr, query):
    start = 0
    end = len(arr) - 1

    for i, val in enumerate(query):
        if i % 2 == 0:
            end = start + val
        else:
            start += val

    return arr[start:end + 1]


test_cases = [
    ([0, 1, 2, 3, 4, 5], [4, 1, 2], [1, 2, 3])
]

for i, (arr, query, expected) in enumerate(test_cases, 1):
    result = solution(arr, query)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
