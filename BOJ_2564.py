import sys
inputs = sys.stdin.readline

# 좌표 구하기
def get_direction(d,x):

    start = [0,0]
    if d == 1:
        start[1] += x
    elif d == 2:
        start[1] += x
        start[0] = M
    elif d == 3:
        start[0] += x
    else:
        start[0] += x
        start[1] = N

    return start


N,M = map(int,inputs().split())
T = int(input())

stores = []
for _ in range(T):
    sd,sx = map(int,inputs().split())
    s_loc = get_direction(sd,sx)
    stores.append((s_loc,sd))

dong_d,dong_x = map(int,inputs().split())
d_loc = get_direction(dong_d,dong_x)
dx,dy = d_loc

total = 2*(N+M)
mini = 0
for s_loc,s_d in stores:
    sx,sy = s_loc
    # 동근이가 남,서에 있으면
    if dong_d == 2 or dong_d == 3:
        if s_d == 2 or s_d == 3:        # 상점이 남,서에 있으면 => 겹침
            mini += abs(sx-dx) + abs(sy-dy)
        else:                           # 아니면 안겹침
            case1 = dx + sx + sy + dy
            case2 = total - case1
            mini += min(case1,case2)
    # 반대의 경우
    else:
        if s_d == 1 or s_d == 4:
            mini += abs(sx-dx) + abs(sy-dy)
        else:
            case1 = dx + sx + sy + dy
            case2 = total - case1
            mini += min(case1,case2)

print(mini)
