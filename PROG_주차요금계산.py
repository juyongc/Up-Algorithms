def solution(fees, records):
    answer = []
    
    car_in = {}
    car_out = {}
    park_time = {}
    # 모든 기록 확인
    for record in records:
        rec,num,condition = record.split()
        h,m = rec.split(":")
        mm = int(h) * 60 + int(m)
        if condition == "IN":   # IN이면 => 딕셔너리 추가
            car_in[num] = mm
        else:                   # OUT이면 => 시간 계산 후, park_time에 추가
            t = mm - car_in[num]
            car_in[num] = -1
            if num in park_time:
                park_time[num] += t
            else:
                park_time[num] = t
                
    max_time = 23*60 + 59
    # 출차기록 없는 차 자동처리
    for key,val in car_in.items():
        if val != -1:
            t = max_time - val
            val = -1
            if key in park_time:
                park_time[key] += t
            else:
                park_time[key] = t
                
    calculate = []
    # 요금 계산
    for key,val in park_time.items():
        cost = fees[1]
        if (val - fees[0]) > 0:
            share,rem = divmod(val - fees[0],fees[2])
            if rem != 0:
                share += 1
            cost += (share * fees[3])
        calculate.append([key,cost])
        
    calculate.sort()
    # 차량번호 순으로 정렬
    for cal in calculate:
        answer.append(cal[1])
        
    return answer