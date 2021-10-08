def solution(arr):
    answer = []
    ze,one = 0,0
    s = []
    row,col = len(arr),len(arr[0])
    s.append((0,0,row,col))

    while s:
        flag = 0
        sx,sy,ex,ey = s.pop()
        now = arr[sx][sy]
        # 해당 영역이 다 같은 값인지 확인
        for i in range(sx,ex):
            for j in range(sy,ey):
                if arr[i][j] != now:
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 1:   # 4등분하기
            if ex-sx <= 2:  # 다음값이 1이라면 => 해당 값 확인
                for i in range(sx,ex):
                    for j in range(sy,ey):
                        if arr[i][j] == 0:
                            ze += 1
                        else:
                            one += 1
                continue
            mx = (sx+ex)//2
            my = (sy+ey)//2
            s.append((sx,sy,mx,my))
            s.append((mx,sy,ex,my))
            s.append((sx,my,mx,ey))
            s.append((mx,my,ex,ey))
        else:
            if now == 0:
                ze += 1
            else:
                one += 1
            
    answer = [ze,one]
    return answer