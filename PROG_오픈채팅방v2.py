def solution(record):
    answer = []
    user = {}
    
    # 입장, 변경 => 유저 닉네임 변경
    for rec in record:
        rec_list = rec.split(" ")
        if rec_list[0] == "Leave":
            continue
        status, user_id, name = rec_list
        user[user_id] = name
    
    # 입장, 퇴장 => 사용자 닉네임 + 메시지 출력
    for rec in record:
        rec_list = rec.split(" ")
        if rec_list[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(user[rec_list[1]]))
            continue
        status, user_id, name = rec_list
        if status == "Enter":
            answer.append("{}님이 들어왔습니다.".format(user[user_id]))
        
    return answer