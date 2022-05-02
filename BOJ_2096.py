import sys
inputs = sys.stdin.readline


N = int(input())

dp_min = [0]*3
dp_max = [0]*3

temp_min = [0]*3
temp_max = [0]*3

for i in range(N):
    a,b,c = map(int,inputs().split())
    temp_max[0] = max(dp_max[0],dp_max[1]) + a
    temp_min[0] = min(dp_min[0],dp_min[1]) + a

    temp_max[1] = max(dp_max[0], dp_max[1], dp_max[2]) + b
    temp_min[1] = min(dp_min[0], dp_min[1], dp_min[2]) + b

    temp_max[2] = max(dp_max[1], dp_max[2]) + c
    temp_min[2] = min(dp_min[1], dp_min[2]) + c

    for j in range(3):
        dp_min[j] = temp_min[j]
        dp_max[j] = temp_max[j]

print(max(dp_max),min(dp_min))
