def solution(my_string, n):
    return "".join([ch * n for ch in my_string])


my_string = "hello"
n = 3

print(solution(my_string, n))  # "hhheeellllllooo"
