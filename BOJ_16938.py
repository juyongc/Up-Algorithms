import sys
from itertools import combinations
inputs = sys.stdin.readline

N,L,R,X = map(int,inputs().split())
problem = list(map(int,inputs().split()))
problem.sort()

answer = 0
for i in range(2,N+1):
    pick_list = list(combinations(problem,i))
    for pick in pick_list:
        balance = pick[-1] - pick[0]
        if balance < X:
            continue
        total = sum(pick)
        if total < L:
            continue
        if total > R:
            continue
        answer += 1

print(answer)
