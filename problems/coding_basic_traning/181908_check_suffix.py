def solution(my_string, is_suffix):
    return int(my_string[-len(is_suffix):] == is_suffix)


my_string = "banana"
is_suffix_1 = "ana"
is_suffix_2 = "nan"
is_suffix_3 = "wxyz"
is_suffix_4 = "abanana"

print(solution(my_string, is_suffix_1))  # 1
print(solution(my_string, is_suffix_2))  # 0
print(solution(my_string, is_suffix_3))  # 0
print(solution(my_string, is_suffix_4))  # 0
