# DFS
def dfs(info,trees,sheep,wolf):
    global visit,max_sheep
    max_sheep = max(max_sheep,sheep)
    if wolf >= sheep:
        return
    # 모든 노드 확인 => 방문한 노드만 추가 진행
    for i in range(len(visit)):
        if visit[i]:
            # 해당 자식 노드 중 미방문만 방문
            for tree in trees[i]:
                if not visit[tree]:
                    visit[tree] = 1
                    if info[tree]:
                        dfs(info,trees,sheep,wolf+1)
                    else:
                        dfs(info,trees,sheep+1,wolf)
                    visit[tree] = 0
    
    
def solution(info, edges):
    global visit,max_sheep
    trees = [[] for _ in range(len(info))]
    for edge in edges:
        trees[edge[0]].append(edge[1])
        trees[edge[1]].append(edge[0])
    visit = [0]*len(info)
    visit[0] = 1
    max_sheep = 0
    dfs(info,trees,1,0)
    return max_sheep