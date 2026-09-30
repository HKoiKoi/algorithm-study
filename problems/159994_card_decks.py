def solution(cards1, cards2, goal):
    answer = ''
    return answer


test_cards1_1 = ["i", "drink", "water"]
test_cards1_2 = ["i", "water", "drink"]
test_cards2 = ["want", "to"]
test_goal = ["i", "want", "to", "drink", "water"]

print(solution(test_cards1_1, test_cards2, test_goal))  # "Yes"
print(solution(test_cards1_2, test_cards2, test_goal))  # "No"
