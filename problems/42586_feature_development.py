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


test_progresses1 = [93, 30, 55]
test_speeds1 = [1, 30, 5]
test_progresses2 = [95, 90, 99, 99, 80, 99]
test_speeds2 = [1, 1, 1, 1, 1, 1]

print(solution(test_progresses1, test_speeds1))  # [2, 1]
print(solution(test_progresses2, test_speeds2))  # [1, 3, 2]
