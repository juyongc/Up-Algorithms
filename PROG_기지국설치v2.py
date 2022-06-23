def solution(n, stations, w):
    answer = 0
    now = 1
    idx = 0
    # 현재 위치와 stations 위치를 비교하며 올라가기
    while now <= n:
        
        mid = now + w   # 기지국 위치는 중간
        # 아직 미확인 stations가 남았는지 확인
        if idx < len(stations):
            if mid == stations[idx]:    # stations가 설치할 기지국 위치와 같으면
                now = mid + w + 1       # => 설치안하고 다음으로 넘어감
                idx += 1
            elif mid < stations[idx]:   # stations가 설치할 기지국 위치와 인덱스가 뒤면
                now = mid + w + 1       # => 설치
                answer += 1
            else:                               # stations가 설치할 기지국 위치와 인덱스가 앞이면
                now = stations[idx] + w + 1     # => 기지국 위치를 기준으로 다음으로 넘어감
                idx += 1
        else:
            now = mid + w + 1
            answer += 1
            
    return answer