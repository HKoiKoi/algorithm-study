def solution(myString):
    return myString.lower().replace("a", "A")


test_cases = [
    ("abstract algebra", "AbstrAct AlgebrA"),
    ("PrOgRaMmErS", "progrAmmers")
]

for i, (myString, expected) in enumerate(test_cases, 1):
    result = solution(myString)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
