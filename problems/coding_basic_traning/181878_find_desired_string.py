def solution(myString, pat):
    return int(pat.lower() in myString.lower())


myString_1 = "AbCdEfG"
pat_1 = "aBc"
myString_2 = "aaAA"
pat_2 = "aaaaa"

print(solution(myString_1, pat_1))  # 1
print(solution(myString_2, pat_2))  # 0
