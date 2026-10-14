def is_movable(x, y):
    if x > 5 or x < -5 or y > 5 or y < -5:
        return False

    return True


def move(dir, x, y):
    if dir == "U":
        return x, y + 1
    elif dir == "D":
        return x, y - 1
    elif dir == "L":
        return x - 1, y
    else:
        return x + 1, y


def solution(dirs):
    x, y = 0, 0
    answer = set()

    for dir in dirs:
        nx, ny = move(dir, x, y)

        if not is_movable(nx, ny):
            continue

        answer.add((x, y, nx, ny))
        answer.add((nx, ny, x, y))

        x, y = nx, ny

    return len(answer) // 2


dirs_1 = "ULURRDLLU"
dirs_2 = "LULLLLLLU"

print(solution(dirs_1))  # 7
print(solution(dirs_2))  # 7
