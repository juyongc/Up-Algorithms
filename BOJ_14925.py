import sys
inputs = sys.stdin.readline

N,M = map(int,inputs().split())
land = [list(map(int,inputs().split())) for _ in range(N)]

ans = 0
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,M+1):
        if land[i-1][j-1]:
            continue
        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
        ans = max(ans,dp[i][j])

print(ans)
