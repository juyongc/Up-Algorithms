import sys
import heapq

# 부모 찾기
def find(x):
    if parent[x] == x:
        return x
    else:
        y= find(parent[x])
        parent[x] = y
        return y

# 부모 변경하기
def union(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        if x > y:
            parent[x] = y
        else:
            parent[y] = x

# 가까운 행성 연결
def connections():
    hq = []
    tot = 0
    cnt = 0
    # x,y,z 중 가장 가까운 행성끼리 연결함
    # 각각 비교해서 가장 가까운 행성끼리 연결(list 0~1, 1~2 이렇게)
    # 한번에 x,y,z 비교하면 메모리 초과
    pos.sort(key=lambda x:x[1])
    for i in range(N-1):
        mini = abs(pos[i][1]-pos[i+1][1])
        heapq.heappush(hq,[mini,pos[i][0],pos[i+1][0]])
    pos.sort(key=lambda x:x[2])
    for i in range(N-1):
        mini = abs(pos[i][2]-pos[i+1][2])
        heapq.heappush(hq,[mini,pos[i][0],pos[i+1][0]])
    pos.sort(key=lambda x:x[3])
    for i in range(N-1):
        mini = abs(pos[i][3]-pos[i+1][3])
        heapq.heappush(hq,[mini,pos[i][0],pos[i+1][0]])
    # 부모가 달라야지만 카운트
    while cnt < N-1:
        now = heapq.heappop(hq)
        if find(now[1]) != find(now[2]):
            union(now[1],now[2])
            tot += now[0]
            cnt += 1

    return tot

inputs = sys.stdin.readline
N = int(inputs())
parent = [i for i in range(N)]
# 행성 번호, x,y,z 값
pos = [[i]+list(map(int,inputs().split())) for i in range(N)]
ans = connections()

print(ans)