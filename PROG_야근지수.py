def solution(n, works):
    answer = 0      
    times = dict()  # 해시 사용하기 위해 딕셔너리
    times[0]=0      # 계산 용이하기 위해 0 만들기
    if sum(works) <= n:     # 야근 일자가 작업보다 더 많으면
        answer = 0      
    else:                   # 아니면
        # "dict[작업량] = 해당 일 수" 만들기
        for work in works:
            if work in times:
                now = times[work] + 1
                times[work] = now
            else:
                times[work] = 1
        cnt = 0                     # 카운팅용
        start = max(times.keys())   # 가장 많은 작업량
        # 가장 많은 작업량부터 내려오기
        for i in range(start,0,-1):
            cur = times[i]          # 현재 작업량
            if cur + cnt >= n:      # (카운팅 + 현재)가 N 보다 크면
                cur = n - cnt       
                times[i] -= cur     # 현재 작업량에 남은 일수만큼 빼줌
            else:                   # (카운팅 + 현재)가 N 보다 작으면
                del(times[i])       # 현재 작업량 삭제
            cnt += cur              # 카운팅 ++
            # cur-1이 딕셔너리 존재 여부 확인 후 생성 or 더하기
            if i-1 in times:
                times[i-1] += cur
            else:
                times[i-1] = cur
            if cnt >= n:    # 카운팅이 N보다 크거나 같으면 break
                break
        # 제곱합 계산하기
        for key,val in times.items():
            answer += (key ** 2) * val
    return answer