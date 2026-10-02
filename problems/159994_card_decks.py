from collections import deque


def solution(cards1, cards2, goal):
    cards1_queue = deque(cards1)
    cards2_queue = deque(cards2)

    for s in goal:
        if cards1_queue and cards1_queue[0] == s:
            cards1_queue.popleft()

        elif cards2_queue and cards2_queue[0] == s:
            cards2_queue.popleft()

        else:
            return "No"

    return "Yes"


test_cards1_1 = ["i", "drink", "water"]
test_cards1_2 = ["i", "water", "drink"]
test_cards2 = ["want", "to"]
test_goal = ["i", "want", "to", "drink", "water"]

print(solution(test_cards1_1, test_cards2, test_goal))  # "Yes"
print(solution(test_cards1_2, test_cards2, test_goal))  # "No"
