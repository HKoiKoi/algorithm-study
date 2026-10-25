def solution(numbers, direction):
    answer = []
    return answer


test_cases = [
    ([1, 2, 3], "right", [3, 1, 2]),
    ([4, 455, 6, 4, -1, 45, 6], "left", [455, 6, 4, -1, 45, 6, 4])
]

for i, (box, n, expected) in enumerate(test_cases, 1):
    result = solution(box, n)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
