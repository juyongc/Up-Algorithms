import sys
inputs = sys.stdin.readline

N = int(input())
nums = list(map(int,inputs().split()))
x = int(input())

nums.sort()

ans = 0
s,e = 0,N-1

# 투포인터
# 합이 작으면 s ++ / 합이 크면 e --
while e > s:
    summ = nums[s] + nums[e]
    if summ == x:
        ans += 1
        s += 1
        e -= 1
    elif summ > x:
        e -= 1
    else:
        s += 1

print(ans)
