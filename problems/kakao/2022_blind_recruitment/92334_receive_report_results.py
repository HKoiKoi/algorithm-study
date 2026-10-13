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


test_id_list1 = ["muzi", "frodo", "apeach", "neo"]
test_report1 = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
test_k1 = 2
test_id_list2 = ["con", "ryan"]
test_report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
test_k2 = 3

print(solution(test_id_list1, test_report1, test_k1))  # [2,1,1,0]
print(solution(test_id_list2, test_report2, test_k2))  # [0,0]
