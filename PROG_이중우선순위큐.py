import heapq
def solution(operations):
    answer = [0,0]
    hq = []
    for operation in operations:
        order, num = operation.split()
        num = int(num)
        if order == "I":
            heapq.heappush(hq,num)
        # 최소값은 heapq.heappop
        # 최대값은 sort -> pop 으로
        else:
            if not hq:
                continue
            if num == 1:
                hq.sort()
                hq.pop()
            else:
                heapq.heappop(hq)
                
    if hq:
        hq.sort()
        maxi = hq[-1]
        mini = heapq.heappop(hq)
        answer = [maxi,mini]
    return answer