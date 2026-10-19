import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, value, info, left=None, right=None):
        self.value = value
        self.info = info
        self.left = left
        self.right = right

    def has_left(self):
        return self.left is not None

    def has_right(self):
        return self.right is not None


def preorder(node, result):
    # 나, 왼쪽, 오른쪽
    result.append(node.value)

    if node.left is not None:
        preorder(node.left, result)

    if node.right is not None:
        preorder(node.right, result)


def postorder(node, result):
    # 왼쪽, 오른족, 나
    if node.left is not None:
        postorder(node.left, result)

    if node.right is not None:
        postorder(node.right, result)

    result.append(node.value)


def make_binary_tree(nodeinfo):
    nodes = [i for i in range(1, len(nodeinfo) + 1)]
    nodes.sort(key=lambda idx: (-nodeinfo[idx - 1][1], nodeinfo[idx - 1][0]))

    root = None

    for idx in nodes:
        curr = Node(idx, nodeinfo[idx - 1])

        if root is None:
            root = curr
            continue

        parent = root

        while True:
            # 왼쪽 자식
            if curr.info[0] < parent.info[0]:
                # 만약 왼쪽 자식이 있으면 왼쪽 자식과 비교해야 함.
                if parent.has_left():
                    parent = parent.left
                else:
                    parent.left = curr
                    break

            # 오른쪽 자식
            else:
                # 만약 오른쪽 자식이 있으면 오른쪽 자식과 비교해야 함.
                if parent.has_right():
                    parent = parent.right
                else:
                    parent.right = curr
                    break

    return root


def solution(nodeinfo):
    answer = [[], []]

    root = make_binary_tree(nodeinfo)

    preorder(root, answer[0])
    postorder(root, answer[1])

    return answer


nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]

print(solution(nodeinfo))  # [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]
