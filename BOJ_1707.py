import sys
from collections import deque
inputs = sys.stdin.readline


def bfs(s):
    global visit
    q = deque()
    q.append((0,s))
    visit[s] = 1    # 시작값 => 1
    while q:
        prev,now = q.popleft()
        color = visit[now]      # 현재 노드 색깔
        for num in trees[now]:
            if num == prev:     # 이전에 방문한 노드면 continue
                continue

            if visit[num] == 0:     # 미방문 => 현재 색 반대로 / 큐에 추가
                visit[num] = -color
                q.append((now,num))
            else:                           # 이미 방문했으면
                if visit[num] == color:     # 색이 같으면 => False
                    return False

    return True


K = int(input())
for _ in range(K):
    V,E = map(int,inputs().split())
    trees = [[] for _ in range(V+1)]
    for _ in range(E):
        u,v = map(int,inputs().split())
        trees[u].append(v)
        trees[v].append(u)

    visit = [0] * (V + 1)
    ans = 0
    # 모든 노드 확인
    for i in range(1,V+1):
        if visit[i] == 0:
            check = bfs(i)
            if not check:
                ans = -1
                break

    if ans == 0:
        print("YES")
    else:
        print("NO")
