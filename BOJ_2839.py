import sys

inputs = sys.stdin.readline

N = int(inputs())
shr5 = N//5     # 5로 나눈 몫
rem5 = N%5      # 5로 나눈 나머지
ans = -1        # 디폴트 값
if rem5 != 0:   # 5로 안나눠지면
    # 0부터 shr5까지 N에서 빼고, 3으로 나눠봄
    for i in range(shr5+1):
        now = N - (5*(shr5-i))
        rem3 = now%3
        if rem3 == 0:       # 나눠떨어지면
            shr3 = now//3   
            ans = (shr5-i) + shr3   # 답은 두 개의 몫 합
            break
else:   # 5로 나눠떨어지면 => 답은 5의 몫
    ans = shr5
print(ans)