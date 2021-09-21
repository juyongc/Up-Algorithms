import sys
from collections import deque
inputs = sys.stdin.readline

# BFS 탐색
def bfs(i1, j1, n, m):
    dx = [1, 1, 1, 0, 0, -1, -1, -1]
    dy = [1, 0, -1, 1, -1, 1, 0, -1]

    q = deque()
    q.append((i1, j1, 1))
    visit = [[0]*M for _ in range(N)]
    visit[i1][j1] = 1
    while q:
        x, y, val = q.popleft()
        for k in range(8):
            a = x + dx[k]
            b = y + dy[k]
            if 0 <= a < N and 0 <= b < M and visit[a][b] == 0:
                if dis[a][b] == 1:  # 상어 도달 => 값 반환
                    return val
                else:
                    q.append((a, b, val + 1))
                    visit[a][b] = 1
    return val      # 상어없을 때 값 반환용

N,M = map(int,inputs().split())
dis = [list(map(int,inputs().split())) for _ in range(N)]

maxi = 0
for i in range(N):
    for j in range(M):
        if dis[i][j] == 0:
            now = bfs(i,j,N,M)
            if now > maxi:
                maxi = now

print(maxi)
