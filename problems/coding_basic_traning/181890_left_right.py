def solution(str_list):
    for i, ch in enumerate(str_list):
        if ch == "l":
            return str_list[:i]
        elif ch == "r":
            return str_list[i + 1:]

    return []


test_cases = [
    (["u", "u", "l", "r"], ["u", "u"]),
    (["l"], [])
]

for i, (str_list, expected) in enumerate(test_cases, 1):
    result = solution(str_list)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
