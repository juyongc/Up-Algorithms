def solution(n):
    answer = 0
    dp = [0]*(n+1)
    dp[1] = 1
    # n번째 수까지 dp
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    answer = dp[-1]
    return answer%1234567