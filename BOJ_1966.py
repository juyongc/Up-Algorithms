import sys
inputs = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,M = map(int,inputs().split())
    papers = list(map(int,inputs().split()))
    visit = [0]*N
    cur = N-1   # 출발점
    i = 0       # 현재 위치값
    maxi = 0    # 최대값
    s = 0       # 최대값 인덱스값
    cnt = 0     # 인쇄 번수
    while visit[M] == 0:
        if i >= N:
            i = i % N   # 원형 큐 만들기
        if visit[i] == 0:   # 미방문 중 최대값,인덱스 찾기
            if papers[i] > maxi:
                maxi = papers[i]
                s = i
        if i == cur:        # 한바퀴 돌면
            visit[s] = 1    # 최대값 위치 방문체크
            cur = s         # 변수들 초기화
            i = s
            maxi = 0
            cnt += 1
        i += 1
    print(cnt)