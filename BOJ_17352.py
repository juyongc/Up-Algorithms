import sys
from collections import deque
inputs = sys.stdin.readline

# 통행 가능한 모든 다리 확인
def find_connection(x):
    q = deque()
    q.append(x)
    visit[x] = x

    while q:
        now = q.popleft()
        for val in bridge[now]:
            if not visit[val]:
                visit[val] = now
                q.append(val)
    return x


N = int(input())
bridge = [[] for _ in range(N+1)]
for _ in range(N-2):
    a,b = map(int,inputs().split())
    bridge[a].append(b)
    bridge[b].append(a)

visit = [0]*(N+1)
answer = []
# 아직 방문하지 않은 다리 연결 여부 확인
for i in range(1,N+1):
    if not visit[i]:
        ans = find_connection(i)
        answer.append(ans)

print(answer[0],answer[1])