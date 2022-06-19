import sys
inputs = sys.stdin.readline

N = int(inputs())
nums = list(map(int,inputs().split()))
M = int(inputs())

dp = [[0]*N for _ in range(N)]

# 길이 == 1 => 무조건 팰린드롬
for i in range(N):
    dp[i][i] = 1

# 길이 == 2 => 서로 같으면 팰린드롬
for i in range(N-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1

# 길이 >= 3 => 시작,끝이 같고 중간이 팰린드롬이면 팰린드롬
for i in range(2,N):
    for j in range(N-i):
        if nums[j] == nums[j+i] and dp[j+1][j+i-1] == 1:
            dp[j][j+i] = 1

for _ in range(M):
    s,e = map(int,inputs().split())
    print(dp[s-1][e-1])
