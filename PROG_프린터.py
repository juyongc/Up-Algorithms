def solution(priorities, location):
    waitings = len(priorities)  # 대기목록 개수
    now = 0     # 현재 위치
    cnt = 0     # 프린팅된 개수
    cur = 0     # 빈 그릇
    visit = [0]*waitings    # 방문체크
    # 프린팅 개수가 대기목록 수보다 작으면
    while cnt < waitings:
        maxi = -1           # 현재 가장 큰 값
        for i in range(now,now+waitings):   
            num = i % waitings      # 현재 위치
            if visit[num] == 0:     # 미방문이면
                if priorities[num] > maxi:      # maxi보다 크면
                    maxi = priorities[num]      # 교체
                    cur = num                   # num값 담기
        cnt += 1    # 카운팅 ++
        if cur == location:     # 목표값이었으면 => break
            break
        else:                   # 아니면 => 방문표시 & 다음 시작값 변경
            visit[cur] = 1
            now = cur + 1
    return cnt