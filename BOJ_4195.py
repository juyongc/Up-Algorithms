import sys

# 부모 찾기
def upper(x):
    if parent[x] == x:
        return x
    else:
        y = upper(parent[x])
        parent[x] = y
        return y

# 작은 부모 값이 큰 부모 값의 부모되기
# num값 갱신하기
def union(x, y):
    x = upper(x)
    y = upper(y)

    if x == y:
        return num[x]
    elif x < y:
        parent[y] = x
        num[x] = num[x] + num[y]
        num[y] = 0
        return num[x]
    else:
        parent[x] = y
        num[y] = num[y] + num[x]
        num[x] = 0
        return num[y]


inputs = sys.stdin.readline

T = int(inputs())
for t in range(1,T+1):
    F = int(inputs())
    # 시간 효율을 위해 dict 사용
    parent = dict()
    num = dict()
    for i in range(F):
        a, b = map(str, inputs().split())
        # 기존 parent에 없으면 만들기
        if a not in parent:
            parent[a] = a
            num[a] = 1
        if b not in parent:
            parent[b] = b
            num[b] = 1

        ans = union(a,b)
        print(ans)