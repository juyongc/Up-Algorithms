def solution(k, room_number):
    answer = [0]*len(room_number)
    
    room = {}
    cnt = 0
    
    for num in room_number:
        visit = [num]
        while visit:
            if visit[-1] in room:   # 이미 배정받은 방이면, 다음 가능한 방 추가
                visit.append(room[visit[-1]])
            else:                   # 미배정인 방이면 => 방 배정, 이전 확인한 방 모두 다음 배정가능한 방으로 변경
                given = visit[-1]
                answer[cnt] = given
                while visit:
                    now = visit.pop()
                    room[now] = given+1
        cnt += 1
    
    return answer