import sys
inputs = sys.stdin.readline

N = int(input())
B = list(map(int,inputs().split()))
share,rem = divmod(100,2)
cnt = 0
maxi = 0
for val in B:
    if val == 0:
        continue
    elif val == 1:
        cnt += 1
        continue

    one,two = 0,0
    while val > 1:
        share,rem = divmod(val,2)
        two += 1
        if rem > 0:
            one += 1
        val = share
        if share == 1:
            one += 1
            break

    cnt += one
    maxi = max(two,maxi)

cnt += maxi
print(cnt)
