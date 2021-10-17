import sys
from collections import deque
inputs = sys.stdin.readline

N,M,T = map(int,input().split())
plates = [list(map(int,input().split())) for _ in range(N)]
q = deque()

for _ in range(T):
    given = tuple(map(int,input().split()))
    q.append(given)

dx = [1,0]
dy = [0,1]
# T번 돌리기
while q:
    x,d,k = q.popleft()
    check = []
    for i in range(1,N+1):
        if i % x == 0:
            now = [0]*M
            for j in range(M):
                if d == 0:  # 시계방향
                    now[(j+k)%M] = plates[i-1][j]
                else:       # 반시계방향
                    now[(j-k)%M] = plates[i - 1][j]
            plates[i-1] = now
    flag = 0    # 하나라도 같은 숫자 있는지 확인 플레그
    # 주변에 같은 숫자 있는지 확인
    for i in range(N):
        for j in range(M):
            if plates[i][j] != 0:
                cnt = 0
                for k in range(2):
                    a,b = i+dx[k],(j+dy[k])%M
                    if 0<=a<N:
                        # 같은 수가 있으면
                        if plates[a][b] == plates[i][j]:
                            check.append((a,b))
                            cnt = 1
                            flag = 1
                if cnt == 1:
                    check.append((i,j))

    if flag == 0:       # 같은 수 없으면 => 평균 구해서 +1 / -1 
        tot = 0
        nzero = 0
        for i in range(N):
            for j in range(M):
                if plates[i][j] != 0:
                    tot += plates[i][j]
                    nzero += 1
        if nzero != 0:      # 다 "0"이다!
            avgs = tot / nzero
            for i in range(N):
                for j in range(M):
                    if plates[i][j] != 0:
                        if plates[i][j] > avgs:
                            plates[i][j] -= 1
                        elif plates[i][j] < avgs:
                            plates[i][j] += 1
    else:               # 같은 수가 있으면 => 모두 0 만들기
        while check:
            x,y = check.pop()
            plates[x][y] = 0

ans = 0     # 정답 구하기
for i in range(N):
    ans += sum(plates[i])
print(ans)