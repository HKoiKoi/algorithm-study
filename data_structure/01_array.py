# 배열

# 배열 선언

# 일반적인 선언

basic_arr1 = [0, 0, 0, 0, 0, 0]
print(basic_arr1)  # [0, 0, 0, 0, 0, 0]
basic_arr2 = [0] * 6
print(basic_arr2)  # [0, 0, 0, 0, 0, 0]

# 리스트 생성자를 사용하는 방법

numbers = list(range(6))
print(numbers)  # [0, 1, 2, 3, 4, 5]

# 리스트 컴프리헨션을 활용하는 방법

zeros = [0 for _ in range(6)]
print(zeros)  # [0, 0, 0, 0, 0, 0]

# 2차원 배열

two_d_arr = [[1, 2, 3, 4], [2, 4, 6, 8], [1, 3, 5, 7]]
print(two_d_arr)  # [[1, 2, 3, 4], [2, 4, 6, 8], [1, 3, 5, 7]]
# two_d_arr[2][3]에 저장된 값을 9로 변경
two_d_arr[2][1] = 9
print(two_d_arr[2][1])  # 9

# 리스트 컴프리헨션을 활용하여 선언
# 크기가 3 * 4 리스트
two_d_arr = [[i] * 4 for i in range(3)]
print(two_d_arr)  # [[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2]]
