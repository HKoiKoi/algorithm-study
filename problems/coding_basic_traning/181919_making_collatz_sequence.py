def solution(n):
    answer = [n]

    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        answer.append(n)

    return answer


n = 10

print(solution(n))  # [10, 5, 16, 8, 4, 2, 1]
