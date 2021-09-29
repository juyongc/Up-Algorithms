import sys
inputs = sys.stdin.readline

N,K = map(int,inputs().split())
prods = [[0,0]] + [list(map(int,inputs().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    w = prods[i][0]
    val = prods[i][1]
    for j in range(1,K+1):
        if w <= j:  # 배낭이 현재 무게 이상 포함가능하면 => 최대 무게 구한뒤 비교 
            dp[i][j] = max(dp[i-1][j],val+dp[i-1][j-w])
        else:       # 포함못하면, 그대로 계승
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])
