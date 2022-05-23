def solution(lines):
    answer = 0
    se = []
    # 시간만 가져와서 float형식으로 계산
    for li in lines:
        dates,start,dur = li.split()
        hh,mm,ss = start.split(":")
        e_time = 3600.0*float(hh) + 60.0*float(mm) +float(ss)
        s_time = e_time - float(dur[:-1]) + float(0.001)
        se.append([s_time,e_time])
    # 시작 시간 ~ 1초
    for i in range(len(lines)):
        cnt = 0
        fs,fe = se[i][0],round(se[i][0] + 0.999,3)
        for j in range(len(lines)):
            cur_s,cur_e = se[j]
            if cur_e < fs or fe < cur_s:
                continue
            cnt += 1
        answer = max(answer,cnt)
    # 시작 시간 - 1 ~ 시작 시간
    for i in range(len(lines)):
        cnt = 0
        fs,fe = round(se[i][0] - 0.999,3),se[i][0]
        for j in range(len(lines)):
            cur_s,cur_e = se[j]
            if cur_e < fs or fe < cur_s:
                continue
            cnt += 1
        answer = max(answer,cnt)
    # 완료 시간 - 1 ~ 완료 시간
    for i in range(len(lines)):
        cnt = 0
        bs,be = round(se[i][1] - 0.999,3),se[i][1] 
        for j in range(len(lines)):
            cur_s,cur_e = se[j]
            if cur_e < bs or be < cur_s:
                continue
            cnt += 1
        answer = max(answer,cnt)
    # 완료 시간 ~ 완료 시간 + 1
    for i in range(len(lines)):
        cnt = 0
        bs,be = se[i][1],round(se[i][1]  + 0.999,3)
        for j in range(len(lines)):
            cur_s,cur_e = se[j]
            if cur_e < bs or be < cur_s:
                continue
            cnt += 1
        answer = max(answer,cnt)
    return answer