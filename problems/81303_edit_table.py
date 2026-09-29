def solution(n, k, cmd):
    answer = ''
    return answer


test_n = 8
test_k = 2
test_cmd1 = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
test_cmd2 = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]

print(solution(test_n, test_k, test_cmd1))  # "OOOOXOOO"
print(solution(test_n, test_k, test_cmd2))  # "OOXOXOOO"
