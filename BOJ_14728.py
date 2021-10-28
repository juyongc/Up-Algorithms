import sys
inputs = sys.stdin.readline

N,T = map(int,inputs().split())
study,score = [],[]
for _ in range(N):
    K,S = map(int,inputs().split())
    study.append(K)
    score.append(S)

dp = [[0]*(T+1) for _ in range(N+1)]

# 현재 투자해야 하는 시간 이상이면 => 이전 행 dp값과 예상공부시간+배점 비교
# 아니면 => 이전 행 dp값 
for i in range(1,N+1):
    for j in range(1,T+1):
        if j >= study[i-1]:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-study[i-1]]+score[i-1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[-1][-1])
