T = int(input())
for _ in range(T):
    chrome = input()
    allow = 'ABCDEF'    # 첫번째, 마지막 염색체가 가능한 문자열

    if chrome[0] not in allow:  # 첫번재 염색체 체크
        print('Good')
        continue
    if chrome[-1] not in allow: # 마지막 염색체 체크
        print('Good')
        continue

    cnt = 1     # 인덱스 카운팅
    flag = 0    # 문제 유무 확인용
    now = 'A'   # 현재 문자열

    while cnt < len(chrome)-1:
        if chrome[cnt] == now:      # 이전 문자열과 같다면 -> cnt ++
            cnt += 1
        else:
            if now == 'A' and chrome[cnt] == 'F':   # A->F 상황이라면
                now = 'F'
                cnt += 1
            elif now == 'F' and chrome[cnt] == 'C': # F->C 상황이라면
                now = 'C'
                cnt += 1
            else:           # 그 외 -> 문제 발생
                flag = 1    # flag 값 변경 -> break
                break
    # flag 값에 따른 출력
    if flag == 0:
        print('Infected!')
    else:
        print('Good')
