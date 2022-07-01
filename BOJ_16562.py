import sys
from collections import deque
inputs = sys.stdin.readline

# 친구의 친구를 찾으며 더 싼 친구가 나오면 금액 갱신
def check_friend(x):
    global visit
    q = deque()
    q.append(x)
    visit[x] = 1
    money = cost[x]
    while q:
        now = q.popleft()
        for f in friend[now]:
            if visit[f] == 0:
                visit[f] = 1
                q.append(f)
                money = min(money, cost[f])

    return money


N,M,K = map(int,input().split())
cost = [0] + list(map(int,inputs().split()))
friend = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,inputs().split())
    friend[a].append(b)
    friend[b].append(a)

visit = [0]*(N+1)
min_cost = 0    # 최소 금액 계산하기
flag = 0        # 친구비 이내 가능한지 확인하기
# 모든 친구 확인
for i in range(1,N+1):
    if visit[i] == 0:   # 방문 체크
        min_cost += check_friend(i)
        if min_cost > K:
            flag = 1
            break

if flag == 1:
    print("Oh no")
else:
    print(min_cost)
