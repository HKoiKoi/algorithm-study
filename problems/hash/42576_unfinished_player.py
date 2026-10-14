from collections import Counter


def solution(participant, completion):
    participant_count = Counter(participant)
    completion_count = Counter(completion)

    unfinished_player = participant_count - completion_count

    return list(unfinished_player.keys())[0]


participant_1 = ["leo", "kiki", "eden"]
completion_1 = ["eden", "kiki"]
participant_2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion_2 = ["josipa", "filipa", "marina", "nikola"]
participant_3 = ["mislav", "stanko", "mislav", "ana"]
completion_3 = ["stanko", "ana", "mislav"]

print(solution(participant_1, completion_1))  # leo
print(solution(participant_2, completion_2))  # vinko
print(solution(participant_3, completion_3))  # mislav
