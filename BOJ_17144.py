import sys

inputs = sys.stdin.readline
R,C,T = map(int,inputs().split())
dust = [list(map(int,inputs().split())) for _ in range(R)]
purf = []       # 공기청정기 찾기
for i in range(R):
    if dust[i][0] == -1:
        purf.append(i)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
tot = 0
# 시간만큼 반복
while tot < T:
    # 미세먼지 상태
    new = [[0]*C for _ in range(R)]
    # 미세먼지 확산
    for r in range(R):
        for c in range(C):
            if dust[r][c] == -1:
                new[r][c] = -1
                continue
            else:
                cnt = 0
            for k in range(4):
                x = r+dx[k]
                y = c+dy[k]
                if 0<=x<R and 0<=y<C:
                    if dust[x][y] != -1:
                        new[x][y] += dust[r][c]//5
                        cnt += 1
            if dust[r][c] != -1:
                new[r][c] += dust[r][c] - (dust[r][c]//5)*cnt
    # 공기청정기 순환
    for r in range(purf[0]-1,0,-1):
        new[r][0] = new[r-1][0]
    for r in range(purf[1]+1,R-1):
        new[r][0] = new[r+1][0]
    for c in range(C-1):
        new[0][c] = new[0][c+1]
        new[-1][c] = new[-1][c+1]
    for r in range(0,purf[0]):
        new[r][-1] = new[r+1][-1]
    for r in range(R-1,purf[0]-1,-1):
        new[r][-1] = new[r-1][-1]
    for c in range(C-1,1,-1):
        new[purf[0]][c] = new[purf[0]][c-1]
        new[purf[1]][c] = new[purf[1]][c-1]
    new[purf[0]][1] = 0
    new[purf[1]][1] = 0
    tot += 1
    dust = new[:]

amount = 0
# 미세먼지 카운팅
for r in range(R):
    for c in range(C):
        if dust[r][c] > 0:
            amount += dust[r][c]

print(amount)
