def solution(n):
    # n * n 이차원 배열을 0으로 초기화
    answer = [[0] * n for _ in range(n)]

    # 행과 열의 이동 값을 배열로 구분한다.
    move_row = [0, 1, 0, -1]
    move_col = [1, 0, -1, 0]

    row, col = 0, 0
    direction = 0  # 0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위

    for number in range(1, n ** 2 + 1):
        answer[row][col] = number

        next_row = row + move_row[direction]
        next_col = col + move_col[direction]

        # 1. 행과 열이 0부터 n - 1인지 체크
        # 2. 해당 값이 0인지 체크
        # 둘에 해당하지 않으면 방향 바꿔야 함.
        if not (0 <= next_row < n and 0 <= next_col < n and answer[next_row][next_col] == 0):
            # 0, 1, 2, 3, 0, 1, 2, 3, 반복
            direction = (direction + 1) % 4

            next_row = row + move_row[direction]
            next_col = col + move_col[direction]

        row = next_row
        col = next_col

    return answer


n_1 = 4
n_2 = 5

print(solution(n_1))  # [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
print(solution(
    n_2))  # [[1, 2, 3, 4, 5], [16, 17, 18, 19, 6], [15, 24, 25, 20, 7], [14, 23, 22, 21, 8], [13, 12, 11, 10, 9]]
