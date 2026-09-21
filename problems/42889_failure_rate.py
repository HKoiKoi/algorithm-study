def solution(N, stages):
    # 현재 스테이지에 남아있는 사람을 담은 stay 배열
    # 인덱스: 스테이지
    # 값: 남아 있는 사람
    stay = [0] * (N + 2)

    for stage in stages:
        stay[stage] += 1

    print(stay)

    # 실패율 구하기
    failures = {}
    players = len(stages)

    # 각 스테이지를 돌면서 실패율 구하고
    # 다음 스테이지에서는 지금 스테이지의 인원 빼야함.
    for i in range(1, N + 1):
        if stay[i] == 0:
            failures[i] = 0
        else:
            failures[i] = stay[i] / players
            players -= stay[i]

    print(failures)

    answer = sorted(failures, key=lambda x: failures[x], reverse=True)

    return answer


test_n_1 = 5
test_stages_1 = [2, 1, 2, 6, 2, 4, 3, 3]
test_n_2 = 4
test_stages_2 = [4, 4, 4, 4, 4]

print(solution(test_n_1, test_stages_1))
print(solution(test_n_2, test_stages_2))
