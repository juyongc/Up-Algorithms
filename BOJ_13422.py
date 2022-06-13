import sys
inputs = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,M,K = map(int,inputs().split())
    money = list(map(int,inputs().split()))
    for i in range(M-1):
        money.append(money[i])

    answer = 0
    if N == M:      # 예외 케이스 - 전체를 다 훔치면 한 번만 가능
        steal_tot = sum(money[:M])
        if steal_tot < K:
            answer += 1
    else:           # 그 외 - M개씩 합한 후, 방범값과 비교
        steal_tot = [0]*N
        steal_tot[0] = sum(money[:M])
        for i in range(1,N):
            steal_tot[i] = steal_tot[i-1] - money[i-1] + money[i-1+M]

        for steal in steal_tot:
            if steal < K:
                answer += 1

    print(answer)
