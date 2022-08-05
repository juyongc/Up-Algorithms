import sys
inputs = sys.stdin.readline

N,M,K = map(int,inputs().split())
route = [[] for _ in range(N+1)]
for _ in range(K):
    s,e,val = map(int,inputs().split())
    if s < e:
        route[s].append((e,val))

dp = [[0]*(M+1) for _ in range(N+1)]

# 2번째 방문 도시 초기화
for loc,val in route[1]:
    dp[loc][2] = max(dp[loc][2],val)

for i in range(2,N+1):
    for j in range(3,M+1):
        for loc,val in route[i]:
            # 방문횟수 확인하기
            if dp[i][j-1] > 0:
                dp[loc][j] = max(dp[loc][j],dp[i][j-1] + val)

print(max(dp[-1]))
