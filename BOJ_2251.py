import sys
from collections import deque
inputs = sys.stdin.readline

bottle = list(map(int,inputs().split()))

answer = []
visit = [[0]*201 for _ in range(201)]   # visit[A물통][C물통]
q = deque()
q.append([0,0,bottle[2]])

while q:
    water = q.popleft()
    # i => j로 물 옮김
    for i in range(3):
        if water[i] == 0:
            continue

        for j in range(3):
            if i == j:
                continue

            water_move = water[:]
            rem = (bottle[j] - water[j])
            # 두 물통 중에 어디가 빨리 차나/비나에 따라 달라짐
            if water_move[i] >= rem:
                water_move[j] += rem
                water_move[i] -= rem
            else:
                water_move[j] += water[i]
                water_move[i] = 0
            # 방문체크 / 큐에 추가
            if visit[water_move[0]][water_move[2]] == 0:
                q.append(water_move)
                visit[water_move[0]][water_move[2]] = 1
                if water_move[0] == 0:
                    answer.append(water_move[2])

answer = list(set(answer))
answer.sort()
print(' '.join(map(str,answer)))
