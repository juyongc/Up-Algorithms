import sys
import heapq

# 최소 신장 트리 함수
def mst():
    hq = []
    heapq.heappush(hq,[0,0])
    tot = 0
    while hq:
        # 거리값, 현재 인덱스
        val,now = heapq.heappop(hq)
        # 방문에 따른 조건
        if visit[now] == 1:
            continue
        else:
            visit[now] = 1
            tot += val
        # 현재 인덱스 거리값 heapq에 추가
        for i in range(N):
            if i != now:
                heapq.heappush(hq,[dis[now][i],i])
    return tot

inputs = sys.stdin.readline
N = int(inputs())
pos = []
visit = [0]*N
for _ in range(N):
    a,b = map(float,input().split())
    pos.append((a,b))
dis = [[0]*N for _ in range(N)]
# i,j 정점 사이의 거리 구하기
for i in range(N-1):
    for j in range(i+1,N):
        dis[i][j] = round(((pos[i][0]-pos[j][0])**2+(pos[i][1]-pos[j][1])**2)**(1/2),2)
        dis[j][i] = dis[i][j]

ans = mst()
print(ans)