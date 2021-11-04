import sys
from collections import deque
inputs = sys.stdin.readline

# 가장 값이 큰 노드찾기
def bfs(root,rval):
    q = deque()
    q.append((root,rval))
    visit = [-1]*(N+1)      # 방문 체크 및 값 확인용
    visit[root] = 0
    node,maxi = 0,0
    while q:
        pp,pv = q.popleft()
        for tree in trees[pp]:
            cc,cv = tree
            if visit[cc] == -1:     # 미방문이면
                nval = pv + cv      # 값 갱신
                visit[cc] = nval
                q.append((cc,nval))
                if nval > maxi:     # 최대값 갱신
                    maxi = nval
                    node = cc
    return (node,maxi)


N = int(input())
trees = [[] for _ in range(N+1)]
for _ in range(N-1):
    p,c,v = map(int,inputs().split())
    trees[p].append((c,v))
    trees[c].append((p,v))

dist,cost = bfs(1,0)        # 루트에서 가장 값이 큰 노드 찾기
dist,ans = bfs(dist,0)      # 해당 노드에서 가장 값이 큰 노드 찾기

print(ans)
