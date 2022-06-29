import sys
inputs = sys.stdin.readline

N = int(input())
arr = [list(map(int,inputs().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]

ans = 9999999999

# RGB별 첫번째 집 정하기
for k in range(3):
    # 두번쩨 집은 첫번째 집 값 + 각자 집 값
    for i in range(3):
        dp[1][i] = (arr[0][k] + arr[1][i])
    dp[1][k] = 10000        # 첫번째 집과 같은 색은 선택 불가 - 값 강제로 크게 조정

    for i in range(2,N):
        dp[i][0] = min(dp[i-1][1],dp[i-1][2]) + arr[i][0]
        dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + arr[i][1]
        dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + arr[i][2]

    for i in range(3):
        if i == k:
            continue
        ans = min(ans,dp[-1][i])

print(ans)
