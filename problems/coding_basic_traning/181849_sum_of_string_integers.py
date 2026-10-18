def solution(num_str):
    return sum(map(int, num_str))


num_str_1 = "123456789"
num_str_2 = "1000000"

print(solution(num_str_1))  # 45
print(solution(num_str_2))  # 1
