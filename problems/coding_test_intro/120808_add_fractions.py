import math
from fractions import Fraction


def solution(numer1, denom1, numer2, denom2):
    new_numer = (numer1 * denom2) + (numer2 * denom1)
    new_denom = denom1 * denom2

    gcd = math.gcd(new_numer, new_denom)

    return [new_numer // gcd, new_denom // gcd]


def solution_2(numer1, denom1, numer2, denom2):
    fountain1 = Fraction(numer1, denom1)
    fountain2 = Fraction(numer2, denom2)

    result = fountain1 + fountain2

    return [result.numerator, result.denominator]


numer1_1 = 1
denom1_1 = 2
numer2_1 = 3
denom2_1 = 4
numer1_2 = 9
denom1_2 = 2
numer2_2 = 1
denom2_2 = 3

print(solution_2(numer1_1, denom1_1, numer2_1, denom2_1))  # [5, 4]
print(solution_2(numer1_2, denom1_2, numer2_2, denom2_2))  # [29, 6]
