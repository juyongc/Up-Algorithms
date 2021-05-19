import sys
from collections import deque

# 공주 구출 함수
def rescue():
    global mini
    # 큐에 값 있는 동안 반복
    while q1:
        x,y,cnt = q1.popleft()      # 행,열,움직인 횟수
        for k in range(4):
            a,b= x+dx[k],y+dy[k]
            if 0<=a<N and 0<=b<M and visit[a][b] == 0 and D[a][b] != 1:
                visit[a][b] = 1     # 방문 체크
                if D[a][b] == 2:                        # 명검 찾으면
                    cnt = cnt + (N-1-a) + (M-1-b) + 1   # 바로 공주까지 이동
                    if cnt < mini:                      # 움직인 횟수 체크
                        mini = cnt
                else:                                   # 일반 길이면
                    if a == N-1 and b == M-1:           # 끝까지 도달했는지 체크
                        if cnt+1 < mini:
                            mini = cnt + 1
                        return
                    if mini > cnt:                      # 움직인 횟수가 현재 최소값보다 작으면
                        q1.append((a,b,cnt+1))          # 큐에 추가


N,M,T = map(int,input().split())
D = [list(map(int,input().split())) for _ in range(N)]

visit = [[0]*M for _ in range(N)]
# 4방향 탐색
dx = [0,0,1,-1]
dy = [1,-1,0,0]

start = (0,0,0)     # 시작점
mini = 9999999999   # 최소값 정의

q1 = deque()
q1.append(start)

rescue()
# 정답 추출하기
if mini > T:
    ans = 'Fail'
else:
    ans = mini

print(ans)