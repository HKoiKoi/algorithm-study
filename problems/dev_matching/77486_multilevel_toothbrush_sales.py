def solution(enroll, referral, seller, amount):
    parent = dict(zip(enroll, referral))
    total = {name: 0 for name in enroll}

    for name, num in zip(seller, amount):
        sales = num * 100

        curr = name
        while curr != "-" and sales > 0:
            fee = sales // 10
            total[curr] += sales - fee

            curr = parent[curr]
            sales = fee

    return list(total.values())


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller_1 = ["young", "john", "tod", "emily", "mary"]
seller_2 = ["sam", "emily", "jaimie", "edward"]
amount_1 = [12, 4, 2, 5, 10]
amount_2 = [2, 3, 5, 4]

print(solution(enroll, referral, seller_1, amount_1))  # [360, 958, 108, 0, 450, 18, 180, 1080]
print(solution(enroll, referral, seller_2, amount_2))  # [0, 110, 378, 180, 270, 450, 0, 0]
