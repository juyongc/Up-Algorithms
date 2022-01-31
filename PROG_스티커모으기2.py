def solution(sticker):
    answer = 0
    N = len(sticker)
    include_first = [0]*(N-1)
    exclude_first = [0]*N
    include_max = 0
    exclude_max = 0
    if N == 1:
        answer = sticker[0]
        return answer
    # 첫 값을 무조건 포함하는 경우 => 마지막 값은 선택 X
    for i in range(N-1):
        if i == 0:
            include_first[i] = sticker[i]
        elif i == 1:
            include_first[i] = 0
        elif i == 2:
            include_first[i] = include_first[i-2] + sticker[i]
        else:
            include_first[i] = max(include_first[i-2],include_first[i-3]) + sticker[i]
        include_max = max(include_max,include_first[i])
    # 첫 값을 선택하지 않는 경우
    for i in range(1,N):
        if i == 1:
            exclude_first[i] = sticker[i]
        elif i == 2:
            exclude_first[i] = exclude_first[i-2] + sticker[i]
        else:
            exclude_first[i] = max(exclude_first[i-2],exclude_first[i-3]) + sticker[i]
        exclude_max = max(exclude_max,exclude_first[i])
    answer = max(include_max,exclude_max)
    return answer