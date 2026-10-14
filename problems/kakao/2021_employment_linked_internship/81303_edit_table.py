def solution(n, k, cmd):
    deleted = []
    result = ["O"] * n

    up = [i - 1 for i in range(n)]
    down = [i + 1 for i in range(n)]
    down[-1] = -1

    for c in cmd:
        if c == "C":
            up_node, down_node = up[k], down[k]

            deleted.append((k, up_node, down_node))

            if up_node != -1:
                down[up_node] = down_node
            if down_node != -1:
                up[down_node] = up_node

            k = down_node if down_node != -1 else up_node

        elif c == "Z":
            node, up_node, down_node = deleted.pop()

            if up_node != -1:
                down[up_node] = node
            if down_node != -1:
                up[down_node] = node

        else:
            move, num = c.split()

            if move == "U":
                for _ in range(int(num)):
                    k = up[k]


            else:
                for _ in range(int(num)):
                    k = down[k]

    for node, _, _ in deleted:
        result[node] = "X"

    return "".join(result)


n = 8
k = 2
cmd_1 = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
cmd_2 = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]

print(solution(n, k, cmd_1))  # "OOOOXOOO"
print(solution(n, k, cmd_2))  # "OOXOXOOO"
