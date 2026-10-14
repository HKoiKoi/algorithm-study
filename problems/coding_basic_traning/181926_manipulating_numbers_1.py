def solution(n, control):
    command = dict(zip(["w", "s", "d", "a"], [1, -1, 10, -10]))

    return n + sum(command[ch] for ch in control)


test_n = 0
test_control = "wsdawsdassw"

print(solution(test_n, test_control))  # -1
