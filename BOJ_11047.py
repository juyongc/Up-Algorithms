import sys
inputs = sys.stdin.readline

N,K = map(int,inputs().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)

cnt = 0     # 총 동전개수
# 동전 나눈 몫 = 개수 ++
# 동전 나눈 나머지 = K값 갱신
for coin in coins:
    cnt += K // coin
    K = K % coin

    if K == 0:
        break

print(cnt)