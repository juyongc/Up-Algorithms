import sys
inputs = sys.stdin.readline

# arr1과 arr2가 다르면 뒤집기
# 같거나 행렬 범위 벗어나면 뒤집기 X
def flip(x,y,N,M):
    global arr1,arr2
    flag = 0
    if arr1[x][y] == arr2[x][y]:
        return flag
    if x + 3 > N or y + 3 > M:
        return flag

    for a in range(x,x+3):
        for b in range(y,y+3):
            if arr1[a][b] == "0":
                arr1[a][b] = "1"
            else:
                arr1[a][b] = "0"
    flag = 1
    return flag


N,M = map(int,inputs().split())
arr1 = []
arr2 = []
for i in range(2):
    for _ in range(N):
        if i == 0:
            arr1.append(list(input()))
        else:
            arr2.append(list(input()))

cnt = 0     # 뒤집기 카운팅
for i in range(N):
    for j in range(M):
        cnt += flip(i,j,N,M)

check = 0   # arr1과 arr2 같은지 확인
for i in range(N):
    for j in range(M):
        if arr1[i][j] != arr2[i][j]:
            check = 1
            break
    if check == 1:
        break

if check:
    print(-1)
else:
    print(cnt)
