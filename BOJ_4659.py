import sys

inputs = sys.stdin
for input in inputs:
    line = input.rstrip()   # \n 없애기
    if line == "end":   # 끝나는 조건
        break
    else:               # 그 외
        vowel = {'a','e','i','o','u'}   # 모음 
        check = 0                       # 모음 체크용
        flag1,flag2 = 0,0               # 모음,자음 연속 체크용
        ans = 0                         # 불/통과 flag 용
        # 알파벳별 체크
        for i in range(len(line)):
            if line[i] in vowel:    # 모음이면
                check += 1          # 모음 존재 체크
                flag1 += 1          # 모음 연속 개수 +
                flag2 = 0           # 자음 연속 개수 초기화
            else:                   # 자음이면
                flag1 = 0
                flag2 += 1
            if flag1 >= 3 or flag2 >= 3:    # 모/자음 3개 이상 체크
                ans = 1
                break
            if i > 0:                       # 2번째 자리부터는
                prev = line[i-1]            # 이전값이랑 비교해서 연속 체크
                if line[i] == prev:         # 연속된 알파벳이면
                    if line[i] not in ['o','e']:    # 'o'나 'e'가 아니면
                        ans = 1
                        break
        if check == 0:              # 모음이 없으면
            ans = 1
        # 상태에 따른 출력
        if ans == 0:
            print("<{0}> is acceptable.".format(line))
        else:
            print("<{0}> is not acceptable.".format(line))