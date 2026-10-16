from collections import Counter


def solution(a, b, c, d):
    count = Counter((a, b, c, d))
    size = len(count)

    if size == 4:
        return min(a, b, c, d)
    elif size == 1:
        return 1111 * a
    elif size == 3:
        q, r = 0, 0

        for key, val in count.items():
            if val == 1:
                if q:
                    r = key
                else:
                    q = key

        return q * r
    else:
        p, q = 0, 0
        flag = False

        for key, val in count.items():
            if val == 1:
                q = key
            elif val == 2:
                if p:
                    q = key
                else:
                    p = key

                flag = True
            else:
                p = key

        if flag:
            return (p + q) * abs(p - q)

        return (10 * p + q) ** 2


def solution_2(a, b, c, d):
    counts = Counter([a, b, c, d]).most_common()

    if len(counts) == 1:
        return counts[0][0] * 1111
    elif len(counts) == 2:
        p, count_p = counts[0]
        q, count_q = counts[1]

        if count_p != count_q:
            return (10 * p + q) ** 2
        else:
            return (p + q) * abs(p - q)
    elif len(counts) == 3:
        return counts[1][0] * counts[2][0]
    else:
        return min(a, b, c, d)


a_1 = 2
b_1 = 2
c_1 = 2
d_1 = 2
a_2 = 4
b_2 = 1
c_2 = 4
d_2 = 4
a_3 = 6
b_3 = 3
c_3 = 3
d_3 = 6
a_4 = 2
b_4 = 5
c_4 = 2
d_4 = 6
a_5 = 6
b_5 = 4
c_5 = 2
d_5 = 5

print(solution_2(a_1, b_1, c_1, d_1))  # 2222
print(solution_2(a_2, b_2, c_2, d_2))  # 1681
print(solution_2(a_3, b_3, c_3, d_3))  # 27
print(solution_2(a_4, b_4, c_4, d_4))  # 30
print(solution_2(a_5, b_5, c_5, d_5))  # 2
