import sys
inputs = sys.stdin.readline

N,K = map(int,inputs().split())
lion = list(map(int,inputs().split()))
s = 0
mini = 999999999999999
cnt = 0

# 투포인터
for i in range(N):
    if lion[i] == 1:
        cnt += 1

    if cnt >= K:
        mini = min(mini,i-s+1)
        # K개 이상이면 => 1 하나 뺄 때까지 s ++
        while cnt >= K:
            if lion[s] == 1:
                cnt -= 1
            s += 1
        # 다음 1이 나오기전까지 s ++
        while lion[s] == 2:
            s += 1
            if i == s:
                break

if mini == 999999999999999:
    mini = -1

print(mini)
