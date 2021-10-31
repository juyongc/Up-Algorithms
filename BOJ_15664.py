import sys
inputs = sys.stdin.readline

# 모든 조합 구하기
def dfs(n,m,cur,prev,arr):
    global check,nums
    if cur >= m:
        now = ' '.join(map(str,arr))
        if now not in check:
            check[now] = 1
        return
    # 이전 값보다 큰 인덱스만 확인
    for i in range(prev+1,n):
        arr[cur] = nums[i]
        prev = i
        dfs(n,m,cur+1,prev,arr)


N,M = map(int,inputs().split())
nums = list(map(int,inputs().split()))

nums.sort()     # 비내림차순 => 정렬

check = {}
s = [0]*M
dfs(N,M,0,-1,s)

for key in check.keys():
    print(key)