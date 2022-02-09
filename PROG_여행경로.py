import collections
answer = ["ICN"]
final = []
route = collections.defaultdict(list)
visit = collections.defaultdict(list)

#DFS 탐색
def dfs(route, now):
    global N,visit
    if final:
        return
    if len(answer) > N:
        final.append(answer[:])
        return
    
    route_visit = visit[now]
    for i in range(len(route_visit)):
        if route_visit[i] == 0:
            answer.append(route[now][i])
            route_visit[i] = 1
            next_loc = route[now][i]
            dfs(route,next_loc)
            route_visit[i] = 0
            answer.pop()

def solution(tickets):
    global N,visit
    N = len(tickets)
    
    for ticket in tickets:
        route[ticket[0]].append(ticket[1])
        
    for key,val in route.items():
        val.sort()
        visit[key] = [0]*len(val)
    dfs(route,"ICN")
    return final[0]