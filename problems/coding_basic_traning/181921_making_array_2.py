def solution(l, r):
    answer = []

    for num in range(l, r + 1):
        if set(str(num)).issubset({"0", "5"}):
            answer.append(num)

    return [-1] if not answer else answer


l_1 = 5
r_1 = 555
l_2 = 10
r_2 = 20

print(solution(l_1, r_1))  # [5, 50, 55, 500, 505, 550, 555]
print(solution(l_2, r_2))  # [-1]
