M = int(input())
N = int(input())
small = 0   # 가장 작은 소수
plus = 0    # 소수들의 합
for i in range(N,M-1,-1):
    if i == 1:      # 1은 소수가 아니다
        continue
    # 2 ~ i-1 로 나눠떨어지면 소수가 아니다
    for j in range(2,i):
        if i % j == 0:
            break
    else:           # 끝까지 살아남으면
        plus += i   # 소수 +
        small = i   # 가장 작은 소수 갱신
# 조건에 따른 출력
if small == 0:
    print(-1)
else:
    print(plus)
    print(small)