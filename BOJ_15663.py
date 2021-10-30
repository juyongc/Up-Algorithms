import sys
inputs = sys.stdin.readline


def dfs(n, m, cur, arr):
    global check,visit
    if cur >= m:        # m 이상이면 중복 여부 확인
        now = ' '.join(map(str,arr))
        if now not in check:
            check[now] = 1
        return
    # 모든 경우의 수 중복 확인하며 체크 
    for i in range(n):
        if visit[i] == 0:
            arr[cur] = nums[i]
            visit[i] = 1
            dfs(N, M, cur + 1, arr)
            visit[i] = 0


N,M = map(int,inputs().split())
nums = list(map(int,inputs().split()))
nums.sort()

check = {}
visit = [0]*N
pos = [0]*M
dfs(N,M,0,pos)

for key in check.keys():
    print(key)