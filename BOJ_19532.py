import sys

inputs = sys.stdin.readline
a,b,c,d,e,f = map(int,inputs().split())
answer = 0
for x in range(-999,1000):
    for y in range(-999,1000):
        q1 = a*x + b*y
        q2 = d*x + e*y
        if q1 == c and q2 == f:
            ans = (x,y)
            answer = 1
            break
    if answer == 1:
        break

print(ans[0],ans[1])
