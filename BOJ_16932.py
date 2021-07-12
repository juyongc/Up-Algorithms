import sys
from collections import deque

# bfs 탐색
def bfs(pos):
    global team,num
    q = deque()         # 주변 '1' 탐색용
    q.append(pos)

    stack = []          # 그룹 지정용
    stack.append(pos)

    cnt = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            a,b = x+dx[k],y+dy[k]
            if 0<=a<N and 0<=b<M and arr[a][b] == 1 and group[a][b] == 0:
                cnt += 1                # 1 개수 카운팅 ++
                group[a][b] = -1        # 방문체크 + 추후 그룹 지정용
                q.append((a,b))
                stack.append((a,b))
    num += 1                # 그룹번호 ++
    team[num] = cnt         # 해당 그룹, 인원 딕셔너리에 추가
    # 그룹 소속 시키기
    while stack:
        x,y = stack.pop()
        group[x][y] = num


inputs = sys.stdin.readline
N,M = map(int,inputs().split())
arr = [list(map(int,inputs().split())) for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

group = [[0]*M for _ in range(N)]   # 그룹화용 리스트
team = {}                           # 그룹별 1의 개수

num = 0                             # 그룹 나누기용
# '1' 그룹화 하기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and group[i][j] == 0:
            group[i][j] = -1
            bfs((i,j))

maxi = 0
# 0 찾아서 주변 그룹 더하기
for x in range(N):
    for y in range(M):
        if group[x][y] == 0:
            tot = 1
            check = [0,0,0,0]       # 그룹 체크용 - 중복 방지
            # 4방향 탐색
            for k in range(4):
                a, b = x + dx[k], y + dy[k]
                if 0 <= a < N and 0 <= b < M:
                    if group[a][b] not in check:    # 해당 그룹 없으면,
                        tot += team[group[a][b]]    # 그룹 1 개수 더하기
                        check[k] = group[a][b]      # 그룹 체크
            if tot > maxi:
                maxi = tot

print(maxi)
