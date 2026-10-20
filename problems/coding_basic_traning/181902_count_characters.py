def solution(my_string):
    answer = [0] * 52

    for ch in my_string:
        if 65 <= ord(ch) <= 90:
            answer[ord(ch) - 65] += 1
        else:
            answer[ord(ch) - 71] += 1

    return answer


def solution_2(my_string):
    answer = [0] * 52

    for ch in my_string:
        if ch.isupper():
            answer[ord(ch) - 65] += 1
        else:
            answer[ord(ch) - 71] += 1

    return answer


my_string = "Programmers"

print(solution_2(
    my_string))  # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0]
