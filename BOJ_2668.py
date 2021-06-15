import sys

inputs = sys.stdin.readline

N = int(inputs())

nums = [0] * (N+1)          # 해당 인덱스와 짝인 수 리스트
for i in range(1,N+1):
    nums[i] = int(inputs())

tot = [0]*(N+1)         # 그룹 체크
cnt = 0                 # 그룹을 이루는 수 개수
# 그룹에 들어가지않은 수에 한해서 반복
for i in range(1,N+1):
    if tot[i] == 0:
        stack = [i]
        check = [0]*(N+1)
        while stack:            # 스택에 값이 존재하면
            now = stack.pop()
            if check[nums[now]] == 0:
                check[nums[now]] = 1
                stack.append(nums[now])
        if now == i:            # 마지막 값이 첫번째 수와 같다면 => 그룹임
            for k in range(1,N+1):
                if check[k] == 1:   # 1이면 그룹에 속하는 수임
                    tot[k] = 1      # 그룹에 추가
                    cnt += 1        # 그룹에 숫자 개수 ++
# 출력하기
print(cnt)
for i in range(1,N+1):
    if tot[i] == 1:
        print(i)
