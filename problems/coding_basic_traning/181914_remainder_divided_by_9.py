def solution(number):
    return sum((map(int, number))) % 9


number_1 = "123"
number_2 = "78720646226947352489"

print(solution(number_1))  # 6
print(solution(number_2))  # 2
