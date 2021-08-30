# 풀이1: 효율성 실패
def solution(scov, K):
    scov.sort()
    cnt = 0
    while scov[0] < K:
        if len(scov) == 1:
            return -1
        else:
            f = scov.pop(0)
            s = scov.pop(0)
            new = f + 2*s
            scov.append(new)
            scov.sort()
            cnt += 1
    answer = cnt
    return answer


# 풀이2: heapq 사용 - 효율성 통과
import heapq
def solution(scov, K):
    heap = []
    for sco in scov:
        heapq.heappush(heap,sco)
    cnt = 0
    while heap[0] < K:
        if len(heap) == 1:
            return -1
        else:
            f = heapq.heappop(heap)
            s = heapq.heappop(heap)
            heapq.heappush(heap,f+2*s)
            cnt += 1
    answer = cnt
    return answer


