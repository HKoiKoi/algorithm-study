def solution(rny_string):
    return rny_string.replace("m", "rn")


rny_string_1 = "masterpiece"
rny_string_2 = "programmers"
rny_string_3 = "jerry"
rny_string_4 = "burn"

print(solution(rny_string_1))  # "rnasterpiece"
print(solution(rny_string_2))  # "prograrnrners"
print(solution(rny_string_3))  # "jerry"
print(solution(rny_string_4))  # "burn"
