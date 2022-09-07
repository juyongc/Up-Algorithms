import sys
inputs = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int,inputs().split()))
    M = int(input())

    dp = [0]*(M+1)
    # 코인별로, 코인 ~ 금액까지 가능한 경우의 수 DP
    for coin in coins:
        dp[coin] += 1
        for k in range(coin+1,M+1):
            dp[k] += dp[k-coin]

    print(dp[-1])
