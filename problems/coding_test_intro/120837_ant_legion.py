def solution(hp):
    attack_power = [5, 3, 1]
    answer = 0

    for power in attack_power:
        if hp == 0:
            break

        answer += hp // power
        hp %= power

    return answer


def solution_2(hp):
    answer = 0

    for power in [5, 3, 1]:
        count, hp = divmod(hp, power)
        answer += count

    return answer


def solution_3(hp):
    return hp // 5 + (hp % 5) // 3 + (hp % 5) % 3


# 테스트 케이스
test_cases = [
    (23, 5),
    (24, 6),
    (999, 201)
]

# 테스트할 함수들을 리스트로 묶기
functions = [solution, solution_2, solution_3]

for i, (hp, expected) in enumerate(test_cases, 1):
    print(f"\n[테스트 {i}] hp: {hp}")

    # 각 함수별로 결과 검증
    for func in functions:
        result = func(hp)

        if result == expected:
            print(f"  {func.__name__} 통과 ✅")
        else:
            print(f"  {func.__name__} 실패 ❌ (기댓값: {expected}, 실제: {result})")
