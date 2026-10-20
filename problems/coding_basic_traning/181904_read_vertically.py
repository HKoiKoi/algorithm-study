def solution(my_string, m, c):
    return my_string[c - 1::m]


my_string_1 = "ihrhbakrfpndopljhygc"
m_1 = 4
c_1 = 2
my_string_2 = "programmers"
m_2 = 1
c_2 = 1

print(solution(my_string_1, m_1, c_1))  # "happy"
print(solution(my_string_2, m_2, c_2))  # "programmers"
