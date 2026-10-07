def is_valid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False

            stack.pop()

    return len(stack) == 0


def solution(s):
    if len(s) % 2 != 0:
        return 0

    answer = 0

    for i in range(len(s)):
        if is_valid(s[i:] + s[:i]):
            answer += 1

    return answer


test_s1 = "[](){}"
test_s2 = "}]()[{"
test_s3 = "[)(]"
test_s4 = "}}}"
test_s5 = "({)}"

print(solution(test_s1))
print(solution(test_s2))
print(solution(test_s3))
print(solution(test_s4))
print(solution(test_s5))
