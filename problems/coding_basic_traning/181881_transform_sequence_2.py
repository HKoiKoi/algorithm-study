def solution(arr):
    x = 0

    while True:
        prev_arr = arr.copy()

        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
            elif arr[i] < 50 and arr[i] % 2 != 0:
                arr[i] = arr[i] * 2 + 1

        if prev_arr == arr:
            return x

        x += 1


test_cases = [
    ([1, 2, 3, 100, 99, 98], 5)
]

for i, (arr, expected) in enumerate(test_cases, 1):
    result = solution(arr)

    if result == expected:
        print(f"테스트 {i} 통과 ✅")
    else:
        print(f"테스트 {i} 실패 ❌ (기댓값: {expected}, 실제 반환값: {result})")
