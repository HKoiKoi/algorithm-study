import math


def solution(progresses, speeds):
    answer = []

    deploy_day = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    max_day = deploy_day[0]
    count = 0

    for i in range(len(progresses)):
        if deploy_day[i] <= max_day:
            count += 1
        else:
            answer.append(count)

            count = 1

            max_day = deploy_day[i]

    answer.append(count)

    return answer


progresses_1 = [93, 30, 55]
speeds_1 = [1, 30, 5]
progresses_2 = [95, 90, 99, 99, 80, 99]
speeds_2 = [1, 1, 1, 1, 1, 1]

print(solution(progresses_1, speeds_1))  # [2, 1]
print(solution(progresses_2, speeds_2))  # [1, 3, 2]
