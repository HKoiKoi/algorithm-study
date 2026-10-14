def solution(n, control):
    command = dict(zip(["w", "s", "d", "a"], [1, -1, 10, -10]))

    return n + sum(command[ch] for ch in control)


n = 0
control = "wsdawsdassw"

print(solution(n, control))  # -1
