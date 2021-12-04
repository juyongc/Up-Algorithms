import sys
inputs = sys.stdin.readline

N = int(input())
nums = list(map(int,inputs().split()))

stack = []      # idx 추가용 스택
stack.append(0)
ans = [-1]*N
# 1~N-1번까지 최신 스택값과 현재값 비교
# 현재값이 더 크면, 스택 꺼내고 다음 값과 비교
# 현재값이 더 작으면, 스택에 추가
for i in range(1,N):
    while nums[stack[-1]] < nums[i]:
        idx = stack.pop()
        ans[idx] = nums[i]
        if not stack:
            break
    stack.append(i)

print(' '.join(map(str,ans)))