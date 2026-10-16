def solution(my_strings, parts):
    answer = []

    for i in range(len(my_strings)):
        string = my_strings[i]
        s, e = parts[i]

        answer.append(string[s:e + 1])

    return "".join(answer)


my_strings = ["progressive", "hamburger", "hammer", "ahocorasick"]
parts = [[0, 4], [1, 2], [3, 5], [7, 7]]

print(solution(my_strings, parts))  # "programmers"
