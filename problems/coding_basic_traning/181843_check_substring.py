def solution(my_string, target):
    return 1 if target in my_string else 0


my_string = "banana"
target_1 = "ana"
target_2 = "wxyz"

print(solution(my_string, target_1))  # 1
print(solution(my_string, target_2))  # 0
