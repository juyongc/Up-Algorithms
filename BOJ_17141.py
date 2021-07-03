import sys
from collections import deque

# 조합 찾기
def selection(cnt,s,arr):
    if cnt >= M:
        pos.append(arr[:])
        return
    if s >= tot - M + cnt + 1:
        return
    for i in range(s,tot-M+cnt+1):
        arr[cnt] = i
        selection(cnt+1,i+1,arr)

# 최단 거리 찾기
def bfs(s):
    global mini
    q = deque()
    maxi = 0
    for z in range(M):
        q.append(s[z])

    while q:
        x, y = q.popleft()
        for k in range(4):
            a, b = x + dx[k], y + dy[k]
            if 0 <= a < N and 0 <= b < N:
                if (labs[a][b] == '0' or labs[a][b] == '2') and lab[a][b] == -1:
                    lab[a][b] = lab[x][y] + 1
                    q.append((a,b))
                    if maxi < lab[a][b]:
                        maxi = lab[a][b]
                        # 현재 mini보다 크면 return
                        if maxi >= mini:
                            return
    for m in range(N):
        for n in range(N):
            # 빈 칸 있으면 return
            if (labs[m][n] == '0' or labs[m][n] == '2') and lab[m][n] == -1:
                return

    if maxi < mini:
        mini = maxi
    return


inputs = sys.stdin.readline
N,M = map(int,inputs().split())
labs = [list(inputs().split()) for _ in range(N)]

area = []
for i in range(N):
    for j in range(N):
        if labs[i][j] == '2':
            area.append((i,j))

mini = 10000
pos = []
tot = len(area)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

selection(0,0,[0]*M)

for i in range(len(pos)):
    lab = [[-1]*N for _ in range(N)]
    exper = pos[i]
    start = []
    for j in range(M):
        sx,sy = area[exper[j]]
        lab[sx][sy] = 0
        start.append((sx,sy))
    bfs(start)


if mini == 10000:
    ans = -1
else:
    ans = mini

print(ans)
