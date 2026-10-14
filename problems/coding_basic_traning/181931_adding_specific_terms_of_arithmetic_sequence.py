def solution(a, d, included):
    answer = 0

    for i in range(len(included)):
        if included[i]:
            answer += a + (i * d)

    return answer


a_1 = 3
d_1 = 4
included_1 = [True, False, False, True, True]
a_2 = 7
d_2 = 1
included_2 = [False, False, False, True, False, False, False]

print(solution(a_1, d_1, included_1))  # 37
print(solution(a_2, d_2, included_2))  # 10
