def solution(angle):
    if angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif angle == 180:
        return 4
    else:
        return 3


angle_1 = 70
angle_2 = 91
angle_3 = 180

print(solution(angle_1))  # 1
print(solution(angle_2))  # 3
print(solution(angle_3))  # 4
