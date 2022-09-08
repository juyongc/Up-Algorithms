import sys
from collections import deque
from itertools import combinations
inputs = sys.stdin.readline


def bfs(combi,block,N):

    arr = [[0]*N for _ in range(N)]

    for cr,cc in combi:
        arr[cr][cc] = 2

    for br,bc in block:
        arr[br][bc] = 1

    virus_num = {}
    virus_num[2] = combi
    q = deque(combi)
    while q:
        r,c = q.popleft()
        for k in range(4):
            x,y = r + dx[k], c + dy[k]
            if 0<=x<N and 0<=y<N and arr[x][y] == 0:
                q.append((x,y))
                arr[x][y] = arr[r][c] + 1
                if arr[x][y] in virus_num:
                    virus_num[arr[x][y]].append((x,y))
                else:
                    virus_num[arr[x][y]] = [(x, y)]
    key_list = list(virus_num)
    key_list.sort(reverse=True)

    # 빈 칸 여부 확인 - 있으면 -1 리턴
    for z in range(N):
        check = min(arr[z])
        if check == 0:
            return -1
    # 비활성 바이러스가 마지막인지 확인 - 아니면 해당 key 리턴
    for key in key_list:
        for xx,yy in virus_num[key]:
            if lab[xx][yy] != 2:
                return key
    # 빈칸 없고, 모든 칸이 바이러스였다
    # => 처음부터 바이러스였음
    return 2


N,M = map(int,inputs().split())

lab = []
for _ in range(N):
    lab_row = list(map(int,inputs().split()))
    lab.append(lab_row)

virus = []      # 모든 바이러스 위치
block = []      # 모든 벽 위치
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append((i,j))
        elif lab[i][j] == 1:
            block.append((i,j))

# M개 조합 구하기
possible_combi = list(combinations(virus,M))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

answer = -1     # 최소값
# 모든 조합 확인
for combi in possible_combi:
    now = bfs(combi,block,N)
    # 불가능 => continue
    if now == -1:
        continue
    else:
        now -= 2    # 시작이 2이므로 -2 해주기
        # 현재 최소값이 -1이었으면 바로 갱신
        if answer == -1:
            answer = now
        # 이외에는 최소값 갱신
        else:
            answer = min(answer,now)

print(answer)