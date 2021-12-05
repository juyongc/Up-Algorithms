import sys
inputs = sys.stdin.readline

# 테트로미노 "ㅗ"빼고 만들기
# dfs로 4개의 점 찍는 거랑 같음
def dfs(a,b,tot,cnt):
    global maxi
    if cnt >= 4:
        maxi = max(maxi,tot)
        return

    for k in range(4):
        x,y = a+dx[k], b+dy[k]
        if 1<=x<N+1 and 1<=y<M+1 and visit[x][y] == 0:
            visit[x][y] = 1
            dfs(x,y,tot+board[x][y],cnt+1)
            visit[x][y] = 0

# ㅗ,ㅜ,ㅏ,ㅗ 만들기
def star(a,b,tot):
    global maxi
    # 상,하,좌,우 값 다 더하기
    for k in range(4):
        x, y = a + dx[k], b + dy[k]
        tot += board[x][y]
    # 각각 뺀 값 max값과 비교
    for k in range(4):
        xx, yy = a + dx[k], b + dy[k]
        pos = tot - board[xx][yy]
        maxi = max(maxi,pos)


N,M = map(int,inputs().split())
board = [[0]*(M+2)] + [([0] + list(map(int,inputs().split())) + [0]) for _ in range(N)] + [[0]*(M+2)]
visit = [[0]*(M+2) for _ in range(N+2)]
maxi = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

# dfs 시작
for i in range(1,N+1):
    for j in range(1,M+1):
        star(i,j,board[i][j])
        visit[i][j] = 1
        dfs(i,j,board[i][j],1)
        visit[i][j] = 0

print(maxi)
