def solution(progresses, speeds):
    answer = []
    days = 0        # 배포 일자
    together = 0    # 함께 배포될 작업 개수
    for i in range(len(progresses)):
        current = progresses[i] + days * speeds[i]
        if current < 100:
            share,rem = divmod(100 - progresses[i], speeds[i])
            # 나머지가 있으면 => 하루 추가
            if rem > 0:
                days = share + 1
            else:
                days = share
            # 이미 배포해야할 작업이 있으면 배포
            if together != 0:
                answer.append(together)
            together = 1
        else:   # 일자보다 빨리 끝난 작업은 함께 배포
            together += 1
    # 남은 작업 배포
    answer.append(together)
    return answer