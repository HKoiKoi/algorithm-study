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


test_s1 = "()()"
test_s2 = "(())()"
test_s3 = ")()("
test_s4 = "(()("

print(solution(test_s1))
print(solution(test_s2))
print(solution(test_s3))
print(solution(test_s4))
