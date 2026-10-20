def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))


my_string = "banana"
is_prefix_1 = "ban"
is_prefix_2 = "nan"
is_prefix_3 = "abcd"
is_prefix_4 = "bananan"

print(solution(my_string, is_prefix_1))  # 1
print(solution(my_string, is_prefix_2))  # 0
print(solution(my_string, is_prefix_3))  # 0
print(solution(my_string, is_prefix_4))  # 0
