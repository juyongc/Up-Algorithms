import sys

# 부모 찾기
def upper(x):
    if parent[x] == x:
        return x
    else:
        y = upper(parent[x])
        parent[x] = y
        return y

# x,y 중 부모 값이 더 작은 부모가
# 더 큰 부모의 부모 되기
def union(x, y):
    x = upper(x)
    y = upper(y)

    if x <= y:
        parent[y] = x
    else:
        parent[x] = y


inputs = sys.stdin.readline
N = int(inputs())
M = int(inputs())

parent = [i for i in range(N+1)]

# 여행지별 연결된 여행지의 부모 통일하기
for i in range(1,N+1):
    info = list(map(int,inputs().split()))
    # 1이 나오면 => union(i,j+1)
    for j in range(N):
        if info[j] == 1:
            if upper(i) != upper(j+1):
                union(i,j+1)

trip = list(map(int,inputs().split()))

ans = 0
# 여행지의 부모 여행지가 다르면 break
for i in range(len(trip)):
    if i == 0:
        now = parent[trip[i]]
    else:
        if parent[trip[i]] != now:
            ans = 1
            break

if ans == 0:
    print('YES')
else:
    print('NO')