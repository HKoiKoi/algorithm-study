def solution(age):
    answer = []

    for num in str(age):
        answer.append(chr(ord(num) + 49))

    return "".join(answer)


test_cases = [
    (23, "cd"),
    (51, "fb"),
    (100, "baa")
]

for i, (age, expected) in enumerate(test_cases, 1):
    result = solution(age)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
