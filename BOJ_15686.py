import sys
inputs = sys.stdin.readline

# 조합 계산
def dfs(n,cnt,now,arr):
    global cans
    if cnt >= M:
        cans.append(arr[:])
        return
    for i in range(now+1,n):
        arr[cnt] = i
        dfs(n,cnt+1,i,arr)


N,M = map(int,input().split())
roads = [list(map(int,input().split())) for _ in range(N)]
homes = []
stores = []
# 가게 / 집 위치 찾기
for i in range(N):
    for j in range(N):
        if roads[i][j] == 1:
            homes.append((i,j))
        elif roads[i][j] == 2:
            stores.append((i,j))
        else:
            continue

# 조합 구하기
if M == len(stores):
    cans = [[i for i in range(M)]]
else:
    cans = []
    dfs(len(stores),0,-1,[0]*M)

mini = 99999999999

# 조합별 치킨거리 계산
for can in cans:
    tot = 0
    for home in homes:
        dist = 999999
        for ca in can:
            dist = min(dist,abs(home[0]-stores[ca][0])+abs(home[1]-stores[ca][1]))
        tot += dist
        if tot > mini:
            break
    mini = min(tot,mini)

print(mini)
