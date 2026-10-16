def solution(my_string):
    return sorted([my_string[i:] for i in range(len(my_string))])


my_string_1 = "banana"
my_string_2 = "programmers"

print(solution(my_string_1))  # ["a", "ana", "anana", "banana", "na", "nana"]
print(solution(
    my_string_2))  # ["ammers", "ers", "grammers", "mers", "mmers", "ogrammers", "programmers", "rammers", "rogrammers", "rs", "s"]
