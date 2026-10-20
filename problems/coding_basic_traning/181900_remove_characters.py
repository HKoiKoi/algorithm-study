def solution(my_string, indices):
    answer = [i for i in my_string]

    for i in indices:
        answer[i] = ""

    return "".join(answer)


my_string = "apporoograpemmemprs"
indices = [1, 16, 6, 15, 0, 10, 11, 3]

print(solution(my_string, indices))  # "programmers"
