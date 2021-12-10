import sys
inputs = sys.stdin.readline

N = int(input())
A = list(map(int,inputs().split()))

memo = [0]
# 모든 수 확인
for a in A:
    # 마지막 수보다 크면 => append
    if memo[-1] < a:
        memo.append(a)
    else:   # 작거나 같으면 => 이진탐색
        s,e = 0,len(memo)
        while s < e:
            mid = (s+e) // 2
            if memo[mid] >= a:
                e = mid
            else:
                s = mid + 1
        memo[e] = a

print(len(memo)-1)