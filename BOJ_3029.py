import sys

inputs = sys.stdin.readline

cur = list(map(int,inputs().rstrip().split(':')))
throw = list(map(int,inputs().rstrip().split(':')))
ans = [0,0,0]
# 시간별 숫자 구하기
for i in range(3):
    if i == 0:
        ans[i] = abs((24 + throw[i] - cur[i]) % 24)
    else:   # 작은 수 - 큰 수의 경우, 앞 자리에서 숫자 빼기
        if throw[i] < cur[i]:
            ans[i-1] -= 1
            if ans[i-1] < 0:
                ans[i-1] += 60
                ans[i-2] -= 1
        ans[i] = abs((60 + throw[i] - cur[i]) % 60)

if ans == [0,0,0]:  # 1초 이상 기다려야함
    ans[0] = 24

# 형식에 맞게 string 변경
for i in range(3):
    if ans[i] < 10:     # 10보다 작으면 "0x" 로 나오게
        ans[i] = '0' + str(ans[i])
    else:
        ans[i] = str(ans[i])
# 출력
print(':'.join(ans))