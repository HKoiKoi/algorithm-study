def solution(want, number, discount):
    answer = 0
    return answer


test_want1 = ["banana", "apple", "rice", "pork", "pot"]
test_number1 = [3, 2, 2, 2, 1]
test_discount1 = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",
                  "banana", "apple", "banana"]
test_want2 = ["apple"]
test_number2 = [10]
test_discount2 = ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]

print(solution(test_want1, test_number1, test_discount1))  # 3
print(solution(test_want2, test_number2, test_discount2))  # 0
