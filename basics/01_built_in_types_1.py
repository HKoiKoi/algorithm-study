# 정수형

a = 12
b = 5

print(a + b)  # 덧셈 / 17
print(a - b)  # 뺄셈 / 7
print(a * b)  # 곱셈 / 60
print(a / b)  # 나눗셈 (소수점 O) / 2.4
print(a // b)  # 나눗셈 (소수점 X) / 2
print(a % b)  # 모듈러 연산 (나머지) / 2
print(-a)  # 반대 부호 / -12
print(abs(-a))  # 절대값 / 12
print(a ** b)  # 제곱 연산 / 248832

print(a == b)  # 같은 값인지 비교 / False
print(a != b)  # 같지 않은 값인지 비교 / True
print(a > b)  # 왼쪽 값이 오른쪽 값보다 큰지 비교 / True
print(a < b)  # 왼쪽 값이 오른쪽 값보다 작은지 비교 / False
print(a >= b)  # 왼쪽 값이 오른쪽 값이랑 같거나 더 큰지 비교 / True
print(a <= b)  # 왼쪽 값이 오른쪽 값이랑 같거나 더 작은지 비교 / False

print(a & b)  # AND 연산: 1100 AND 0101 -> 0100 / 4
print(a | b)  # OR 연산: 1100 OR 0101 -> 1101 / 13
print(a ^ b)  # XOR 연산: 1100 XOR 0101 -> 1001 / 9
print(~a)  # NOT 연산: NOT 1100 -> 1111 0011 -> 0000 1100 -> 0000 1101 (2의 보수) / -13
print(a << 2)  # 왼쪽 시프트: 0000 1100 -> 0011 0000 / 48
print(a >> 1)  # 오른쪽 시프트: 1100 -> 0110 / 6

# 파이썬에서 0, "", None 등이 아니면 True
print(a and b)  # 논리 연산 AND: a가 12로 참이므로 b가 0이 아니면 b 반환 / 5
print(a or b)  # 논리 연산 OR: a가 12로 참이므로 b 검사하지 않고 a 반환 / 12
print(not a)  # 논리 연산 NOT: a가 12로 참이므로 False 반환 / False

# 부동 소수형

print(9.1 + 4.4)  # 덧셈 / 13.5
print(9.1 - 4.3)  # 뺄셈 / 4.8
print(9.1 * 4.6)  # 곱셈 / 41.85999999999999
print(9.9 / 4.4)  # 나눗셈 / 2.25
print(9.1 // 4.4)  # 나눗셈 (소수점 X) / 2.0
print(9.1 % 4.4)  # 모듈러 연산 (나머지) / 0.29999999999999893
print(2.1 ** 5.1)  # 제곱 연산 / 43.9863983676249

x = 9.14
y = 4.48
z = 2.7

print(x > y and y < z)  # AND 연산: x > y이 True이므로 y < z의 값에 따라 True/False 반환 / False
print(x < y or y < z)  # OR 연산: x < y가 False이므로 y < z의 값에 따라 True/False 반환 / False
print(not (x > y))  # NOT 연산: x > y가 True이므로 NOT True 반환 / False
