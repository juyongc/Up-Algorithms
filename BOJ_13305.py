import sys
inputs = sys.stdin.readline

N = int(input())
roads = list(map(int,inputs().split()))
costs = list(map(int,inputs().split()))

tot = 0
cur = costs[0]
# 다음 도시 가격과 비교해서 최소값으로 갱신
for i in range(N-1):
    if costs[i] < cur:
        cur = costs[i]
    tot += (roads[i]*cur)

print(tot)