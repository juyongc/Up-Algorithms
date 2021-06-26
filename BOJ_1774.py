import sys
import heapq

# 두 좌표간 거리 측정
def distance(a,b):
    # 이미 연결되어 있으면 => 0
    if b in already[a]:
        ab = 0.00
    # 아니면 계산
    else:
        ab = ((pos[a][0]-pos[b][0])**2+(pos[a][1]-pos[b][1])**2)**(1/2)
    return ab

# 부모 찾기
def find(a):
    if parent[a] == a:
        return a
    else:
        b = find(parent[a])
        parent[a] = b
        return b

# 부모가 다르면 변경
def union(a,b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a
        return

# 가장 가까운 신들끼리 연결해서 사이클 만들기
def mst():
    cnt = N - 1     # 반복 횟수
    hq = []         # 힙 만들기
    tot = 0.00      # 총 좌표 합
    # 신들간 거리,신1,신2 힙에 넣기
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            heapq.heappush(hq, [distance(i, j),i,j])
    hq.sort()       # 거리 가까운 순으로 정렬
    # 반복
    while cnt > 0:
        now,x,y = heapq.heappop(hq)
        # 두 신이 연결 안됐으면,
        if find(x) != find(y):
            union(x,y)      # 신끼리 연결하고 부모 변경
            tot += now      # 좌표 거리 더하기
            cnt -= 1        # 반복 카운트 -1
    return tot


inputs = sys.stdin.readline
N,M = map(int,inputs().split())
parent = [i for i in range(N+1)]
pos = [(0,0)]
for _ in range(N):
    a,b = map(int,inputs().split())
    pos.append((a,b))

already = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,inputs().split())
    already[a].append(b)
    already[b].append(a)

ans = mst()
print(format(ans,".2f"))