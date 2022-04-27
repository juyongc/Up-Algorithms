import sys
inputs = sys.stdin.readline


def dfs(x,y):

    if x == N-1 and y == M-1:
        return 1

    if memo[x][y] != -1:
        return memo[x][y]

    way = 0
    for k in  range(4):
        nx,ny = x+dx[k],y+dy[k]
        if 0<=nx<N and 0<=ny<M:
            if road[x][y] > road[nx][ny]:
                way += dfs(nx,ny)

    memo[x][y] = way
    return memo[x][y]

N,M = map(int,input().split())
road = [list(map(int,input().split())) for _ in range(N)]

memo = [[-1]*M for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = dfs(0,0)
print(ans)