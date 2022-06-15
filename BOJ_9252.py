import sys
inputs = sys.stdin.readline

sentence1 = list(input())
sentence2 = list(input())

# s1 - 긴 문장 / s2 - 짧은 문장
if len(sentence1) >= len(sentence2):
    s1,s2 = sentence1,sentence2
else:
    s1,s2 = sentence2,sentence1

dp = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]

# dp[i][j] = max(dp[i-1][j-1]+x,dp[i-1][j],dp[i][j-1])
for i in range(1,len(s2)+1):
    for j in range(1,len(s1)+1):
        if s2[i-1] == s1[j-1]:
            dp[i][j] = max(dp[i-1][j-1]+1,dp[i-1][j],dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])

lcs_length = max(dp[-1])
if lcs_length == 0:
    print(lcs_length)
else:
    answer = ""
    x,y = len(s2), len(s1)
    # 대각선 방향으로 값 변경되는 위치 찾기
    while x > 0 and y > 0:
        if dp[x][y] == dp[x][y-1]:
            y -= 1
        elif dp[x][y] == dp[x-1][y]:
            x -= 1
        else:
            answer += s1[y-1]
            x -= 1
            y -= 1

    print(lcs_length)
    print(answer[::-1])

