def solution(orders, course):
    answer = []
    return answer


test_orders1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
test_course1 = [2, 3, 4]
test_orders2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
test_course2 = [2, 3, 5]
test_orders3 = ["XYZ", "XWY", "WXA"]
test_course3 = [2, 3, 4]

print(solution(test_orders1, test_course1))  # ["AC", "ACDE", "BCFG", "CDE"]
print(solution(test_orders2, test_course2))  # ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(test_orders3, test_course3))  # ["WX", "XY"]
