import sys
inputs = sys.stdin.readline

N = int(input())

dp = [[0]*10 for _ in range(N+1)]
dp[1] = [1]*10
dp[1][0] = 0
if N > 1:   # 1보다 크면 => 마지막 자리수 수를 기준으로 +,- 1에 ++
    for i in range(2,N+1):
        for j in range(10):
            if j == 0:
                dp[i][j+1] += dp[i-1][j]
            elif j == 9:
                dp[i][j-1] += dp[i-1][j]
            else:
                dp[i][j + 1] += dp[i - 1][j]
                dp[i][j - 1] += dp[i - 1][j]

print(sum(dp[-1])%1000000000)