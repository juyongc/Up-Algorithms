import sys

inputs = sys.stdin.readline
written = inputs().rstrip()
wish = inputs().rstrip()
written_num = len(written)
wish_num = len(wish)
number = {'1','2','3','4','5','6','7','8','9','0'}
now = 0     # wish 자릿수
ans = 0     # 정답 flag용
for i in range(written_num):
    # 백트래킹
    if wish_num > now + (written_num - i):
        break
    else:
        if written[i] in number:        # 숫자면 continue
            continue
        else:                           # 아니면
            # 현재번째 wish와 written 문자가 같은지 비교
            if written[i] == wish[now]: # 같으면 
                now += 1                # +1
                if now == wish_num:     # wish의 모든 문자확인이면 break
                    ans = 1
                    break
            else:                       # 다르면
                check = 0               # defult 값
                # now번째자리까지 비교
                for j in range(now):
                    # 횬쟈 written 자리수가 이전 wish 문자열 중에 있다면
                    if written[i] == wish[j]:
                        if written[i-j:i+1] == wish[:j+1]:  # 이전값들 비교
                            check = j+1                     # 다 같으면 
                now = check                                 # 현재 자리수 갱신

print(ans)