mtds = []   # 조합 저장용 리스트
# 모든 조합 고르기
def dfs(n,cur,arr,vis):
    global mtds
    if cur >= n:
        mtds.append(arr[:])
        return
    for i in range(n):
        if vis[i] == 0:
            arr[cur] = i
            vis[i] = 1
            dfs(n,cur+1,arr,vis)
            vis[i] = 0
        
def solution(k, dgs):
    global mtds
    ans = -1
    num = len(dgs)
    s = [0]*num
    visit = [0]*num
    dfs(num,0,s,visit)
    # 모든 조합 실행하면서 max 값 구하기
    for mtd in mtds:
        now = k
        cnt = 0
        for mt in mtd:
            if dgs[mt][0] <= now:
                now -= dgs[mt][1]
                cnt += 1
            else:
                break
        ans = max(ans,cnt)
    return ans