def solution(begin, end):
    answer = []
    
    for i in range(begin,end+1):
        num = i
        # 1이면 0이다
        if i == 1:
            answer.append(0)
            continue
            
        now = 1
        # 제곱근까지 확인
        for j in range(2,int(num**(1/2)+1)):
            share,rem = divmod(num,j)
            if share > 10000000:        # 제한사항 - 10,000,000번 블록까지
                continue
            if rem == 0:                # 나머지 = 0 => 가장 큰 수의 블록
                now = share
                break
        answer.append(now)
            
    return answer