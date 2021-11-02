import sys
from collections import deque
inputs = sys.stdin.readline

def check(n,m):
    for i in range(n):
        for j in range(m):
            if czs[i][j] == 1:
                return False
    return True

N,M = map(int,inputs().split())
czs = [list(map(int,inputs().split())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

q = deque()
q.append((0,0))
# 바깥 공기 => 방문체크
while q:
    x,y = q.popleft()
    for k in range(4):
        a,b = x+dx[k],y+dy[k]
        if 0<=a<N and 0<=b<M and czs[a][b] == 0:
            if czs[a][b] == 0:
                q.append((a,b))
                czs[a][b] = -1

s = []      # 치즈 위치
# 외부공기 => 0 / 내부공기 => 2
for i in range(N):
    for j in range(M):
        if czs[i][j] == 1:      # 치즈면
            s.append((i,j))     # => s에 추가
melting = 0         # 녹을 때까지 시간
# 치즈가 다 녹을때까지
while True:

    now = check(N,M)
    if now:
        break

    cur = []    # 지금 녹을 치즈 리스트
    for i in range(len(s)):
        x,y = s[i]
        if czs[x][y] == -1:    # 방문했으면 => continue
            continue
        side = 0            # 4방향 확인용
        for k in range(4):
            a,b = x+dx[k],y+dy[k]
            if 0<=a<N and 0<=b<M and czs[a][b] == -1:
                side += 1
        if side >= 2:
            cur.append((x,y))
    # 치즈 녹이기
    # 내부 공기도 -1로 만들기
    while cur:
        cx,cy = cur.pop()
        if czs[cx][cy] != -1:
            czs[cx][cy] = -1
            for ck in range(4):
                ca, cb = cx + dx[ck], cy + dy[ck]
                if 0 <= ca < N and 0 <= cb < M and czs[ca][cb] == 0:
                    cur.append((ca,cb))
    melting += 1

print(melting)