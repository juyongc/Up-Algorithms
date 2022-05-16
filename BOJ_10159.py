import sys
import heapq
inputs = sys.stdin.readline

# 힙 사용 => 미방문이면 방문하고 cnt ++
def dijkstra(start, evaluate,N):

    visit = [0]*(N+1)
    hq = []
    heapq.heappush(hq,start)
    cnt = 0
    visit[start] = 1
    while hq:
        now = heapq.heappop(hq)

        for val in evaluate[now]:
            if visit[val] == 0:
                cnt += 1
                visit[val] = 1
                heapq.heappush(hq,val)

    return cnt


N = int(input())
M = int(input())

smaller = [[] for _ in range(N+1)]      # 인덱스보다 작은 값
bigger = [[] for _ in range(N+1)]       # 인덱스보다 큰 값

# 자신보다 큰 값만 넣는 리스트 / 작은 값만 넣는 리스트 따로 생성
for _ in range(M):
    b,s = map(int,input().split())
    smaller[b].append(s)
    bigger[s].append(b)

check = [0]*(N+1)
# 방문 불가 수 = 총 개수 - (자신보다 작은 값 개수 + 큰 값 개수 + 1)
for i in range(1,N+1):
    cnt_s = dijkstra(i,smaller,N)
    cnt_b = dijkstra(i,bigger,N)

    check[i] = N - (cnt_b + cnt_s + 1)

for i in range(1,N+1):
    print(check[i])
