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


test_want1 = ["banana", "apple", "rice", "pork", "pot"]
test_number1 = [3, 2, 2, 2, 1]
test_discount1 = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",
                  "banana", "apple", "banana"]
test_want2 = ["apple"]
test_number2 = [10]
test_discount2 = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]

print(solution(test_want1, test_number1, test_discount1))  # 3
print(solution(test_want2, test_number2, test_discount2))  # 0
