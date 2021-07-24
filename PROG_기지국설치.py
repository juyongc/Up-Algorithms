def solution(n, stations, w):
    answer = 0
    now = 1     # 현재 위치
    while now < n + 1:
        flag = 0    # 기지국 범위 내 체크용
        # 한 기지국 범위 내에 있으면 -> 범위 밖으로 이동
        for station in stations:
            if station - w <= now <= station + w:
                flag = 1
                now = station + w + 1
                break
        # 기지국 범위에 없으면, 설치 후 이동
        if flag == 0:
            answer += 1
            now += 2 * w + 1

    return answer