import sys
from collections import deque
inputs = sys.stdin.readline


def find_max(build_list):
    global building
    maxi = 0
    flag = 0
    # 아직 building의 값이 0인게 있으면 넘기기
    for build in build_list:
        if building[build] == 0:
            flag = 1
            break
        else:
            maxi = max(maxi, building[build])

    if flag == 1:
        return 0

    return maxi


N = int(input())
building = [0]*(N+1)

q = deque()
# info = [인덱스, 시간, 건물 번호들]
for i in range(N):
    info = [i+1] + list(map(int,inputs().split()))
    info.pop()
    q.append(info)

# 개수가 2개면 => 선건물 없음
# 개수 2개 초과면 => 선건물 중 가장 시간 많이 필요한 것 찾기
while q:
    order = q.popleft()
    if len(order) == 2:
        idx,sec = order
        building[idx] = sec
        continue
    sec = find_max(order[2:])
    if sec == 0:
        q.append(order)
    else:
        building[order[0]] = sec + order[1]

for i in range(1,N+1):
    print(building[i])
