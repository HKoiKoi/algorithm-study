# 데이터 삽입

# append() 메서드

test_list = [1, 2, 3]
test_list.append(4)
print(test_list)  # [1, 2, 3, 4]

# + 연산자

test_list = [1, 2, 3]
test_list = test_list + [4, 5]
print(test_list)  # [1, 2, 3, 4, 5]

# insert() 메서드

test_list = [1, 2, 3]
test_list.insert(1, 4)
print(test_list)  # [1, 4, 2, 3]

# 데이터 삭제

# pop()

test_list = [1, 2, 3, 4, 5]
popped_data = test_list.pop(2)
print(test_list)  # [1, 2, 4, 5]
print(f"삭제된 데이터: {popped_data}")  # 삭제된 데이터: 3

# remove()

test_list = [1, 2, 3, 3, 4, 5]
test_list.remove(3)
print(test_list)  # [1, 2, 3, 4, 5]

# 리스트 컴프리헨션

numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print(numbers)  # [1, 2, 3, 4, 5]
print(squares)  # [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]
times = [x * 2 for x in numbers]
print(numbers)  # [1, 2, 3, 4, 5]
print(times)  # [2, 4, 6, 8, 10]

# 유용한 함수

names = ["kim", "nam", "jeon", "park", "lee", "choi", "ham", "kang", "ko", "shin", "yoo", "ham", "cho"]
print(len(names))  # 13
print(names.index("ham"))  # 6
names.sort()
print(names)  # ['cho', 'choi', 'ham', 'ham', 'jeon', 'kang', 'kim', 'ko', 'lee', 'nam', 'park', 'shin', 'yoo']

names = ["kim", "nam", "jeon", "park", "lee", "choi", "ham", "kang", "ko", "shin", "yoo", "ham", "cho"]
names.sort(reverse=True)
print(names)  # ['yoo', 'shin', 'park', 'nam', 'lee', 'ko', 'kim', 'kang', 'jeon', 'ham', 'ham', 'choi', 'cho']

names = ["kim", "nam", "jeon", "park", "lee", "choi", "ham", "kang", "ko", "shin", "yoo", "ham", "cho"]
print(names.count("ham"))  # 2
