from collections import deque
def solution(n):
    ans = 0
    share = n
    while share > 0:
        share,rem = divmod(share,2)
        if rem == 1:
            ans += 1
    return ans