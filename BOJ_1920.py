import sys
inputs = sys.stdin.readline

N = int(input())
nums = list(map(int,inputs().split()))
M = int(input())
checks = list(map(int,inputs().split()))

nums.sort()

# 숫자 순서대로 체크
for check in checks:
    # 끝이나 마지막 넘버와 같다면
    if check == nums[0] or check == nums[N-1]:
        print(1)
    else:   # 이진탐색
        s,e = 0,N-1
        flag = 0
        while s <= e:
            mid = (s+e) // 2
            if nums[mid] == check:
                flag = 1
                break
            elif nums[mid] > check:
                e = mid - 1
            else:
                s = mid + 1
        if flag == 0:
            print(0)
        else:
            print(1)