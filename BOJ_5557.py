import sys
inputs = sys.stdin.readline

N = int(inputs())
nums = list(map(int,inputs().split()))

dp = [[0]*21 for _ in range(N-1)]
dp[0][nums[0]] += 1
# 0~20까지 나오는 개수를 다음 수 +/- 해서 
# 다음 리스트에 추가
for i in range(1,N-1):
    for j in range(0,21):
        if dp[i-1][j] != 0:
            plus = j + nums[i]
            minus = j - nums[i]
            if 0 <= plus <= 20:
                dp[i][plus] += dp[i-1][j]
            if 0 <= minus <= 20:
                dp[i][minus] += dp[i-1][j]

print(dp[N-2][nums[-1]])
