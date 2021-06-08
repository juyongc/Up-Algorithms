import sys

# 연결된 노드 찾는 함수(DFS)
def move(x):
    visit[x] = 1
    stack = [x]
    while stack:
        now = stack.pop()
        for num in nodes[now]:
            if visit[num] == 0:
                visit[num] = 1
                stack.append(num)

inputs = sys.stdin.readline

N,M = map(int,inputs().split())
nodes = [[] for _ in range(N+1)]

for _ in range(M):
    u,v = map(int,inputs().split())
    # 양방향
    nodes[u].append(v)
    nodes[v].append(u)

visit = [0]*(N+1)   # 방문 체크
cnt = 0             # 연결 요소 카운트
for i in range(1,N+1):
    if visit[i] == 0:   # 방문 안했으면
        cnt += 1        # 연결요소 카운트 +1
        move(i)         # 연결 노드 탐색

print(cnt)