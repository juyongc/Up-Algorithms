import sys

inputs = sys.stdin
# 받은 모든 문자열에서 확인
for val in inputs:
    val = val.rstrip()
    s,t = val.split()
    ans = 1     # 정답 여부
    cur = 0     # 현재 인덱스 위치
    # 모든 s 문자열에 대해
    for i in range(len(s)):
        daum = 0    # 다음 인덱스로 넘어갈지 체크
        # 이전 인덱스 위치 +1 ~ 반복
        for j in range(cur,len(t)):
            if s[i] == t[j]:    # s문자가 t문자에 있으면
                cur = j+1       # j의 시작점 변경
                daum = 1        # 다음 인덱스로 넘어간다
                break
        if daum == 0:   # 못 넘어가면
            ans = 0     # 답없음
            break
    # 조건에 따른 출력
    if ans == 0:
        print("No")
    else:
        print("Yes")
