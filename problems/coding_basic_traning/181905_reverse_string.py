def solution(my_string, s, e):
    answer = []

    answer.append(my_string[0:s])
    answer.append(my_string[s:e + 1][::-1])
    answer.append(my_string[e + 1:])

    return "".join(answer)


my_string_1 = "Progra21Sremm3"
s_1 = 6
e_1 = 12
my_string_2 = "Stanley1yelnatS"
s_2 = 4
e_2 = 10

print(solution(my_string_1, s_1, e_1))  # "ProgrammerS123"
print(solution(my_string_2, s_2, e_2))  # "Stanley1yelnatS"
