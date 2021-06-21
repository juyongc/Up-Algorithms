import sys
sys.setrecursionlimit(10**5)

# 부모 찾기
def upper(x):
    if parent[x] == x:
        return x
    else:
        y = upper(parent[x])
        parent[x] = y
        return y

# 부모 vs 부모
# 작은 값의 부모가 더 큰 값의 부모의 부모가 됨
def union(x, y):
    x = upper(x)
    y = upper(y)

    if x <= y:
        parent[y] = x
    else:
        parent[x] = y


inputs = sys.stdin.readline
N,M = map(int,inputs().split())

parent = [i for i in range(N+1)]

for _ in range(M):
    flag,a,b = map(int,inputs().split())
    if flag == 0:
        union(a,b)
    else:
        if upper(a) == upper(b):
            print('YES')
        else:
            print('NO')
