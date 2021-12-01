def solution(line):

    cross = []
    # 최소, 최대값 계산해서 정하기!
    x_max,y_max = -999999999999,-999999999999
    x_min,y_min = 999999999999,999999999999
    # 모든 교점 경우의 수
    for i in range(len(line)):
        a,b,e = line[i]
        for j in range(i+1,len(line)):
            c,d,f = line[j]
            demo = a*d - b*c
            # 분모 0 아니고
            if demo != 0:
                x_rem = (b*f - e*d)
                y_rem = (e*c - a*f)
                # 나누어 떨어져야 함
                if (x_rem % demo) == 0 and (y_rem % demo) == 0 :
                    x = x_rem // demo
                    y = y_rem // demo
                    
                    x_min = min(x,x_min)
                    y_min = min(y,y_min)
                    x_max = max(x,x_max)
                    y_max = max(y,y_max)
                    
                    cross.append((x,y))

    
    answer = [["."]*(x_max-x_min+1) for _ in range(y_max-y_min+1)]
    
    cross = list(set(cross))    # 중복 제거
    # 행/열 조건 맞게 만들기
    for cro in cross:
        new_x = cro[0]-x_min    # x의 최소값 -> 0(기준)이 되야 함
        new_y = -(cro[1]-y_max) # y의 최대값 -> 0(기준)이 되야 함
        answer[new_y][new_x] = "*"
        
    return ["".join(ans) for ans in answer]