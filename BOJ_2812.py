import sys
inputs = sys.stdin.readline

N,M = map(int,inputs().split())
arr = list(map(int,input()))
k = M
ans = []
# 모든 수 확인
for i in range(N):
    # 스택이 안비었고, k > 0 이면
    while ans and k > 0:
        if ans[-1] < arr[i]:    # 현재값이 이전값보다 크면
            ans.pop()           # => pop / k --
            k -= 1
        else:
            break
    ans.append(arr[i])
answer = ''.join(map(str,ans[:N-M]))    # N-M개만(뒤에가 작으면 붙음)

print(answer)