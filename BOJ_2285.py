import sys
inputs = sys.stdin.readline

N = int(input())
area = [list(map(int,inputs().split())) for _ in range(N)]
area.sort(key=lambda x: x[0])

l, r = [0]*N, [0]*N
tot = 0
for i in range(N):
    tot += area[i][1]

people = 0
ans = area[0][0]
# 인원이 절반 이상인 곳 찾기
# 같으면 위치 작은 곳이어야 함
for i in range(N):
    people += area[i][1]
    if people >= tot / 2:
        ans = area[i][0]
        break

print(ans)
