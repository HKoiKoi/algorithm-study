stack = []  # 스택 리스트 초기화
max_size = 10  # 스택의 최대 크기 정의


# 가득 찼는지 확인하는 함수
def isFull(stack):
    return len(stack) == max_size


# 비었는지 확인하는 함수
def isEmpty(stack):
    return len(stack) == 0


# 푸시 함수
def push(stack, item):
    if isFull(stack):
        print("Full")
    else:
        stack.append(item)
        print("Pushed")


# 팝 함수
def pop(stack):
    if isEmpty(stack):
        print("Empty")
        return None
    else:
        return stack.pop()


def push(stack, item):
    if len(stack) == 0:
        return
