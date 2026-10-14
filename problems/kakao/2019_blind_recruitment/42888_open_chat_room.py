def solution(record):
    user_dict = {}

    for command in record:
        parts = command.split()

        if len(parts) == 3:
            user_dict[parts[1]] = parts[2]

    result = []

    messages = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

    for command in record:
        parts = command.split()

        action, uid = parts[0], parts[1]

        if action in messages:
            result.append(f"{user_dict[uid]}{messages[action]}")

    return result


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo",
          "Change uid4567 Ryan"]

print(solution(record))  # ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
