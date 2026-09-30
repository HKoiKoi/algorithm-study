def solution(s):
    stack = []

    for ch in s:
        if not stack:
            stack.append(ch)
            continue

        if stack[-1] == ch:
            stack.pop()
            continue

        stack.append(ch)

    return 1 if len(stack) == 0 else 0


test_s1 = "baabaa"
test_s2 = "cdcd"

print(solution(test_s1))  # 1
print(solution(test_s2))  # 0
