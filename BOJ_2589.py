import sys
from collections import deque

# BFS 함수
def bfs(a,b):
    global maxi
    q = deque()
    q.append((a,b))     # 시작값 큐에 넣기
    visit = [[0]*M for _ in range(N)]   # 방문체크용
    visit[a][b] = 1     # 시작점 방문체크
    # 큐만큼 반복
    while q:
        x,y = q.popleft()
        # 4방향 탐색
        for k in range(4):
            r,c = x+dx[k],y+dy[k]
            # 행/열 범위 내, 육지, 미방문 시에는
            # 큐에 삽입 + 방문체크(이전방문값 + 1)
            if 0<=r<N and 0<=c<M:
                if mapping[r][c] == 'L' and visit[r][c] == 0:
                    q.append((r,c))
                    visit[r][c] = visit[x][y] + 1
    cur = visit[x][y] -1    # 현 BFS에서 가장 큰 값(시작이 1이니 -1)
    if cur > maxi:          # 최고값 비교
        maxi = cur


inputs = sys.stdin.readline

N,M = map(int,input().split())
mapping = [list(inputs().rstrip()) for _ in range(N)]
maxi = 0    # 가장 먼 거리
# 4방향 탐색
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 육지면 BFS 탐색
for i in range(N):
    for j in range(M):
        if mapping[i][j] == 'L':
            bfs(i,j)
print(maxi)