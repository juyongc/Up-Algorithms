import sys


inputs = sys.stdin.readline

N = int(inputs())
table = [list(map(int,inputs().split())) for _ in range(N)]

# memoization용
memo = [0]*(N+1)
# 리스트의 끝부터 처음까지 반복
for i in range(N-1,-1,-1):
    prev = memo[i+1]        # 이전값
    # 상담 후 날짜가 퇴사날 이후면 -> maximum 값은 prev값
    if i + table[i][0] > N:
        memo[i] = prev
        continue
    # 상담 후 날짜가 퇴사날이면 -> now = 오늘 상담비
    elif i + table[i][0] == N:
        now = table[i][1]
    # 상담 후 날짜가 퇴사날까지 남았으면 -> now = 오늘 상담비 + 상담 후 날짜 memo 값
    else:
        now = table[i][1] + memo[i+table[i][0]]
    # 해당 날 최대 상담비용 구하기
    memo[i] = max(now,prev)

print(memo[0])
