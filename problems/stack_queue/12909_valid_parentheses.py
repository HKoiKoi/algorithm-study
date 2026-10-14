def solution(s):
    pair = 0

    for c in s:
        if c == "(":
            pair += 1
        else:
            pair -= 1

        if pair < 0:
            return False

    return pair == 0


s_1 = "()()"
s_2 = "(())()"
s_3 = ")()("
s_4 = "(()("

print(solution(s_1))
print(solution(s_2))
print(solution(s_3))
print(solution(s_4))
