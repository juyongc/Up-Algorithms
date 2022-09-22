import sys
from copy import deepcopy
inputs = sys.stdin.readline

N = int(input())
current = list(map(int,inputs().rstrip()))
current2 = deepcopy(current)
want = list(map(int,inputs().rstrip()))

# current2는 0번째 전구 상태 변경한 상황
for i in range(2):
    if current2[i]:
        current2[i] = 0
    else:
        current2[i] = 1

count,count2 = 0,1      # on, off 카운팅
# current, current2 별로 이전 값 기준으로 on,off 판단
for i in range(1,N-1):
    if current[i-1] != want[i-1]:
        count += 1
        for j in range(-1,2):
            if current[i+j]:
                current[i+j] = 0
            else:
                current[i+j] = 1

    if current2[i-1] != want[i-1]:
        count2 += 1
        for j in range(-1,2):
            if current2[i+j]:
                current2[i+j] = 0
            else:
                current2[i+j] = 1

if current[N-1] != want[N-1]:
    count += 1
    for j in range(-1,1):
        if current[N-1+j]:
            current[N - 1 + j] = 0
        else:
            current[N - 1 + j] = 1

if current2[N-1] != want[N-1]:
    count2 += 1
    for j in range(-1,1):
        if current2[N-1+j]:
            current2[N - 1 + j] = 0
        else:
            current2[N - 1 + j] = 1

flag, flag2 = 0,0
# 주어진 상태 만들 수 있는지 확인
# 1 : 불가 / 0 : 가능
for i in range(N):
    if flag == 1 and flag2 == 1:
        break

    if current[i] != want[i]:
        flag = 1
    if current2[i] != want[i]:
        flag2 = 1

answer = 9999999999
# 주어진 상태 만들 수 있는지 확인 및 갱신
if not flag:
    answer = min(answer,count)
if not flag2:
    answer = min(answer, count2)
if answer == 9999999999:
    answer = -1
print(answer)
