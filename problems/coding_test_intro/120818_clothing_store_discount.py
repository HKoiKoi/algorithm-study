def solution(price):
    if price >= 500000:
        return int(price * 0.8)

    elif price >= 300000:
        return int(price * 0.9)

    elif price >= 100000:
        return int(price * 0.95)

    else:
        return price


price_1 = 150000
price_2 = 580000

print(solution(price_1))  # 142500
print(solution(price_2))  # 464000
