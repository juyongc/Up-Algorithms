import sys
from collections import deque
inputs = sys.stdin.readline


def rot(num,N):
    global ice
    arr = [[0]*(2**N) for _ in range(2**N)]
    for r in range(0,2**N,num):
        for c in range(0,2**N,num):
            for i in range(num):
                for j in range(num):
                    arr[r+j][c+num-1-i] = ice[r+i][c+j]
    return arr[:]


def reduce_ice(ice):

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    minus = []
    for r in range(len(ice)):
        for c in range(len(ice)):
            if ice[r][c] == 0:
                continue
            cnt = 0
            for k in range(4):
                xx = r + dx[k]
                yy = c + dy[k]
                if 0 <= xx < len(ice) and 0 <= yy < len(ice):
                    if ice[xx][yy] > 0:
                        cnt += 1
            if cnt < 3:
                minus.append((r,c))
    for mx,my in minus:
        ice[mx][my] -= 1
    return ice


def connection(ice):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visit = [[0]*(2**N) for _ in range(2**N)]
    maxi = 0
    q = deque()
    cnt = 1
    for r in range(len(ice)):
        for c in range(len(ice)):
            if visit[r][c] == 0 and ice[r][c] > 0:
                visit[r][c] = cnt
                cc = 1
                q.append((r,c))
                while q:
                    x,y = q.popleft()
                    for k in range(4):
                        xx = x + dx[k]
                        yy = y + dy[k]
                        if 0 <= xx < len(ice) and 0 <= yy < len(ice) and visit[xx][yy] == 0 and ice[xx][yy] > 0:
                            visit[xx][yy] = cnt
                            cc += 1
                            q.append((xx,yy))
                cnt += 1
                maxi = max(cc,maxi)
    return maxi


N,Q = map(int,input().split())
ice = [list(map(int,input().split())) for _ in range(2**N)]
level = list(map(int,input().split()))

for lev in level:
    num = 2 ** lev
    ice = rot(num,N)
    ice = reduce_ice(ice)

tot = 0
for k in range(len(ice)):
    tot += sum(ice[k])
con = connection(ice)

print(tot)
print(con)