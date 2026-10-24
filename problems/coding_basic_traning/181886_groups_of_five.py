def solution(names):
    return names[::5]


test_cases = [
    (["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"], ["nami", "vex"])
]

for i, (names, expected) in enumerate(test_cases, 1):
    result = solution(names)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
