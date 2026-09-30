def grab_doll(board, col):
    for row in range(len(board)):
        if board[row][col] != 0:
            doll = board[row][col]
            board[row][col] = 0
            return doll

    return 0


def solution(board, moves):
    popped_dolls = 0
    basket = []

    for move in moves:
        col = move - 1

        doll = grab_doll(board, col)

        if doll == 0:
            continue

        if basket and basket[-1] == doll:
            basket.pop()
            popped_dolls += 2
        else:
            basket.append(doll)

    return popped_dolls


test_board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(test_board, moves))  # 4
