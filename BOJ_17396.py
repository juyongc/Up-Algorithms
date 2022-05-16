import sys
import heapq
inputs = sys.stdin.readline

N,M = map(int,inputs().split())
discover = list(map(int,input().split()))
move = [{} for _ in range(N)]

# 양뱡향
for _ in range(M):
    a,b,t = map(int,inputs().split())
    move[a][b] = t
    move[b][a] = t

W = [10**20] * N
hq = [(0,0)]
W[0] = 0

# 넥서스를 제외한 발각되는 곳 W값 0으로 변경
for i in range(N-1):
    if discover[i] == 1:
        W[i] = 0

# 다익스트라
while hq:
    cost, now = heapq.heappop(hq)
    if cost > W[now]:
        continue

    for key,val in move[now].items():
        if W[key] > cost + val:
            W[key] = cost + val
            heapq.heappush(hq, (cost+val, key))

answer = W[-1]
if answer == 10**20:
    answer = -1

print(answer)