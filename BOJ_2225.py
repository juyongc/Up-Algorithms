import sys
inputs = sys.stdin.readline

N,K = map(int,inputs().split())

dp = [[0]*(N+1) for _ in range(K+1)]
dp[0][0] = 1    # 0~N까지 합이므로 0도 포함해야 함
# 현재 행 인덱스값 = 이전행의 0 ~ 현재 인덱스 합
for i in range(1,K+1):
    for j in range(N+1):
        dp[i][j] += sum(dp[i-1][0:j+1])
print(dp[K][N]%1000000000)