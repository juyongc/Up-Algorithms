def solution(cacheSize, cities):
    tot = 0
    stack = [""]*cacheSize  # 캐시사이즈만큼 배열
    nums = len(cities) 
    cnt = 0             # 현재 인덱스
    if cacheSize == 0:  # 사이즈가 0이면 => 답 = 개수*5
        tot = nums*5
    else:               # 그 외
        # 전체 도시이름만큼 반복
        while cnt < nums:
            now = cities[cnt].lower()   # 소문자로 변형
            if now in stack:            # 캐시에 있으면 => +1
                tot += 1
                pos = stack.index(now)  # 해당 위치 빼서 맨 뒤로 넣기
                stack.pop(pos)
                stack.append(now)
            else:                       # 캐시에 없으면 => +5
                tot += 5
                stack.pop(0)            # 맨 앞 빼고, 최근 도시 캐시에 넣기
                stack.append(now)
            cnt += 1
    return tot