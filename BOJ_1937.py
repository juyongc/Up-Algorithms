import sys
inputs = sys.stdin.readline


def dfs(x,y):
    global dp,tree
    # 이미 지나간 적 있으면 그대로 반환
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    # 상하좌우 체크
    for k in range(4):
        r,c = x+dx[k], y+dy[k]
        if 0<=r<N and 0<=c<N:
            if tree[r][c] > tree[x][y]:
                dp[x][y] = max(dfs(r,c)+1,dp[x][y])     # dfs값 + 1(한칸 넘어간거니까 +1 하는거), 현재 값 비교
    return dp[x][y]


N = int(input())
tree = [list(map(int,input().split())) for _ in range(N)]

dp = [[-1]*N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
# 지나간 적 없으면 dfs 실시
for i in range(N):
    for j in range(N):
        if dp[i][j] == -1:
            dfs(i,j)
            
ans = 0
# 최대값 구하기
for i in range(N):
    for j in range(N):
        ans = max(ans,dp[i][j])

print(ans + 1)  # 처음 시작점 포함