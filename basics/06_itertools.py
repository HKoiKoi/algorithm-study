from itertools import permutations, combinations, combinations_with_replacement, product

# 순열
data = ["A", "B", "C"]
result = list(permutations(data, 2))  # data에서 2개를 뽑아 나열하는 모든 순열
print(result)  # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 조합
result = list(combinations(data, 2))  # data에서 2개를 뽑는 모든 조합
print(result)  # [('A', 'B'), ('A', 'C'), ('B', 'C')]

result = list(combinations_with_replacement(data, 2))  # data에서 중복을 허용하여 2개를 뽑는 모든 조합
print(result)  # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

# 데카르트 곱

# 두 개 이상의 리스트에서 모든 조합을 구할 때
list1 = ['A', 'B']
list2 = [1, 2]
result1 = list(product(list1, list2))
print(result1)  # [('A', 1), ('A', 2), ('B', 1), ('B', 2)]

# 하나의 리스트에서 중복을 허용하여 뽑는 순열(중복 순열)을 구할 때
data = ["A", "B"]
result2 = list(product(data, repeat=2))
print(result2)  # [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]
