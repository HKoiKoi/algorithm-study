import math
import sys

a = 0.1 + 0.2
print(a)  # 0.3이 아니라 0.30000000000000004
print(a == 0.3)  # False

print(sys.float_info.epsilon)  # 2.220446049250313e-16

b = 0.3

print(math.isclose(a, b))  # True
