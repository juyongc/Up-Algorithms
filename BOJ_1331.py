import sys
inputs = sys.stdin.readline

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [1,-1,2,-2,2,-2,1,-1]

# 시작점
start_loc = input()
start_alpha = ord(start_loc[0])
start_num = int(start_loc[1:])

x,y = start_num,start_alpha
visit = [[0]*6 for _ in range(7)]       # 방문체크용
visit[x][y-65] = 1
flag = 1                                # 다음 위치 이동 확인용 플래그
# 다음 위치로 나이트 이동할 수 있는지 확인
# 이미 방문한 위치 방문하면 => 모든 위치 방문 불가 & break
for _ in range(35):
    loc = input()
    alpha = ord(loc[0])
    num = int(loc[1:])

    cx = x - num
    cy = y - alpha

    for i in range(8):
        if cx == dx[i] and cy == dy[i]:
            x,y = num,alpha
            break

    if visit[x][y-65]:
        flag = 0
        break
    else:
        visit[x][y-65] = 1

    if x != num and y != alpha:
        flag = 0
        break

# 마지막까지 가면 마지막에서 처음 위치 올 수 있는지 확인
if flag:
    cx = x - start_num
    cy = y - start_alpha
    for i in range(8):
        if cx == dx[i] and cy == dy[i]:
            x,y = start_num,start_alpha
            break
    if x != start_num and y != start_alpha:
        flag = 0

if flag:
    answer = "Valid"
else:
    answer = "Invalid"

print(answer)