def solution(n, k):
    answer = []
    nums = [0]*(n+1)    # 사용숫자 체크용
    cur = n             # 남은 자릿수
    flag = 0            # 백트래킹용
    # n번 반복
    while cur > 0:
        factorial = 1
        for i in range(1,cur):  # 현재 팩토리얼 계싼
            factorial *= i
        share = k // factorial  # 몫
        remain = k % factorial  # 나머지
        # 나누어떨어지면 -> 숫자+1 하기 전인 상태
        if share != 0 and remain == 0:
            share -= 1
            remain = factorial
            flag = 1    # 백트래킹 적용
        k = remain      # k = 나머지
        cur -= 1        # 반복 수 - 1
        cnt = -1        # 숫자 크기 체크용(자기자신 세기 위해 -1)

        for i in range(1,n+1):
            if nums[i] == 0:    # 해당 자리가 0이면 -> +1
                cnt += 1
            if cnt == share:        # 몫이랑 같으면
                answer.append(i)    # append
                nums[i] = 1         # 방문체크
                break
        # 백트래킹 => 몫이 0이 아니고, 나머지가 0이면 break
        if flag == 1:
            break
    # 뒷자리들을 큰 수부터 정렬시키기
    for i in range(n,0,-1):
        if nums[i] == 0:
            answer.append(i)
    return answer