# 리스트

test_list = [1, 2, 3, 4, 5]
test_list2 = [1, 3, 5] + [7, 9]
test_list3 = list(test_list)
print(test_list)  # [1, 2, 3, 4, 5]
print(test_list2)  # [1, 3, 5, 7, 9]
print(test_list3)  # [1, 2, 3, 4, 5]

test_list = [1, 2, 4]

# 값 추가
test_list.append(6)
print(test_list, test_list[2])  # [1, 2, 4, 6] 4

# 인덱싱으로 값 삭제
del test_list[2]  # del: 인덱스 위치에 있는 원소 지우는 메서드
print(test_list)  # [1, 2, 6]

#   인덱스:  0  1  2  3  4
test_list = [1, 2, 3, 4, 5]
#   인덱스: -5 -4 -3 -2 -1
print(test_list[0:2])  # [1, 2]
print(test_list[1:])  # [2, 3, 4, 5]
print(test_list[3:4])  # [4]
print(test_list[-4:-2])  # [2, 3]

numbers = [x for x in range(5)]
print(numbers)  # [0, 1, 2, 3, 4]

cartesian_product = [(x, y) for x in range(2) for y in range(3)]
print(cartesian_product)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]


def square(x):
    return x * x


squares = [square(x) for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

squares = list(map(lambda x: x * x, range(5)))
print(squares)  # [0, 1, 4, 9, 16]

even_numbers = [x for x in range(5) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4]

numbers = [x if x % 2 == 0 else -x for x in range(5)]
print(numbers)  # [0, -1, 2, -3, 4]

test_dict = {}

# 딕셔너리 값 삽입
test_dict["ham"] = 1
test_dict["kim"] = 2
test_dict["nam"] = 3
# 딕셔너리 값 출력
print(test_dict)  # {'ham': 1, 'kim': 2, 'nam': 3}

key = "ham"
if key in test_dict:
    value = test_dict[key]
    print(f"{key}: {value}")  # ham: 1
else:
    print(f"{key}: None")

test_dict["nam"] = 4
print(test_dict)  # {'ham': 1, 'kim': 2, 'nam': 4}

del test_dict["kim"]
print(test_dict)  # {'ham': 1, 'nam': 4}

# del test_dict["woo"]  # KeyError: 'woo' 발생

test_dict = {"ham": 1, "kim": 2, "nam": 3}

key = "woo"

if key in test_dict:
    print(f"{key}: {test_dict[key]}")
else:
    print(f"{key}: None")  # woo: None

# 빈 셋 생성
empty_set = set()
print(empty_set)  # set()

# 리스트를 셋으로 변환
list_to_set = set([1, 2, 3, 3, 2])
print(list_to_set)  # {1, 2, 3}

# 중괄호를 이용한 셋 생성
set_from_braces = {63, 2, 10, 16}
print(set_from_braces)  # {16, 2, 10, 63}

# 문자열을 셋으로 변환 (중복 문자 제거)
string_to_set = set("helloworld")
print(string_to_set)  # {'w', 'h', 'r', 'l', 'd', 'e', 'o'}

# 튜플을 셋으로 변환
tuple_to_set = set((1, 2, 3, 3, 4))
print(tuple_to_set)  # {1, 2, 3, 4}

# 셋 컴프리헨션을 이용한 초기화
comprehension_set = {x for x in range(5) if x % 2 == 0}
print(comprehension_set)  # {0, 2, 4}

# add() 메서드: 하나의 원소 추가
test_set = {1, 3, 5, 7, 11}
test_set.add(13)
print(test_set)  # {1, 3, 5, 7, 11, 13}

# update() 메서드: 여러 원소 한 번에 추가
test_set.update([17, 19, 23])
print(test_set)  # {1, 3, 5, 7, 11, 13, 17, 19, 23}

# remove() 메서드: 특정 원소 제거 (제거 대상 원소가 없는 경우 오류 발생)
test_set = {2, 4, 6, 8}
test_set.remove(2)
print(test_set)  # {8, 4, 6}

# test_set.remove(5)  # KeyError: 5 발생

test_set.discard(6)
print(test_set)  # {8, 4}

test_set.discard(5)  # 없는 원소를 제거하려고 해도 오류가 발생하지 않음.
print(test_set)  # {8, 4}

test_set.clear()
print(test_set)  # set()

# union() 메서드를 이용한 합집합
set1 = {2, 4, 8}
set2 = {4, 8, 16}
union_set = set1.union(set2)
print(union_set)  # {16, 2, 4, 8}

# | 연산자를 사용한 합집합
set1 |= set2  # set1에 set2의 원소 추가
print(set1)  # {16, 2, 4, 8}

# intersection() 메서드를 이용한 교집합
set1 = {3, 6, 9}
set2 = {2, 4, 6}
intersection_set = set1.intersection(set2)
print(intersection_set)  # {6}

# & 연산자를 사용한 교집합
set1 &= set2  # set1에 set2의 교집합 저장
print(set1)  # {6}

# difference() 메서드를 이용한 차집합
set1 = {2, 4, 6}
set2 = {3, 6, 9}
difference_set = set1.difference(set2)
print(difference_set)  # {2, 4}

# - 연산자를 사용한 차집합
set1 -= set2  # set1에 set2와의 차집합 저장
print(set1)  # {2, 4}

test_tuple = (1, 2, 3)

# 인덱싱
print(test_tuple[0])  # 1
print(test_tuple[1])  # 2
print(test_tuple[2])  # 3

# 슬라이싱
print(test_tuple[1:])  # (2, 3)
print(test_tuple[:2])  # (1, 2)
print(test_tuple[1:2])  # (2,)

string = "Hello World!"
string2 = 'Hello World!'

string = "Hello"
string += " World!"
print(string)  # Hello World!   <- 기존 "Hello"에 " World!"를 추가하는 게 아니라 "Hello World!"라는 새로운 문자열을 참조한다.

#  문자열을 리스트에 담아두고 한 번에 결합
string_list = ["Hello", " World!"]
final_string = "".join(string_list)
print(final_string)  # Hello World!

string = "Hello World!"
string = string.replace("l", "")  # "l"을 찾아 모두 삭제
print(string)  # Heo Word!
