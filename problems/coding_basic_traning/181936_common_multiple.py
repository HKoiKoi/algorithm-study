def solution(number, n, m):
    return int(not ((number % n) or (number % m)))


number_1 = 60
n_1 = 2
m_1 = 3
number_2 = 55
n_2 = 10
m_2 = 5

print(solution(number_1, n_1, m_1))  # 1
print(solution(number_2, n_2, m_2))  # 0
