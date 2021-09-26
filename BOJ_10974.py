import sys
inputs = sys.stdin.readline

# DFS 탐색
def dfs(cnt):

    if cnt == N:    # N이면 출력
        print(' '.join(map(str,nums)))
        return
    else:           
        for i in range(1,N+1):
            if visit[i] == 0:   # 방문안했으면
                nums[cnt] = i   # 현재 인덱스 = 현 숫자 
                visit[i] = 1    # 방문체크
                dfs(cnt+1)      # 다음 인덱스 넘어감
                visit[i] = 0    # 돌아오면, 방문체크 해제


N = int(inputs())

visit = [0]*(N+1)
nums = [0]*N
dfs(0)
