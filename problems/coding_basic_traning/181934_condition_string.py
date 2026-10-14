def solution(ineq, eq, n, m):
    if eq == "=":
        return int(eval(f"{n} {ineq}= {m}"))

    return int(eval(f"{n} {ineq} {m}"))


ineq_1 = "<"
eq_1 = "="
n_1 = 20
m_1 = 50
ineq_2 = ">"
eq_2 = "!"
n_2 = 41
m_2 = 78

print(solution(ineq_1, eq_1, n_1, m_1))  # 1
print(solution(ineq_2, eq_2, n_2, m_2))  # 0
