# 연산자 행렬(=operators), 현재까지 계산값, 계산한 횟수
def comb(operator, val, cnt):
    global maxi, mini
    # 계산 완료 => max, min 값 비교
    if cnt == N-1:
        if val > maxi:
            maxi = val
        if val < mini:
            mini = val
        return
    # operator가 4개니까 모든 operator 확인
    for k in range(4):
        # operator가 계산 가능하면 계산
        if operator[k] != 0:
            operator[k] -= 1
            if k == 0:
                comb(operator,val + nums[cnt+1],cnt+1)
            elif k == 1:
                comb(operator, val - nums[cnt+1], cnt + 1)
            elif k == 2:
                comb(operator, val * nums[cnt+1], cnt + 1)
            else:
                if val < 0 and val % nums[cnt+1] != 0:
                    val = val // nums[cnt+1] + 1
                else:
                    val = val // nums[cnt + 1]
                comb(operator, val, cnt + 1)
            # 다음 연산을 위해 operator 복구
            operator[k] += 1


T = int(input())
for t in range(1,T+1):
    N = int(input())
    operators = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    # max,min 값 정의
    maxi = -9999999999999
    mini = 999999999999

    comb(operators, nums[0], 0)
    print('#{0} {1}'.format(t,maxi-mini))