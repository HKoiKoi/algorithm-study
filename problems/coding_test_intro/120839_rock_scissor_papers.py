def solution(rsp):
    return "".join({"2": "0", "0": "5", "5": "2"}[i] for i in rsp)


test_cases = [
    ("2", "0"),
    ("205", "052")
]

for i, (rsp, expected) in enumerate(test_cases, 1):
    result = solution(rsp)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
