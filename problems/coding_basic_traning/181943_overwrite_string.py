def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]


test_my_string1 = "He11oWor1d"
test_overwrite_string1 = "lloWorl"
test_s1 = 2
test_my_string2 = "Program29b8UYP"
test_overwrite_string2 = "merS123"
test_s2 = 7

print(solution(test_my_string1, test_overwrite_string1, test_s1))  # HelloWorld
print(solution(test_my_string2, test_overwrite_string2, test_s2))  # ProgrammerS123
