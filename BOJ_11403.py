import sys
from collections import deque

# num -> origin 정점 
def check(num):
    visit = [0]*N   # 정점별 방문체크
    q = deque()     # 큐
    q.append(num)
    # 큐 돌리기
    while q:
        now = q.popleft()   # 현재 정점 위치
        for k in range(N):
            if G[now][k] == 1 and visit[k] == 0:
                q.append(k)
                ans[num][k] = 1     # origin 정점 -> 도착 정점 = 1 이어야 함
                visit[k] = 1        # 방문체크


inputs = sys.stdin.readline
N = int(inputs())
G = [list(map(int,inputs().split())) for _ in range(N)]
ans = [[0]*N for _ in range(N)]

for i in range(N):
    check(i)

for i in range(N):
    print(' '.join(map(str,ans[i])))