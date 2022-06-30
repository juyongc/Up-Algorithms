import sys
inputs = sys.stdin.readline

N = int(input())
K = int(input())
sensor = list(set(map(int,inputs().split())))
sensor.sort()

# 가까운 센서끼리의 위치
diff = [(sensor[i+1] - sensor[i]) for i in range(len(sensor)-1)]
diff.sort()
ans = 0
# 기지국이 여러 개면 먼 거리의 센서 (K-1) 개는 끊을 수 있음
# 더 가까운 기지국으로 연결되기 때문
if len(diff) + 1 <= K:
    ans = 0
else:
    for i in range(len(diff)-K+1):
        ans += diff[i]

print(ans)