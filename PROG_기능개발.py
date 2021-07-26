import math


def solution(progresses, speeds):
    answer = []
    num = len(progresses)
    n = 0       # 현재 숫자
    cnt = 0     # 현 차례에 배포될 수
    days = math.ceil((100 - progresses[0]) / speeds[0])     # 첫날 배포일자
    # n까지 반복
    while n < num:      
        if progresses[n] + speeds[n] * days >= 100:     # 현재 배포 가능하면
            cnt += 1
        else:                                           # 안되면
            answer.append(cnt)                          # 이전 자료들 배포
            days = math.ceil((100 - progresses[n]) / speeds[n]) # 새로 날짜 정하기
            cnt = 1                                 
        n += 1      # n ++
    answer.append(cnt)      # 마지막 배포
    return answer