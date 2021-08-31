def solution(triangle):
    answer = 0
    num = len(triangle)
    semo = [[0]*i for i in range(1,num+1)]
    semo[0][0] = triangle[0][0]
    # 밑으로 내려가면서 위에 해당하는 값과 더한 뒤
    # 중복되는 부분은 비교 후 가장 큰 값만 남김
    for i in range(1,num):
        for j in range(i+1):
            if j != 0:
                now = triangle[i][j] + semo[i-1][j-1]
                if now > semo[i][j]:
                    semo[i][j] = now
            if j != i:
                now = triangle[i][j] + semo[i-1][j]
                if now > semo[i][j]:
                    semo[i][j] = now
    # 마지막 줄에서 max값이 정담
    answer = max(semo[-1])
    return answer