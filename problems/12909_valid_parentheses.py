def solution(s):
    answer = True

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return True


test_s1 = "()()"
test_s2 = "(())()"
test_s3 = ")()("
test_s4 = "(()("

print(solution(test_s1))
print(solution(test_s2))
print(solution(test_s3))
print(solution(test_s4))
