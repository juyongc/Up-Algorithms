import sys
import heapq
inputs = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,K = map(int,inputs().split())
    times = [0] + list(map(int,inputs().split()))

    towers = [0]*(N+1)
    rules = {}

    for _ in range(K):
        X,Y = map(int,inputs().split())
        towers[Y] += 1
        if X not in rules:
            rules[X] = [Y]
        else:
            rules[X].append(Y)

    W = int(input())

    hq = []     # 우선순위 큐 사용
    for i in range(1,N+1):
        if towers[i] == 0:
            heapq.heappush(hq,[times[i],i])

    ans = 0     # 총 걸린 시간
    # 동시 건설 가능해서 같은 시간이 공유됨
    # 해당 건물이 완성되면 큐 안에 있는 건물 시간도 줄여야 함
    while hq:
        build_t,idx = heapq.heappop(hq)
        ans += build_t
        if idx == W:    # 마지막 건물 완성 => 나가기
            break
        else:           # 큐 안에 있는 시간들도 해당 값만큼 줄이기
            for i in range(len(hq)):
                hq[i][0] -= build_t
        if idx not in rules:
            continue
        for rule in rules[idx]:
            towers[rule] -= 1
            if towers[rule] == 0:
                heapq.heappush(hq,[times[rule],rule])

    print(ans)