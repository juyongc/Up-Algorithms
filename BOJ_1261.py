import sys
import heapq
inputs = sys.stdin.readline

N,M = map(int,input().split())
maze = [list(input()) for _ in range(M)]
W = [[10**15]*N for _ in range(M)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

hq = [(0,0,0)]      # (value,x,y) 값
W[0][0] = 0
# 다익스트라
while hq:
    w,x,y = heapq.heappop(hq)
    if w > W[x][y]:
        continue
    if x == M-1 and y == N-1:
        break

    for k in range(4):
        r,c = x+dx[k], y+dy[k]
        if 0<=r<M and 0<=c<N:
            if maze[r][c] == '1':
                if W[r][c] > w + 1:
                    W[r][c] = w+1
                    heapq.heappush(hq,(w+1,r,c))
            else:
                if W[r][c] > w:
                    W[r][c] = w
                    heapq.heappush(hq,(w,r,c))

answer = W[-1][-1]
print(answer)