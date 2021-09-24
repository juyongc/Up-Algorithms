import sys
inputs = sys.stdin.readline

N = int(inputs())
nums = [0] + list(map(int,inputs().split()))

dp = [0]*(N+1)
# 0~현재 인덱스 비교해서 max값 구하기
for i in range(1,N+1):
    for j in range(0,i):
        if nums[j] < nums[i]:           # 자신보다 작으면
            dp[i] = max(dp[i],dp[j]+1)  # max값 비교

print(max(dp))
