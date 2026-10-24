def solution(num_list):
    answer = 0
    return answer


test_cases = [
    ([12, 4, 15, 1, 14], 11)
]

for i, (num_list, expected) in enumerate(test_cases, 1):
    result = solution(num_list)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
