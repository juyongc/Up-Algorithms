import sys
inputs = sys.stdin.readline

N = int(input())
nums = [0] + list(map(int,inputs().split()))

dp_up = [0]*(N+1)   # 앞에서부터 LIS
# 해당 위치 값과 이전 값들을 비교하며
# 해당 위치가 더 크면, max값 비교
for i in range(1,N+1):
    for j in range(i):
        if nums[j] < nums[i]:
            dp_up[i] = max(dp_up[j]+1,dp_up[i])

dp_down = [0]*(N+1) # 뒷값과 LIS
# 해당 위치 값과 뒤에 값들을 비교하며
# 해당 위치가 더 크면, max값 비교
for i in range(N-1,0,-1):
    for j in range(N,i,-1):
        if nums[i] > nums[j]:
            dp_down[i] = max(dp_down[j]+1,dp_down[i])

dp = [0]*(N+1)
# dp 값 합치기
for i in range(1,N+1):
    dp[i] = dp_up[i] + dp_down[i]

print(max(dp))
