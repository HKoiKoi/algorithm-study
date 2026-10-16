def solution(intStrs, k, s, l):
    answer = []

    for str in intStrs:
        number = int(str[s:s + l])

        if number > k:
            answer.append(number)

    return answer


intStrs = ["0123456789", "9876543210", "9999999999999"]
k = 50000
s = 5
l = 5

print(solution(intStrs, k, s, l))  # [56789, 99999]
