def solution(ineq, eq, n, m):
    if eq == "=":
        return int(eval(f"{n} {ineq}= {m}"))

    return int(eval(f"{n} {ineq} {m}"))


test_ineq1 = "<"
test_eq1 = "="
test_n1 = 20
test_m1 = 50
test_ineq2 = ">"
test_eq2 = "!"
test_n2 = 41
test_m2 = 78

print(solution(test_ineq1, test_eq1, test_n1, test_m1))  # 1
print(solution(test_ineq2, test_eq2, test_n2, test_m2))  # 0
