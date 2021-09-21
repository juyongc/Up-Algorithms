import sys
inputs = sys.stdin.readline

N,M = map(int,inputs().split())
rec = [list(inputs().rstrip()) for _ in range(N)]
dp = [[0]*(M+1) for _ in range(N+1)]
maxi = 0
# 우측 대각선이 항상 끝나는 시점임
# 좌,상,좌상대각 값 중 min값 + 1 하면서 최대값 찾기
for i in range(1,N+1):
    for j in range(1,M+1):
        if rec[i-1][j-1] == '1':
            dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
            if dp[i][j] > maxi:
                maxi = dp[i][j]
print(maxi**2)