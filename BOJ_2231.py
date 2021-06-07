N = input()         # str로 받기
arr = list(N)       # 리스트로 변환 <= 숫자 길이 알아내려고

len_N = len(arr)    # 숫자자리 length
num = int(N)        # int형 input값

start = num - (len_N * 9)   # input값 - 자리수 * 9 가 가능범위 끝자락
if start <= 0:              # 시작값이 0보다 작으면, 1로 시작하게 만들기
    start = 1

ans = 0                     # 답 default
for i in range(start,num+1):
    check = list(str(i))        # 현 숫자자리 length 알아내려고 + 각 자리 더해서 input값이랑 같은지 체크
    now = i                     # now = i + 각 자리수
    for k in range(len(check)):
        now += int(check[k])

    if now == num:          # 정답이면 반복문 빠져나오기
        ans = i
        break

print(ans)