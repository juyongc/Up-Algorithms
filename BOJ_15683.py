import sys
from itertools import product
from copy import deepcopy
inputs = sys.stdin.readline


# possible - 해당 cctv 방향들
# current - 방문체크용 리스트
def dfs(possible, current, dx, dy, cctv_list):
    global visit, answer
    for i in range(len(cctv_list)):
        key, x, y = cctv_list[i]
        num = possible[i]

        for k in cctv_direction[key][num-1]:
            rx, ry = x + dx[k], y + dy[k]
            while 0 <= rx < N and 0 <= ry < M and office[rx][ry] != 6:
                current[rx][ry] += 1
                rx += dx[k]
                ry += dy[k]
    cnt = count(current)
    answer = min(cnt,answer)
    return

# 사각지대 카운팅 함수
def count(current):
    zero_cnt = 0
    for i in range(len(current)):
        for j in range(len(current[0])):
            if current[i][j] == 0:
                zero_cnt += 1

    return zero_cnt


N,M = map(int,inputs().split())
office = [list(map(int,inputs().split())) for _ in range(N)]

cctv = {i:[] for i in range(1,6)}
cctv_cnt = 0
visit = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if 0 < office[i][j] < 6:
            cctv[office[i][j]].append((i,j))
            cctv_cnt += 1
            visit[i][j] += 1
        elif office[i][j] == 6:
            visit[i][j] = -1

cctv_direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3], [2, 0], [3, 1]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
]

dx = [0,-1,0,1]
dy = [1,0,-1,0]
# 5번 CCTV 미리 방문해놓기
for val in cctv[5]:
    cx,cy = val
    for k in range(4):
        kx,ky = cx + dx[k], cy + dy[k]
        while 0<=kx<N and 0<=ky<M and office[kx][ky] != 6:
            visit[kx][ky] += 1
            kx += dx[k]
            ky += dy[k]

cctv_wo5 = cctv_cnt - len(cctv[5])
possible_list = list(product([1,2,3,4],repeat=cctv_wo5))        # CCTV별 탐색 위치
answer = 9999999

cctv_list = []      # CCTV 리스트(5번 제외)
for key,val in cctv.items():
    if key == 5:
        break
    for i in range(len(val)):
        cctv_list.append((key,val[i][0],val[i][1]))

# CCTV 탐색 위치별 사각지대 탐색
for possible in possible_list:
    current = deepcopy(visit)
    dfs(possible, current, dx, dy, cctv_list)

print(answer)
