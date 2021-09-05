import heapq
def solution(n, s, a1, a2, fares):
    answer = 0
    node = [[] for _ in range(n+1)]
    for fare in fares:
        a,b,c = fare[0],fare[1],fare[2]
        node[a].append((b,c))
        node[b].append((a,c))
    costs = [999999999999]*(n+1)
    hq = []
    heapq.heappush(hq,s)
    costs[s] = 0 
    while hq:
        now = heapq.heappop(hq)
        for vals in node[now]:
            nod,val = vals[0],vals[1]
            if costs[nod] > costs[now]+val:
                costs[nod] = costs[now]+val
                heapq.heappush(hq,nod)
                
    maxi = costs[a1] + costs[a2]

    for i in range(1,n+1):
        if i == s:
            continue
        else:
            if costs[i] > maxi:
                continue
            else:
                curs = [999999999999]*(n+1)
                hq = []
                heapq.heappush(hq,i)
                curs[i] = 0
                while hq:
                    now = heapq.heappop(hq)
                    for vals in node[now]:
                        nod,val = vals[0],vals[1]
                        if curs[nod] > curs[now]+val:
                            curs[nod] = curs[now]+val
                            heapq.heappush(hq,nod)
                summ = curs[a1]+curs[a2]+costs[i]

                if summ < maxi:
                    maxi = summ
                
    return maxi