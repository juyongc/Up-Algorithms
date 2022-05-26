def dfs(cnt,now,dungeons):
    global answer,visit
    
    if cnt > answer:
        answer = cnt
    
    for i in range(len(dungeons)):
        start,use = dungeons[i]
        # 필수 필요도보다 작거나, 방문했으면 => continue
        if start > now or visit[i] == 1:
            continue
        visit[i] = 1
        dfs(cnt+1,now-use,dungeons)
        visit[i] = 0
        
        
def solution(k, dungeons):
    global answer,visit
    answer = -1
    
    visit = [0]*len(dungeons)
    dfs(0,k,dungeons)
    
    return answer