import sys
from collections import deque
inputs = sys.stdin.readline

# 가장 가까운 승객 찾기
def bfs(ttx,tty):
    global F
    q = deque()
    q.append((ttx,tty))
    visit = [[-1]*N for _ in range(N)]  # 최단거리, 방문 체크
    visit[ttx][tty] = 0
    check = []                  # 승객 파악하기
    if areas[ttx][tty] == 2:
        check.append((ttx,tty))
    while q:
        x,y = q.popleft()
        if check:               # 승객 있으면
            num = check[0]
            if visit[x][y] >= visit[num[0]][num[1]]:    # 최단거리 승객보다 멀면
                check.sort(key=lambda x: (x[0],x[1]))   # 최단거리 승객 파악
                F -= visit[num[0]][num[1]]              # 연료 갱신
                return check[0]               
        for k in range(4):
            a,b = x+dx[k],y+dy[k]
            if 0<=a<N and 0<=b<N and visit[a][b] == -1 and areas[a][b] != 1:
                visit[a][b] = visit[x][y] + 1
                q.append((a,b))
                if areas[a][b] == 2:
                    check.append((a,b))
    if check:
        check.sort(key=lambda x: (x[0], x[1]))
        F -= visit[num[0]][num[1]]
        return check[0]
    else:
        return 0

# 해당 목적지 최단거리 찾기
def drive(sval,eval):
    q = deque()
    q.append(sval)
    visit = [[-1] * N for _ in range(N)]
    visit[sval[0]][sval[1]] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            a, b = x + dx[k], y + dy[k]
            if 0 <= a < N and 0 <= b < N and visit[a][b] == -1 and areas[a][b] != 1:
                visit[a][b] = visit[x][y] + 1
                q.append((a, b))
                if (a,b) == eval:
                    return visit[a][b]
    return -1


N,M,F = map(int,inputs().split())
areas = [list(map(int,inputs().split())) for _ in range(N)]
tx,ty= map(int,inputs().split())
loc = {}
for i in range(M):
    p1,p2,d1,d2 = map(int,inputs().split())
    areas[p1-1][p2-1] = 2
    loc[(p1-1,p2-1)] = (d1-1,d2-1)

dx = [-1,0,0,1]
dy = [0,-1,1,0]
# 파이썬 리스트는 0부터 시작
tx -= 1
ty -= 1

for i in range(M):
    now = bfs(tx,ty)        # 승객 찾기
    if now == 0 or F < 0:   # 못감
        F = -1
        break
    else:                   # 승객위치 도착 완료
        areas[now[0]][now[1]] = 0   # 해당 승객 위치 갱신
        goal = loc[now]             # 목적지 탐색
        tx,ty = loc[now][0],loc[now][1]
        fuel = drive(now,goal)      # 목적지 최단거리
        if fuel == -1:              # 연료 없음
            F = -1
            break
        F = F-fuel                  # 연료 갱신
        if F >= 0:                  # 연료 조건 파악
            F += (fuel*2)
        else:
            F = -1
            break
print(F)