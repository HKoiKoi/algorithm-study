def solution(a, d, included):
    answer = 0

    for i in range(len(included)):
        if included[i]:
            answer += a + (i * d)

    return answer


test_a_1 = 3
test_d_1 = 4
test_included_1 = [True, False, False, True, True]
test_a_2 = 7
test_d_2 = 1
test_included_2 = [False, False, False, True, False, False, False]

print(solution(test_a_1, test_d_1, test_included_1))  # 37
print(solution(test_a_2, test_d_2, test_included_2))  # 10
