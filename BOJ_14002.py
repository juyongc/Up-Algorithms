import sys
inputs = sys.stdin.readline


N = int(input())
num = list(map(int,inputs().split()))

dp = [1]*N

# 증가하는 개수 카운팅
for i in range(N):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i],dp[j]+1)

maxi = max(dp)
answer = []
now = maxi
# 내려가면서 현재 랭크랑 같은 값 확인
for i in range(N-1,-1,-1):
    if dp[i] == now:
        answer.append(num[i])
        now -= 1

answer.reverse()    # 뒤집어주기

print(maxi)
print(" ".join(map(str,answer)))