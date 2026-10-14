def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]


my_string_1 = "He11oWor1d"
overwrite_string_1 = "lloWorl"
s_1 = 2
my_string_2 = "Program29b8UYP"
overwrite_string_2 = "merS123"
s_2 = 7

print(solution(my_string_1, overwrite_string_1, s_1))  # HelloWorld
print(solution(my_string_2, overwrite_string_2, s_2))  # ProgrammerS123
