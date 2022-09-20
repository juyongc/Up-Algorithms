import sys
inputs = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    cost = list(map(int,input().split()))
    cost.reverse()

    max_list = [0]*len(cost)
    max_list[0] = cost[0]
    for i in range(1,len(cost)):
        max_list[i] = max(max_list[i-1],cost[i])

    answer = 0
    for i in range(len(cost)):
        answer += (max_list[i] - cost[i])

    print(answer)
