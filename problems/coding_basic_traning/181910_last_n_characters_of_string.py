def solution(my_string, n):
    return my_string[-n:]


my_string_1 = "ProgrammersS123"
n_1 = 11
my_string_2 = "He110W0r1d"
n_2 = 5

print(solution(my_string_1, n_1))  # "grammerS123"
print(solution(my_string_2, n_2))  # "W0r1d"
