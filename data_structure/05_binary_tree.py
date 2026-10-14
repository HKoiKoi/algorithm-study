# 전위 순회
def preorder(nodes, idx, result):
    # idx가 노드 리스트의 길이보다 작을 때
    if idx < len(nodes):
        # 1. 부모 노드
        result.append(str(nodes[idx]))

        # 2. 왼쪽 자식 노드
        preorder(nodes, idx * 2 + 1, result)

        # 3. 오른쪽 자식 노드
        preorder(nodes, idx * 2 + 2, result)


nodes = [1, 2, 3, 4, 5, 6, 7]
result = []

preorder(nodes, 0, result)

print(" ".join(result))  # 1 2 4 5 3 6 7


# 중위 순회
def inorder(nodes, idx, result):
    # idx가 노드 리스트의 길이보다 작을 때
    if idx < len(nodes):
        # 1. 왼쪽 자식 노드
        inorder(nodes, idx * 2 + 1, result)

        # 2. 부모 노드
        result.append(str(nodes[idx]))

        # 3. 오른쪽 자식 노드
        inorder(nodes, idx * 2 + 2, result)


nodes = [1, 2, 3, 4, 5, 6, 7]
result = []

inorder(nodes, 0, result)

print(" ".join(result))  # 4 2 5 1 6 3 7


# 후위 순회
def postorder(nodes, idx, result):
    # idx가 노드 리스트의 길이보다 작을 때
    if idx < len(nodes):
        # 1. 왼쪽 자식 노드
        postorder(nodes, idx * 2 + 1, result)

        # 2. 오른쪽 자식 노드
        postorder(nodes, idx * 2 + 2, result)

        # 3. 부모 노드
        result.append(str(nodes[idx]))


nodes = [1, 2, 3, 4, 5, 6, 7]
result = []

postorder(nodes, 0, result)

print(" ".join(result))  # 4 5 2 6 7 3 1


# 이진 탐색 트리 구현
# 노드 클래스 정의
class Node:
    # 노드 클래스 생성자
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# 이진 탐색 트리 클래스
class BST:
    # 초기에 아무 노드도 없는 상태
    def __init__(self):
        self.root = None

    # 루트 노드부터 시작해서 이진 탐색 트리 규칙에 맞는 위치에 새 노드 삽입
    def insert(self, key):
        # 루트 노드가 없는 경우 새로운 노드를 루트 노드로 추가
        if not self.root:
            self.root = Node(key)
        else:
            curr = self.root

            while True:
                # 삽입하려는 값이 현재 노드의 값보다 작은 경우 왼쪽 자식 노드로 이동
                if key < curr.val:
                    if curr.left:
                        curr = curr.left
                    else:
                        curr.left = Node(key)
                        break
                # 삽입하려는 값이 현재 노드의 값보다 큰 경우 오른쪽 자식 노드로 이동
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = Node(key)
                        break

    # 이진 탐색 규칙에 따라 특정값이 있는지 확인 (루트 노드부터 시작)
    def search(self, key):
        curr = self.root

        # 현재 노드가 존재하고, 찾으려는 값과 현재 노드의 값이 같지 않은 경우 반복
        while curr and curr.val != key:
            if key < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        return curr


def solution(lst, search_lst):
    bst = BST()

    # 리스트의 각 요소를 이용해서 이진 탐색 트리 생성
    for key in lst:
        bst.insert(key)

    result = []

    # 검색 리스트의 각 요소를 이진 탐색 트리에서 검색하고 검색 결과를 리스트에 추가
    for search_val in search_lst:
        if bst.search(search_val):
            result.append(True)
        else:
            result.append(False)

    return result


test_lst_1 = [5, 3, 8, 4, 2, 1, 7, 10]
test_search_lst_1 = [1, 2, 5, 6]
test_lst_2 = [1, 3, 5, 7, 9]
test_search_lst_2 = [2, 4, 6, 8, 10]

print(solution(test_lst_1, test_search_lst_1))  # [True, True, True, False]
print(solution(test_lst_2, test_search_lst_2))  # [False, False, False, False, False]
