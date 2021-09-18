import sys
inputs = sys.stdin.readline
N = int(inputs())
grape = [0,0,0] + [int(inputs()) for _ in range(N)]
# 3잔까지 마실 수 없다 - 0,1,2잔째로 나눠서 카운팅
dp = [[0,0,0] for _ in range(N+3)]

for i in range(3,N+3):
    for j in range(3):
        if j == 0:  # 0잔 max는 이전값 max
            dp[i][j] = max(dp[i - 1])
        else:       # 1,2잔 max는 이전 인덱스 값 + 현재 포도주 양
            dp[i][j] = max(dp[i - 1][j - 1] + grape[i], dp[i][j])

print(max(dp[-1]))