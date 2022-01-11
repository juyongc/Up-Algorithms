import sys
inputs = sys.stdin.readline

N = int(input())
nums = list(map(int,inputs().split()))

num_dic = {}

ans = 0
left,right = 0,0

while True:
    if right >= N:
        if left >= N:
            break
        else:
            ans += (right - left)
            left += 1

    elif nums[right] not in num_dic:        # 딕셔너리에 없으면
        num_dic[nums[right]] = right        # => right ++
        right += 1
    else:                                   # 딕셔너리에 있으면
        ans += (right - left)               # left ++
        del(num_dic[nums[left]])
        left += 1

print(ans)

