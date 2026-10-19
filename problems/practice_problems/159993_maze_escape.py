from collections import deque


def solution(maps):
    rows = len(maps)
    cols = len(maps[0])

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    start_pos, lever_pos, exit_pos = None, None, None

    for i in range(rows):
        for j in range(cols):
            if maps[i][j] == "S":
                start_pos = (i, j)
            elif maps[i][j] == "L":
                lever_pos = (i, j)
            elif maps[i][j] == "E":
                exit_pos = (i, j)

    def bfs(start, target):
        queue = deque([(start[0], start[1], 0)])
        visited = [[False] * cols for _ in range(rows)]
        visited[start[0]][start[1]] = True

        while queue:
            row, col, dist = queue.popleft()

            if (row, col) == target:
                return dist

            for i in range(4):
                nr = row + dr[i]
                nc = col + dc[i]

                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and maps[nr][nc] != "X":
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))

        return -1

    to_lever = bfs(start_pos, lever_pos)
    if to_lever == -1:
        return -1

    to_exit = bfs(lever_pos, exit_pos)
    if to_exit == -1:
        return -1

    return to_lever + to_exit


maps_1 = ["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]
maps_2 = ["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]

print(solution(maps_1))  # 16
print(solution(maps_2))  # -1
