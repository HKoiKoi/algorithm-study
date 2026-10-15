def solution(n, a, b):
    answer = 0

    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2

        answer += 1

    return answer


N = 8
A = 4
B = 7

print(solution(N, A, B))  # 3
