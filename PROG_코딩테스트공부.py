def solution(alp, cop, problems):
    answer = 0
    
    alp_max,cop_max = 0,0
    for problem in problems:
        alp_max = max(alp_max, problem[0])
        cop_max = max(cop_max, problem[1])

    dp = [[99999999]*(cop_max+1) for _ in range(alp_max+1)]
    # alp,cop가 주어진 문제의 max보다 클 수 있으므로
    # min으로 시작할 alp, cop 정하기
    alp,cop = min(alp,alp_max),min(cop,cop_max)
    dp[alp][cop] = 0
    problems.sort()
    
    for i in range(alp,alp_max+1):
        for j in range(cop_max+1):
            # max값 범위 내에 다음 값 갱신하기
            if i + 1 <= alp_max:
                dp[i+1][j] = min(dp[i+1][j],dp[i][j] + 1)
            if j + 1 <= cop_max:
                dp[i][j+1] = min(dp[i][j+1],dp[i][j] + 1)
            # 모든 문제 풀면서 갱신하기
            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                # 요구 조건 안되면 continue
                if alp_req > i or cop_req > j:
                    continue
                # max값을 넘을 수 있으므로 min으로 제한하기
                next_alp, next_cop = min(i+alp_rwd,alp_max), min(j+cop_rwd,cop_max)
                # min(현재 dp값+문제푼 시간, 해당 dp값, 갱신된 dp값)
                dp[next_alp][next_cop] = min(dp[i][j]+cost,dp[next_alp][next_cop],dp[i][j]+next_alp+next_cop)
    answer = dp[-1][-1]
    return answer