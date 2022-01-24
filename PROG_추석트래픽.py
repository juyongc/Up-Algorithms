def solution(lines):
    answer = 0
    periods = []
    
    # 숫자 추출
    for line in lines:
        date,time,duration = line.split()
        h,m,s = map(float,time.split(":"))
        end_time = int((s + m * 60 + h * 3600) * 1000)
        duration = duration.replace("s","")
        start_time = end_time - int(float(duration)*1000) + 1
        periods.append((start_time,end_time))
    
    # 현재 end_time > 다음 start_time - 999 이면 타임라인에 미포함됨
    for i in range(len(periods)):
        ts = periods[i][1] 
        cnt = 0
        for j in range(i,len(periods)):
            if periods[j][0] - 999 <= ts:
                cnt += 1
        answer = max(answer,cnt)
    return answer