import sys
inputs = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
plus,minus,zero,one = [],[],0,0
for num in nums:
    if num > 1:
        plus.append(num)
    elif num == 0:
        zero += 1
    elif num == 1:
        one += 1
    else:
        minus.append(num)

plus.sort(reverse=True)
minus.sort()
ans = 0
i = 0
# 양수는 다 곱한다
# 홀수면 마지막 값만 더한다
while i < len(plus):
    if i == len(plus)-1:
        ans += plus[i]
        break
    else:
        ans += (plus[i]*plus[i+1])
        i += 1
    i += 1

ans += one  # 일은 다 더한다

i = 0 
# 음수는 다 곱한다
# 홀수면 마지막값은 0이 있으면 0,
# 없으면 더한다
while i < len(minus):
    if i == len(minus) - 1:
        if zero == 0:
            ans += minus[i]
        break
    else:
        ans += (minus[i] * minus[i + 1])
        i += 1
    i += 1

print(ans)