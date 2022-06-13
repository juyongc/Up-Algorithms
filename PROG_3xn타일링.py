def solution(n):
    answer = 0
    dp = [0]*(n+1)
    dp[2] = 3
    addition = 0    # 추가로 생기는 값(2개)와 i-2번째와의 조합 
    for i in range(4,n+1,2):
        dp[i] = (dp[i-2]*3 + 2) + addition * 2
        addition += dp[i-2]     # (i-짝수)와 짝수에서 생긴 추가 도형과의 조합 더해주기 위해 
    answer = dp[-1] % 1000000007
    return answer
