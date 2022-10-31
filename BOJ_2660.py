import sys
import heapq
inputs = sys.stdin.readline

# 다익스트라
def dij(x):
    global visit
    hq = []
    # 친구 => 1로 갱신
    for m in member[x]:
        visit[x][m] = 1
        heapq.heappush(hq, (1, m))

    while hq:
        val, mem = heapq.heappop(hq)
        if visit[x][mem] < val:     # 이미 방문이면 => 넘기기
            continue

        # 미방문 친구의 친구 찾기
        for cand in member[mem]:
            if visit[x][cand] == 9999999999:
                heapq.heappush(hq, (val + 1, cand))
                visit[x][cand] = val+1
    return max(visit[x][1:])


N = int(input())
member = [[] for _ in range(N+1)]
while True:
    a,b = map(int,inputs().split())
    if a == -1 and b == -1:
        break
    member[a].append(b)
    member[b].append(a)

visit = [[9999999999]*(N+1) for _ in range(N+1)]

answer = [[] for _ in range(N+1)]
# 모든 회원 친구 찾기
for i in range(1,N+1):
    visit[i][i] = 0
    score = dij(i)
    answer[score].append(i)

for i in range(1,N+1):
    if answer[i]:
        answer[i].sort()
        print(i,len(answer[i]))
        print(" ".join(map(str,answer[i])))
        break
