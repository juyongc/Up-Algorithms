def solution(N, number):
    global answer,dp
    answer = -1
    
    # 주어진 N이 정답인 경우, 1 반환
    if N == number:
        answer = 1
        return answer
    
    # 숫자 8개까지 사용해서 값 구하기 - dp
    dp = [[] for _ in range(9)]
    dp[1].append(N)
    dp[1].append(-N)
    
    for i in range(2,9):
        # 5, 55, 555처럼 증가 가능 확인
        ten = int(str(N)*i)
        dp[i].append(ten)
        if ten == number:
            answer = i
            break
        # 1 ~ 현재 인덱스의 절반까지 확인  ex.현재 인덱스가 5면, 1-4,2-3 만 확인하면 됨
        for j in range(1,i//2+1):
            check(i-j,j,i,number)   # 사칙연산 계산
        dp[i] = list(set(dp[i]))    # 중복 제거
        if answer != -1:            # 최솟값 발견 여부 확인
            break
    return answer

def check(k,z,now,number):
    global answer,dp
    
    for knum in dp[k]:
        for znum in dp[z]:
            plus = knum + znum      # 덧셈
            if plus == number:
                answer = now
                return
            dp[now].append(plus)
            minus = knum - znum     # 뺄셈
            dp[now].append(minus)
            if minus == number:
                answer = now
                return
            multiple = knum * znum  # 곱셈
            dp[now].append(multiple)
            if multiple == number:
                answer = now
                return
            if znum != 0:           # 나눗셈 - 분모 0 안됨
                divide = knum // znum
                dp[now].append(divide)
                if divide == number:
                    answer = now
                    return