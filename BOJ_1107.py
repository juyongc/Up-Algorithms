import sys
inputs = sys.stdin.readline

N = int(input())
M = int(input())
if M != 0:
    button = set(map(str,input().split()))
else:
    button = set()

answer = abs(N - 100)               # +,- 버튼만 조작
num_cnt = len(list(str(N))) + 1     # 숫자의 자릿수 개수 + 1

for i in range(1000001):
    num = list(str(i))
    # 숫자 자릿수가 2자리 차이나면 break
    if len(num) > num_cnt:
        break
    flag = 0                    # 고장난 버튼 유무 확인
    for val in num:
        if val in button:
            flag = 1
            break
    # 고장난 버튼 없으면 => 최소값 갱신
    if not flag:
        answer = min(answer, abs(i - N) + len(num))

print(answer)
