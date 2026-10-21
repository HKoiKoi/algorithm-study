def solution(money):
    return [money // 5500, money % 5500]


money_1 = 5500
money_2 = 15000

print(solution(money_1))  # [1, 0]
print(solution(money_2))  # [2, 4000]
