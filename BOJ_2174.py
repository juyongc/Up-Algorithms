import sys
inputs = sys.stdin.readline

A,B = map(int,inputs().split())
N,M = map(int,inputs().split())

robot = {}
visit = [[0]*A for _ in range(B)]
for i in range(N):
    message = inputs().split()
    y,x,direct = int(message[0]) - 1,B - int(message[1]),message[2]
    robot[i+1] = [x,y,direct]
    visit[x][y] = i+1

# 방향별 이동 방향
direction = {"E": (0, 1), "W": (0, -1),
             "S": (1, 0), "N": (-1, 0)
             }

rotation = ["E","N","W","S"]    # 인덱스 ++ => 왼쪽 90도 회전

answer = "OK"
for _ in range(M):
    message = inputs().split()
    idx, order, repeat = int(message[0]),message[1],int(message[2])
    flag = 0
    x,y,direct = robot[idx]
    # 현재 방향으로 이동
    if order == "F":
        mx,my = direction[direct]
        robot_x, robot_y = x + mx*repeat, y + my*repeat
        cnt = 1
        while cnt <= repeat:
            rx,ry = x + mx*cnt, y + my*cnt
            # 맵 밖으로 벗아나면 충돌
            if ry < 0 or ry >= A or rx < 0 or rx >= B:
                answer = ("Robot {} crashes into the wall").format(idx)
                flag = 1
                break
            # 다른 로봇과 충돌
            elif visit[rx][ry] != 0:
                answer = ("Robot {} crashes into robot {}").format(idx,visit[rx][ry])
                flag = 1
                break
            cnt += 1
        if flag == 1:   # 이미 충돌났으니 stop
            break
        visit[x][y] = 0                         # 방문 체크 변경(기존 방문지 0으로) 
        robot[idx] = [robot_x,robot_y,direct]   # 로봇 위치 변경
        visit[robot_x][robot_y] = idx           # 방문 체크 변경(현재 위치)
    # 왼쪽으로 90도 회전
    elif order == "L":
        now = 0                 # 현재 방향 인덱스 찾기
        for k in range(4):  
            if rotation[k] == direct:
                now = k
                break
        d = (now + repeat) % 4  # 왼쪽으로 이동한 인덱스
        robot[idx] = [x,y,rotation[d]]
    # 오른쪽으로 90도 회전
    else:
        now = 0                         # 현재 방향 인덱스 찾기
        for k in range(4):
            if rotation[k] == direct:
                now = k
                break
        repeat = repeat % 4 
        d = (now + (4 - repeat)) % 4    # 오른쪽으로 이동한 인덱스
        robot[idx] = [x, y, rotation[d]]

print(answer)
