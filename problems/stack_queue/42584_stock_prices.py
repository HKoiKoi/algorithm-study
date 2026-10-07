def solution(prices):
    length = len(prices)
    answer = [0] * length
    stack = []

    for i in range(length):
        # 스택이 비어있지 않고 가격이 떨어진 경우
        while stack and prices[stack[-1]] > prices[i]:
            # 이전 시간
            past_idx = stack.pop()

            # 가격이 떨어졌으면 현재 초와 이전 시간 간의 차이가 가격이 떨어지지 않은 기간임을 나타낸다.
            answer[past_idx] = i - past_idx

        # 가격이 떨어지지 않은 경우 시간 스택에 추가한다.
        stack.append(i)

    # 다 끝내고 남은 주식들의 기간을 체크한다.
    while stack:
        past_idx = stack.pop()

        # 인덱스는 0부터 시작이므로 전체 시간에 - 1 해서 맞춰야 한다.
        answer[past_idx] = length - 1 - past_idx

    return answer


test_prices = [1, 2, 3, 2, 3]

print(solution(test_prices))  # [4, 3, 1, 1, 0]
