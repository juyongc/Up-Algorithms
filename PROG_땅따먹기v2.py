def solution(land):
    answer = 0
    
    dp = [[0]*4 for _ in range(len(land))]
    for i in range(4):
        dp[0][i] = land[0][i]
    
    # 이전 dp값과 현재 땅 위치를 더한 값이 max인지 비교
    # 같은 열은 통과
    for i in range(1,len(land)):
        for j in range(4):
            for k in range(4):
                if j == k:
                    continue
                dp[i][j] = max(dp[i-1][k]+land[i][j],dp[i][j])
    answer = max(dp[-1])
    return answer