def solution(str1, str2):
    return int(str1 in str2)


str1_1 = "abc"
str2_1 = "aabcc"
str1_2 = "tbt"
str2_2 = "tbbttb"

print(solution(str1_1, str2_1))  # 1
print(solution(str1_2, str2_2))  # 0
