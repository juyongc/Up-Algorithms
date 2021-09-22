import sys
inputs = sys.stdin.readline

N = int(inputs())
loc = [list(inputs().rstrip()) for _ in range(N)]
click = [list(inputs().rstrip()) for _ in range(N)]

dx = [1,1,1,0,0,-1,-1,-1]
dy = [1,0,-1,1,-1,1,0,-1]
pang = 0
# 클릭한 부분 숫자 / 지뢰 표시하기
for x in range(N):
    for y in range(N):
        if click[x][y] == 'x':
            if loc[x][y] == '*':
                loc[x][y] = '*'
                pang = 1
            else:
                cnt = 0
                for k in range(8):
                    a = x + dx[k]
                    b = y + dy[k]
                    if 0<=a<N and 0<=b<N:
                        if loc[a][b] == '*':
                            cnt += 1
                click[x][y] = str(cnt)
# 지뢰를 건드렸다면
if pang == 1:
    mines = []
    # 모든 지뢰 위치 찾기
    for i in range(N):
        for j in range(N):
            if loc[i][j] == '*':
                mines.append((i,j))
    # 지뢰 위치 보여주기
    for mine in mines:
        mx,my = mine[0],mine[1]
        click[mx][my] = '*'

for i in range(N):
    print(''.join(click[i]))
