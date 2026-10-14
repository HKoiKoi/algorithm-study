from collections import Counter


def solution(want, number, discount):
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    possible_sign_up = 0

    for i in range(len(discount) - 9):
        discount_10d = discount[i:i + 10]
        discount_10d_dict = Counter(discount_10d)
        if want_dict == discount_10d_dict:
            possible_sign_up += 1

    return possible_sign_up


want_1 = ["banana", "apple", "rice", "pork", "pot"]
number_1 = [3, 2, 2, 2, 1]
discount_1 = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",
              "banana", "apple", "banana"]
want_2 = ["apple"]
number_2 = [10]
discount_2 = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]

print(solution(want_1, number_1, discount_1))  # 3
print(solution(want_2, number_2, discount_2))  # 0
