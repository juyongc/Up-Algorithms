import sys
from collections import deque
inputs = sys.stdin.readline

N,M,R = map(int,input().split())
arrs = [list(map(int,input().split())) for _ in range(N)]

rot = min(N,M)//2
for i in range(rot):
    q = deque()
    # 현재 해당하는 배열값들 큐에 추가
    for j in range(i,M-1-i):
        q.append(arrs[i][j])
    for j in range(i,N-1-i):
        q.append(arrs[j][M-1-i])
    for j in range(M-1-i,i,-1):
        q.append(arrs[N-1-i][j])
    for j in range(N-1-i,i,-1):
        q.append(arrs[j][i])

    # 큐 돌리기
    tot = R % ((N-i*2)*2 + (M-i*2)*2 - 4)   # 필요한만큼만 돌릴 수 있게 나머지 구하기
    for _ in range(tot):
        num = q.popleft()
        q.append(num)

    # 순서대로 배열에 재배치하기
    cnt = 0
    for j in range(i,M-1-i):
        arrs[i][j] = q[cnt]
        cnt += 1
    for j in range(i,N-1-i):
        arrs[j][M-1-i] = q[cnt]
        cnt += 1
    for j in range(M-1-i,i,-1):
        arrs[N-1-i][j] = q[cnt]
        cnt += 1
    for j in range(N-1-i,i,-1):
        arrs[j][i] = q[cnt]
        cnt += 1

for i in range(N):
    print(' '.join(map(str,arrs[i])))
