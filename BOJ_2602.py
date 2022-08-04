import sys
inputs = sys.stdin.readline

magic = list(input())
angel = list(input())
evil = list(input())

dp = [[[0]*(len(magic)+1) for _ in range(len(angel)+1)] for _ in range(2)]

# dp로 이전값을 받아오면서 문자열에 같은 값 있으면 갱신
# dp[i][j][k] = dp[i][j-1][k] + dp[(i+1)%2][j-1][k-1] (같은 값인 문자가 있으면)
for j in range(1,len(angel)+1):
    for k in range(1,len(magic)+1):
        dp[0][j][k] = dp[0][j - 1][k]
        dp[1][j][k] = dp[1][j - 1][k]
        if magic[k-1] == angel[j-1]:
            if k == 1:
                dp[0][j][k] += 1
            else:
                dp[0][j][k] += dp[1][j-1][k-1]

        if magic[k-1] == evil[j-1]:
            if k == 1:
                dp[1][j][k] += 1
            else:
                dp[1][j][k] += dp[0][j - 1][k - 1]

answer = dp[0][-1][-1] + dp[1][-1][-1]
print(answer)
