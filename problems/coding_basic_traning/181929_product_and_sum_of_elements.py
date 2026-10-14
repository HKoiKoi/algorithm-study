def solution(num_list):
    product = 1
    sum = 0

    for num in num_list:
        product *= num
        sum += num

    return int(product < sum ** 2)


test_num_list_1 = [3, 4, 5, 2, 1]
test_num_list_2 = [5, 7, 8, 3]

print(solution(test_num_list_1))  # 1
print(solution(test_num_list_2))  # 0
