def solution(enroll, referral, seller, amount):
    answer = []
    return answer


enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller_1 = ["young", "john", "tod", "emily", "mary"]
seller_2 = ["sam", "emily", "jaimie", "edward"]
amount_1 = [12, 4, 2, 5, 10]
amount_2 = [2, 3, 5, 4]

print(solution(enroll, referral, seller_1, amount_1))  # [360, 958, 108, 0, 450, 18, 180, 1080]
print(solution(enroll, referral, seller_2, amount_2))  # [0, 110, 378, 180, 270, 450, 0, 0]
