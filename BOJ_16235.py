import sys
inputs = sys.stdin.readline

N,M,K = map(int,inputs().split())
land = [list(map(int,inputs().split())) for _ in range(N)]
A = [[5]*N for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

for _ in range(M):
    x,y,z = map(int,inputs().split())
    trees[x-1][y-1].append(z)

for _ in range(K):
    # 봄
    dies = [[0]*N for _ in range(N)]    # 죽은 나무 값
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                trees[i][j].sort()
                new = []
                for k in range(len(trees[i][j])):
                    if A[i][j] >= trees[i][j][k]:
                        new.append(trees[i][j][k]+1)
                        A[i][j] -= trees[i][j][k]
                    else:
                        dies[i][j] += (trees[i][j][k] // 2)
                trees[i][j] = new[:]
            else:
                continue
    # 여름
    for i in range(N):
        for j in range(N):
            A[i][j] += dies[i][j]
    # 가을
    born = []   # 주변에 태어날 나무
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                if trees[i][j][-1] >= 5:
                    for k in range(len(trees[i][j])):
                        if trees[i][j][k] % 5 == 0:
                            born.append((i,j))
            else:
                continue

    while born:
        x,y = born.pop()
        for k in range(8):
            a,b = x+dx[k],y+dy[k]
            if 0<=a<N and 0<=b<N:
                trees[a][b].append(1)
    # 겨울
    for i in range(N):
        for j in range(N):
            A[i][j] += land[i][j]

ans = 0
for i in range(N):
    for j in range(N):
        ans += len(trees[i][j])

print(ans)
