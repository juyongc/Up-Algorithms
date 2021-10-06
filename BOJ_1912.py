import sys
inputs = sys.stdin.readline

N = int(inputs().rstrip())
costs = list(map(int,inputs().split()))
maxi = -1111111111
now = 0
# 더하면서 비교
# 0보다 작으면 0으로 리셋
for i in range(N):
    now += costs[i]
    if now > maxi:
        maxi = now
    if now <= 0:
        now = 0

print(maxi)
