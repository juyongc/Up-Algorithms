import sys

inputs = sys.stdin.readline
N = int(inputs())
music = [0]+list(map(int,inputs().split()))
Q = int(inputs())
mistake = [0]*(N+1) # 현재까지 한 실수 누적 합
# 마지막은 실수 안하니까 범위 : (1,N)
for i in range(1,N):
    mistake[i] = mistake[i - 1]     # 현재 값 = 이전 값
    if music[i+1] < music[i]:       # 실수하면 -> 현재 값 +1
        mistake[i] += 1
mistake[N] = mistake[N-1]           # 마지막  값 = 이전 값

for _ in range(Q):
    x,y = map(int,inputs().split())
    # 마지막은 실수 안하니까 -> y-1 까지
    # 처음 값 초기화하려면 -> x-1 값까지 누적 값 빼주기
    ans = mistake[y-1] - mistake[x-1]

    print(ans)