import sys
from collections import deque
inputs = sys.stdin.readline

N,M,K = map(int,inputs().split())
plates = [[[]*N for _ in range(N)] for _ in range(N)]
q = deque()
# q에 값 넣기
for _ in range(M):
    r,c,m,s,d = map(int,inputs().split())
    q.append((r-1,c-1,m,s,d))

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]

for _ in range(K):      # K번 반복
    while q:            # 큐에 있는 모든 값 plates에 넣기
        x,y,m,s,d = q.popleft()
        a,b = (x+(s*dx[d]))%N, (y+(s*dy[d]))%N
        if a < 0:
            a = a + N
        if b < 0:
            b = b + N
        plates[a][b].append([m,s,d])
    tot = 0
    # 모든 인덱스 확인
    for i in range(N):
        for j in range(N):
            if len(plates[i][j]) == 0:      # 빈 곳이면 => continue
                continue
            elif len(plates[i][j]) == 1:    # 하나면 => 큐에 추가 / plates 해당 위치 초기화
                q.append((i,j,plates[i][j][0][0],plates[i][j][0][1],plates[i][j][0][2]))
                tot += plates[i][j][0][0]
                plates[i][j] = []
            else:                           # 두개 이상이면
                mm = plates[i][j][0][0]
                ss = plates[i][j][0][1]
                dd = (plates[i][j][0][2] % 2)
                pos = 0
                for k in range(1,len(plates[i][j])):        # 조건에 맞게 더하기
                    mm += plates[i][j][k][0]
                    ss += plates[i][j][k][1]
                    if pos == 0:
                        if dd != (plates[i][j][k][2]%2):
                            pos = 1
                mval = mm // 5
                sval = ss // len(plates[i][j])
                if mval != 0:                               # 질량이 0이 아니면
                    tot += mval * 4
                    if pos == 0:
                        for p in range(4):
                            q.append((i, j, mval, sval, 2 * p))
                    else:
                        for p in range(4):
                            q.append((i, j, mval, sval, 2 * p + 1))
                plates[i][j] = []
print(tot)