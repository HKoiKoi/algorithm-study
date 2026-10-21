def solution(my_string, alp):
    answer = []

    for str in my_string:
        if str == alp:
            answer.append(str.upper())
        else:
            answer.append(str)

    return "".join(answer)


def solution_2(my_string, alp):
    return my_string.replace(alp, alp.upper())


my_string_1 = "programmers"
alp_1 = "p"
my_string_2 = "lowercase"
alp_2 = "x"

print(solution(my_string_1, alp_1))  # "Programmers"
print(solution_2(my_string_2, alp_2))  # "lowercase"
