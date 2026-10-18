def solution(my_string):
    return my_string.split()


my_string_1 = "i    love  you"
my_string_2 = "    programmers  "

print(solution(my_string_1))  # ["i", "love", "you"]
print(solution(my_string_2))  # ["programmers"]
