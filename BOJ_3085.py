import sys

# 같은 행에서의 비교
def row(x):
    global maxi
    cnt = 1
    for k in range(N-1):
        if candy[x][k] == candy[x][k+1]:
            cnt += 1
        else:
            if cnt > maxi:
                maxi = cnt
            cnt = 1
    if cnt > maxi:
        maxi = cnt

# 같은 열에서의 비교
def col(y):
    global maxi
    cnt = 1
    for k in range(N-1):
        if candy[k][y] == candy[k+1][y]:
            cnt += 1
        else:
            if cnt > maxi:
                maxi = cnt
            cnt = 1
    if cnt > maxi:
        maxi = cnt


inputs = sys.stdin.readline

N = int(inputs())
candy = [list(inputs().rstrip()) for _ in range(N)]
maxi = 0
# 기본 행렬에서 maximum(=N)인 행/열 확인
for i in range(N):
    xcnt = 1
    for j in range(N-1):
        if candy[i][j] == candy[i][j+1]:
            xcnt += 1
        else:
            if xcnt > maxi:
                maxi = xcnt
            xcnt = 1
    if xcnt > maxi:
        maxi = xcnt

for j in range(N):
    ycnt = 1
    for i in range(N-1):
        if candy[i][j] == candy[i+1][j]:
            ycnt += 1
        else:
            if ycnt > maxi:
                maxi = ycnt
            ycnt = 1
    if ycnt > maxi:
        maxi = ycnt

if maxi == N:
    print(maxi)
else:           # 기본 행렬에서 maximum 없으면 사탕 바꿔보기
    for i in range(N):          # 같은 행에서 변경
        for j in range(N-1):
            if candy[i][j] != candy[i][j+1]:
                candy[i][j],candy[i][j+1] = candy[i][j+1],candy[i][j]
                row(i)
                col(j)
                col(j+1)
                candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
    for j in range(N):          # 같은 열에서 변경
        for i in range(N-1):
            if candy[i][j] != candy[i+1][j]:
                candy[i][j],candy[i+1][j] = candy[i+1][j],candy[i][j]
                row(i)
                row(i+1)
                col(j)
                candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
    print(maxi)