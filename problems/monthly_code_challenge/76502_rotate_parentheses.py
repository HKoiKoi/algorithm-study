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


s_1 = "[](){}"
s_2 = "}]()[{"
s_3 = "[)(]"
s_4 = "}}}"
s_5 = "({)}"

print(solution(s_1))
print(solution(s_2))
print(solution(s_3))
print(solution(s_4))
print(solution(s_5))
