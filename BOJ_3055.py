import sys
from collections import deque

# 홍수랑 고슴도치 위치
def move(arr):
    global cnt1,cnt2
    tot = 0
    # 고슴도치 아직 있으면,
    while gochi:
        # 이동횟수 +1
        tot += 1
        # 이번 턴 홍수 이동
        while cnt2>0:
            wx,wy = water.popleft()
            cnt2 -= 1
            for k in range(4):
                if 0<=wx+dx[k]<R and 0<=wy+dy[k]<C:
                    if arr[wx+dx[k]][wy+dy[k]] == '.' or arr[wx+dx[k]][wy+dy[k]] == 'S':
                        water.append([wx+dx[k],wy+dy[k]])
                        arr[wx + dx[k]][wy + dy[k]] = '*'
        # 다음 턴 홍수 위치 개수
        cnt2 += len(water)
        # 이번 턴 고슴도치 이동
        while cnt1>0:
            gx, gy = gochi.popleft()
            cnt1 -= 1
            for k in range(4):
                if 0 <= gx + dx[k] < R and 0 <= gy + dy[k] < C:
                    if arr[gx + dx[k]][gy + dy[k]] == '.':
                        gochi.append([gx + dx[k], gy + dy[k]])
                        arr[gx + dx[k]][gy + dy[k]] = 'S'
                    # 비버집 도착
                    elif arr[gx + dx[k]][gy + dy[k]] == 'D':
                        return tot
        # 다음 턴 고슴도치 위치 개수
        cnt1 += len(gochi)
    return 'KAKTUS'


R,C = map(int,input().split())
forest = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
gochi = deque()
water = deque()
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt1,cnt2 = 0,0
# 홍수랑 고슴도치 첫 위치
for i in range(R):
    for j in range(C):
        if forest[i][j] == 'S':
            gochi.append([i,j])
            cnt1 += 1
        elif forest[i][j] == '*':
            water.append([i,j])
            cnt2 += 1
ans = move(forest)
print(ans)