def solution(answers):
    methods = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]

    scores = [0] * 3

    winner = []

    for i, answer in enumerate(answers):
        first_index = i % len(methods[0])
        second_index = i % len(methods[1])
        third_index = i % len(methods[2])

        if answer == methods[0][first_index]:
            scores[0] += 1

        if answer == methods[1][second_index]:
            scores[1] += 1

        if answer == methods[2][third_index]:
            scores[2] += 1

    max_count = max(scores)

    for i, score in enumerate(scores):
        if score == max_count:
            winner.append(i + 1)

    return winner


answers1 = [1, 2, 3, 4, 5]
answers2 = [1, 3, 2, 4, 2]
answers3 = [2, 1, 2, 3, 2, 4, 2, 5]
answers4 = [4, 4]

print(solution(answers1))
print(solution(answers2))
print(solution(answers3))
print(solution(answers4))
