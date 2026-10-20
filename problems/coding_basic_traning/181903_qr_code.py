def solution(q, r, code):
    return code[r::q]


q_1 = 3
r_1 = 1
code_1 = "qjnwezgrpirldywt"
q_2 = 1
r_2 = 0
code_2 = "programmers"

print(solution(q_1, r_1, code_1))  # "jerry"
print(solution(q_2, r_2, code_2))  # "programmers"
