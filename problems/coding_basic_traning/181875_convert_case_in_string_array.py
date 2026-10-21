def solution(strArr):
    answer = []

    for i, str in enumerate(strArr):
        if i % 2 == 0:
            answer.append(str.lower())
        else:
            answer.append(str.upper())

    return answer


strArr_1 = ["AAA", "BBB", "CCC", "DDD"]
strArr_2 = ["aBc", "AbC"]

print(solution(strArr_1))  # ["aaa","BBB","ccc","DDD"]
print(solution(strArr_2))  # ["abc","ABC"]
