import sys
sys.setrecursionlimit(100000000)
inputs = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int,inputs().split())
    tree[a].append(b)
    tree[b].append(a)

answer = N+1
visit = [0]*(N+1)
# dp[x][0] : x가 얼리일 때 / dp[x][1] : 아닐때 최소값
dp = [[1,0] for _ in range(N+1)]

def dfs(now):
    visit[now] = 1
    for friend in tree[now]:
        if visit[friend] == 0:
            dfs(friend)     # 친구 얼리/노얼리 최소값 구하기
            # 자신이 얼리면 => 친구가 얼리든 아니든 최소값이면 됨
            dp[now][0] += min(dp[friend][0],dp[friend][1])
            # 자신이 아니면 => 친구는 얼리여야 함
            dp[now][1] += dp[friend][0]

dfs(1)

print(min(dp[1]))