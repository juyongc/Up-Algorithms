import sys
inputs = sys.stdin.readline

# 멤버 정하기
def dfs(cnt,n):
    global nums,others,visit
    if cnt == N//2:             # 수가 맞으면
        blue = []
        red = []
        for k in range(N):      # 방문여부에 따라 팀 정하기
            if visit[k] == 1:
                blue.append(k)
            else:
                red.append(k)
        nums.append(blue)
        others.append(red)
    else:
        for j in range(n+1,N):
            visit[j] = 1
            dfs(cnt+1,j)
            visit[j] = 0


N = int(inputs())
ability = [list(map(int,inputs().split())) for _ in range(N)]

nums = []
others = []
visit = [0]*N
for i in range(N//2):
    visit[i] = 1
    dfs(1,i)
    visit[i] = 0

mini = 9999999999
# 모든 팀 확인하기
for k in range(len(nums)):
    num = nums[k]
    other = others[k]
    summ = 0
    opp = 0
    # 자신이 아니면 값 더하기
    for i in range(N//2):
        for j in range(N//2):
            if i != j:
                summ += ability[num[i]][num[j]]
                opp += ability[other[i]][other[j]]
    final = abs(summ - opp)

    if final == 0:
        mini = 0
        break
    if final < mini:
        mini = final
print(mini)