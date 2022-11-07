def solution(distance, scope, times):
    answer = distance
    
    guard_info = []
    # scope이랑 times 맞춰주기 위해 합치기
    for i in range(len(scope)):
        info = [scope[i][0],scope[i][1],times[i][0],times[i][1]]
        guard_info.append(info)
    guard_info.sort()
    
    flag = 0
    for d1,d2,work,rest in guard_info:
        work_time = work+rest       # 경비병 전체 시간
        if d1 > d2:
            s,e = d2,d1
        else:
            s,e = d1,d2
        # scope에서 해당 경비병 근무 여부 확인
        for i in range(s,e+1):
            rem = i % work_time
            if rem != 0 and rem <= work:    # 근무시간이면 => 걸림
                flag = 1
                answer = i
                break
        if flag:
            break
    
    return answer