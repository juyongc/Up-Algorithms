def shoot(rem,num,info):
    global score,answer,plate
    # 끝까지 찾았거나 남은 화살이 없거나
    if num == 11 or rem == 0:
        plate[10] += rem
        apache,lion = 0,0
        # 아파치, 라이언 점수 구하기
        for s in range(11):
            if plate[s] > info[s]:
                lion += (10-s)
            else:
                if info[s] != 0:
                    apache += (10-s)
        # 라이언이 더 크면
        # 현재 점수 차이랑 최대 점수 차이 비교
        if lion > apache:
            diff = lion - apache
            if diff > score:
                score = diff
                answer = plate[:]
            elif diff == score:
                for i in range(10,-1,-1):
                    if plate[i] > answer[i]:
                        answer = plate[:]
                        break
                    elif answer[i] > plate[i]:
                        break
        plate[10] -= rem
        return
                
    for i in range(num,11):
        shoot(rem,i+1,info)     # 안쏘고 지나감
        # 남은 화살이 더 많으면 => 현재 과녁에 쏜다
        if rem > info[i]:
            plate[i] += info[i] + 1
            rem -= info[i] + 1
            shoot(rem,i+1,info)
            plate[i] -= info[i] + 1
            rem += info[i] + 1
            

            
def solution(n, info):
    global score,answer,plate
    answer = [0]*11
    plate = [0]*11
    score = 0
    
    shoot(n,0,info)
        
    if score == 0:
        answer = [-1]
    return answer