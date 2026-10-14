def solution(numLog):
    command = dict(zip([1, -1, 10, -10], ["w", "s", "d", "a"]))

    return "".join(command[numLog[i] - numLog[i - 1]] for i in range(1, len(numLog)))


test_numLog = [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]

print(solution(test_numLog))  # "wsdawsdassw"
