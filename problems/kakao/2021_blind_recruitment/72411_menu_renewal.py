from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    for course_size in course:
        candidates = []

        for order in orders:
            comb = combinations(sorted(order), course_size)
            candidates.extend(comb)

        order_count = Counter(candidates)

        if order_count:
            max_count = max(order_count.values())

            if max_count >= 2:
                for menu, count in order_count.items():
                    if count == max_count:
                        answer.append("".join(menu))

    return sorted(answer)


orders_1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course_1 = [2, 3, 4]
orders_2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course_2 = [2, 3, 5]
orders_3 = ["XYZ", "XWY", "WXA"]
course_3 = [2, 3, 4]

print(solution(orders_1, course_1))  # ["AC", "ACDE", "BCFG", "CDE"]
print(solution(orders_2, course_2))  # ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(orders_3, course_3))  # ["WX", "XY"]
