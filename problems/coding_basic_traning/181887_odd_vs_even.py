def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))


test_cases = [
    ([4, 2, 6, 1, 7, 6], 17),
    ([-1, 2, 5, 6, 3], 8)
]

for i, (num_list, expected) in enumerate(test_cases, 1):
    result = solution(num_list)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
