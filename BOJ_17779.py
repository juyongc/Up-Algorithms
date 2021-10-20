import sys
inputs = sys.stdin.readline

# 가능한 모든 x,y,d1,d2 구하기
def poss(xx,yy,dd1,dd2):
    global possible
    if (xx,yy,dd1,dd2) in possible:     # possible 셋에 있는지 체크
        return
    if (xx+dd1+dd2 >= N) or (yy-dd1 < 0) or (yy+dd2 >= N):
        return
    possible.add((xx,yy,dd1,dd2))
    poss(xx+1,yy,dd1,dd2)
    poss(xx,yy+1,dd1,dd2)
    poss(xx,yy,dd1+1,dd2)
    poss(xx,yy,dd1,dd2+1)

N = int(input())
roads = [list(map(int,input().split())) for _ in range(N)]

possible = set()
poss(0,1,1,1)
pos = list(set(possible))

mini = 99999999999  # 최소값 초기화
# 모든 경우의 수 확인
for po in pos:
    visit = [[0] * N for _ in range(N)]     # 선거 구 정하기용
    x,y,d1,d2 = po[0],po[1],po[2],po[3]
    # 5번 구역 경계 찾기
    s,e = y,y
    for i in range(x,x+d1+1):
        visit[i][s] = 5
        s -= 1
    for i in range(x,x+d2+1):
        visit[i][e] = 5
        e += 1
    s,e = y-d1,y+d2
    for i in range(x+d1,x+d1+d2+1):
        visit[i][s] = 5
        s += 1
    for i in range(x+d2,x+d1+d2+1):
        visit[i][e] = 5
        e -= 1
    # 5번 구역 확정하기
    for i in range(x+1,x+d1+d2):
        flag = 0
        for j in range(y-d1,y+d2+1):
            if flag == 0:
                if visit[i][j] == 5:
                    flag = 1
            else:
                if visit[i][j] == 0:
                    visit[i][j] = 5
                else:
                    break
    # 구역별 조건에 맞게 구하기
    for i in range(0,x+d1):
        for j in range(0,y+1):
            if visit[i][j] == 0:
                visit[i][j] = 1
    for i in range(x+d2+1):
        for j in range(y+1,N):
            if visit[i][j] == 0:
                visit[i][j] = 2
    for i in range(x+d1,N):
        for j in range(y-d1+d2):
            if visit[i][j] == 0:
                visit[i][j] = 3
    for i in range(x+d2+1,N):
        for j in range(y-d1+d2,N):
            if visit[i][j] == 0:
                visit[i][j] = 4
    # 최소,최대 구역값 구하기
    vote = [0,0,0,0,0,0]
    for i in range(N):
        for j in range(N):
            k = visit[i][j]
            vote[k] += roads[i][j]

    mmax = max(vote[1:])
    mmin = min(vote[1:])

    cost = mmax - mmin      # 구역값=> 최대 - 최소
    if cost < mini:         # 비교
        mini = cost

print(mini)