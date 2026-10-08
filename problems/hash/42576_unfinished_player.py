from collections import Counter


def solution(participant, completion):
    participant_count = Counter(participant)
    completion_count = Counter(completion)

    unfinished_player = participant_count - completion_count

    return list(unfinished_player.keys())[0]


test_participant1 = ["leo", "kiki", "eden"]
test_completion1 = ["eden", "kiki"]
test_participant2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
test_completion2 = ["josipa", "filipa", "marina", "nikola"]
test_participant3 = ["mislav", "stanko", "mislav", "ana"]
test_completion3 = ["stanko", "ana", "mislav"]

print(solution(test_participant1, test_completion1))  # leo
print(solution(test_participant2, test_completion2))  # vinko
print(solution(test_participant3, test_completion3))  # mislav
