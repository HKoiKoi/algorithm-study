def solution(id_list, report, k):
    reported_dict = {user_id: set() for user_id in id_list}
    mail_count_dict = {user_id: 0 for user_id in id_list}

    for record in report:
        reporter, reported_user = record.split()

        reported_dict[reported_user].add(reporter)

    for reported_user, reporters in reported_dict.items():
        if len(reporters) >= k:
            for reporter in reporters:
                mail_count_dict[reporter] += 1

    return [mail_count_dict[user_id] for user_id in id_list]


id_list_1 = ["muzi", "frodo", "apeach", "neo"]
report_1 = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
k_1 = 2
id_list_2 = ["con", "ryan"]
report_2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
k_2 = 3

print(solution(id_list_1, report_1, k_1))  # [2,1,1,0]
print(solution(id_list_2, report_2, k_2))  # [0,0]
