import sys
inputs = sys.stdin.readline

N,K = map(int,inputs().split())
nums = list(map(int,inputs().split()))
ans = 0
# 두 수의 차이값
diff = [nums[i+1]-nums[i] for i in range(N-1)]
diff.sort()
# K-1개는 뺄 수 있음
for i in range(N-K):
    ans += diff[i]
print(ans)