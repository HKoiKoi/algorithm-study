from collections import deque


def solution(info, edges):
    answer = 0

    # 트리 생성 (노드, 자식 노드)
    tree = [[] for _ in range(len(info))]
    for edge in edges:
        tree[edge[0]].append(edge[1])

    # (현재 노드, 양의 수, 늑대의 수, 인접 노드)
    queue = deque([(0, 1, 0, set())])

    # BFS
    while queue:
        curr, sheep_cnt, wolf_cnt, next_nodes = queue.popleft()

        answer = max(answer, sheep_cnt)
        next_nodes.update(tree[curr])

        # 인접 노드를 돌면서 늑대인지 양인지 체크
        for next_node in next_nodes:
            # 늑대인 경우
            if info[next_node] == 1:
                if sheep_cnt > wolf_cnt + 1:
                    queue.append((next_node, sheep_cnt, wolf_cnt + 1, next_nodes - {next_node}))

            # 양인 경우
            else:
                queue.append((next_node, sheep_cnt + 1, wolf_cnt, next_nodes - {next_node}))

    return answer


info_1 = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
info_2 = [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
edges_1 = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
edges_2 = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]

print(solution(info_1, edges_1))  # 5
print(solution(info_2, edges_2))  # 5
