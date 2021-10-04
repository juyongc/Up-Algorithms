def solution(land):
    answer = 0

    row = len(land)
    col = len(land[0])
    # 이전값에서 가장 큰 값 더하기
    for i in range(1,row):
        for j in range(col):
            land[i][j] += max(land[i-1][0:j] + land[i-1][j+1:])
            
    answer = max(land[-1])
    return answer