import sys
from collections import deque

# BFS 탐색
def bfs(s):
    visit = [[0] * M for _ in range(N)]
    q = deque()
    q.append(s)
    visit[s[0]][s[1]] = 1
    num = 1
    # 시작점과 연결된 빙산 개수 카운팅
    while q:
        x,y = q.popleft()
        for k in range(4):
            row = x+dx[k]
            col = y+dy[k]
            if 0<=row<N and 0<=col<M and visit[row][col] == 0:
                if areas[row][col] > 0:
                    q.append([row,col])
                    visit[row][col] = 1
                    num += 1        # 시작점과 연결된 빙산 +1
    return num


inputs = sys.stdin.readline
N,M = map(int,inputs().split())
areas = []

dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(N):
    area = list(map(int,inputs().split()))
    areas.append(area)

tot = 0     # 반복 횟수
# 반복
while True:
    sea = [[0] * M for _ in range(N)]   # 주변 바다 개수 리스트
    # 주변 바다 개수 카운팅
    for i in range(1,N-1):
        for j in range(1,M-1):
            if areas[i][j] > 0:
                for k in range(4):
                    if areas[i+dx[k]][j+dy[k]] == 0:
                        sea[i][j] += 1

    start = [-1,-1]     # 시작점
    cnt = 0             # 0보다 큰 빙산 개수 
    # 빙산 녹이기 및 시작점 초기화
    for i in range(N):
        for j in range(M):
            if areas[i][j] != 0:
                areas[i][j] -= sea[i][j]
                if areas[i][j] < 0:
                    areas[i][j] = 0
                if areas[i][j] > 0:
                    cnt += 1
                    if start == [-1,-1]:
                        start = [i,j]
    # 시작점이 처음 그대로면 ans => '0'
    if start == [-1,-1]:
        ans = 0
        break
    # BFS 탐색
    num_ice = bfs(start)
    tot += 1        # 반복 횟수 +1
    # 시작점과 연결된 빙산개수가 전체 개수와 다르면,
    # ans => tot
    if num_ice != cnt:
        ans = tot
        break

print(ans)
