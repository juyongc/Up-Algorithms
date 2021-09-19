import sys
inputs = sys.stdin.readline
T = int(inputs())
for _ in range(T):
    N = int(inputs())
    coins = list(map(int,inputs().split()))
    money = int(inputs())
    dp = [0]*(money+1)
    dp[0] = 1
    # 현재 값에서 현 코인 뺀 값 더하기
    for coin in coins:
        for i in range(coin,len(dp)):
            dp[i] += dp[i-coin]
    print(dp[-1])