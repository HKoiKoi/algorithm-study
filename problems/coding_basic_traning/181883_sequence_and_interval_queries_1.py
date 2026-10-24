def solution(arr, queries):
    for s, e in queries:
        for i in range(s, e + 1):
            arr[i] += 1

    return arr


test_cases = [
    ([0, 1, 2, 3, 4], [[0, 1], [1, 2], [2, 3]], [1, 3, 4, 4, 4])
]

for i, (arr, queries, expected) in enumerate(test_cases, 1):
    result = solution(arr, queries)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
