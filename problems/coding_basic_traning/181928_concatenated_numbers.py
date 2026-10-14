def solution(num_list):
    odd = int("".join(str(num) for num in num_list if num % 2 != 0))
    even = int("".join(str(num) for num in num_list if num % 2 == 0))

    return odd + even


num_list_1 = [3, 4, 5, 2, 1]
num_list_2 = [5, 7, 8, 3]

print(solution(num_list_1))  # 393
print(solution(num_list_2))  # 581
