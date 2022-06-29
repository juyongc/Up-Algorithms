import sys
inputs = sys.stdin.readline

# DFS - 범위 벗어나면 카운팅
# 벽이면 - 위치 유지
def dfs(x1, y1, x2, y2, cnt):
    global ans,dx,dy

    if cnt >= ans:
        return

    for k in range(4):
        flag = 0
        xx1, yy1 = x1 + dx[k], y1 + dy[k]
        xx2, yy2 = x2 + dx[k], y2 + dy[k]

        if (xx1 < 0 or xx1 >= N) or (yy1 < 0 or yy1 >= M):
            flag += 1
        elif board[xx1][yy1] == "#":
                xx1, yy1 = x1, y1

        if (xx2 < 0 or xx2 >= N) or (yy2 < 0 or yy2 >= M):
            flag += 1
        elif board[xx2][yy2] == "#":
            xx2, yy2 = x2, y2

        if flag == 0:
            dfs(xx1, yy1, xx2, yy2, cnt + 1)
        elif flag == 1:
            ans = min(ans, cnt+1)
            return
        else:
            continue


N,M = map(int,inputs().split())
board = [inputs().rstrip() for _ in range(N)]

coin = []

# 코인 위치 찾기
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            coin.append([i,j])

dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = 11
dfs(coin[0][0],coin[0][1],coin[1][0],coin[1][1],0)

if ans == 11:
    ans = -1

print(ans)
