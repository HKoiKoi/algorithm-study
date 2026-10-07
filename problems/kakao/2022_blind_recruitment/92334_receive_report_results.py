def solution(id_list, report, k):
    answer = []
    return answer


test_id_list1 = ["muzi", "frodo", "apeach", "neo"]
test_report1 = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
test_k1 = 2
test_id_list2 = ["con", "ryan"]
test_report2 = ["ryan con", "ryan con", "ryan con", "ryan con"]
test_k2 = 3

print(solution(test_id_list1, test_report1, test_k1))  # [2,1,1,0]
print(solution(test_id_list2, test_report2, test_k2))  # [0,0]
