queue = []

# 큐에 데이터 추가
queue.append(1)
queue.append(2)
queue.append(3)

# 큐의 맨 앞 데이터 제거
first_item = queue.pop(0)
print(first_item)  # 1

# 큐에 데이터 추가
queue.append(4)
queue.append(5)

# 큐의 맨 앞 데이터 제거
first_item = queue.pop(0)
print(first_item)  # 2

from collections import deque

queue = deque()

# 큐에 데이터 추가
queue.append(1)
queue.append(2)
queue.append(3)

# 큐의 맨 앞 데이터 제거
first_item = queue.popleft()
print(first_item)  # 1

# 큐에 데이터 추가
queue.append(4)
queue.append(5)

# 큐의 맨 앞 데이터 제거
first_item = queue.popleft()
print(first_item)  # 2

import time

lst = list(range(100000))
dq = deque(range(100000))

# pop(0) 성능 측정
start_time = time.time()
for i in range(100000):
    lst.pop(0)
print("pop(0) 소요 시간: ", time.time() - start_time)  # pop(0) 소요 시간:  0.5691769123077393

# popleft() 성능 측정
start_time = time.time()
for i in range(100000):
    dq.popleft()
print("deque의 popleft() 소요 시간: ", time.time() - start_time)  # deque의 popleft() 소요 시간:  0.0027320384979248047
