import sys
inputs = sys.stdin.readline

# DFS => 사칙연산 전부 다 해보기
def dfs(tot,n_idx):
    global mini,maxi
    if n_idx >= len(nums):  # 전체 수 다했으면 => max,min값 찾기
        mini = min(tot,mini)
        maxi = max(tot,maxi)

    for k in range(4):
        if opers[k] != 0:
            opers[k] -= 1
            if k == 0:
                dfs(tot + nums[n_idx],n_idx+1)
            elif k == 1:
                dfs(tot - nums[n_idx], n_idx + 1)
            elif k == 2:
                dfs(tot * nums[n_idx], n_idx + 1)
            else:               # 나눗셈 조건 
                if tot < 0:     # 음수면 양수 상태에서 몫 찾고 다시 음수로
                    val = -((-tot) // nums[n_idx])
                else:
                    val = tot // nums[n_idx]
                dfs(val, n_idx + 1)
            opers[k] += 1
            
            
N = int(input())
nums = list(map(int,inputs().split()))
opers = list(map(int,inputs().split()))
mini,maxi = 999999999999999, -999999999999999

dfs(nums[0],1)

print(maxi)
print(mini)