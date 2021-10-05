def solution(dirs):
    answer = 0
    tot = set()
    move = {'U':(1,0),'D':(-1,0),'L':(0,-1),'R':(0,1)}
    x,y = 0,0
    for i in range(len(dirs)):
        plus = move[dirs[i]]
        a,b = x+plus[0],y+plus[1]
        if -5<=a<6 and -5<=b<6:
            if (x,y,a,b) not in tot:
                tot.add((x,y,a,b))
                tot.add((a,b,x,y))  # 양방향 확인
                answer += 1
            x,y = a,b
    return answer