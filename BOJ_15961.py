import sys
inputs = sys.stdin.readline

N,D,K,C = map(int,inputs().split())
sushi = [int(inputs()) for _ in range(N)]
plate = {}
answer = 0
cnt = 0
# 초기값 세팅
for i in range(K):
    if sushi[i] in plate:
        plate[sushi[i]] += 1
    else:
        plate[sushi[i]] = 1
        cnt += 1
if C not in plate:
    cnt += 1
answer = max(answer,cnt)
s,e = 0,K-1
# 투포인터
for i in range(N):
    if answer >= K+1:
        break

    e += 1
    e = e % N
    if sushi[e] in plate:
        plate[sushi[e]] += 1
    else:
        plate[sushi[e]] = 1
        if sushi[e] != C:
            cnt += 1

    plate[sushi[s]] -= 1
    if plate[sushi[s]] == 0:
        del(plate[sushi[s]])
        if sushi[s] != C:
            cnt -= 1
    s += 1
    answer = max(answer, cnt)

print(answer)