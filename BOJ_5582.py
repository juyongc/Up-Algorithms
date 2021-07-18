import sys
inputs = sys.stdin.readline

A = inputs().rstrip()
B = inputs().rstrip()

dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]  # 문자열 결과값 저장용
ans = 0     # max 값 비교용
# 해당 문자가 같다면, dp[i-1][j-1] + 1 저장
# 이후 비교
for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans,dp[i][j])
print(ans)
