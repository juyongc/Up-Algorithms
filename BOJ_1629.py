import sys
inputs = sys.stdin.readline

# 수학식
def calculate(a, b):
    if b == 1:
        return a % C

    now = calculate(a, b // 2)

    if b % 2 == 0:  # (나머지 * 나머지) % C
        return now * now % C
    else:           # (나머지 * 나머지 * 현재값) % C
        return now * now * a % C


A,B,C = map(int,inputs().split())
ans = calculate(A,B)
print(ans)