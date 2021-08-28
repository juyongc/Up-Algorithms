def solution(N, stages):
    play = [0]*(N+2)
    for stage in stages:
        play[stage] += 1
    clear = len(stages)
    fail = [0]*(N+1)
    for i in range(1,N+1):
        yet = play[i]
        percent = (yet/clear)*100
        fail[i] = percent
        clear -= yet
        if clear == 0:
            break
    final = [0]*N
    for i in range(1,N+1):
        cnt = 0
        for j in range(1,N+1):
            if i == j:
                continue
            if fail[i] > fail[j]:
                cnt += 1
            if fail[i] == fail[j] and i < j:
                cnt += 1
        final[cnt] = i
                
    return final[::-1]