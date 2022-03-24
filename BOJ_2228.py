import sys
inputs = sys.stdin.readline

N,M = map(int,input().split())

num_plus = [[0]+[-999999999999]*M for _ in range(N+1)]  # 현재 값 더하기
num_no = [[0]+[-999999999999]*M for _ in range(N+1)]    # 현재 값 제외

# 모든 경우의 수,
# O - O : plus[i-1][j] + now
# X - 0 : no[i-1][j-1] + now
# O - X : plus[i-1][j]
# X - X : no[i-1][j]
for i in range(1,N+1):
    now = int(input())
    for j in range(1,M+1):
        num_plus[i][j] = max(num_plus[i-1][j],num_no[i-1][j-1]) + now
        num_no[i][j] = max(num_no[i-1][j],num_plus[i-1][j])

print(max(num_no[-1][-1],num_plus[-1][-1]))