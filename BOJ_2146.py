import sys
from collections import deque

# BFS 탐색
def bfs(sx, sy, val, maxi_val):
    q = deque()
    q.append((sx, sy))
    visit = [[0] * N for _ in range(N)]
    visit[sx][sy] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            a, b = x + dx[k], y + dy[k]
            if 0 <= a < N and 0 <= b < N and visit[a][b] == 0 and field[a][b] != val:
                if field[a][b] == 0:    # 바다면
                    visit[a][b] += (visit[x][y] + 1)
                    if visit[a][b] > maxi_val:
                        return maxi_val
                    else:
                        q.append((a, b))
                else:                   # 다른 섬이면
                    answer = visit[x][y]
                    return answer
    return maxi_val

inputs = sys.stdin.readline
N = int(inputs())
field = [list(map(int,inputs().split())) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

lands = []  # 전체 땅 위치 리스트
# 전체 섬 위치 구하기
for i in range(N):
    for j in range(N):
        if field[i][j] == 1:
            lands.append((i,j))
now = 0
# 섬 구별하기
for land in lands:
    lx,ly = land[0],land[1]
    if field[lx][ly] == 1:
        now -= 1
        field[lx][ly] = now
        lq = deque()
        lq.append((lx,ly))
        while lq:
            x,y = lq.popleft()
            for k in range(4):
                a,b = x+dx[k],y+dy[k]
                if 0<=a<N and 0<=b<N and field[a][b] == 1:
                    field[a][b] = now
                    lq.append((a,b))

maxi = 9999999999999
# 가장 짧은 다리 구하기
for land in lands:
    lx, ly = land[0], land[1]
    cur = bfs(lx,ly,field[lx][ly],maxi)
    if cur < maxi:
        maxi = cur

print(maxi-1)