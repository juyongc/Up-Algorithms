import sys
inputs = sys.stdin.readline


def rotate(arr, n, d):
    if d > 0:       # 0보다 크면 => 8로 나누기
        d = d % 8
    else:           # 0보다 작으면 => 양수로 만든 후, 다시 음수로 만들기
        d = 8 - ((-d) % 8)
        if d == 8:  # 계산 시간 절약용
            d = 0

    stack = []
    mid = (n + 1) // 2 - 1      # 가운데 위치
    while d > 0:
        for i in range(n):
            stack.append((i, mid, arr[i][i]))
            stack.append((i, n - 1 - i, arr[i][mid]))
            stack.append((mid, n - 1 - i, arr[i][n - 1 - i]))
            stack.append((i, i, arr[mid][i]))
        while stack:
            x, y, val = stack.pop()
            arr[x][y] = val
        d -= 1
    return arr


T = int(input())
for _ in range(T):
    n,d = map(int,inputs().split())
    d = d // 45     # 45로 나눠서 회전 횟수로 생각하기
    arrs = [list(map(int,inputs().split())) for _ in range(n)]

    ans = rotate(arrs,n,d)
    for k in range(n):
        print(' '.join(map(str,ans[k])))