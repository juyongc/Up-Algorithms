def solution(n):
    answer = []
    
    cnt = 0
    floors = [[0]*(i+1) for i in range(n)]
    num = 1
    row,col = -1,0
    # 규칙 찾기
    # 아래로 n -> 오른쪽으로 n-1 -> 위로 n-2 ...
    while cnt < n:
        rem = cnt % 3
        tot = n-cnt
        if rem == 0:
            for i in range(tot):
                row += 1
                floors[row][col] = num
                num += 1
        elif rem == 1:
            for i in range(tot):
                col += 1
                floors[row][col] = num
                num += 1
        else:
            for i in range(tot):
                row -= 1
                col -= 1
                floors[row][col] = num
                num += 1
        cnt += 1
        
    for i in range(n):
        answer += floors[i]
        
    return answer