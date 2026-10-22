def solution(my_string, letter):
    return my_string.replace(letter, "")


my_string_1 = "abcdef"
letter_1 = "f"
my_string_2 = "BCBdbe"
letter_2 = "B"

print(solution(my_string_1, letter_1))  # "abcde"
print(solution(my_string_2, letter_2))  # "Cdbe"
