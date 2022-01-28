def solution(n, m, x, y, queries):
    answer = 0
    x1,y1,x2,y2 = x,y,x,y
    flag = 0
    # 쿼리 역순으로
    while queries:
        command,num = queries.pop()
        # 커맨드별 사각형 위치 재조정
        if command == 0:
            if y2 + num >= m:
                val = m-1
            else:
                val = y2 + num
            if y1 != 0:
                y1 += num
            y2 = val
        elif command == 1:
            if y1 - num < 0:
                val = 0
            else:
                val = y1 - num
            if y2 != m-1:
                y2 -= num
            y1 = val
        elif command == 2:
            if x2 + num >= n:
                val = n-1
            else:
                val = x2 + num
            if x1 != 0:
                x1 += num
            x2 = val
        else:
            if x1 - num < 0:
                val = 0
            else:
                val = x1 - num
            if x2 != n-1:
                x2 -= num
            x1 = val
        # 불가능한 위치 제시 => flag = 1, break
        if y1 > m - 1 or y2 < 0 or x1 > n - 1 or x2 < 0:
            flag = 1
            break
    # 무사히 종료됐으면 => 정답 갱신
    if flag == 0:    
        answer = (y2-y1+1) * (x2-x1+1)
    
    return answer