import sys
inputs = sys.stdin.readline

# 상어 잡기
def find_shark(col,row):
    global answer,shark,shark_list
    catch_row,catch_col = -1,-1
    # 해당 열에서 가장 가까운 상어 찾기
    for k in range(row):
        if shark[k][col]:
            answer += shark[k][col][0][-1]
            shark[k][col].pop()
            catch_row = k
            catch_col = col
            break
    # 이동 후 상어 위치 리스트
    shark_list = move_shark(catch_row,catch_col)
    shark = [[[] for _ in range(C)] for _ in range(R)]
    # 새 상어 위치 행렬 만들기
    for shar in shark_list:
        r, c, s, d, z = shar
        shark[r][c].append([s, d, z])

# 상어 이동 및 잡아먹은 후 리스트 만들기
def move_shark(catch_row,catch_col):
    global shark_list,shark
    shark_move_dict = {}
    for shar in shark_list:
        r,c,vel,direct,size = shar
        if r == catch_row and c == catch_col:   # 잡은 상어니까 continue
            continue

        mr,mc = r,c
        # 위,아래 이동이면
        if direct == 0 or direct == 1:
            if vel > (2*(R-1)):     # 반복 줄이기 위해 => 한바퀴이내로 이동시키기
                vel %= (2*(R-1))
            rem = vel
            # 이동 => 0이면 - 아래로 / 마지막 열이면 - 위로
            while rem > 0:
                if mr <= 0:
                    direct = 1
                if mr >= R-1:
                    direct = 0
                mr = mr + dx[direct]
                rem -= 1
            # 잡아먹기 확인하기 위해 딕셔너리에 추가
            if (mr,mc) in shark_move_dict:
                shark_move_dict[(mr,mc)].append((vel,direct,size))
            else:
                shark_move_dict[(mr, mc)] = [(vel,direct,size)]
        else:       # 옆으로 이동
            if vel > (2*(C-1)):
                vel %= (2*(C-1))
            rem = vel
            # 이동 => 0이면 - 오른쪽 / 마지막 행이면 - 왼쪽
            while rem > 0:
                if mc <= 0:
                    direct = 2
                if mc >= C-1:
                    direct = 3
                mc = mc + dy[direct]
                rem -= 1
            if (mr,mc) in shark_move_dict:
                shark_move_dict[(mr,mc)].append((vel,direct,size))
            else:
                shark_move_dict[(mr, mc)] = [(vel,direct,size)]

    new_shark_list = []
    # 잡아먹기 확인하기
    for key,val in shark_move_dict.items():
        if len(val) > 1:        # 잡아먹기 => 가장 큰 사이즈만 리스트 추가
            val.sort(key=lambda x:-x[2])
            new_shark_list.append([key[0], key[1], val[0][0], val[0][1], val[0][2]])
        else:
            new_shark_list.append([key[0], key[1], val[0][0], val[0][1], val[0][2]])
    return new_shark_list


R,C,M = map(int,inputs().split())
shark = [[[] for _ in range(C)] for _ in range(R)]
shark_list = []
for _ in range(M):
    r,c,s,d,z = map(int,inputs().split())
    shark[r-1][c-1].append([s,d-1,z])
    shark_list.append([r-1,c-1,s,d-1,z])
    
dx = [-1,1,0,0]
dy = [0,0,1,-1]

answer = 0      # 잡은 상어 크키
# 한칸씩 옆으로 가면서 상어 체크
for i in range(C):
    find_shark(i,R)

print(answer)