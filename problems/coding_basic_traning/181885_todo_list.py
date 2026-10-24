def solution(todo_list, finished):
    return [todo for todo, is_finished in zip(todo_list, finished) if not is_finished]


test_cases = [
    (["problemsolving", "practiceguitar", "swim", "studygraph"], [True, False, True, False],
     ["practiceguitar", "studygraph"])
]

for i, (todo_list, finished, expected) in enumerate(test_cases, 1):
    result = solution(todo_list, finished)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
