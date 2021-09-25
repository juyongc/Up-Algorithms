import sys
from collections import deque
inputs = sys.stdin.readline

N = int(inputs())
seas = [list(map(int,inputs().split())) for _ in range(N)]

# 상어 위치 찾기
for i in range(N):
    for j in range(N):
        if seas[i][j] == 9:
            sx,sy = i,j
            seas[sx][sy] = 0
            break

shark = 2   # 상어 크기
eats = 0    # 먹은 횟수
move = 0    # 움직인 거리

dx = [-1,0,0,1]
dy = [0,-1,1,0]

while True:
    q = deque()
    q.append((sx,sy,0))
    visit = [[0] * N for _ in range(N)] # 방문체크
    visit[sx][sy] = 1
    flag = 99999999999999   # 같은 거리 체크용
    candi = []      # 먹이 위치 후보
    while q:
        x,y,cnt = q.popleft()
        cnt += 1
        if cnt > flag:  # 가능한 먹이 거리보다 커지면 => break
            break
        for k in range(4):
            a = x + dx[k]
            b = y + dy[k]
            if 0 <= a < N and 0 <= b < N and visit[a][b] == 0:
                if 0 < seas[a][b] < shark:      # 가능한 먹이면
                    candi.append((a,b,cnt))     # 후보 등록
                    flag = cnt                  # flag 갱신
                    visit[a][b] = 1
                elif seas[a][b] == 0 or seas[a][b] == shark:    # 통과만 가능하면
                    q.append((a,b,cnt))                         # q에 추가
                    visit[a][b] = 1

    if len(candi) > 0:      # 가능한 후보가 있으면
        candi.sort()        # 정렬
        sx,sy,t = candi[0]
        move += t
        eats += 1
        if eats == shark:   # 크기만큼 먹었으면 => 사이즈 + 1
            shark += 1
            eats = 0
        seas[sx][sy] = 0    # 먹었으니 물고기 사라짐
    else:                   # 후보 없음 => 끝
        break

print(move)
