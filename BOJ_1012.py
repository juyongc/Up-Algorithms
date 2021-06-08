import sys
from collections import deque


# 주변 배추 탐색 함수
def move(row,col,num):
    q = deque()
    q.append((row,col))
    farm[row][col] = num    # farm[첫 배추 위치] = num
    while q:
        r,c = q.popleft()
        for k in range(4):
            nr = r+dx[k]
            nc = c+dy[k]
            if 0<=nr<N and 0<=nc<M and farm[nr][nc] == -1:
                farm[nr][nc] = num      # farm[탐색된 배추 위치] = num
                q.append((nr,nc))       # 해당 배추 주변 탐색 위해 append


inputs = sys.stdin.readline

T = int(inputs())
for t in range(1,T+1):
    M,N,K = map(int,inputs().split())
    farm = [[0]*M for _ in range(N)]
    for _ in range(K):
        x,y = map(int,inputs().split())
        farm[y][x] = -1     # 배추 위치 = -1 / 없으면 = 0

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    cnt = 0     # 배추 집결지 카운트
    # 배추 집결지 찾기
    for i in range(N):
        for j in range(M):
            if farm[i][j] == -1:
                cnt += 1
                move(i,j,cnt)

    print(cnt)