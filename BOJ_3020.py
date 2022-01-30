import sys
inputs = sys.stdin.readline

N,H = map(int,inputs().split())

up = [0]*(H+1)
down = [0]*(H+1)

# 석순 / 종유석 구분
for i in range(N):
    if i % 2 == 0:
        up[int(input())] += 1
    else:
        down[int(input())] += 1

# 누적합
for i in range(H-1,0,-1):
    up[i] += up[i+1]
    down[i] += down[i+1]

mini = N
ans = 0
# 최소값, 구간 개수 카운팅
for i in range(1,H+1):
    if mini > (up[i] + down[H-i+1]):
        mini = up[i] + down[H-i+1]
        ans = 1
    elif (up[i] + down[H-i+1]) == mini:
        ans += 1
print(mini, ans)