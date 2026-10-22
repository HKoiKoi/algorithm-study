PRICE_LAMB_SKEWER = 12000
PRICE_DRINK = 2000


def solution(n, k):
    free_drink = n // 10

    return (PRICE_LAMB_SKEWER * n) + (PRICE_DRINK * (k - free_drink))


n_1 = 10
k_1 = 3
n_2 = 64
k_2 = 6

print(solution(n_1, k_1))  # 124000
print(solution(n_2, k_2))  # 768000
