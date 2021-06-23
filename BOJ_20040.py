import sys

# 부모 찾기
def find(x):
    if parent[x] == x:
        return x
    else:
        y = find(parent[x])
        parent[x] = y
        return y

# num값 비교해서 부모, 자식 정하기
def union(x, y):
    x = find(x)
    y = find(y)

    if num[x] > num[y]:
        parent[y] = x
        num[x] += num[y]
    elif num[x] < num[y]:
        parent[x] = y
        num[y] += num[x]
    else:
        num[x] += 1
        parent[y] = x


inputs = sys.stdin.readline
N,M = map(int,inputs().split())
parent = [i for i in range(N)]
num = [0]*N
ans = 0
for i in range(1,M+1):
    a,b = map(int,inputs().split())
    # 부모가 같으면 => 사이클이 생김
    if find(a) == find(b):
        ans = i
        break
    # 부모,자식 정하기
    else:
        union(a,b)

print(ans)
