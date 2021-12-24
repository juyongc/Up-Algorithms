import sys
inputs = sys.stdin.readline

N = int(input())
electros = [(0,0)]
for _ in range(N):
    a,b = map(int,inputs().split())
    electros.append((a,b))
electros.sort()

dp = [0]*(N+1)

# LIS => 이전값들과 비교해서 크면 해당값+1과 현재 dp[i] 비교 후 갱신
for i in range(1,N+1):
    for j in range(i):
        if electros[i][1] > electros[j][1]:
            dp[i] = max(dp[i],dp[j]+1)

ans = N - max(dp)
print(ans)