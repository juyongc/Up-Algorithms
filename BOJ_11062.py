import sys
inputs = sys.stdin.readline


def pick(turn, i, j):
    if i > j:
        return 0
    if dp[i][j]:
        return dp[i][j]
    # 근우 차례
    # 자신의 점수를 최대로 할 수 있는 값 선택
    if turn:
        score = max(pick(False, i + 1, j) + card[i], pick(False, i, j - 1) + card[j])
        dp[i][j] = score
        return score
    # 명우 차례
    # 근우의 점수를 최소로 할 수 있는 값 선택
    else:
        score = min(pick(True, i + 1, j), pick(True, i, j - 1))
        dp[i][j] = score
        return score


T = int(input())
for _ in range(T):
    N = int(input())
    card = list(map(int,inputs().split()))
    dp = [[0]*N for _ in range(N)]

    pick(True,0,N-1)
    print(dp[0][N-1])
