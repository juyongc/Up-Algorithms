import sys
from collections import deque

# BFS 탐색
def bfs():
    q = deque()     # 큐에 x,y 추가
    q.append(x)
    q.append(y)
    visit = [0] * (N + 1)
    visit[x] = 1    # x,y 방문 체크
    visit[y] = 1
    # 큐 반복
    while q:
        now = q.popleft()
        par = node[now]
        if par == 0:    # 루트 노드면 -> continue
            continue
        
        if visit[par] == 1:     # 방문한 적 있으면 -> 조상
            return par
        else:                   # 방문한 적 없으면 -> 방문체크, 큐 추가
            visit[par] = 1  
            q.append(par)

inputs = sys.stdin.readline
T = int(inputs())
for _ in range(T):
    N = int(inputs())
    node = [0]*(N+1)
    # node[자식] = 부모
    for _ in range(N-1):
        a,b = map(int,inputs().split())
        node[b] = a
    x,y = map(int,inputs().split())

    if x == y:      # x == y라면 
        ans = x
    else:           # 다르다면
        ans = bfs()
    print(ans)