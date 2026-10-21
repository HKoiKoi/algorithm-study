def solution(str_list, ex):
    return "".join([str for str in str_list if ex not in str])


str_list_1 = ["abc", "def", "ghi"]
ex_1 = "ef"
str_list_2 = ["abc", "bbc", "cbc"]
ex_2 = "c"

print(solution(str_list_1, ex_1))  # "abcghi"
print(solution(str_list_2, ex_2))  # ""
