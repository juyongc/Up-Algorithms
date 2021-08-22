import sys

inputs = sys.stdin.readline
N,M = map(int,inputs().split())
coins = [int(inputs().rstrip()) for _ in range(N)]  # 주어진 동전값
dp = [0]*(M+1)                      # M까지 각 위치별 동전 수
dp[0] = 1                           # 초기 값
# dp[현재] += dp[현재 - 현 코인값]
for coin in coins:
    for j in range(coin,M+1):
        dp[j] += dp[j-coin]

print(dp[M])