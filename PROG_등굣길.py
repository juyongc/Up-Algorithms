def solution(m, n, puddles):
    answer = 0
    # set으로 변경 및 좌표 (행,열) 변경
    puddle_set = set()
    for puddle in puddles:
        puddle_set.add((puddle[1],puddle[0]))
    
    dx = [1,0]
    dy = [0,1]
    
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = 1
    # dp => 상,우 이동가능하면 dp[상,우] += dp[현재]
    for x in range(n):
        for y in range(m):
            
            if (x+1,y+1) in puddle_set:
                continue
            
            for k in range(2):
                r,c = x+dx[k],y+dy[k]
                if 0<=r<n and 0<=c<m and (r+1,c+1) not in puddle_set:
                    dp[r][c] += dp[x][y]
                    
    answer = dp[-1][-1] % 1000000007
    return answer